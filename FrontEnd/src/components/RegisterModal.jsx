import React, { useState } from 'react'
import { usuariosService } from '../services/api'

export default function RegisterModal({ setShowRegister, setShowLogin }) {
  const [formData, setFormData] = useState({
    username: '',
    email: '',
    password: '',
    confirmPassword: ''
  })
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  const handleSubmit = async (e) => {
    e.preventDefault()
    setLoading(true)
    setError('')

    // Validar que las contraseñas coincidan
    if (formData.password !== formData.confirmPassword) {
      setError('Las contraseñas no coinciden')
      setLoading(false)
      return
    }

    try {
      const response = await usuariosService.register({
        username: formData.username,
        email: formData.email,
        password: formData.password
      })
      console.log('Registration successful:', response)
      
      setShowRegister(false)
      setShowLogin(true)
      // Aquí puedes mostrar un mensaje de éxito
    } catch (error) {
      console.error('Registration failed:', error)
      setError('Error al registrarse. Verifica los datos ingresados.')
    } finally {
      setLoading(false)
    }
  }

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    })
  }

  return (
    <div className="modal-backdrop" onClick={() => setShowRegister(false)}>
      <div className="modal" onClick={e => e.stopPropagation()}>
        <h2>Registrarse</h2>
        <form className="register-form" onSubmit={handleSubmit}>
          <input 
            type="text" 
            name="username"
            placeholder="Nombre de usuario" 
            value={formData.username}
            onChange={handleChange}
            required 
          />
          <input 
            type="email" 
            name="email"
            placeholder="Email" 
            value={formData.email}
            onChange={handleChange}
            required 
          />
          <input 
            type="password" 
            name="password"
            placeholder="Contraseña" 
            value={formData.password}
            onChange={handleChange}
            required 
          />
          <input 
            type="password" 
            name="confirmPassword"
            placeholder="Confirmar contraseña" 
            value={formData.confirmPassword}
            onChange={handleChange}
            required 
          />
          {error && <p className="error-message">{error}</p>}
          <button type="submit" disabled={loading}>
            {loading ? 'Registrando...' : 'Registrarse'}
          </button>
          <button 
            type="button" 
            className="login-btn" 
            onClick={() => { setShowRegister(false); setShowLogin(true); }}
          >
            Ya tengo cuenta
          </button>
        </form>
        <button className="close-modal" onClick={() => setShowRegister(false)}>Cerrar</button>
      </div>
    </div>
  )
} 