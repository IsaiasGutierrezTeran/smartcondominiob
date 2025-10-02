// Test de CORS para React - Código que usarías en tu aplicación React
// Este código muestra exactamente cómo conectar React con tu backend Django

// 1. Configuración base de la API
const API_BASE_URL = 'http://127.0.0.1:8000/api';

// 2. Servicio de autenticación (lo que usarías en React)
const authService = {
  // Login de usuario
  async login(username, password) {
    try {
      const response = await fetch(`${API_BASE_URL}/usuarios/login/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          // CORS headers se manejan automáticamente por el navegador
        },
        credentials: 'include', // Para cookies si las usas
        body: JSON.stringify({
          username,
          password
        })
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      
      // Guardar token si el login es exitoso
      if (data.token) {
        localStorage.setItem('authToken', data.token);
      }
      
      return data;
    } catch (error) {
      console.error('Error en login:', error);
      throw error;
    }
  },

  // Obtener datos con autenticación
  async fetchWithAuth(endpoint) {
    const token = localStorage.getItem('authToken');
    
    try {
      const response = await fetch(`${API_BASE_URL}${endpoint}`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Token ${token}`, // Formato de token de Django REST
        },
        credentials: 'include',
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      return await response.json();
    } catch (error) {
      console.error('Error en petición autenticada:', error);
      throw error;
    }
  }
};

// 3. Ejemplo de uso en componente React
const ejemploUsoReact = `
import React, { useState } from 'react';

function LoginComponent() {
  const [credentials, setCredentials] = useState({ username: '', password: '' });
  const [loading, setLoading] = useState(false);

  const handleLogin = async (e) => {
    e.preventDefault();
    setLoading(true);
    
    try {
      const result = await authService.login(credentials.username, credentials.password);
      console.log('Login exitoso:', result);
      
      // Redirigir o actualizar estado de la app
      // navigate('/dashboard');
      
    } catch (error) {
      console.error('Error de login:', error);
      alert('Error de login: ' + error.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleLogin}>
      <input
        type="text"
        placeholder="Usuario"
        value={credentials.username}
        onChange={(e) => setCredentials({...credentials, username: e.target.value})}
      />
      <input
        type="password"
        placeholder="Contraseña"
        value={credentials.password}
        onChange={(e) => setCredentials({...credentials, password: e.target.value})}
      />
      <button type="submit" disabled={loading}>
        {loading ? 'Iniciando sesión...' : 'Iniciar Sesión'}
      </button>
    </form>
  );
}

export default LoginComponent;
`;

// 4. Endpoints disponibles en tu API
const endpoints = {
  // Autenticación
  login: '/usuarios/login/',
  registro: '/usuarios/registro/',
  
  // Gestión de usuarios
  residentes: '/usuarios/residentes/',
  perfil: '/usuarios/perfil/',
  
  // Condominio
  propiedades: '/condominio/propiedades/',
  amenidades: '/condominio/amenidades/',
  reservas: '/condominio/reservas/',
  
  // Seguridad
  visitantes: '/seguridad/visitantes/',
  controlAcceso: '/seguridad/control-acceso/',
  
  // Finanzas
  pagos: '/finanzas/pagos/',
  recibos: '/finanzas/recibos/',
  
  // Mantenimiento
  solicitudes: '/mantenimiento/solicitudes/',
  
  // Notificaciones
  notificaciones: '/notificaciones/notificaciones/',
};

// 5. Verificación de estado de CORS
console.log('📋 CONFIGURACIÓN DE CORS PARA REACT');
console.log('='.repeat(50));
console.log('✅ URL Base del API:', API_BASE_URL);
console.log('✅ Puertos permitidos: 3000 (Create React App), 5173 (Vite)');
console.log('✅ Endpoints disponibles:', Object.keys(endpoints).length);
console.log('');
console.log('🔧 Para probar la conexión:');
console.log('1. Inicia tu app React: npm start (puerto 3000) o npm run dev (puerto 5173)');
console.log('2. Usa authService.login("admin", "admin123") en el navegador');
console.log('3. Revisa la consola del navegador para ver las peticiones CORS');
console.log('');
console.log('⚠️  Si ves errores de CORS:');
console.log('- Verifica que el servidor Django esté corriendo en puerto 8000');
console.log('- Confirma que tu React está en puerto 3000 o 5173');
console.log('- Revisa la consola del servidor Django para ver las peticiones OPTIONS');

// Exportar para uso en React
if (typeof module !== 'undefined' && module.exports) {
  module.exports = { authService, endpoints };
}