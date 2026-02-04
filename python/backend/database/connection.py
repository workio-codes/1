"""
MySQL database connection management.
"""

import mysql.connector
from mysql.connector import pooling, Error
from typing import Optional
from contextlib import contextmanager
from backend.config import DatabaseConfig


class DatabaseConnection:
    """Manages MySQL database connections using connection pooling."""
    
    _pool: Optional[pooling.MySQLConnectionPool] = None
    
    @classmethod
    def initialize_pool(cls, pool_size: int = 5):
        """
        Initialize the connection pool.
        
        Args:
            pool_size: Number of connections in the pool
        """
        try:
            config = DatabaseConfig.get_connection_string()
            cls._pool = pooling.MySQLConnectionPool(
                pool_name="employee_pool",
                pool_size=pool_size,
                pool_reset_session=True,
                **config
            )
            print(f"Database connection pool initialized with {pool_size} connections")
        except Error as e:
            print(f"Error creating connection pool: {e}")
            raise
    
    @classmethod
    @contextmanager
    def get_connection(cls):
        """
        Get a database connection from the pool.
        
        Yields:
            MySQL connection object
            
        Raises:
            Error: If connection cannot be obtained
        """
        if cls._pool is None:
            cls.initialize_pool()
        
        connection = None
        try:
            connection = cls._pool.get_connection()
            yield connection
        except Error as e:
            print(f"Error getting connection from pool: {e}")
            if connection:
                connection.rollback()
            raise
        finally:
            if connection and connection.is_connected():
                connection.close()
    
    @classmethod
    def test_connection(cls) -> bool:
        """
        Test database connection.
        
        Returns:
            True if connection is successful, False otherwise
        """
        try:
            with cls.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT 1")
                cursor.close()
                return True
        except Error as e:
            print(f"Connection test failed: {e}")
            return False
    
    @classmethod
    def create_tables(cls):
        """
        Create database tables if they don't exist.
        """
        create_table_query = """
        CREATE TABLE IF NOT EXISTS employees (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            phone VARCHAR(20),
            department VARCHAR(50),
            position VARCHAR(50),
            salary DECIMAL(10, 2),
            hire_date DATE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
        )
        """
        
        try:
            with cls.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(create_table_query)
                conn.commit()
                cursor.close()
                print("Employee table created or already exists")
        except Error as e:
            print(f"Error creating table: {e}")
            raise
