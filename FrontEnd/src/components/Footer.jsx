import React from 'react'

export default function Footer({ setCurrentPage }) {
  return (
    <footer className="footer">
      <div className="footer-left">
        <div style={{display: 'flex', alignItems: 'center', gap: '10px', marginBottom: '8px'}}>
          <img src="/src/assets/icons/logo_agrouy.png" alt="Logo AgroUY" style={{ height: '50px' }} />
          <span style={{fontWeight: 'bold', fontSize: '1.5rem'}}>AgroUY</span>
        </div>
        <div style={{marginBottom: '2px'}}>contacto@agrouy.com</div>
        <div style={{marginBottom: '2px'}}>+598 1234 5678</div>
      </div>
      <div className="footer-right">
        <div style={{display: 'flex', gap: '16px', marginBottom: '8px'}}>
          <span style={{ color: '#fff', fontWeight: 'bold', cursor: 'pointer' }} onClick={() => setCurrentPage('home')}>Inicio</span>
          <span style={{ color: '#fff', fontWeight: 'bold', cursor: 'pointer' }} onClick={() => setCurrentPage('nosotros')}>Nosotros</span>
          <a href="https://instagram.com" target="_blank" rel="noopener noreferrer" aria-label="Instagram">
            <img src="https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/instagram.svg" alt="Instagram" style={{height: '28px', width: '28px', filter: 'invert(100%)'}} />
          </a>
          <a href="https://youtube.com" target="_blank" rel="noopener noreferrer" aria-label="YouTube">
            <img src="https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/youtube.svg" alt="YouTube" style={{height: '28px', width: '28px', filter: 'invert(100%)'}} />
          </a>
          <a href="https://facebook.com" target="_blank" rel="noopener noreferrer" aria-label="Facebook">
            <img src="https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/facebook.svg" alt="Facebook" style={{height: '28px', width: '28px', filter: 'invert(100%)'}} />
          </a>
          <a href="https://x.com" target="_blank" rel="noopener noreferrer" aria-label="X">
            <img src="https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/x.svg" alt="X" style={{height: '28px', width: '28px', filter: 'invert(100%)'}} />
          </a>
        </div>
        <div className="footer-copy">© 2025</div>
      </div>
    </footer>
  )
} 