"""
MySQL database connection management.
"""

from typing import Optional
from contextlib import contextmanager
from mysql.connector import pooling, Error  # type: ignore
import mysql.connector  # type: ignore

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
            # Expected dict: {"host": "...", "user": "...", "password": "...", "database": "...", "port": 3306}
            config = DatabaseConfig.get_connection_string()

            base_conn_kwargs = {
                **config,
                "autocommit": True,        # keep transactions clean
                "charset": "utf8mb4",
                "use_pure": True,
                "raise_on_warnings": True,
            }

            cls._pool = pooling.MySQLConnectionPool(
                pool_name="employee_pool",
                pool_size=pool_size,
                pool_reset_session=True,   # reset state when returning to pool
                **base_conn_kwargs,
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
        """
        if cls._pool is None:
            cls.initialize_pool()

        connection = cls._pool.get_connection()
        try:
            # Ensure the connection is alive; reconnect if needed
            try:
                connection.ping(reconnect=True, attempts=1, delay=0)
            except Exception:
                pass
            yield connection
        finally:
            try:
                if connection and connection.is_connected():
                    connection.close()
            except Exception:
                pass

    @classmethod
    def test_connection(cls) -> bool:
        """
        Test database connection.

        Returns:
            True if connection is successful, False otherwise
        """
        try:
            with cls.get_connection() as conn:
                # Use buffered cursor or fetch to consume result set
                cursor = conn.cursor(buffered=True)
                try:
                    cursor.execute("SELECT 1")
                    row = cursor.fetchone()
                    return bool(row and row[0] == 1)
                finally:
                    cursor.close()
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
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
        """

        with cls.get_connection() as conn:
            cursor = conn.cursor()
            try:
                cursor.execute(create_table_query)
                conn.commit()
                print("Employee table created or already exists")
            finally:
                cursor.close()
