# Employee Management System

A full-stack Employee Management System built with FastAPI (Python), React, and MySQL. This application provides complete CRUD (Create, Read, Update, Delete) operations for managing employee records.

## Features

- **Full CRUD Operations**: Create, read, update, and delete employee records
- **RESTful API**: FastAPI backend with Pydantic validation
- **Modern React UI**: Responsive frontend with form validation
- **MySQL Database**: Relational database for persistent storage
- **Modular Architecture**: Well-organized code structure with separate modules
- **Object-Oriented Design**: Employee class with attributes and methods
- **Error Handling**: Comprehensive error handling and debugging support

## Tech Stack

### Backend
- **FastAPI**: Modern Python web framework
- **Pydantic**: Data validation using Python type annotations
- **MySQL Connector**: MySQL database integration
- **Uvicorn**: ASGI server

### Frontend
- **React**: UI library
- **Axios**: HTTP client for API calls
- **Vite**: Build tool and dev server

### Database
- **MySQL**: Relational database management system

## Project Structure

```
python/
├── backend/
│   ├── __init__.py
│   ├── main.py                 # FastAPI application entry point
│   ├── config.py              # Database configuration
│   ├── models/
│   │   ├── __init__.py
│   │   ├── employee.py        # Employee class with attributes and methods
│   │   └── schemas.py         # Pydantic models for request/response
│   ├── database/
│   │   ├── __init__.py
│   │   ├── connection.py      # MySQL connection management
│   │   └── operations.py      # CRUD operations module
│   ├── api/
│   │   ├── __init__.py
│   │   └── routes.py          # FastAPI route handlers
│   └── utils/
│       ├── __init__.py
│       └── validators.py      # Input validation utilities
├── frontend/
│   ├── package.json
│   ├── vite.config.js
│   ├── src/
│   │   ├── App.jsx
│   │   ├── components/
│   │   │   ├── EmployeeList.jsx
│   │   │   ├── EmployeeForm.jsx
│   │   │   └── EmployeeCard.jsx
│   │   ├── services/
│   │   │   └── api.js         # API service functions
│   │   └── index.jsx
│   └── public/
├── database_schema.sql        # Database schema script
├── requirements.txt           # Python dependencies
├── .env.example              # Environment variables template
└── README.md                 # This file
```

## Prerequisites

- Python 3.8 or higher
- Node.js 16 or higher and npm
- MySQL Server 5.7 or higher
- Git (optional)

## Installation

### 1. Clone or Navigate to the Project

```bash
cd python
```

### 2. Set Up Backend

1. Create a virtual environment (recommended):

```bash
python -m venv venv
```

2. Activate the virtual environment:

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. Install Python dependencies:

```bash
pip install -r requirements.txt
```

4. Set up environment variables:

   - Copy `.env.example` to `.env`:
     ```bash
     copy .env.example .env
     ```
   - Edit `.env` and update database credentials:
     ```
     DB_HOST=localhost
     DB_PORT=3306
     DB_USER=root
     DB_PASSWORD=your_password
     DB_NAME=employee_db
     ```

### 3. Set Up Database

1. Start MySQL server

2. Create the database:

```sql
CREATE DATABASE IF NOT EXISTS employee_db;
```

3. Run the schema script (optional, tables are created automatically):

```bash
mysql -u root -p employee_db < database_schema.sql
```

Or manually execute the SQL in `database_schema.sql` using MySQL Workbench or command line.

### 4. Set Up Frontend

1. Navigate to the frontend directory:

```bash
cd frontend
```

2. Install dependencies:

```bash
npm install
```

## Running the Application

### Start the Backend

1. Activate your virtual environment (if not already activated)

2. Navigate to the project root:

```bash
cd python
```

3. Run the FastAPI server:

```bash
python -m uvicorn backend.main:app --reload
```

The API will be available at `http://localhost:8000`
- API Documentation: `http://localhost:8000/docs`
- Alternative docs: `http://localhost:8000/redoc`

### Start the Frontend

1. Navigate to the frontend directory:

```bash
cd frontend
```

2. Start the development server:

```bash
npm run dev
```

The frontend will be available at `http://localhost:3000`

## API Endpoints

- `GET /api/employees` - Get all employees
- `GET /api/employees/{id}` - Get employee by ID
- `POST /api/employees` - Create new employee
- `PUT /api/employees/{id}` - Update employee
- `DELETE /api/employees/{id}` - Delete employee
- `GET /health` - Health check endpoint

## Employee Attributes

- **id**: Unique identifier (auto-generated)
- **name**: Full name (required)
- **email**: Email address (required, unique)
- **phone**: Phone number (optional)
- **department**: Department name (optional)
- **position**: Job position/title (optional)
- **salary**: Salary amount (optional)
- **hire_date**: Date of hire (optional)
- **created_at**: Timestamp of creation (auto-generated)
- **updated_at**: Timestamp of last update (auto-updated)

## Debugging

### Backend Debugging

- Set `DEBUG=True` in `.env` for detailed error messages
- Check console output for database connection errors
- Use FastAPI's interactive docs at `/docs` to test endpoints
- Enable Python logging for more detailed information

### Frontend Debugging

- Check browser console for API errors
- Verify API base URL in `frontend/src/services/api.js`
- Ensure backend is running and accessible
- Check network tab in browser dev tools

### Database Debugging

- Verify MySQL server is running
- Check database credentials in `.env`
- Test connection using MySQL client
- Review database logs for errors

## Troubleshooting

### Backend Issues

1. **Database Connection Error**:
   - Verify MySQL server is running
   - Check credentials in `.env`
   - Ensure database exists

2. **Import Errors**:
   - Make sure virtual environment is activated
   - Verify all dependencies are installed
   - Check Python path

### Frontend Issues

1. **API Connection Error**:
   - Verify backend is running on port 8000
   - Check CORS configuration
   - Verify API URL in `api.js`

2. **Build Errors**:
   - Clear `node_modules` and reinstall
   - Check Node.js version compatibility

## Development

### Code Organization

- **Models**: Employee class and Pydantic schemas
- **Database**: Connection management and CRUD operations
- **API**: FastAPI route handlers
- **Utils**: Validation and utility functions
- **Frontend**: React components and services

### Adding New Features

1. Update database schema if needed
2. Add new methods to Employee class
3. Create/update Pydantic schemas
4. Implement CRUD operations
5. Add API routes
6. Update frontend components

## License

This project is for educational purposes.

## Contributing

Feel free to submit issues and enhancement requests!
