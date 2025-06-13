import { useState } from 'react'
import Header from './components/Header'
import Footer from './components/Footer'
import LoginModal from './components/LoginModal'
import Nosotros from './components/Nosotros'
import './styles/App.css'

// Componente para la página de inicio
const Home = () => {
  return (
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
  );
};

function App() {
  const [showLogin, setShowLogin] = useState(false)
  const [currentPage, setCurrentPage] = useState('home')

  const renderPage = () => {
    switch(currentPage) {
      case 'home':
        return <Home />;
      case 'nosotros':
        return <Nosotros />;
      case 'cultivos':
        return <div>Cultivos</div>;
      case 'maquinaria':
        return <div>Maquinaria</div>;
      case 'procesos':
        return <div>Procesos</div>;
      case 'optimizacion':
        return <div>Optimización</div>;
      case 'reportes':
        return <div>Reportes</div>;
      default:
        return <Home />;
    }
  }

  return (
    <div className="main-container">
      <Header setShowLogin={setShowLogin} setCurrentPage={setCurrentPage} currentPage={currentPage} />
      <main className="content">
        {renderPage()}
      </main>
      {showLogin && <LoginModal setShowLogin={setShowLogin} />}
      <Footer />
    </div>
  )
}

export default App
