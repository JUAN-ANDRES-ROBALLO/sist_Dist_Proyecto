import React from 'react'

export default function Footer() {
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
      <div className="footer-center">
        <a href="https://instagram.com" target="_blank" rel="noopener noreferrer" aria-label="Instagram">
          <img src="https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/instagram.svg" alt="Instagram" style={{height: '28px', width: '28px', filter: 'invert(100%)', margin: '0 8px'}} />
        </a>
        <a href="https://youtube.com" target="_blank" rel="noopener noreferrer" aria-label="YouTube">
          <img src="https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/youtube.svg" alt="YouTube" style={{height: '28px', width: '28px', filter: 'invert(100%)', margin: '0 8px'}} />
        </a>
        <a href="https://facebook.com" target="_blank" rel="noopener noreferrer" aria-label="Facebook">
          <img src="https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/facebook.svg" alt="Facebook" style={{height: '28px', width: '28px', filter: 'invert(100%)', margin: '0 8px'}} />
        </a>
        <a href="https://x.com" target="_blank" rel="noopener noreferrer" aria-label="X">
          <img src="https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/x.svg" alt="X" style={{height: '28px', width: '28px', filter: 'invert(100%)', margin: '0 8px'}} />
        </a>
      </div>
      <div className="footer-right">
        <a href="/" style={{ color: '#fff', textDecoration: 'underline', fontWeight: 'bold', marginRight: '16px' }} onClick={e => {e.preventDefault(); window.scrollTo({top: 0, behavior: 'smooth'});}}>Inicio</a>
        <a href="#" style={{ color: '#fff', textDecoration: 'underline', fontWeight: 'bold', marginRight: '16px' }} onClick={e => {e.preventDefault(); window.location.hash = '#nosotros';}}>Nosotros</a>
        <div className="footer-copy">© 2025</div>
      </div>
    </footer>
  )
} 