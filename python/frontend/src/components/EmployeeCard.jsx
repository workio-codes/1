import React, { useState } from 'react'
import { deleteEmployee } from '../services/api'
import './EmployeeCard.css'

const EmployeeCard = ({ employee, onEdit, onDelete }) => {
  const [isDeleting, setIsDeleting] = useState(false)
  const [error, setError] = useState(null)

  const handleDelete = async () => {
    if (!window.confirm(`Are you sure you want to delete ${employee.name}?`)) {
      return
    }

    try {
      setIsDeleting(true)
      setError(null)
      await deleteEmployee(employee.id)
      onDelete()
    } catch (err) {
      setError(err.message || 'Failed to delete employee')
    } finally {
      setIsDeleting(false)
    }
  }

  const formatCurrency = (amount) => {
    if (!amount) return 'N/A'
    return new Intl.NumberFormat('en-US', {
      style: 'currency',
      currency: 'USD',
    }).format(amount)
  }

  const formatDate = (dateString) => {
    if (!dateString) return 'N/A'
    return new Date(dateString).toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'long',
      day: 'numeric',
    })
  }

  return (
    <div className="employee-card">
      <div className="employee-header">
        <h3>{employee.name}</h3>
        <div className="employee-actions">
          <button
            className="btn btn-secondary btn-sm"
            onClick={() => onEdit(employee)}
            disabled={isDeleting}
          >
            Edit
          </button>
          <button
            className="btn btn-danger btn-sm"
            onClick={handleDelete}
            disabled={isDeleting}
          >
            {isDeleting ? 'Deleting...' : 'Delete'}
          </button>
        </div>
      </div>

      {error && <div className="error">{error}</div>}

      <div className="employee-details">
        <div className="detail-item">
          <span className="label">Email:</span>
          <span className="value">{employee.email}</span>
        </div>
        {employee.phone && (
          <div className="detail-item">
            <span className="label">Phone:</span>
            <span className="value">{employee.phone}</span>
          </div>
        )}
        {employee.department && (
          <div className="detail-item">
            <span className="label">Department:</span>
            <span className="value">{employee.department}</span>
          </div>
        )}
        {employee.position && (
          <div className="detail-item">
            <span className="label">Position:</span>
            <span className="value">{employee.position}</span>
          </div>
        )}
        {employee.salary && (
          <div className="detail-item">
            <span className="label">Salary:</span>
            <span className="value">{formatCurrency(employee.salary)}</span>
          </div>
        )}
        {employee.hire_date && (
          <div className="detail-item">
            <span className="label">Hire Date:</span>
            <span className="value">{formatDate(employee.hire_date)}</span>
          </div>
        )}
      </div>
    </div>
  )
}

export default EmployeeCard
