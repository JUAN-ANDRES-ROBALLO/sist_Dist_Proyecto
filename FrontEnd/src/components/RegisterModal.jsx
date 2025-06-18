import React from 'react';

export default function RegisterModal({ setShowRegister, setShowLogin }) {
  return (
    <div className="modal-backdrop" onClick={() => setShowRegister(false)}>
      <div className="modal" onClick={e => e.stopPropagation()}>
        <h2>Registrarse</h2>
        <form className="login-form" onSubmit={e => { e.preventDefault(); setShowRegister(false); }}>
          <input type="text" placeholder="Usuario" required />
          <input type="email" placeholder="Email" required />
          <input type="password" placeholder="Contraseña" required />
          <button type="submit">Crear cuenta</button>
          <button type="button" className="login-btn" onClick={() => { setShowRegister(false); setShowLogin(true); }}>Volver al inicio de sesión</button>
        </form>
        <button className="close-modal" onClick={() => setShowRegister(false)}>Cerrar</button>
      </div>
    </div>
  )
} 