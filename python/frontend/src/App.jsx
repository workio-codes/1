import React, { useState, useEffect } from 'react'
import EmployeeList from './components/EmployeeList'
import EmployeeForm from './components/EmployeeForm'
import { getEmployees } from './services/api'
import './App.css'

function App() {
  const [employees, setEmployees] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)
  const [showForm, setShowForm] = useState(false)
  const [editingEmployee, setEditingEmployee] = useState(null)

  useEffect(() => {
    loadEmployees()
  }, [])

  const loadEmployees = async () => {
    try {
      setLoading(true)
      setError(null)
      const data = await getEmployees()
      setEmployees(data)
    } catch (err) {
      setError('Failed to load employees. Please check if the backend is running.')
      console.error('Error loading employees:', err)
    } finally {
      setLoading(false)
    }
  }

  const handleAddEmployee = () => {
    setEditingEmployee(null)
    setShowForm(true)
  }

  const handleEditEmployee = (employee) => {
    setEditingEmployee(employee)
    setShowForm(true)
  }

  const handleFormClose = () => {
    setShowForm(false)
    setEditingEmployee(null)
    loadEmployees()
  }

  return (
    <div className="App">
      <header className="app-header">
        <h1>Employee Management System</h1>
        <button className="btn btn-primary" onClick={handleAddEmployee}>
          Add New Employee
        </button>
      </header>

      <div className="container">
        {error && <div className="error-message">{error}</div>}
        
        {showForm && (
          <EmployeeForm
            employee={editingEmployee}
            onClose={handleFormClose}
            onSuccess={loadEmployees}
          />
        )}

        {loading ? (
          <div className="loading">Loading employees...</div>
        ) : (
          <EmployeeList
            employees={employees}
            onEdit={handleEditEmployee}
            onDelete={loadEmployees}
          />
        )}
      </div>
    </div>
  )
}

export default App
