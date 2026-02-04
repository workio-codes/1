"""
Input validation utilities.
"""

import re
from typing import Optional, Tuple


def validate_email(email: str) -> bool:
    """
    Validate email format.
    
    Args:
        email: Email address to validate
        
    Returns:
        True if valid, False otherwise
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def validate_phone(phone: str) -> bool:
    """
    Validate phone number format (basic validation).
    
    Args:
        phone: Phone number to validate
        
    Returns:
        True if valid, False otherwise
    """
    # Remove common separators
    cleaned = re.sub(r'[\s\-\(\)]', '', phone)
    # Check if it contains only digits and optional + at start
    return bool(re.match(r'^\+?\d{7,15}$', cleaned))


def validate_salary(salary: Optional[float]) -> Tuple[bool, Optional[str]]:
    """
    Validate salary value.
    
    Args:
        salary: Salary amount to validate
        
    Returns:
        Tuple of (is_valid, error_message)
    """
    if salary is None:
        return True, None
    
    if salary < 0:
        return False, "Salary cannot be negative"
    
    if salary > 10000000:  # Reasonable upper limit
        return False, "Salary exceeds maximum allowed value"
    
    return True, None
