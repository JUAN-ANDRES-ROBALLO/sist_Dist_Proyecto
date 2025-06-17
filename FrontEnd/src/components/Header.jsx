import React from 'react'

export default function Header({ setShowLogin, setCurrentPage, currentPage }) {
  const handleNavigation = (page) => {
    setCurrentPage(page);
  };

  return (
    <header className="header">
      <div className="logo">
        <img src="/src/assets/icons/logo_agrouy.png" alt="Logo AgroUY" style={{ height: '60px', marginRight: '10px' }} />
        <span 
          onClick={() => handleNavigation('home')} 
          style={{ cursor: 'pointer' }}
        >
          AGROUY
        </span>
      </div>
      <nav className="nav">
        <span 
          onClick={() => handleNavigation('home')}
          className={currentPage === 'home' ? 'active' : ''}
          style={{ cursor: 'pointer' }}
        >
          Inicio
        </span>
        <div className="dropdown">
          <button className="dropbtn">Servicios</button>
          <div className="dropdown-content">
            <span onClick={() => handleNavigation('cultivos')} style={{ cursor: 'pointer' }}>Cultivos</span>
            <span onClick={() => handleNavigation('maquinaria')} style={{ cursor: 'pointer' }}>Maquinaria</span>
            <span onClick={() => handleNavigation('procesos')} style={{ cursor: 'pointer' }}>Procesos</span>
          </div>
        </div>
        <span 
          onClick={() => handleNavigation('nosotros')}
          className={currentPage === 'nosotros' ? 'active' : ''}
          style={{ cursor: 'pointer', color: '#fff' }}
        >
          Nosotros
        </span>
        <div className="dropdown">
          <button className="dropbtn">Gestión</button>
          <div className="dropdown-content">
            <span onClick={() => handleNavigation('optimizacion')} style={{ cursor: 'pointer' }}>Optimización</span>
            <span onClick={() => handleNavigation('reportes')} style={{ cursor: 'pointer' }}>Reportes</span>
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