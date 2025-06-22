import React, { useState, useRef, useEffect } from 'react'

export default function Header({ setShowLogin, setCurrentPage, currentPage }) {
  const [isSearchVisible, setSearchVisible] = useState(false);
  const [searchQuery, setSearchQuery] = useState('');
  const searchInputRef = useRef(null);

  useEffect(() => {
    if (isSearchVisible) {
      searchInputRef.current.focus();
    }
  }, [isSearchVisible]);

  const handleNavigation = (page) => {
    setCurrentPage(page);
  };

  const executeSearch = () => {
    const query = searchQuery.toLowerCase().trim();
    const pageMap = {
      cultivos: 'cultivos',
      maquinaria: 'maquinaria',
      maquinarias: 'maquinaria',
      procesos: 'procesos',
    };

    if (pageMap[query]) {
      handleNavigation(pageMap[query]);
      setSearchQuery('');
      setSearchVisible(false);
    } else if (query) {
      alert(`No se encontró una página para "${searchQuery}"`);
    }
  };

  const handleSearchKeyPress = (e) => {
    if (e.key === 'Enter') {
      executeSearch();
    }
  };

  const handleSearchClick = () => {
    if (isSearchVisible) {
      executeSearch();
    } else {
      setSearchVisible(true);
    }
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
      </nav>
      <div className="header-actions">
        <div className={`search-container ${isSearchVisible ? 'visible' : ''}`}>
          <input
            ref={searchInputRef}
            type="text"
            className="search-input"
            placeholder="Buscar..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            onKeyPress={handleSearchKeyPress}
            onBlur={() => {
              if (!searchQuery) {
                setSearchVisible(false);
              }
            }}
          />
          <button className="search-btn" aria-label="Buscar" onClick={handleSearchClick}>
            🔍
          </button>
        </div>
        <button 
          className="test-btn" 
          onClick={() => handleNavigation('test')}
          style={{
            backgroundColor: '#28a745',
            color: 'white',
            border: 'none',
            padding: '8px 12px',
            borderRadius: '4px',
            cursor: 'pointer',
            marginRight: '10px',
            fontSize: '12px'
          }}
        >
          🔍 Test
        </button>
        <button className="login-btn" onClick={() => setShowLogin(true)}>Iniciar sesión</button>
      </div>
    </header>
  )
} 