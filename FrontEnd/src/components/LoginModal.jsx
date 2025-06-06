import React from 'react'

export default function LoginModal({ setShowLogin }) {
  return (
    <div className="modal-backdrop" onClick={() => setShowLogin(false)}>
      <div className="modal" onClick={e => e.stopPropagation()}>
        <h2>Iniciar sesión</h2>
        <form className="login-form" onSubmit={e => { e.preventDefault(); setShowLogin(false); }}>
          <input type="text" placeholder="Usuario" required />
          <input type="password" placeholder="Contraseña" required />
          <button type="submit">Entrar</button>
          <button type="button" className="register-btn">Registrarse</button>
        </form>
        <button className="close-modal" onClick={() => setShowLogin(false)}>Cerrar</button>
      </div>
    </div>
  )
} 