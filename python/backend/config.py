"""
Configuration settings for the application.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class DatabaseConfig:
    """Database configuration settings."""
    
    HOST = os.getenv("DB_HOST", "localhost")
    PORT = int(os.getenv("DB_PORT", 3306))
    USER = os.getenv("DB_USER", "root")
    PASSWORD = os.getenv("DB_PASSWORD", "")
    DATABASE = os.getenv("DB_NAME", "employee_db")
    
    @classmethod
    def get_connection_string(cls) -> dict:
        """Get database connection parameters as dictionary."""
        return {
            "host": cls.HOST,
            "port": cls.PORT,
            "user": cls.USER,
            "password": cls.PASSWORD,
            "database": cls.DATABASE
        }


class AppConfig:
    """Application configuration settings."""
    
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"
    API_PREFIX = "/api"
    CORS_ORIGINS = os.getenv("CORS_ORIGINS", "http://localhost:3000").split(",")
