import { useState, useEffect } from 'react'
import Header from './components/Header'
import Footer from './components/Footer'
import LoginModal from './components/LoginModal'
import RegisterModal from './components/RegisterModal'
import Nosotros from './components/Nosotros'
import CultivosServicios from './components/CultivosServicios'
import MaquinariaServicios from './components/MaquinariaServicios'
import ProcesosServicios from './components/ProcesosServicios'
import TestConnection from './components/TestConnection'
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
  const [showRegister, setShowRegister] = useState(false)
  const [currentPage, setCurrentPage] = useState('home')

  useEffect(() => {
    switch (currentPage) {
      case 'home':
        document.title = 'Inicio';
        break;
      case 'nosotros':
        document.title = 'Nosotros';
        break;
      case 'cultivos':
        document.title = 'Cultivos';
        break;
      case 'maquinaria':
        document.title = 'Maquinaria';
        break;
      case 'procesos':
        document.title = 'Procesos';
        break;
      case 'test':
        document.title = 'Test de Conexión';
        break;
      default:
        document.title = 'AGROUY'; // Título por defecto si la página no se reconoce
    }
  }, [currentPage]);

  const renderPage = () => {
    switch(currentPage) {
      case 'home':
        return <Home />;
      case 'nosotros':
        return <Nosotros />;
      case 'cultivos':
        return <CultivosServicios />;
      case 'maquinaria':
        return <MaquinariaServicios />;
      case 'procesos':
        return <ProcesosServicios />;
      case 'test':
        return <TestConnection />;
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
      {showLogin && <LoginModal setShowLogin={setShowLogin} setShowRegister={setShowRegister} />}
      {showRegister && <RegisterModal setShowRegister={setShowRegister} setShowLogin={setShowLogin} />}
      <Footer setCurrentPage={setCurrentPage} />
    </div>
  )
}

export default App
