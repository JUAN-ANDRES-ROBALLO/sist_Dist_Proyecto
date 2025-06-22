import React, { useState } from 'react';
import '../styles/MaquinariaServicios.css';

const maquinarias = [
  { nombre: 'Tractor', categoria: 'Tracción', descripcion: 'Vehículo fundamental para múltiples tareas agrícolas.', descripcionLarga: 'El tractor es la máquina más versátil del campo, utilizado para arar, sembrar, transportar y accionar otros implementos agrícolas. Su potencia y adaptabilidad lo convierten en el aliado principal de cualquier explotación agrícola.', imagen: '/maquinaria/tractor.jpg' },
  { nombre: 'Cosechadora', categoria: 'Cosecha', descripcion: 'Máquina para recolectar granos y otros cultivos.', descripcionLarga: 'La cosechadora permite recolectar, trillar y limpiar granos en una sola pasada, optimizando el tiempo y reduciendo pérdidas. Existen modelos para diferentes cultivos como trigo, soja, maíz y arroz.', imagen: '/maquinaria/Cosechadora.jpg' },
  { nombre: 'Sembradora', categoria: 'Siembra', descripcion: 'Equipo para depositar semillas en el suelo.', descripcionLarga: 'La sembradora asegura una distribución uniforme de las semillas, regulando profundidad y distancia entre ellas. Es clave para lograr una germinación homogénea y maximizar el rendimiento del cultivo.', imagen: '/maquinaria/Sembradora.jpg' },
  { nombre: 'Pulverizadora', categoria: 'Aplicación', descripcion: 'Equipo para aplicar fitosanitarios y fertilizantes líquidos.', descripcionLarga: 'La pulverizadora permite la aplicación precisa de agroquímicos y fertilizantes líquidos, protegiendo los cultivos de plagas y enfermedades. Puede ser autopropulsada o de arrastre.', imagen: '/maquinaria/pulverizadora.jpg' },
  { nombre: 'Arado', categoria: 'Preparación de suelo', descripcion: 'Implemento para remover y airear la tierra.', descripcionLarga: 'El arado es esencial para preparar el terreno antes de la siembra, mejorando la estructura del suelo y facilitando la incorporación de residuos orgánicos.', imagen: '/maquinaria/arado.jpg' },
  { nombre: 'Empacadora', categoria: 'Forraje', descripcion: 'Máquina para compactar y embalar forrajes.', descripcionLarga: 'La empacadora transforma el forraje en pacas compactas y fáciles de transportar o almacenar, conservando su calidad y facilitando la logística en la explotación ganadera.', imagen: '/maquinaria/empacadora.jpg' },
  { nombre: 'Rastra', categoria: 'Preparación de suelo', descripcion: 'Implemento para nivelar y desmenuzar el suelo.', descripcionLarga: 'La rastra se utiliza después del arado para desmenuzar los terrones, nivelar el terreno y preparar una cama de siembra óptima.', imagen: '/maquinaria/rastra.jpg' },
  { nombre: 'Fertilizadora', categoria: 'Aplicación', descripcion: 'Equipo para distribuir fertilizantes sólidos.', descripcionLarga: 'La fertilizadora permite una aplicación uniforme de fertilizantes granulados o en polvo, asegurando una nutrición equilibrada para los cultivos.', imagen: '/maquinaria/fertilizadora.jpg' },
  { nombre: 'Segadora', categoria: 'Corte', descripcion: 'Máquina para cortar pasto y forrajes.', descripcionLarga: 'La segadora es utilizada para el corte eficiente de pasturas y forrajes, facilitando la recolección y el manejo del alimento para el ganado.', imagen: '/maquinaria/segador.jpg' },
];

const categorias = ['Todos', ...Array.from(new Set(maquinarias.map(m => m.categoria)))]

export default function MaquinariaServicios() {
  const [textoFiltro, setTextoFiltro] = useState('');
  const [categoriaFiltro, setCategoriaFiltro] = useState('Todos');
  const [modalMaquinaria, setModalMaquinaria] = useState(null);

  const maquinariasFiltradas = maquinarias.filter(m => {
    const coincideTexto = m.nombre.toLowerCase().includes(textoFiltro.toLowerCase()) || m.descripcion.toLowerCase().includes(textoFiltro.toLowerCase());
    const coincideCategoria = categoriaFiltro === 'Todos' || m.categoria === categoriaFiltro;
    return coincideTexto && coincideCategoria;
  });

  return (
    <div className="maquinaria-container">
      <div className="maquinaria-filtros">
        <input
          type="text"
          placeholder="Buscar maquinaria..."
          value={textoFiltro}
          onChange={e => setTextoFiltro(e.target.value)}
        />
        <select value={categoriaFiltro} onChange={e => setCategoriaFiltro(e.target.value)}>
          {categorias.map(cat => (
            <option key={cat} value={cat}>{cat}</option>
          ))}
        </select>
      </div>
      <div className="maquinaria-grid">
        {maquinariasFiltradas.map((maquinaria, idx) => (
          <div className="maquinaria-card" key={maquinaria.nombre + idx}>
            {maquinaria.imagen ? (
              <img src={maquinaria.imagen} alt={maquinaria.nombre} className="maquinaria-img" />
            ) : (
              <div className="maquinaria-img-placeholder">Imagen</div>
            )}
            <h3>{maquinaria.nombre}</h3>
            <p className="maquinaria-categoria">{maquinaria.categoria}</p>
            <p>{maquinaria.descripcion}</p>
            <button className="maquinaria-btn" onClick={() => setModalMaquinaria(maquinaria)}>Ver más</button>
          </div>
        ))}
        {maquinariasFiltradas.length === 0 && <p>No se encontraron maquinarias.</p>}
      </div>
      {modalMaquinaria && (
        <div className="maquinaria-modal-backdrop" onClick={() => setModalMaquinaria(null)}>
          <div className="maquinaria-modal" onClick={e => e.stopPropagation()}>
            <img src={modalMaquinaria.imagen} alt={modalMaquinaria.nombre} className="maquinaria-modal-img" />
            <h2>{modalMaquinaria.nombre}</h2>
            <p className="maquinaria-categoria">{modalMaquinaria.categoria}</p>
            <p>{modalMaquinaria.descripcionLarga}</p>
            <button className="maquinaria-btn" onClick={() => setModalMaquinaria(null)}>Cerrar</button>
          </div>
        </div>
      )}
    </div>
  );
} 