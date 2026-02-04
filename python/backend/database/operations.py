"""
CRUD operations for employee records.
"""

from typing import Optional, List, Dict, Any
from datetime import date
from mysql.connector import Error
from backend.database.connection import DatabaseConnection
from backend.models.employee import Employee


def create_employee(employee_data: Dict[str, Any]) -> Optional[Employee]:
    """
    Create a new employee record in the database.
    
    Args:
        employee_data: Dictionary containing employee information
        
    Returns:
        Employee object if successful, None otherwise
    """
    insert_query = """
    INSERT INTO employees (name, email, phone, department, position, salary, hire_date)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    
    try:
        with DatabaseConnection.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                insert_query,
                (
                    employee_data['name'],
                    employee_data['email'],
                    employee_data.get('phone'),
                    employee_data.get('department'),
                    employee_data.get('position'),
                    employee_data.get('salary'),
                    employee_data.get('hire_date')
                )
            )
            conn.commit()
            employee_id = cursor.lastrowid
            cursor.close()
            
            # Fetch the created employee
            return get_employee(employee_id)
    except Error as e:
        print(f"Error creating employee: {e}")
        raise


def get_employee(employee_id: int) -> Optional[Employee]:
    """
    Retrieve a single employee by ID.
    
    Args:
        employee_id: Unique employee identifier
        
    Returns:
        Employee object if found, None otherwise
    """
    select_query = """
    SELECT id, name, email, phone, department, position, salary, hire_date
    FROM employees
    WHERE id = %s
    """
    
    try:
        with DatabaseConnection.get_connection() as conn:
            cursor = conn.cursor(dictionary=True)
            cursor.execute(select_query, (employee_id,))
            row = cursor.fetchone()
            cursor.close()
            
            if row:
                # Convert hire_date string to date object if present
                if row.get('hire_date') and isinstance(row['hire_date'], str):
                    row['hire_date'] = date.fromisoformat(row['hire_date'])
                return Employee.from_dict(row)
            return None
    except Error as e:
        print(f"Error retrieving employee: {e}")
        raise


def get_all_employees() -> List[Employee]:
    """
    Retrieve all employees from the database.
    
    Returns:
        List of Employee objects
    """
    select_query = """
    SELECT id, name, email, phone, department, position, salary, hire_date
    FROM employees
    ORDER BY id DESC
    """
    
    try:
        with DatabaseConnection.get_connection() as conn:
            cursor = conn.cursor(dictionary=True)
            cursor.execute(select_query)
            rows = cursor.fetchall()
            cursor.close()
            
            employees = []
            for row in rows:
                # Convert hire_date string to date object if present
                if row.get('hire_date') and isinstance(row['hire_date'], str):
                    row['hire_date'] = date.fromisoformat(row['hire_date'])
                employees.append(Employee.from_dict(row))
            
            return employees
    except Error as e:
        print(f"Error retrieving employees: {e}")
        raise


def update_employee(employee_id: int, employee_data: Dict[str, Any]) -> Optional[Employee]:
    """
    Update an existing employee record.
    
    Args:
        employee_id: Unique employee identifier
        employee_data: Dictionary containing fields to update
        
    Returns:
        Updated Employee object if successful, None otherwise
    """
    # Build dynamic update query based on provided fields
    update_fields = []
    values = []
    
    allowed_fields = ['name', 'email', 'phone', 'department', 'position', 'salary', 'hire_date']
    for field in allowed_fields:
        if field in employee_data and employee_data[field] is not None:
            update_fields.append(f"{field} = %s")
            values.append(employee_data[field])
    
    if not update_fields:
        # No fields to update
        return get_employee(employee_id)
    
    values.append(employee_id)
    update_query = f"""
    UPDATE employees
    SET {', '.join(update_fields)}
    WHERE id = %s
    """
    
    try:
        with DatabaseConnection.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(update_query, tuple(values))
            conn.commit()
            affected_rows = cursor.rowcount
            cursor.close()
            
            if affected_rows > 0:
                return get_employee(employee_id)
            return None
    except Error as e:
        print(f"Error updating employee: {e}")
        raise


def delete_employee(employee_id: int) -> bool:
    """
    Delete an employee record from the database.
    
    Args:
        employee_id: Unique employee identifier
        
    Returns:
        True if deletion was successful, False otherwise
    """
    delete_query = """
    DELETE FROM employees
    WHERE id = %s
    """
    
    try:
        with DatabaseConnection.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(delete_query, (employee_id,))
            conn.commit()
            affected_rows = cursor.rowcount
            cursor.close()
            
            return affected_rows > 0
    except Error as e:
        print(f"Error deleting employee: {e}")
        raise
