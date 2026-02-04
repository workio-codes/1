/**
 * API service functions for employee CRUD operations.
 */

import axios from 'axios'

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api'

// Create axios instance with default config
const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
})

// Request interceptor for debugging
apiClient.interceptors.request.use(
  (config) => {
    console.log(`Making ${config.method.toUpperCase()} request to ${config.url}`)
    return config
  },
  (error) => {
    return Promise.reject(error)
  }
)

// Response interceptor for error handling
apiClient.interceptors.response.use(
  (response) => {
    return response.data
  },
  (error) => {
    const message = error.response?.data?.detail || error.message || 'An error occurred'
    console.error('API Error:', message)
    return Promise.reject(new Error(message))
  }
)

/**
 * Get all employees.
 * @returns {Promise<Array>} Array of employee objects
 */
export const getEmployees = async () => {
  try {
    return await apiClient.get('/employees')
  } catch (error) {
    throw error
  }
}

/**
 * Get a single employee by ID.
 * @param {number} id - Employee ID
 * @returns {Promise<Object>} Employee object
 */
export const getEmployee = async (id) => {
  try {
    return await apiClient.get(`/employees/${id}`)
  } catch (error) {
    throw error
  }
}

/**
 * Create a new employee.
 * @param {Object} employeeData - Employee data
 * @returns {Promise<Object>} Created employee object
 */
export const createEmployee = async (employeeData) => {
  try {
    return await apiClient.post('/employees', employeeData)
  } catch (error) {
    throw error
  }
}

/**
 * Update an existing employee.
 * @param {number} id - Employee ID
 * @param {Object} employeeData - Updated employee data
 * @returns {Promise<Object>} Updated employee object
 */
export const updateEmployee = async (id, employeeData) => {
  try {
    return await apiClient.put(`/employees/${id}`, employeeData)
  } catch (error) {
    throw error
  }
}

/**
 * Delete an employee.
 * @param {number} id - Employee ID
 * @returns {Promise<void>}
 */
export const deleteEmployee = async (id) => {
  try {
    return await apiClient.delete(`/employees/${id}`)
  } catch (error) {
    throw error
  }
}
