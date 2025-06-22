// Global state
let currentUser = null;

// API Base URLs
const API_BASE = {
    usuarios: '/api/usuarios',
    terrenos: '/api/terrenos',
    maquinaria: '/api/maquinaria',
    notificaciones: '/api/notificaciones'
};

// Utility functions
function showScreen(screenId) {
    document.querySelectorAll('.screen').forEach(screen => {
        screen.classList.remove('active');
    });
    document.getElementById(screenId).classList.add('active');
}

function showError(elementId, message) {
    const errorElement = document.getElementById(elementId);
    errorElement.textContent = message;
    errorElement.classList.add('show');
    setTimeout(() => {
        errorElement.classList.remove('show');
    }, 5000);
}

function clearError(elementId) {
    const errorElement = document.getElementById(elementId);
    errorElement.classList.remove('show');
    errorElement.textContent = '';
}

// Navigation functions
function showInitial() {
    showScreen('initial-screen');
    currentUser = null;
}

function showLogin() {
    showScreen('login-screen');
    clearError('login-error');
}

function showSignup() {
    showScreen('signup-screen');
    clearError('signup-error');
}

function showHomepage() {
    showScreen('homepage-screen');
    if (currentUser) {
        document.getElementById('user-name').textContent = currentUser.nombre;
    }
}

// API functions
async function apiCall(url, options = {}) {
    try {
        const response = await fetch(url, {
            headers: {
                'Content-Type': 'application/json',
                ...options.headers
            },
            ...options
        });
        
        const data = await response.json();
        
        if (!response.ok) {
            throw new Error(data.error || 'Error en la petición');
        }
        
        return data;
    } catch (error) {
        console.error('API Error:', error);
        throw error;
    }
}

// Authentication functions
async function loginUser(email, password) {
    try {
        const response = await apiCall(`${API_BASE.usuarios}/login/`, {
            method: 'POST',
            body: JSON.stringify({ email, password })
        });
        
        currentUser = response.user;
        localStorage.setItem('currentUser', JSON.stringify(currentUser));
        showHomepage();
    } catch (error) {
        showError('login-error', error.message);
    }
}

async function signupUser(userData) {
    try {
        const response = await apiCall(`${API_BASE.usuarios}/signup/`, {
            method: 'POST',
            body: JSON.stringify(userData)
        });
        
        showInitial();
        alert('Usuario registrado exitosamente. Por favor, inicia sesión.');
    } catch (error) {
        showError('signup-error', error.message);
    }
}

function logout() {
    currentUser = null;
    localStorage.removeItem('currentUser');
    showInitial();
}

// Navigation to other applications
function navigateToTerrenos() {
    if (!currentUser) {
        alert('Debe iniciar sesión primero');
        return;
    }
    
    const url = new URL('/terrenos.html', window.location.origin);
    url.searchParams.set('user', JSON.stringify(currentUser));
    window.location.href = url.toString();
}

function navigateToMaquinaria() {
    if (!currentUser) {
        alert('Debe iniciar sesión primero');
        return;
    }
    
    const url = new URL('/maquinaria.html', window.location.origin);
    url.searchParams.set('user', JSON.stringify(currentUser));
    window.location.href = url.toString();
}

function navigateToNotificaciones() {
    if (!currentUser) {
        alert('Debe iniciar sesión primero');
        return;
    }
    
    const url = new URL('/notificaciones.html', window.location.origin);
    url.searchParams.set('user', JSON.stringify(currentUser));
    window.location.href = url.toString();
}

// Event listeners
document.addEventListener('DOMContentLoaded', function() {
    // Check if user is already logged in
    const savedUser = localStorage.getItem('currentUser');
    if (savedUser) {
        try {
            currentUser = JSON.parse(savedUser);
            showHomepage();
        } catch (error) {
            localStorage.removeItem('currentUser');
            showInitial();
        }
    }

    // Login form handler
    document.getElementById('login-form').addEventListener('submit', function(e) {
        e.preventDefault();
        const email = document.getElementById('login-email').value;
        const password = document.getElementById('login-password').value;
        loginUser(email, password);
    });

    // Signup form handler
    document.getElementById('signup-form').addEventListener('submit', function(e) {
        e.preventDefault();
        const userData = {
            cedula: document.getElementById('signup-cedula').value,
            nombre: document.getElementById('signup-nombre').value,
            email: document.getElementById('signup-email').value,
            password: document.getElementById('signup-password').value
        };
        signupUser(userData);
    });
});

// Export functions for use in other modules
window.appFunctions = {
    showInitial,
    showLogin,
    showSignup,
    showHomepage,
    logout,
    navigateToTerrenos,
    navigateToMaquinaria,
    navigateToNotificaciones,
    apiCall,
    currentUser: () => currentUser
}; 