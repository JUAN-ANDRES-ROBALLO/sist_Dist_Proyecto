import React, { useState } from 'react'
import { usuariosService } from '../services/api'

export default function RegisterModal({ setShowRegister, setShowLogin }) {
  const [formData, setFormData] = useState({
    cedula: '',
    nombre: '',
    email: '',
    password: '',
    password_confirm: ''
  })
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  const handleSubmit = async (e) => {
    e.preventDefault()
    setLoading(true)
    setError('')

    // Validar que las contraseñas coincidan
    if (formData.password !== formData.password_confirm) {
      setError('Las contraseñas no coinciden')
      setLoading(false)
      return
    }

    // Validar cédula (solo números, 8-10 dígitos)
    if (!/^\d{8,10}$/.test(formData.cedula)) {
      setError('La cédula debe tener entre 8 y 10 dígitos numéricos')
      setLoading(false)
      return
    }

    try {
      const response = await usuariosService.register(formData)
      console.log('Registration successful:', response)
      
      setShowRegister(false)
      setShowLogin(true)
      // Aquí puedes mostrar un mensaje de éxito
    } catch (error) {
      console.error('Registration failed:', error)
      setError(error.message || 'Error al registrarse. Verifica los datos ingresados.')
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
            name="cedula"
            placeholder="Cédula (8-10 dígitos)" 
            value={formData.cedula}
            onChange={handleChange}
            maxLength="10"
            pattern="[0-9]{8,10}"
            required 
          />
          <input 
            type="text" 
            name="nombre"
            placeholder="Nombre completo" 
            value={formData.nombre}
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
            minLength="6"
            required 
          />
          <input 
            type="password" 
            name="password_confirm"
            placeholder="Confirmar contraseña" 
            value={formData.password_confirm}
            onChange={handleChange}
            minLength="6"
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