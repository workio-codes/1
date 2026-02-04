-- Employee Management System Database Schema
-- Run this script to create the database and table

-- Create database (uncomment if needed)
-- CREATE DATABASE IF NOT EXISTS employee_db;
-- USE employee_db;

-- Create employees table
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
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_email (email),
    INDEX idx_department (department)
);

-- Sample data (optional)
-- INSERT INTO employees (name, email, phone, department, position, salary, hire_date) VALUES
-- ('John Doe', 'john.doe@example.com', '+1234567890', 'Engineering', 'Software Engineer', 75000.00, '2023-01-15'),
-- ('Jane Smith', 'jane.smith@example.com', '+1234567891', 'Marketing', 'Marketing Manager', 65000.00, '2023-02-20'),
-- ('Bob Johnson', 'bob.johnson@example.com', '+1234567892', 'HR', 'HR Specialist', 55000.00, '2023-03-10');
