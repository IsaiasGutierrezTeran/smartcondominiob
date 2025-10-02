# 🚀 GUÍA COMPLETA REACT PARA CONECTAR CON TU BACKEND DJANGO

## 📋 **CONFIGURACIÓN INICIAL**

### 1. **Configuración de URLs del Backend**

```javascript
// src/config/api.js
const API_CONFIG = {
  // Para desarrollo local
  BASE_URL: 'http://127.0.0.1:8000/api',
  
  // Para producción (cuando despliegues en Render)
  // BASE_URL: 'https://smartcondominiob-backend.onrender.com/api',
  
  TIMEOUT: 10000,
  
  // Headers por defecto
  DEFAULT_HEADERS: {
    'Content-Type': 'application/json',
  }
};

export default API_CONFIG;
```

### 2. **Servicio de Autenticación Base**

```javascript
// src/services/authService.js
import API_CONFIG from '../config/api';

class AuthService {
  constructor() {
    this.baseURL = API_CONFIG.BASE_URL;
    this.token = localStorage.getItem('authToken');
  }

  // Configurar headers con token
  getHeaders(includeAuth = true) {
    const headers = { ...API_CONFIG.DEFAULT_HEADERS };
    
    if (includeAuth && this.token) {
      headers['Authorization'] = `Token ${this.token}`;
    }
    
    return headers;
  }

  // Login
  async login(username, password) {
    try {
      const response = await fetch(`${this.baseURL}/usuarios/login/`, {
        method: 'POST',
        headers: this.getHeaders(false),
        body: JSON.stringify({ username, password })
      });

      if (!response.ok) {
        throw new Error(`Error ${response.status}: ${response.statusText}`);
      }

      const data = await response.json();
      
      if (data.token) {
        this.token = data.token;
        localStorage.setItem('authToken', data.token);
        localStorage.setItem('userData', JSON.stringify(data.user || {}));
      }

      return data;
    } catch (error) {
      console.error('Error en login:', error);
      throw error;
    }
  }

  // Registro
  async register(userData) {
    try {
      const response = await fetch(`${this.baseURL}/usuarios/registro/`, {
        method: 'POST',
        headers: this.getHeaders(false),
        body: JSON.stringify(userData)
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.message || 'Error en registro');
      }

      return await response.json();
    } catch (error) {
      console.error('Error en registro:', error);
      throw error;
    }
  }

  // Obtener perfil
  async getProfile() {
    try {
      const response = await fetch(`${this.baseURL}/usuarios/perfil/`, {
        headers: this.getHeaders()
      });

      if (!response.ok) {
        throw new Error('Error al obtener perfil');
      }

      return await response.json();
    } catch (error) {
      console.error('Error obteniendo perfil:', error);
      throw error;
    }
  }

  // Logout
  logout() {
    this.token = null;
    localStorage.removeItem('authToken');
    localStorage.removeItem('userData');
  }

  // Verificar si está autenticado
  isAuthenticated() {
    return !!this.token;
  }

  // Obtener datos del usuario
  getUserData() {
    const userData = localStorage.getItem('userData');
    return userData ? JSON.parse(userData) : null;
  }
}

export default new AuthService();
```

## 🏢 **SERVICIOS POR MÓDULO**

### 3. **Servicio de Usuarios**

```javascript
// src/services/usuariosService.js
import API_CONFIG from '../config/api';
import authService from './authService';

class UsuariosService {
  constructor() {
    this.baseURL = `${API_CONFIG.BASE_URL}/usuarios`;
  }

  async makeRequest(endpoint, options = {}) {
    try {
      const response = await fetch(`${this.baseURL}${endpoint}`, {
        headers: authService.getHeaders(),
        ...options
      });

      if (!response.ok) {
        throw new Error(`Error ${response.status}: ${response.statusText}`);
      }

      return await response.json();
    } catch (error) {
      console.error('Error en petición:', error);
      throw error;
    }
  }

  // Obtener residentes (solo admin)
  async getResidentes() {
    return this.makeRequest('/residentes/');
  }

  // Crear residente
  async createResidente(residenteData) {
    return this.makeRequest('/residentes/', {
      method: 'POST',
      body: JSON.stringify(residenteData)
    });
  }

  // Actualizar residente
  async updateResidente(id, residenteData) {
    return this.makeRequest(`/residentes/${id}/`, {
      method: 'PUT',
      body: JSON.stringify(residenteData)
    });
  }

  // Eliminar residente
  async deleteResidente(id) {
    return this.makeRequest(`/residentes/${id}/`, {
      method: 'DELETE'
    });
  }

  // Registrar rostro para IA
  async registrarRostro(formData) {
    const response = await fetch(`${this.baseURL}/reconocimiento/registrar-rostro/`, {
      method: 'POST',
      headers: {
        'Authorization': `Token ${authService.token}`
        // No incluir Content-Type para FormData
      },
      body: formData
    });

    if (!response.ok) {
      throw new Error('Error al registrar rostro');
    }

    return await response.json();
  }
}

export default new UsuariosService();
```

### 4. **Servicio de Condominio**

```javascript
// src/services/condominioService.js
import API_CONFIG from '../config/api';
import authService from './authService';

class CondominioService {
  constructor() {
    this.baseURL = `${API_CONFIG.BASE_URL}/condominio`;
  }

  async makeRequest(endpoint, options = {}) {
    try {
      const response = await fetch(`${this.baseURL}${endpoint}`, {
        headers: authService.getHeaders(),
        ...options
      });

      if (!response.ok) {
        throw new Error(`Error ${response.status}`);
      }

      return await response.json();
    } catch (error) {
      throw error;
    }
  }

  // Propiedades
  async getPropiedades() {
    return this.makeRequest('/propiedades/');
  }

  async createPropiedad(propiedadData) {
    return this.makeRequest('/propiedades/', {
      method: 'POST',
      body: JSON.stringify(propiedadData)
    });
  }

  async updatePropiedad(id, propiedadData) {
    return this.makeRequest(`/propiedades/${id}/`, {
      method: 'PUT',
      body: JSON.stringify(propiedadData)
    });
  }

  // Áreas comunes
  async getAreasComunes() {
    return this.makeRequest('/areas-comunes/');
  }

  async createAreaComun(areaData) {
    return this.makeRequest('/areas-comunes/', {
      method: 'POST',
      body: JSON.stringify(areaData)
    });
  }

  // Reservas
  async getReservas() {
    return this.makeRequest('/reservas/');
  }

  async createReserva(reservaData) {
    return this.makeRequest('/reservas/', {
      method: 'POST',
      body: JSON.stringify(reservaData)
    });
  }

  async updateReserva(id, reservaData) {
    return this.makeRequest(`/reservas/${id}/`, {
      method: 'PUT',
      body: JSON.stringify(reservaData)
    });
  }

  // Avisos
  async getAvisos() {
    return this.makeRequest('/avisos/');
  }

  async createAviso(avisoData) {
    return this.makeRequest('/avisos/', {
      method: 'POST',
      body: JSON.stringify(avisoData)
    });
  }
}

export default new CondominioService();
```

### 5. **Servicio de Finanzas**

```javascript
// src/services/finanzasService.js
import API_CONFIG from '../config/api';
import authService from './authService';

class FinanzasService {
  constructor() {
    this.baseURL = `${API_CONFIG.BASE_URL}/finanzas`;
  }

  async makeRequest(endpoint, options = {}) {
    try {
      const response = await fetch(`${this.baseURL}${endpoint}`, {
        headers: authService.getHeaders(),
        ...options
      });

      if (!response.ok) {
        throw new Error(`Error ${response.status}`);
      }

      return await response.json();
    } catch (error) {
      throw error;
    }
  }

  // Gastos
  async getGastos(filters = {}) {
    const params = new URLSearchParams(filters);
    return this.makeRequest(`/gastos/?${params}`);
  }

  async createGasto(gastoData) {
    return this.makeRequest('/gastos/', {
      method: 'POST',
      body: JSON.stringify(gastoData)
    });
  }

  // Pagos
  async getPagos(filters = {}) {
    const params = new URLSearchParams(filters);
    return this.makeRequest(`/pagos/?${params}`);
  }

  async createPago(pagoData) {
    return this.makeRequest('/pagos/', {
      method: 'POST',
      body: JSON.stringify(pagoData)
    });
  }

  // Multas
  async getMultas(filters = {}) {
    const params = new URLSearchParams(filters);
    return this.makeRequest(`/multas/?${params}`);
  }

  async createMulta(multaData) {
    return this.makeRequest('/multas/', {
      method: 'POST',
      body: JSON.stringify(multaData)
    });
  }

  // Estado de cuenta
  async getEstadoCuenta() {
    return this.makeRequest('/estado-cuenta-unificado/');
  }

  // Crear checkout de Stripe
  async crearCheckoutStripe(pagoData) {
    return this.makeRequest('/pagos/crear-checkout-stripe/', {
      method: 'POST',
      body: JSON.stringify(pagoData)
    });
  }

  // Generar expensas masivas
  async generarExpensas(expensaData) {
    return this.makeRequest('/generar-expensas/', {
      method: 'POST',
      body: JSON.stringify(expensaData)
    });
  }

  // Reportes
  async getReporteMorosidad() {
    return this.makeRequest('/reporte-morosidad/');
  }

  async getReporteResumen() {
    return this.makeRequest('/reporte-resumen/');
  }

  async getReporteFinanciero() {
    return this.makeRequest('/reporte-financiero/');
  }
}

export default new FinanzasService();
```

### 6. **Servicio de Seguridad**

```javascript
// src/services/seguridadService.js
import API_CONFIG from '../config/api';
import authService from './authService';

class SeguridadService {
  constructor() {
    this.baseURL = `${API_CONFIG.BASE_URL}/seguridad`;
  }

  async makeRequest(endpoint, options = {}) {
    try {
      const response = await fetch(`${this.baseURL}${endpoint}`, {
        headers: authService.getHeaders(),
        ...options
      });

      if (!response.ok) {
        throw new Error(`Error ${response.status}`);
      }

      return await response.json();
    } catch (error) {
      throw error;
    }
  }

  // Visitantes
  async getVisitantes() {
    return this.makeRequest('/visitantes/');
  }

  async createVisitante(visitanteData) {
    return this.makeRequest('/visitantes/', {
      method: 'POST',
      body: JSON.stringify(visitanteData)
    });
  }

  async updateVisitante(id, visitanteData) {
    return this.makeRequest(`/visitantes/${id}/`, {
      method: 'PUT',
      body: JSON.stringify(visitanteData)
    });
  }

  // Visitas
  async getVisitas() {
    return this.makeRequest('/visitas/');
  }

  async createVisita(visitaData) {
    return this.makeRequest('/visitas/', {
      method: 'POST',
      body: JSON.stringify(visitaData)
    });
  }

  // Vehículos
  async getVehiculos() {
    return this.makeRequest('/vehiculos/');
  }

  async createVehiculo(vehiculoData) {
    return this.makeRequest('/vehiculos/', {
      method: 'POST',
      body: JSON.stringify(vehiculoData)
    });
  }

  // Control de acceso
  async controlAcceso(placaData) {
    return this.makeRequest('/control-acceso/', {
      method: 'POST',
      body: JSON.stringify(placaData)
    });
  }

  async controlSalida(placaData) {
    return this.makeRequest('/control-salida/', {
      method: 'POST',
      body: JSON.stringify(placaData)
    });
  }

  // Dashboard
  async getDashboardResumen() {
    return this.makeRequest('/dashboard/resumen/');
  }

  async getDashboardSeries() {
    return this.makeRequest('/dashboard/series/');
  }

  async getTopVisitantes() {
    return this.makeRequest('/dashboard/top-visitantes/');
  }

  // Eventos de seguridad
  async getEventosSeguridad() {
    return this.makeRequest('/eventos/');
  }

  // Detecciones IA
  async getDetecciones() {
    return this.makeRequest('/detecciones/');
  }
}

export default new SeguridadService();
```

### 7. **Servicio de Mantenimiento**

```javascript
// src/services/mantenimientoService.js
import API_CONFIG from '../config/api';
import authService from './authService';

class MantenimientoService {
  constructor() {
    this.baseURL = `${API_CONFIG.BASE_URL}/mantenimiento`;
  }

  async makeRequest(endpoint, options = {}) {
    try {
      const response = await fetch(`${this.baseURL}${endpoint}`, {
        headers: authService.getHeaders(),
        ...options
      });

      if (!response.ok) {
        throw new Error(`Error ${response.status}`);
      }

      return await response.json();
    } catch (error) {
      throw error;
    }
  }

  // Solicitudes de mantenimiento
  async getSolicitudes() {
    return this.makeRequest('/solicitudes/');
  }

  async createSolicitud(solicitudData) {
    return this.makeRequest('/solicitudes/', {
      method: 'POST',
      body: JSON.stringify(solicitudData)
    });
  }

  async updateSolicitud(id, solicitudData) {
    return this.makeRequest(`/solicitudes/${id}/`, {
      method: 'PUT',
      body: JSON.stringify(solicitudData)
    });
  }

  async deleteSolicitud(id) {
    return this.makeRequest(`/solicitudes/${id}/`, {
      method: 'DELETE'
    });
  }

  // Personal de mantenimiento
  async getPersonal() {
    return this.makeRequest('/personal/');
  }

  async createPersonal(personalData) {
    return this.makeRequest('/personal/', {
      method: 'POST',
      body: JSON.stringify(personalData)
    });
  }

  async updatePersonal(id, personalData) {
    return this.makeRequest(`/personal/${id}/`, {
      method: 'PUT',
      body: JSON.stringify(personalData)
    });
  }
}

export default new MantenimientoService();
```

### 8. **Servicio de Notificaciones**

```javascript
// src/services/notificacionesService.js
import API_CONFIG from '../config/api';
import authService from './authService';

class NotificacionesService {
  constructor() {
    this.baseURL = `${API_CONFIG.BASE_URL}/notificaciones`;
  }

  async makeRequest(endpoint, options = {}) {
    try {
      const response = await fetch(`${this.baseURL}${endpoint}`, {
        headers: authService.getHeaders(),
        ...options
      });

      if (!response.ok) {
        throw new Error(`Error ${response.status}`);
      }

      return await response.json();
    } catch (error) {
      throw error;
    }
  }

  // Notificaciones
  async getNotificaciones() {
    return this.makeRequest('/notificaciones/');
  }

  async markAsRead(id) {
    return this.makeRequest(`/notificaciones/${id}/marcar-leida/`, {
      method: 'POST'
    });
  }

  // Dispositivos
  async registrarDispositivo(deviceData) {
    return this.makeRequest('/dispositivos/', {
      method: 'POST',
      body: JSON.stringify(deviceData)
    });
  }

  // Enviar notificación (admin)
  async enviarNotificacion(notificationData) {
    return this.makeRequest('/enviar/', {
      method: 'POST',
      body: JSON.stringify(notificationData)
    });
  }
}

export default new NotificacionesService();
```

### 9. **Servicio de Auditoría**

```javascript
// src/services/auditoriaService.js
import API_CONFIG from '../config/api';
import authService from './authService';

class AuditoriaService {
  constructor() {
    this.baseURL = `${API_CONFIG.BASE_URL}/auditoria`;
  }

  async makeRequest(endpoint, options = {}) {
    try {
      const response = await fetch(`${this.baseURL}${endpoint}`, {
        headers: authService.getHeaders(),
        ...options
      });

      if (!response.ok) {
        throw new Error(`Error ${response.status}`);
      }

      return await response.json();
    } catch (error) {
      throw error;
    }
  }

  // Obtener bitácora
  async getBitacora(filters = {}) {
    const params = new URLSearchParams(filters);
    return this.makeRequest(`/bitacora/?${params}`);
  }
}

export default new AuditoriaService();
```

## 🔗 **HOOK PERSONALIZADO PARA REACT**

### 10. **Hook useApi**

```javascript
// src/hooks/useApi.js
import { useState, useEffect } from 'react';

function useApi(serviceFunction, dependencies = []) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        setLoading(true);
        setError(null);
        const result = await serviceFunction();
        setData(result);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, dependencies);

  const refetch = async () => {
    try {
      setLoading(true);
      setError(null);
      const result = await serviceFunction();
      setData(result);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return { data, loading, error, refetch };
}

export default useApi;
```

## 📱 **COMPONENTES DE EJEMPLO**

### 11. **Componente de Login**

```jsx
// src/components/Login.jsx
import React, { useState } from 'react';
import authService from '../services/authService';

function Login({ onLoginSuccess }) {
  const [credentials, setCredentials] = useState({
    username: '',
    password: ''
  });
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleChange = (e) => {
    setCredentials({
      ...credentials,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');

    try {
      const result = await authService.login(
        credentials.username,
        credentials.password
      );
      
      console.log('Login exitoso:', result);
      onLoginSuccess && onLoginSuccess(result);
      
    } catch (error) {
      setError(error.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="login-container">
      <h2>Iniciar Sesión</h2>
      
      {error && (
        <div className="error-message">
          {error}
        </div>
      )}

      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label>Usuario:</label>
          <input
            type="text"
            name="username"
            value={credentials.username}
            onChange={handleChange}
            required
          />
        </div>

        <div className="form-group">
          <label>Contraseña:</label>
          <input
            type="password"
            name="password"
            value={credentials.password}
            onChange={handleChange}
            required
          />
        </div>

        <button type="submit" disabled={loading}>
          {loading ? 'Iniciando sesión...' : 'Iniciar Sesión'}
        </button>
      </form>
    </div>
  );
}

export default Login;
```

### 12. **Componente Dashboard**

```jsx
// src/components/Dashboard.jsx
import React from 'react';
import useApi from '../hooks/useApi';
import seguridadService from '../services/seguridadService';
import finanzasService from '../services/finanzasService';

function Dashboard() {
  const { 
    data: resumenSeguridad, 
    loading: loadingSeguridad 
  } = useApi(() => seguridadService.getDashboardResumen());
  
  const { 
    data: resumenFinanzas, 
    loading: loadingFinanzas 
  } = useApi(() => finanzasService.getReporteResumen());

  if (loadingSeguridad || loadingFinanzas) {
    return <div>Cargando dashboard...</div>;
  }

  return (
    <div className="dashboard">
      <h1>Dashboard del Condominio</h1>
      
      <div className="dashboard-cards">
        {/* Seguridad */}
        <div className="card">
          <h3>Seguridad</h3>
          {resumenSeguridad && (
            <>
              <p>Visitas hoy: {resumenSeguridad.visitas_hoy}</p>
              <p>Visitantes activos: {resumenSeguridad.visitantes_activos}</p>
              <p>Eventos del mes: {resumenSeguridad.eventos_mes}</p>
            </>
          )}
        </div>

        {/* Finanzas */}
        <div className="card">
          <h3>Finanzas</h3>
          {resumenFinanzas && (
            <>
              <p>Ingresos del mes: ${resumenFinanzas.ingresos_mes}</p>
              <p>Gastos del mes: ${resumenFinanzas.gastos_mes}</p>
              <p>Propiedades morosas: {resumenFinanzas.propiedades_morosas}</p>
            </>
          )}
        </div>
      </div>
    </div>
  );
}

export default Dashboard;
```

¿Quieres que continúe con más componentes específicos o algún módulo en particular?