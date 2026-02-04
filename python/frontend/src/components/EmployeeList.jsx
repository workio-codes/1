import React from 'react'
import EmployeeCard from './EmployeeCard'
import './EmployeeList.css'

const EmployeeList = ({ employees, onEdit, onDelete }) => {
  if (employees.length === 0) {
    return (
      <div className="empty-state">
        <p>No employees found. Add your first employee to get started!</p>
      </div>
    )
  }

  return (
    <div className="employee-list">
      <h2>Employees ({employees.length})</h2>
      <div className="employee-grid">
        {employees.map((employee) => (
          <EmployeeCard
            key={employee.id}
            employee={employee}
            onEdit={onEdit}
            onDelete={onDelete}
          />
        ))}
      </div>
    </div>
  )
}

export default EmployeeList
