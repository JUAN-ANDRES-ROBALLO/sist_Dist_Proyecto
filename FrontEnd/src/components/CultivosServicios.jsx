import React, { useState } from 'react';
import '../styles/CultivosServicios.css';

const servicios = [
  { nombre: 'Siembra', categoria: 'Producción', descripcion: 'Servicio de siembra eficiente y tecnificado.', imagen: '/cultivos/siembra.jpg' },
  { nombre: 'Cosecha', categoria: 'Producción', descripcion: 'Cosecha mecanizada y optimizada para todo tipo de cultivos.', imagen: '/cultivos/cosecha.jpg' },
  { nombre: 'Topografía', categoria: 'Soporte', descripcion: 'Estudios topográficos para optimizar el uso del terreno.', imagen: '/cultivos/topografia.jpg' },
  { nombre: 'Veterinario', categoria: 'Soporte', descripcion: 'Atención veterinaria para el bienestar animal.', imagen: '/cultivos/veterinario.jpg' },
  { nombre: 'Fertilizante', categoria: 'Insumos', descripcion: 'Suministro y aplicación de fertilizantes de alta calidad.' },
  { nombre: 'Labrado', categoria: 'Producción', descripcion: 'Preparación de suelos con maquinaria moderna.' },
  { nombre: 'Abono', categoria: 'Insumos', descripcion: 'Venta y aplicación de abonos orgánicos y químicos.' },
  { nombre: 'Riego', categoria: 'Soporte', descripcion: 'Sistemas de riego automatizados y asesoramiento.' },
  { nombre: 'Monitoreo de Plagas', categoria: 'Soporte', descripcion: 'Detección y control de plagas con tecnología avanzada.', imagen: '/cultivos/monitoreo.jpg' },
];

const categorias = ['Todos', ...Array.from(new Set(servicios.map(s => s.categoria)))];

export default function CultivosServicios() {
  const [textoFiltro, setTextoFiltro] = useState('');
  const [categoriaFiltro, setCategoriaFiltro] = useState('Todos');

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
          </div>
        ))}
        {serviciosFiltrados.length === 0 && <p>No se encontraron servicios.</p>}
      </div>
    </div>
  );
} 