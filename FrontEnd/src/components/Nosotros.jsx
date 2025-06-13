import React from 'react';
import '../styles/Nosotros.css';

const Nosotros = () => {
  return (
    <div className="nosotros-container">
      <div className="nosotros-header">
        <h1>Sobre Nosotros</h1>
        <p className="subtitle">Conectando el campo con el futuro</p>
      </div>

      <div className="nosotros-content">
        <section className="mision-vision">
          <div className="card">
            <h2>Nuestra Misión</h2>
            <p>
              Facilitar la conexión entre agricultores y compradores, promoviendo
              prácticas agrícolas sostenibles y asegurando un futuro más próspero
              para el sector agrícola.
            </p>
          </div>
          <div className="card">
            <h2>Nuestra Visión</h2>
            <p>
              Ser la plataforma líder en la transformación digital del sector
              agrícola, creando un ecosistema sostenible y eficiente que beneficie
              a todos los actores de la cadena de valor.
            </p>
          </div>
        </section>

        <section className="valores">
          <h2>Nuestros Valores</h2>
          <div className="valores-grid">
            <div className="valor-item">
              <h3>Sostenibilidad</h3>
              <p>Comprometidos con prácticas agrícolas responsables y respetuosas con el medio ambiente.</p>
            </div>
            <div className="valor-item">
              <h3>Innovación</h3>
              <p>Buscamos constantemente nuevas soluciones para mejorar el sector agrícola.</p>
            </div>
            <div className="valor-item">
              <h3>Transparencia</h3>
              <p>Fomentamos relaciones honestas y transparentes entre todos los participantes.</p>
            </div>
            <div className="valor-item">
              <h3>Comunidad</h3>
              <p>Construimos una comunidad fuerte y colaborativa en el sector agrícola.</p>
            </div>
          </div>
        </section>

        <section className="equipo">
          <h2>Nuestro Equipo</h2>
          <div className="equipo-grid">
            <div className="miembro">
              <div className="miembro-info">
                <h3>Equipo de Desarrollo</h3>
                <p>Profesionales apasionados por la tecnología y la agricultura, trabajando juntos para crear soluciones innovadoras.</p>
              </div>
            </div>
            <div className="miembro">
              <div className="miembro-info">
                <h3>Expertos Agrícolas</h3>
                <p>Especialistas con amplia experiencia en el sector agrícola, asegurando que nuestras soluciones sean prácticas y efectivas.</p>
              </div>
            </div>
          </div>
        </section>
      </div>
    </div>
  );
};

export default Nosotros; 