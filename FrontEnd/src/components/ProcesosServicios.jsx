import React, { useState } from 'react';
import '../styles/ProcesosServicios.css';

const initialEtapas = [
  {
    id: 1,
    nombre: 'Topografía y Labrado',
    descripcion: 'Análisis del terreno y preparación inicial del suelo para optimizar las condiciones de siembra.',
    icono: '/src/assets/cultivos/Topografia.jpeg',
    completada: false,
  },
  {
    id: 2,
    nombre: 'Siembra',
    descripcion: 'Selección de semillas y plantación en el momento óptimo para maximizar el potencial de rendimiento.',
    icono: '/src/assets/cultivos/Siembra.jpeg',
    completada: false,
  },
  {
    id: 3,
    nombre: 'Riego',
    descripcion: 'Gestión eficiente del agua, aplicando la cantidad necesaria para un crecimiento saludable del cultivo.',
    icono: '/src/assets/cultivos/riego.jpg',
    completada: false,
  },
  {
    id: 4,
    nombre: 'Fertilización y Abono',
    descripcion: 'Aporte de nutrientes esenciales para enriquecer el suelo y asegurar un desarrollo vigoroso de las plantas.',
    icono: '/src/assets/cultivos/fertilizante.jpg',
    completada: false,
  },
  {
    id: 5,
    nombre: 'Monitoreo y Control de Plagas',
    descripcion: 'Vigilancia constante y aplicación de medidas preventivas y correctivas para proteger el cultivo.',
    icono: '/src/assets/cultivos/Monitoreo de plagas.jpg',
    completada: false,
  },
  {
    id: 6,
    nombre: 'Cosecha',
    descripcion: 'Recolección del producto en su punto óptimo de madurez, utilizando técnicas que aseguran su calidad.',
    icono: '/src/assets/cultivos/Cosecha.jpg',
    completada: false,
  },
];

const ProcesosServicios = () => {
  const [etapas, setEtapas] = useState(initialEtapas);

  return (
    <div className="procesos-container">
      <div className="procesos-header">
        <h1>Ciclo de Cultivo Interactivo</h1>
        <p>Visualiza cada etapa de tu producción agrícola de forma sencilla e integrada.</p>
      </div>
      <div className="timeline">
        {etapas.map((etapa) => (
          <div key={etapa.id} className={`timeline-item ${etapa.completada ? 'completada' : ''}`}>
            <div className="timeline-content">
              {etapa.completada && <div className="check-mark">✔️</div>}
              <img src={etapa.icono} alt={etapa.nombre} className="etapa-icono" />
              <h2>{etapa.nombre}</h2>
              <p>{etapa.descripcion}</p>
            </div>
          </div>
        ))}
      </div>
      <div className="procesos-footer">
        <h2>La Evolución de la Gestión Agrícola</h2>
        <p>
          Este ciclo interactivo es una guía visual del proceso agrícola. En futuras versiones, se podrán añadir funcionalidades de gestión para una agricultura de precisión, más eficiente y rentable.
        </p>
      </div>
    </div>
  );
};

export default ProcesosServicios;
