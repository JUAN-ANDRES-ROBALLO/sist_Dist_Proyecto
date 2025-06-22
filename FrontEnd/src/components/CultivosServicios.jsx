import React, { useState } from 'react';
import '../styles/CultivosServicios.css';

const servicios = [
  { nombre: 'Siembra', categoria: 'Producción', descripcion: 'Servicio de siembra eficiente y tecnificado.', descripcionLarga: 'Ofrecemos un servicio de siembra eficiente y tecnificado, utilizando maquinaria de última generación y técnicas modernas para asegurar una germinación uniforme y un óptimo desarrollo de los cultivos. Nuestro equipo de expertos acompaña todo el proceso, desde la preparación del terreno hasta el monitoreo inicial del crecimiento.' , imagen: '/cultivos/Siembra.jpeg' },
  { nombre: 'Cosecha', categoria: 'Producción', descripcion: 'Cosecha mecanizada y optimizada para todo tipo de cultivos.', descripcionLarga: 'Realizamos cosechas mecanizadas y optimizadas, adaptándonos a las necesidades de cada tipo de cultivo. Utilizamos tecnología avanzada para minimizar pérdidas y maximizar la calidad del producto final, garantizando eficiencia y rapidez en cada etapa del proceso.' , imagen: '/cultivos/Cosecha.jpg' },
  { nombre: 'Topografía', categoria: 'Soporte', descripcion: 'Estudios topográficos para optimizar el uso del terreno.', descripcionLarga: 'Nuestros estudios topográficos permiten conocer en detalle las características del terreno, facilitando la planificación de cultivos, sistemas de riego y drenaje. Utilizamos herramientas digitales para obtener mapas precisos y recomendaciones personalizadas.' , imagen: '/cultivos/Topografia.jpeg' },
  { nombre: 'Veterinario', categoria: 'Soporte', descripcion: 'Atención veterinaria para el bienestar animal.', descripcionLarga: 'Brindamos atención veterinaria especializada para garantizar el bienestar y la salud de los animales en tu establecimiento. Realizamos controles sanitarios, vacunaciones, tratamientos preventivos y asesoramiento en manejo animal.' , imagen: '/cultivos/Veterinaria.jpeg' },
  { nombre: 'Fertilizante', categoria: 'Insumos', descripcion: 'Suministro y aplicación de fertilizantes de alta calidad.', descripcionLarga: 'Ofrecemos fertilizantes de alta calidad y un servicio de aplicación profesional, adaptado a las necesidades específicas de cada cultivo y suelo. Nuestro asesoramiento técnico asegura una nutrición balanceada y sostenible para maximizar el rendimiento.' , imagen: '/cultivos/fertilizante.jpg' },
  { nombre: 'Labrado', categoria: 'Producción', descripcion: 'Preparación de suelos con maquinaria moderna.', descripcionLarga: 'El labrado es fundamental para preparar el suelo antes de la siembra. Utilizamos maquinaria moderna que permite una adecuada aireación, descompactación y nivelación del terreno, mejorando la absorción de agua y nutrientes.' , imagen: '/cultivos/labrado.jpg' },
  { nombre: 'Abono', categoria: 'Insumos', descripcion: 'Venta y aplicación de abonos orgánicos y químicos.', descripcionLarga: 'Disponemos de una amplia variedad de abonos orgánicos y químicos, seleccionados para cada tipo de cultivo. Nuestro equipo asesora sobre la mejor estrategia de fertilización y realiza la aplicación de manera eficiente y segura.' , imagen: '/cultivos/abono.jpg' },
  { nombre: 'Riego', categoria: 'Soporte', descripcion: 'Sistemas de riego automatizados y asesoramiento.', descripcionLarga: 'Instalamos sistemas de riego automatizados y brindamos asesoramiento para optimizar el uso del agua. Analizamos las características del terreno y el cultivo para diseñar soluciones eficientes y sostenibles.' , imagen: '/cultivos/riego.jpg' },
  { nombre: 'Monitoreo de Plagas', categoria: 'Soporte', descripcion: 'Detección y control de plagas con tecnología avanzada.', descripcionLarga: 'Implementamos sistemas de monitoreo y control de plagas utilizando tecnología avanzada, como sensores y monitoreo remoto. Ofrecemos estrategias integradas para la prevención y el manejo eficiente de plagas, minimizando el uso de agroquímicos.' , imagen: '/cultivos/Monitoreo de plagas.jpg' },
];

const categorias = ['Todos', ...Array.from(new Set(servicios.map(s => s.categoria)))];

export default function CultivosServicios() {
  const [textoFiltro, setTextoFiltro] = useState('');
  const [categoriaFiltro, setCategoriaFiltro] = useState('Todos');
  const [modalServicio, setModalServicio] = useState(null);

  const serviciosFiltrados = servicios.filter(s => {
    const coincideTexto = s.nombre.toLowerCase().includes(textoFiltro.toLowerCase()) || s.descripcion.toLowerCase().includes(textoFiltro.toLowerCase());
    const coincideCategoria = categoriaFiltro === 'Todos' || s.categoria === categoriaFiltro;
    return coincideTexto && coincideCategoria;
  });

  return (
    <div className="cultivos-container">
      <div className="cultivos-filtros">
        <input
          type="text"
          placeholder="Buscar servicio..."
          value={textoFiltro}
          onChange={e => setTextoFiltro(e.target.value)}
        />
        <select value={categoriaFiltro} onChange={e => setCategoriaFiltro(e.target.value)}>
          {categorias.map(cat => (
            <option key={cat} value={cat}>{cat}</option>
          ))}
        </select>
      </div>
      <div className="cultivos-grid">
        {serviciosFiltrados.map((servicio, idx) => (
          <div className="cultivo-card" key={servicio.nombre + idx}>
            {servicio.imagen ? (
              <img src={servicio.imagen} alt={servicio.nombre} className="cultivo-img" />
            ) : (
              <div className="cultivo-img-placeholder">Imagen</div>
            )}
            <h3>{servicio.nombre}</h3>
            <p className="cultivo-categoria">{servicio.categoria}</p>
            <p>{servicio.descripcion}</p>
            <button className="cultivo-btn" onClick={() => setModalServicio(servicio)}>Ver más</button>
          </div>
        ))}
        {serviciosFiltrados.length === 0 && <p>No se encontraron servicios.</p>}
      </div>
      {modalServicio && (
        <div className="cultivo-modal-backdrop" onClick={() => setModalServicio(null)}>
          <div className="cultivo-modal" onClick={e => e.stopPropagation()}>
            <img src={modalServicio.imagen} alt={modalServicio.nombre} className="cultivo-modal-img" />
            <h2>{modalServicio.nombre}</h2>
            <p className="cultivo-categoria">{modalServicio.categoria}</p>
            <p>{modalServicio.descripcionLarga}</p>
            <button className="cultivo-btn" onClick={() => setModalServicio(null)}>Cerrar</button>
          </div>
        </div>
      )}
    </div>
  );
} 