import React, { useState } from 'react'
import { usuariosService } from '../services/api'

export default function LoginModal({ setShowLogin, setShowRegister }) {
  const [formData, setFormData] = useState({
    username: '',
    password: ''
  })
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  const handleSubmit = async (e) => {
    e.preventDefault()
    setLoading(true)
    setError('')

    try {
      const response = await usuariosService.login(formData)
      console.log('Login successful:', response)
      
      // Aquí puedes guardar el token en localStorage si el backend lo devuelve
      // localStorage.setItem('token', response.token)
      
      setShowLogin(false)
      // Aquí puedes agregar lógica adicional después del login exitoso
    } catch (error) {
      console.error('Login failed:', error)
      setError('Error al iniciar sesión. Verifica tus credenciales.')
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
    <div className="modal-backdrop" onClick={() => setShowLogin(false)}>
      <div className="modal" onClick={e => e.stopPropagation()}>
        <h2>Iniciar sesión</h2>
        <form className="login-form" onSubmit={handleSubmit}>
          <input 
            type="text" 
            name="username"
            placeholder="Usuario" 
            value={formData.username}
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
          {error && <p className="error-message">{error}</p>}
          <button type="submit" disabled={loading}>
            {loading ? 'Iniciando sesión...' : 'Entrar'}
          </button>
          <button 
            type="button" 
            className="register-btn" 
            onClick={() => { setShowLogin(false); setShowRegister(true); }}
          >
            Registrarse
          </button>
        </form>
        <button className="close-modal" onClick={() => setShowLogin(false)}>Cerrar</button>
      </div>
    </div>
  )
} 