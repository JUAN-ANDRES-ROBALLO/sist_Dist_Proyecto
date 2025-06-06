import React from 'react'

export default function Header({ setShowLogin }) {
  return (
    <header className="header">
      <div className="logo">
        <img src="/src/assets/icons/vite.svg" alt="Logo AGROUY" style={{ height: '40px', marginRight: '10px' }} />
        AGROUY
      </div>
      <nav className="nav">
        <a href="#">Inicio</a>
        <div className="dropdown">
          <button className="dropbtn">Servicios</button>
          <div className="dropdown-content">
            <a href="#">Cultivos</a>
            <a href="#">Maquinaria</a>
            <a href="#">Procesos</a>
          </div>
        </div>
        <a href="#">Nosotros</a>
        <div className="dropdown">
          <button className="dropbtn">Gestión</button>
          <div className="dropdown-content">
            <a href="#">Optimización</a>
            <a href="#">Reportes</a>
          </div>
        </div>
      </nav>
      <div className="header-actions">
        <button className="search-btn" aria-label="Buscar">🔍</button>
        <button className="login-btn" onClick={() => setShowLogin(true)}>Iniciar sesión</button>
      </div>
    </header>
  )
} 