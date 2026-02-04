"""
FastAPI route handlers for employee management.
"""

from typing import List
from fastapi import APIRouter, HTTPException, status
from backend.models.schemas import EmployeeCreate, EmployeeUpdate, EmployeeResponse
from backend.database import operations

router = APIRouter(prefix="/employees", tags=["employees"])


@router.post("", response_model=EmployeeResponse, status_code=status.HTTP_201_CREATED)
async def create_employee(employee: EmployeeCreate):
    """
    Create a new employee.
    
    Args:
        employee: Employee data from request body
        
    Returns:
        Created employee object
        
    Raises:
        HTTPException: If employee creation fails
    """
    try:
        employee_dict = employee.model_dump()
        created_employee = operations.create_employee(employee_dict)
        
        if created_employee:
            return EmployeeResponse(**created_employee.to_dict())
        else:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to create employee"
            )
    except Exception as e:
        # Check for duplicate email error
        if "Duplicate entry" in str(e) or "UNIQUE constraint" in str(e):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already exists"
            )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error creating employee: {str(e)}"
        )


@router.get("", response_model=List[EmployeeResponse])
async def get_all_employees():
    """
    Retrieve all employees.
    
    Returns:
        List of all employee objects
    """
    try:
        employees = operations.get_all_employees()
        return [EmployeeResponse(**emp.to_dict()) for emp in employees]
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error retrieving employees: {str(e)}"
        )


@router.get("/{employee_id}", response_model=EmployeeResponse)
async def get_employee(employee_id: int):
    """
    Retrieve a single employee by ID.
    
    Args:
        employee_id: Unique employee identifier
        
    Returns:
        Employee object
        
    Raises:
        HTTPException: If employee not found
    """
    try:
        employee = operations.get_employee(employee_id)
        if employee:
            return EmployeeResponse(**employee.to_dict())
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Employee with ID {employee_id} not found"
            )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error retrieving employee: {str(e)}"
        )


@router.put("/{employee_id}", response_model=EmployeeResponse)
async def update_employee(employee_id: int, employee: EmployeeUpdate):
    """
    Update an existing employee.
    
    Args:
        employee_id: Unique employee identifier
        employee: Employee data to update
        
    Returns:
        Updated employee object
        
    Raises:
        HTTPException: If employee not found or update fails
    """
    try:
        # Check if employee exists
        existing_employee = operations.get_employee(employee_id)
        if not existing_employee:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Employee with ID {employee_id} not found"
            )
        
        # Get only non-None fields from the update request
        update_data = employee.model_dump(exclude_unset=True)
        updated_employee = operations.update_employee(employee_id, update_data)
        
        if updated_employee:
            return EmployeeResponse(**updated_employee.to_dict())
        else:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to update employee"
            )
    except HTTPException:
        raise
    except Exception as e:
        # Check for duplicate email error
        if "Duplicate entry" in str(e) or "UNIQUE constraint" in str(e):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already exists"
            )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error updating employee: {str(e)}"
        )


@router.delete("/{employee_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_employee(employee_id: int):
    """
    Delete an employee.
    
    Args:
        employee_id: Unique employee identifier
        
    Raises:
        HTTPException: If employee not found or deletion fails
    """
    try:
        # Check if employee exists
        existing_employee = operations.get_employee(employee_id)
        if not existing_employee:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Employee with ID {employee_id} not found"
            )
        
        success = operations.delete_employee(employee_id)
        if not success:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to delete employee"
            )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error deleting employee: {str(e)}"
        )
