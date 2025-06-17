import React from 'react'

export default function Footer() {
  return (
    <footer className="footer-pro">
      <div className="footer-pro-top">
        <div className="footer-pro-left">
          <img src="/src/assets/icons/logo_agrouy.png" alt="Logo AgroUY" className="footer-pro-logo" />
          <span className="footer-pro-brand">AgroUY</span>
        </div>
        <nav className="footer-pro-nav">
          <a href="/" onClick={e => {e.preventDefault(); window.scrollTo({top: 0, behavior: 'smooth'});}}>Inicio</a>
          <a href="#" onClick={e => {e.preventDefault(); window.location.hash = '#nosotros';}}>Nosotros</a>
          <a href="#" onClick={e => {e.preventDefault(); window.location.hash = '#contacto';}}>Contacto</a>
        </nav>
        <div className="footer-pro-social">
          <a href="https://instagram.com" target="_blank" rel="noopener noreferrer" aria-label="Instagram">
            <img src="https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/instagram.svg" alt="Instagram" />
          </a>
          <a href="https://youtube.com" target="_blank" rel="noopener noreferrer" aria-label="YouTube">
            <img src="https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/youtube.svg" alt="YouTube" />
          </a>
          <a href="https://facebook.com" target="_blank" rel="noopener noreferrer" aria-label="Facebook">
            <img src="https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/facebook.svg" alt="Facebook" />
          </a>
          <a href="https://x.com" target="_blank" rel="noopener noreferrer" aria-label="X">
            <img src="https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/x.svg" alt="X" />
          </a>
        </div>
      </div>
      <div className="footer-pro-bottom">
        © 2025 AgroUY. Todos los derechos reservados.
      </div>
    </footer>
  )
} 