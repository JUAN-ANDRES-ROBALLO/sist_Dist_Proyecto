import { useState } from 'react'
import Header from './components/Header'
import Footer from './components/Footer'
import LoginModal from './components/LoginModal'
import './styles/App.css'

function App() {
  const [showLogin, setShowLogin] = useState(false)

  return (
    <div className="main-container">
      <Header setShowLogin={setShowLogin} />
      {/* Hero Section con video de fondo */}
      <section className="hero">
        <video className="hero-video" autoPlay loop muted playsInline>
          <source src="/src/assets/video/video.mp4" type="video/mp4" />
          Tu navegador no soporta el video.
        </video>
        <div className="hero-overlay">
          <h1>GESTIÓN AGRÍCOLA<br />MODERNA Y EFICIENTE</h1>
          <p>Optimizamos tus cultivos, maquinaria<br />y procesos desde un solo lugar</p>
        </div>
      </section>
      {/* Modal de Login */}
      {showLogin && <LoginModal setShowLogin={setShowLogin} />}
      <Footer />
    </div>
  )
}

export default App
