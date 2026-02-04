"""
Pydantic schemas for request/response validation.
"""

from datetime import date
from typing import Optional
from pydantic import BaseModel, EmailStr, Field, field_validator


class EmployeeBase(BaseModel):
    """Base schema for employee data."""
    name: str = Field(..., min_length=1, max_length=100, description="Employee's full name")
    email: EmailStr = Field(..., description="Employee's email address")
    phone: Optional[str] = Field(None, max_length=20, description="Employee's phone number")
    department: Optional[str] = Field(None, max_length=50, description="Department name")
    position: Optional[str] = Field(None, max_length=50, description="Job position/title")
    salary: Optional[float] = Field(None, ge=0, description="Employee's salary")
    hire_date: Optional[date] = Field(None, description="Date of hire")
    
    @field_validator('name')
    @classmethod
    def validate_name(cls, v: str) -> str:
        """Validate name is not empty."""
        if not v or not v.strip():
            raise ValueError("Name cannot be empty")
        return v.strip()


class EmployeeCreate(EmployeeBase):
    """Schema for creating a new employee."""
    pass


class EmployeeUpdate(BaseModel):
    """Schema for updating an existing employee."""
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    email: Optional[EmailStr] = None
    phone: Optional[str] = Field(None, max_length=20)
    department: Optional[str] = Field(None, max_length=50)
    position: Optional[str] = Field(None, max_length=50)
    salary: Optional[float] = Field(None, ge=0)
    hire_date: Optional[date] = None
    
    @field_validator('name')
    @classmethod
    def validate_name(cls, v: Optional[str]) -> Optional[str]:
        """Validate name if provided."""
        if v is not None and (not v or not v.strip()):
            raise ValueError("Name cannot be empty")
        return v.strip() if v else None


class EmployeeResponse(EmployeeBase):
    """Schema for employee response."""
    id: int = Field(..., description="Unique employee ID")
    
    class Config:
        """Pydantic config."""
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "name": "John Doe",
                "email": "john.doe@example.com",
                "phone": "+1234567890",
                "department": "Engineering",
                "position": "Software Engineer",
                "salary": 75000.00,
                "hire_date": "2023-01-15"
            }
        }
