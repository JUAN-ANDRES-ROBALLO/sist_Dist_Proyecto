import React from 'react';
import '../styles/Nosotros.css';

const iconos = {
  sostenibilidad: '🌱',
  innovacion: '💡',
  transparencia: '🔍',
  comunidad: '🤝',
  desarrollo: '🖥️',
  expertos: '🌾',
};

const Nosotros = () => {
  return (
    <div className="nosotros-container pro">
      <div className="nosotros-header">
        <h1>Sobre Nosotros</h1>
        <p className="subtitle">Conectando el campo con el futuro</p>
      </div>

      <div className="nosotros-content">
        <section className="mision-vision">
          <div className="card">
            <h2>Nuestra Misión</h2>
            <p>
              Transformar la agricultura a través de soluciones tecnológicas que empoderen a los agricultores, 
              optimicen sus procesos y promuevan la sostenibilidad. Buscamos ser el puente que conecta 
              la tradición del campo con la innovación del futuro, asegurando la prosperidad 
              de las comunidades agrícolas y la salud de nuestro planeta.
            </p>
          </div>
          <div className="card">
            <h2>Nuestra Visión</h2>
            <p>
              Aspiramos a un futuro donde cada agricultor tenga acceso a herramientas inteligentes 
              que le permitan tomar decisiones informadas, maximizar su rendimiento y contribuir a una 
              cadena de suministro alimentaria más transparente y eficiente. Queremos ser líderes en la 
              revolución agrotecnológica, creando un ecosistema global conectado y sostenible.
            </p>
          </div>
        </section>

        <section className="valores">
          <h2>Nuestros Valores</h2>
          <div className="valores-grid">
            <div className="valor-item">
              <div className="valor-icono">{iconos.sostenibilidad}</div>
              <h3>Sostenibilidad</h3>
              <p>Comprometidos con prácticas agrícolas responsables y respetuosas con el medio ambiente.</p>
            </div>
            <div className="valor-item">
              <div className="valor-icono">{iconos.innovacion}</div>
              <h3>Innovación</h3>
              <p>Buscamos constantemente nuevas soluciones para mejorar el sector agrícola.</p>
            </div>
            <div className="valor-item">
              <div className="valor-icono">{iconos.transparencia}</div>
              <h3>Transparencia</h3>
              <p>Fomentamos relaciones honestas y transparentes entre todos los participantes.</p>
            </div>
            <div className="valor-item">
              <div className="valor-icono">{iconos.comunidad}</div>
              <h3>Comunidad</h3>
              <p>Construimos una comunidad fuerte y colaborativa en el sector agrícola.</p>
            </div>
          </div>
        </section>

        <section className="equipo">
          <h2>Nuestro Equipo</h2>
          <div className="equipo-grid">
            <div className="miembro">
              <div className="miembro-icono">{iconos.desarrollo}</div>
              <div className="miembro-info">
                <h3>Equipo de Desarrollo</h3>
                <p>Nuestro motor de innovación. Un equipo multidisciplinario de ingenieros de software, científicos de datos y diseñadores UX/UI apasionados por la agrotecnología. Se especializan en aplicar las últimas tendencias, como Inteligencia Artificial y Big Data, para construir una plataforma robusta, predictiva y, lo más importante, intuitiva para el agricultor moderno.</p>
              </div>
            </div>
            <div className="miembro">
              <div className="miembro-icono">{iconos.expertos}</div>
              <div className="miembro-info">
                <h3>Expertos Agrícolas</h3>
                <p>La raíz de nuestro conocimiento. Un equipo de ingenieros agrónomos y especialistas con décadas de experiencia directa en el campo. Son el puente fundamental entre la tecnología y la agricultura, asegurando que cada herramienta que desarrollamos sea práctica, precisa y verdaderamente útil. Su pericia garantiza que nuestras soluciones están basadas en ciencia y probadas en la práctica.</p>
              </div>
            </div>
          </div>
        </section>

        <div className="nosotros-cta">
          <a href="#contacto" className="cta-btn">Contactar con AgroUY</a>
        </div>
      </div>
    </div>
  );
};

export default Nosotros; 