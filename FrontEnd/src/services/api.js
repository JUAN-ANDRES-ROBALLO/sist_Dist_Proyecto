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
      const errorData = await response.json().catch(() => ({}));
      throw new Error(errorData.error || `HTTP error! status: ${response.status}`);
    }
    
    return await response.json();
  } catch (error) {
    console.error('API request failed:', error);
    throw error;
  }
};

// Servicios para Usuarios
export const usuariosService = {
  // Login - el backend espera email y password
  login: (credentials) => apiRequest('/api/usuarios/login/', {
    method: 'POST',
    body: JSON.stringify({
      email: credentials.email,
      password: credentials.password
    }),
  }),
  
  // Registro - el backend espera cedula, nombre, email, password, password_confirm
  register: (userData) => apiRequest('/api/usuarios/signup/', {
    method: 'POST',
    body: JSON.stringify({
      cedula: userData.cedula,
      nombre: userData.nombre,
      email: userData.email,
      password: userData.password,
      password_confirm: userData.password_confirm
    }),
  }),
  
  // Obtener lista de usuarios
  getAll: () => apiRequest('/api/usuarios/'),
  
  // Obtener usuario por cédula
  getByCedula: (cedula) => apiRequest(`/api/usuarios/${cedula}/`),
  
  // Health check
  health: () => apiRequest('/api/usuarios/health/'),
};

// Servicios para Terrenos
export const terrenosService = {
  // Health check
  health: () => apiRequest('/api/terrenos/health/'),
  
  // Fincas
  getFincas: () => apiRequest('/api/terrenos/fincas/'),
  createFinca: (fincaData) => apiRequest('/api/terrenos/fincas/agregar/', {
    method: 'POST',
    body: JSON.stringify(fincaData),
  }),
  deleteFinca: (fincaData) => apiRequest('/api/terrenos/fincas/eliminar/', {
    method: 'POST',
    body: JSON.stringify(fincaData),
  }),
  
  // Parcelas
  getParcelas: () => apiRequest('/api/terrenos/parcelas/'),
  createParcela: (parcelaData) => apiRequest('/api/terrenos/parcelas/agregar/', {
    method: 'POST',
    body: JSON.stringify(parcelaData),
  }),
  deleteParcela: (parcelaData) => apiRequest('/api/terrenos/parcelas/eliminar/', {
    method: 'POST',
    body: JSON.stringify(parcelaData),
  }),
  
  // Cultivos
  getCultivos: () => apiRequest('/api/terrenos/cultivos/'),
  createCultivo: (cultivoData) => apiRequest('/api/terrenos/cultivos/agregar/', {
    method: 'POST',
    body: JSON.stringify(cultivoData),
  }),
};

// Servicios para Maquinaria
export const maquinariaService = {
  // Health check
  health: () => apiRequest('/api/maquinaria/health/'),
  
  // Maquinaria
  getAll: () => apiRequest('/api/maquinaria/maquinaria/'),
  create: (maquinariaData) => apiRequest('/api/maquinaria/maquinaria/crear/', {
    method: 'POST',
    body: JSON.stringify(maquinariaData),
  }),
  delete: (id) => apiRequest(`/api/maquinaria/maquinaria/${id}/eliminar/`, {
    method: 'POST',
  }),
  
  // Ventas
  getVentas: () => apiRequest('/api/maquinaria/ventas/'),
  createVenta: (ventaData) => apiRequest('/api/maquinaria/ventas/crear/', {
    method: 'POST',
    body: JSON.stringify(ventaData),
  }),
  
  // Reservas
  getReservas: () => apiRequest('/api/maquinaria/reservas/'),
  createReserva: (reservaData) => apiRequest('/api/maquinaria/reservas/crear/', {
    method: 'POST',
    body: JSON.stringify(reservaData),
  }),
};

// Servicios para Notificaciones
export const notificacionesService = {
  // Health check
  health: () => apiRequest('/api/notificaciones/health/'),
  
  // Notificaciones
  getAll: () => apiRequest('/api/notificaciones/notificaciones/'),
  create: (notificacionData) => apiRequest('/api/notificaciones/notificaciones/crear/', {
    method: 'POST',
    body: JSON.stringify(notificacionData),
  }),
  delete: (id) => apiRequest(`/api/notificaciones/notificaciones/${id}/eliminar/`, {
    method: 'POST',
  }),
};

export default {
  usuarios: usuariosService,
  terrenos: terrenosService,
  maquinaria: maquinariaService,
  notificaciones: notificacionesService,
}; 