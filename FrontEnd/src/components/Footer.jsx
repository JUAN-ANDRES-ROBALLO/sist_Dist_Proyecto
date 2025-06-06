import React from 'react'

export default function Footer() {
  return (
    <footer className="footer">
      <div className="footer-left">
        <div className="footer-logo">AGROUY</div>
        <div>contacto@agrouy.com</div>
      </div>
      <div className="footer-right">
        <a href="#" aria-label="Instagram">
          <img src="https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/instagram.svg" alt="Instagram" style={{height: '28px', width: '28px', filter: 'invert(18%) sepia(16%) saturate(1167%) hue-rotate(86deg) brightness(95%) contrast(87%)'}} />
        </a>
        <a href="#" aria-label="YouTube">
          <img src="https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/youtube.svg" alt="YouTube" style={{height: '28px', width: '28px', filter: 'invert(18%) sepia(16%) saturate(1167%) hue-rotate(86deg) brightness(95%) contrast(87%)'}} />
        </a>
        <a href="#" aria-label="Facebook">
          <img src="https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/facebook.svg" alt="Facebook" style={{height: '28px', width: '28px', filter: 'invert(18%) sepia(16%) saturate(1167%) hue-rotate(86deg) brightness(95%) contrast(87%)'}} />
        </a>
        <a href="#" aria-label="X">
          <img src="https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/x.svg" alt="X" style={{height: '28px', width: '28px', filter: 'invert(18%) sepia(16%) saturate(1167%) hue-rotate(86deg) brightness(95%) contrast(87%)'}} />
        </a>
        <div className="footer-copy">© 2025</div>
      </div>
    </footer>
  )
} 