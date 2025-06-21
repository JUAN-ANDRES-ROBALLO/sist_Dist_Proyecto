import React from 'react';
import '../styles/GestionarEtapaModal.css';

const GestionarEtapaModal = ({ etapa, onClose, onSave }) => {
  if (!etapa) {
    return null;
  }

  const handleSave = (e) => {
    e.preventDefault();
    // Aquí se manejaría la lógica para guardar los datos
    console.log(`Guardando datos para la etapa: ${etapa.nombre}`);
    onSave(etapa.id); // Llama a la función onSave para actualizar el estado
    onClose(); // Cierra el modal
  };

  return (
    <div className="modal-backdrop-gestion">
      <div className="modal-gestion">
        <div className="modal-header-gestion">
          <h2>Gestionando: {etapa.nombre}</h2>
          <button onClick={onClose} className="close-modal-gestion">×</button>
        </div>
        <div className="modal-body-gestion">
          <form onSubmit={handleSave}>
            <div className="form-group-gestion">
              <label htmlFor="fechaInicio">Fecha de Inicio</label>
              <input type="date" id="fechaInicio" />
            </div>
            <div className="form-group-gestion">
              <label htmlFor="fechaFin">Fecha de Finalización</label>
              <input type="date" id="fechaFin" />
            </div>
            <div className="form-group-gestion">
              <label htmlFor="notas">Notas Adicionales</label>
              <textarea id="notas" rows="4" placeholder="Añade tus observaciones..."></textarea>
            </div>
            <div className="modal-footer-gestion">
              <button type="button" onClick={onClose} className="btn-cancel-gestion">Cancelar</button>
              <button type="submit" className="btn-save-gestion">Guardar y Marcar como Completada</button>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
};

export default GestionarEtapaModal; 