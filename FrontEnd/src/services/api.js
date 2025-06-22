// Configuración base para las llamadas a la API
const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost';

// Configuración de headers comunes
const getHeaders = () => ({
  'Content-Type': 'application/json',
  // Aquí puedes agregar headers de autenticación si es necesario
  // 'Authorization': `Bearer ${localStorage.getItem('token')}`,
});

// Función helper para hacer peticiones HTTP
const apiRequest = async (endpoint, options = {}) => {
  const url = `${API_BASE_URL}${endpoint}`;
  const config = {
    headers: getHeaders(),
    ...options,
  };

  try {
    const response = await fetch(url, config);
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    
    return await response.json();
  } catch (error) {
    console.error('API request failed:', error);
    throw error;
  }
};

// Servicios para Usuarios
export const usuariosService = {
  // Login
  login: (credentials) => apiRequest('/api/usuarios/login/', {
    method: 'POST',
    body: JSON.stringify(credentials),
  }),
  
  // Registro
  register: (userData) => apiRequest('/api/usuarios/register/', {
    method: 'POST',
    body: JSON.stringify(userData),
  }),
  
  // Obtener perfil del usuario
  getProfile: () => apiRequest('/api/usuarios/profile/'),
  
  // Actualizar perfil
  updateProfile: (userData) => apiRequest('/api/usuarios/profile/', {
    method: 'PUT',
    body: JSON.stringify(userData),
  }),
};

// Servicios para Terrenos
export const terrenosService = {
  // Obtener todos los terrenos
  getAll: () => apiRequest('/api/terrenos/'),
  
  // Obtener terreno por ID
  getById: (id) => apiRequest(`/api/terrenos/${id}/`),
  
  // Crear nuevo terreno
  create: (terrenoData) => apiRequest('/api/terrenos/', {
    method: 'POST',
    body: JSON.stringify(terrenoData),
  }),
  
  // Actualizar terreno
  update: (id, terrenoData) => apiRequest(`/api/terrenos/${id}/`, {
    method: 'PUT',
    body: JSON.stringify(terrenoData),
  }),
  
  // Eliminar terreno
  delete: (id) => apiRequest(`/api/terrenos/${id}/`, {
    method: 'DELETE',
  }),
};

// Servicios para Maquinaria
export const maquinariaService = {
  // Obtener toda la maquinaria
  getAll: () => apiRequest('/api/maquinaria/'),
  
  // Obtener maquinaria por ID
  getById: (id) => apiRequest(`/api/maquinaria/${id}/`),
  
  // Crear nueva maquinaria
  create: (maquinariaData) => apiRequest('/api/maquinaria/', {
    method: 'POST',
    body: JSON.stringify(maquinariaData),
  }),
  
  // Actualizar maquinaria
  update: (id, maquinariaData) => apiRequest(`/api/maquinaria/${id}/`, {
    method: 'PUT',
    body: JSON.stringify(maquinariaData),
  }),
  
  // Eliminar maquinaria
  delete: (id) => apiRequest(`/api/maquinaria/${id}/`, {
    method: 'DELETE',
  }),
};

// Servicios para Notificaciones
export const notificacionesService = {
  // Obtener todas las notificaciones
  getAll: () => apiRequest('/api/notificaciones/'),
  
  // Obtener notificación por ID
  getById: (id) => apiRequest(`/api/notificaciones/${id}/`),
  
  // Crear nueva notificación
  create: (notificacionData) => apiRequest('/api/notificaciones/', {
    method: 'POST',
    body: JSON.stringify(notificacionData),
  }),
  
  // Marcar como leída
  markAsRead: (id) => apiRequest(`/api/notificaciones/${id}/mark-read/`, {
    method: 'POST',
  }),
  
  // Eliminar notificación
  delete: (id) => apiRequest(`/api/notificaciones/${id}/`, {
    method: 'DELETE',
  }),
};

export default {
  usuarios: usuariosService,
  terrenos: terrenosService,
  maquinaria: maquinariaService,
  notificaciones: notificacionesService,
}; 