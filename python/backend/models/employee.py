"""
Employee model class with attributes and methods.
"""

from datetime import date
from typing import Optional, Tuple


class Employee:
    """
    Employee class representing an employee with various attributes.
    """
    
    def __init__(
        self,
        name: str,
        email: str,
        phone: Optional[str] = None,
        department: Optional[str] = None,
        position: Optional[str] = None,
        salary: Optional[float] = None,
        hire_date: Optional[date] = None,
        employee_id: Optional[int] = None
    ):
        """
        Initialize an Employee instance.
        
        Args:
            name: Employee's full name
            email: Employee's email address
            phone: Employee's phone number
            department: Department name
            position: Job position/title
            salary: Employee's salary
            hire_date: Date of hire
            employee_id: Unique employee ID (for existing employees)
        """
        self.id = employee_id
        self.name = name
        self.email = email
        self.phone = phone
        self.department = department
        self.position = position
        self.salary = salary
        self.hire_date = hire_date
    
    def validate(self) -> Tuple[bool, Optional[str]]:
        """
        Validate employee data.
        
        Returns:
            Tuple of (is_valid, error_message)
        """
        if not self.name or not self.name.strip():
            return False, "Name is required"
        
        if not self.email or not self.email.strip():
            return False, "Email is required"
        
        if self.email and '@' not in self.email:
            return False, "Invalid email format"
        
        if self.salary is not None and self.salary < 0:
            return False, "Salary cannot be negative"
        
        return True, None
    
    def to_dict(self) -> dict:
        """
        Convert employee instance to dictionary.
        
        Returns:
            Dictionary representation of the employee
        """
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'department': self.department,
            'position': self.position,
            'salary': float(self.salary) if self.salary is not None else None,
            'hire_date': self.hire_date.isoformat() if self.hire_date else None
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Employee':
        """
        Create Employee instance from dictionary.
        
        Args:
            data: Dictionary containing employee data
            
        Returns:
            Employee instance
        """
        hire_date = None
        if data.get('hire_date'):
            if isinstance(data['hire_date'], str):
                hire_date = date.fromisoformat(data['hire_date'])
            elif isinstance(data['hire_date'], date):
                hire_date = data['hire_date']
        
        return cls(
            employee_id=data.get('id'),
            name=data['name'],
            email=data['email'],
            phone=data.get('phone'),
            department=data.get('department'),
            position=data.get('position'),
            salary=data.get('salary'),
            hire_date=hire_date
        )
    
    def __repr__(self) -> str:
        """String representation of Employee."""
        return f"Employee(id={self.id}, name={self.name}, email={self.email})"
