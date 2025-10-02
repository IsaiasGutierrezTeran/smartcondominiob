# 🔒 MÓDULOS ESPECÍFICOS - SEGURIDAD Y MANTENIMIENTO

## 🛡️ **MÓDULO SEGURIDAD**

### Dashboard de Seguridad

```jsx
// src/components/seguridad/SeguridadDashboard.jsx
import React, { useState, useEffect } from 'react';
import seguridadService from '../../services/seguridadService';
import { Chart as ChartJS, CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend } from 'chart.js';
import { Bar } from 'react-chartjs-2';

ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);

function SeguridadDashboard() {
  const [resumen, setResumen] = useState(null);
  const [series, setSeries] = useState(null);
  const [topVisitantes, setTopVisitantes] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadDashboardData();
  }, []);

  const loadDashboardData = async () => {
    try {
      const [resumenData, seriesData, topData] = await Promise.all([
        seguridadService.getDashboardResumen(),
        seguridadService.getDashboardSeries(),
        seguridadService.getTopVisitantes()
      ]);
      
      setResumen(resumenData);
      setSeries(seriesData);
      setTopVisitantes(topData);
    } catch (error) {
      console.error('Error cargando dashboard de seguridad:', error);
    } finally {
      setLoading(false);
    }
  };

  const chartData = series ? {
    labels: series.fechas,
    datasets: [
      {
        label: 'Visitas por Día',
        data: series.visitas,
        backgroundColor: '#3498db',
        borderColor: '#2980b9',
        borderWidth: 1,
      },
    ],
  } : null;

  const chartOptions = {
    responsive: true,
    plugins: {
      legend: {
        position: 'top',
      },
      title: {
        display: true,
        text: 'Actividad de Visitas - Últimos 7 días',
      },
    },
  };

  if (loading) return <div>Cargando dashboard de seguridad...</div>;

  return (
    <div className="seguridad-dashboard">
      <h1>Dashboard de Seguridad</h1>

      {/* Métricas principales */}
      <div className="dashboard-cards">
        {resumen && (
          <>
            <div className="card metric-card">
              <h3>Visitas Hoy</h3>
              <div className="metric-value">{resumen.visitas_hoy}</div>
            </div>
            <div className="card metric-card">
              <h3>Visitantes Activos</h3>
              <div className="metric-value">{resumen.visitantes_activos}</div>
            </div>
            <div className="card metric-card">
              <h3>Eventos del Mes</h3>
              <div className="metric-value">{resumen.eventos_mes}</div>
            </div>
          </>
        )}
      </div>

      {/* Gráfico de actividad */}
      <div className="chart-section">
        <div className="card">
          {chartData && <Bar data={chartData} options={chartOptions} />}
        </div>
      </div>

      {/* Top visitantes */}
      <div className="top-visitantes">
        <div className="card">
          <h3>Top Visitantes del Mes</h3>
          <div className="visitantes-list">
            {topVisitantes.map((visitante, index) => (
              <div key={index} className="visitante-item">
                <span className="rank">#{index + 1}</span>
                <span className="name">{visitante.visitante}</span>
                <span className="visits">{visitante.total_visitas} visitas</span>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* Acciones rápidas */}
      <div className="quick-actions">
        <h3>Acciones Rápidas</h3>
        <div className="actions-grid">
          <button 
            className="action-btn"
            onClick={() => window.location.href = '/seguridad/visitantes'}
          >
            Gestionar Visitantes
          </button>
          <button 
            className="action-btn"
            onClick={() => window.location.href = '/seguridad/control-acceso'}
          >
            Control de Acceso
          </button>
          <button 
            className="action-btn"
            onClick={() => window.location.href = '/seguridad/eventos'}
          >
            Ver Eventos
          </button>
        </div>
      </div>
    </div>
  );
}

export default SeguridadDashboard;
```

### Control de Acceso

```jsx
// src/components/seguridad/ControlAcceso.jsx
import React, { useState } from 'react';
import seguridadService from '../../services/seguridadService';

function ControlAcceso() {
  const [placa, setPlaca] = useState('');
  const [loading, setLoading] = useState(false);
  const [resultado, setResultado] = useState(null);
  const [error, setError] = useState('');

  const handleControlAcceso = async (tipo) => {
    if (!placa.trim()) {
      setError('Por favor ingresa una placa');
      return;
    }

    setLoading(true);
    setError('');
    setResultado(null);

    try {
      let response;
      if (tipo === 'ingreso') {
        response = await seguridadService.controlAcceso({ placa });
      } else {
        response = await seguridadService.controlSalida({ placa });
      }
      
      setResultado({
        tipo,
        ...response
      });
      
      // Limpiar placa después de procesar
      setPlaca('');
      
    } catch (error) {
      setError('Error en control de acceso: ' + error.message);
    } finally {
      setLoading(false);
    }
  };

  const clearResults = () => {
    setResultado(null);
    setError('');
  };

  return (
    <div className="control-acceso">
      <h2>Control de Acceso Vehicular</h2>
      
      <div className="control-form">
        <div className="form-group">
          <label>Placa del vehículo:</label>
          <input
            type="text"
            value={placa}
            onChange={(e) => setPlaca(e.target.value.toUpperCase())}
            placeholder="Ej: ABC-123"
            className="placa-input"
            disabled={loading}
          />
        </div>

        <div className="control-buttons">
          <button
            onClick={() => handleControlAcceso('ingreso')}
            disabled={loading}
            className="btn-ingreso"
          >
            {loading ? 'Procesando...' : 'Registrar Ingreso'}
          </button>
          
          <button
            onClick={() => handleControlAcceso('salida')}
            disabled={loading}
            className="btn-salida"
          >
            {loading ? 'Procesando...' : 'Registrar Salida'}
          </button>
        </div>

        {(resultado || error) && (
          <button 
            onClick={clearResults}
            className="btn-secondary clear-btn"
          >
            Limpiar
          </button>
        )}
      </div>

      {/* Mostrar resultado */}
      {resultado && (
        <div className={`resultado-card ${resultado.acceso_permitido ? 'success' : 'denied'}`}>
          <h3>
            {resultado.tipo === 'ingreso' ? '🚗 Ingreso' : '🚙 Salida'} - 
            {resultado.acceso_permitido ? ' PERMITIDO' : ' DENEGADO'}
          </h3>
          <p><strong>Placa:</strong> {resultado.placa}</p>
          <p><strong>Mensaje:</strong> {resultado.mensaje}</p>
          {resultado.visitante && (
            <p><strong>Visitante:</strong> {resultado.visitante}</p>
          )}
          {resultado.propiedad && (
            <p><strong>Destino:</strong> Casa {resultado.propiedad}</p>
          )}
        </div>
      )}

      {/* Mostrar error */}
      {error && (
        <div className="error-card">
          <h3>❌ Error</h3>
          <p>{error}</p>
        </div>
      )}

      {/* Instrucciones */}
      <div className="instructions">
        <h3>💡 Instrucciones</h3>
        <ul>
          <li>Ingresa la placa del vehículo en formato ABC-123</li>
          <li>Usa "Registrar Ingreso" cuando un vehículo entre al condominio</li>
          <li>Usa "Registrar Salida" cuando un vehículo salga del condominio</li>
          <li>El sistema verificará automáticamente si el vehículo está autorizado</li>
        </ul>
      </div>
    </div>
  );
}

export default ControlAcceso;
```

### Lista de Visitantes

```jsx
// src/components/seguridad/VisitantesList.jsx
import React, { useState, useEffect } from 'react';
import seguridadService from '../../services/seguridadService';

function VisitantesList() {
  const [visitantes, setVisitantes] = useState([]);
  const [loading, setLoading] = useState(true);
  const [showForm, setShowForm] = useState(false);
  const [formData, setFormData] = useState({
    nombre_completo: '',
    documento: '',
    telefono: '',
    email: ''
  });

  useEffect(() => {
    loadVisitantes();
  }, []);

  const loadVisitantes = async () => {
    try {
      const data = await seguridadService.getVisitantes();
      setVisitantes(data.results || data);
    } catch (error) {
      console.error('Error cargando visitantes:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await seguridadService.createVisitante(formData);
      setShowForm(false);
      setFormData({
        nombre_completo: '',
        documento: '',
        telefono: '',
        email: ''
      });
      loadVisitantes();
    } catch (error) {
      alert('Error creando visitante: ' + error.message);
    }
  };

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  if (loading) return <div>Cargando visitantes...</div>;

  return (
    <div className="visitantes-list">
      <div className="header">
        <h2>Gestión de Visitantes</h2>
        <button 
          onClick={() => setShowForm(!showForm)}
          className="btn-primary"
        >
          {showForm ? 'Cancelar' : 'Nuevo Visitante'}
        </button>
      </div>

      {showForm && (
        <div className="form-container">
          <h3>Nuevo Visitante</h3>
          <form onSubmit={handleSubmit}>
            <input
              type="text"
              name="nombre_completo"
              placeholder="Nombre completo"
              value={formData.nombre_completo}
              onChange={handleChange}
              required
            />
            <input
              type="text"
              name="documento"
              placeholder="Documento de identidad"
              value={formData.documento}
              onChange={handleChange}
              required
            />
            <input
              type="tel"
              name="telefono"
              placeholder="Teléfono"
              value={formData.telefono}
              onChange={handleChange}
            />
            <input
              type="email"
              name="email"
              placeholder="Email (opcional)"
              value={formData.email}
              onChange={handleChange}
            />
            <button type="submit">Registrar Visitante</button>
          </form>
        </div>
      )}

      <div className="visitantes-grid">
        {visitantes.map((visitante) => (
          <div key={visitante.id} className="visitante-card">
            <h3>{visitante.nombre_completo}</h3>
            <p><strong>Documento:</strong> {visitante.documento}</p>
            <p><strong>Teléfono:</strong> {visitante.telefono}</p>
            {visitante.email && (
              <p><strong>Email:</strong> {visitante.email}</p>
            )}
          </div>
        ))}
      </div>
    </div>
  );
}

export default VisitantesList;
```

## 🔧 **MÓDULO MANTENIMIENTO**

### Lista de Solicitudes

```jsx
// src/components/mantenimiento/SolicitudesList.jsx
import React, { useState, useEffect } from 'react';
import mantenimientoService from '../../services/mantenimientoService';

function SolicitudesList() {
  const [solicitudes, setSolicitudes] = useState([]);
  const [loading, setLoading] = useState(true);
  const [showForm, setShowForm] = useState(false);
  const [formData, setFormData] = useState({
    titulo: '',
    descripcion: '',
    prioridad: 'media',
    propiedad_id: ''
  });

  useEffect(() => {
    loadSolicitudes();
  }, []);

  const loadSolicitudes = async () => {
    try {
      const data = await mantenimientoService.getSolicitudes();
      setSolicitudes(data.results || data);
    } catch (error) {
      console.error('Error cargando solicitudes:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await mantenimientoService.createSolicitud(formData);
      setShowForm(false);
      setFormData({
        titulo: '',
        descripcion: '',
        prioridad: 'media',
        propiedad_id: ''
      });
      loadSolicitudes();
    } catch (error) {
      alert('Error creando solicitud: ' + error.message);
    }
  };

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const updateEstado = async (id, nuevoEstado) => {
    try {
      await mantenimientoService.updateSolicitud(id, { estado: nuevoEstado });
      loadSolicitudes();
    } catch (error) {
      alert('Error actualizando estado: ' + error.message);
    }
  };

  const getPrioridadColor = (prioridad) => {
    const colors = {
      'baja': '#28a745',
      'media': '#ffc107', 
      'alta': '#fd7e14',
      'critica': '#dc3545'
    };
    return colors[prioridad] || '#6c757d';
  };

  const getEstadoColor = (estado) => {
    const colors = {
      'pendiente': '#ffc107',
      'en_proceso': '#17a2b8',
      'completado': '#28a745',
      'cancelado': '#dc3545'
    };
    return colors[estado] || '#6c757d';
  };

  if (loading) return <div>Cargando solicitudes...</div>;

  return (
    <div className="solicitudes-list">
      <div className="header">
        <h2>Solicitudes de Mantenimiento</h2>
        <button 
          onClick={() => setShowForm(!showForm)}
          className="btn-primary"
        >
          {showForm ? 'Cancelar' : 'Nueva Solicitud'}
        </button>
      </div>

      {showForm && (
        <div className="form-container">
          <h3>Nueva Solicitud de Mantenimiento</h3>
          <form onSubmit={handleSubmit}>
            <input
              type="text"
              name="titulo"
              placeholder="Título de la solicitud"
              value={formData.titulo}
              onChange={handleChange}
              required
            />
            
            <textarea
              name="descripcion"
              placeholder="Describe el problema o solicitud"
              value={formData.descripcion}
              onChange={handleChange}
              rows="4"
              required
            />
            
            <select
              name="prioridad"
              value={formData.prioridad}
              onChange={handleChange}
            >
              <option value="baja">Baja</option>
              <option value="media">Media</option>
              <option value="alta">Alta</option>
              <option value="critica">Crítica</option>
            </select>
            
            <input
              type="number"
              name="propiedad_id"
              placeholder="ID de la propiedad"
              value={formData.propiedad_id}
              onChange={handleChange}
              required
            />
            
            <button type="submit">Crear Solicitud</button>
          </form>
        </div>
      )}

      <div className="solicitudes-grid">
        {solicitudes.map((solicitud) => (
          <div key={solicitud.id} className="solicitud-card">
            <div className="solicitud-header">
              <h3>{solicitud.titulo}</h3>
              <div className="badges">
                <span 
                  className="badge prioridad"
                  style={{ backgroundColor: getPrioridadColor(solicitud.prioridad) }}
                >
                  {solicitud.prioridad}
                </span>
                <span 
                  className="badge estado"
                  style={{ backgroundColor: getEstadoColor(solicitud.estado) }}
                >
                  {solicitud.estado}
                </span>
              </div>
            </div>
            
            <p className="descripcion">{solicitud.descripcion}</p>
            
            <div className="solicitud-info">
              <p><strong>Propiedad:</strong> Casa {solicitud.propiedad_numero}</p>
              <p><strong>Solicitado por:</strong> {solicitud.solicitado_por}</p>
              <p><strong>Fecha:</strong> {new Date(solicitud.fecha_solicitud).toLocaleDateString()}</p>
              {solicitud.asignado_a_nombre && (
                <p><strong>Asignado a:</strong> {solicitud.asignado_a_nombre}</p>
              )}
            </div>

            {/* Botones de estado */}
            <div className="estado-buttons">
              {solicitud.estado === 'pendiente' && (
                <button
                  onClick={() => updateEstado(solicitud.id, 'en_proceso')}
                  className="btn-small btn-info"
                >
                  Iniciar
                </button>
              )}
              {solicitud.estado === 'en_proceso' && (
                <button
                  onClick={() => updateEstado(solicitud.id, 'completado')}
                  className="btn-small btn-success"
                >
                  Completar
                </button>
              )}
              {solicitud.estado !== 'cancelado' && solicitud.estado !== 'completado' && (
                <button
                  onClick={() => updateEstado(solicitud.id, 'cancelado')}
                  className="btn-small btn-danger"
                >
                  Cancelar
                </button>
              )}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default SolicitudesList;
```

## 🔔 **MÓDULO NOTIFICACIONES**

### Lista de Notificaciones

```jsx
// src/components/notificaciones/NotificacionesList.jsx
import React, { useState, useEffect } from 'react';
import notificacionesService from '../../services/notificacionesService';

function NotificacionesList() {
  const [notificaciones, setNotificaciones] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadNotificaciones();
  }, []);

  const loadNotificaciones = async () => {
    try {
      const data = await notificacionesService.getNotificaciones();
      setNotificaciones(data.results || data);
    } catch (error) {
      console.error('Error cargando notificaciones:', error);
    } finally {
      setLoading(false);
    }
  };

  const markAsRead = async (id) => {
    try {
      await notificacionesService.markAsRead(id);
      loadNotificaciones(); // Recargar lista
    } catch (error) {
      console.error('Error marcando como leída:', error);
    }
  };

  const getNotificationIcon = (tipo) => {
    const icons = {
      'info': '📋',
      'warning': '⚠️',
      'error': '❌',
      'success': '✅',
      'security': '🛡️',
      'maintenance': '🔧',
      'finance': '💰'
    };
    return icons[tipo] || '📢';
  };

  if (loading) return <div>Cargando notificaciones...</div>;

  return (
    <div className="notificaciones-list">
      <h2>Mis Notificaciones</h2>

      {notificaciones.length === 0 ? (
        <div className="empty-state">
          <p>No tienes notificaciones</p>
        </div>
      ) : (
        <div className="notificaciones-container">
          {notificaciones.map((notificacion) => (
            <div
              key={notificacion.id}
              className={`notificacion-card ${notificacion.leida ? 'read' : 'unread'}`}
            >
              <div className="notification-icon">
                {getNotificationIcon(notificacion.tipo)}
              </div>
              
              <div className="notification-content">
                <h3>{notificacion.titulo}</h3>
                <p>{notificacion.mensaje}</p>
                <small className="timestamp">
                  {new Date(notificacion.fecha_envio).toLocaleString()}
                </small>
              </div>

              {!notificacion.leida && (
                <button
                  onClick={() => markAsRead(notificacion.id)}
                  className="mark-read-btn"
                  title="Marcar como leída"
                >
                  ✓
                </button>
              )}
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default NotificacionesList;
```

## 🚀 **INSTRUCCIONES FINALES PARA IMPLEMENTAR**

### 1. **Crear el proyecto React**

```bash
# Crear proyecto
npx create-react-app smart-condominio-frontend
cd smart-condominio-frontend

# Instalar dependencias
npm install react-router-dom
npm install chart.js react-chartjs-2  # Para gráficos
npm install date-fns  # Para manejo de fechas

# Opcional: UI Libraries
npm install @mui/material @emotion/react @emotion/styled
# O
npm install antd
```

### 2. **Crear estructura de carpetas**

```bash
mkdir -p src/components/common
mkdir -p src/components/usuarios
mkdir -p src/components/condominio
mkdir -p src/components/finanzas
mkdir -p src/components/seguridad
mkdir -p src/components/mantenimiento
mkdir -p src/components/notificaciones
mkdir -p src/services
mkdir -p src/hooks
mkdir -p src/context
mkdir -p src/config
mkdir -p src/utils
mkdir -p src/styles
```

### 3. **Configurar proxy para desarrollo**

En `package.json` agrega:

```json
{
  "name": "smart-condominio-frontend",
  "proxy": "http://localhost:8000",
  ...
}
```

### 4. **Variables de entorno**

Crea `.env` en la raíz:

```env
# .env
REACT_APP_API_BASE_URL=http://localhost:8000/api
REACT_APP_API_TIMEOUT=10000

# Para producción (comentar en desarrollo)
# REACT_APP_API_BASE_URL=https://smartcondominiob-backend.onrender.com/api
```

### 5. **Actualizar configuración API**

```javascript
// src/config/api.js
const API_CONFIG = {
  BASE_URL: process.env.REACT_APP_API_BASE_URL || 'http://127.0.0.1:8000/api',
  TIMEOUT: parseInt(process.env.REACT_APP_API_TIMEOUT) || 10000,
  DEFAULT_HEADERS: {
    'Content-Type': 'application/json',
  }
};

export default API_CONFIG;
```

### 6. **Comandos para desarrollo**

```bash
# Desarrollo
npm start          # Inicia en puerto 3000

# Construcción para producción
npm run build

# Testing
npm test

# Análisis del bundle
npm run build
npx serve -s build
```

### 7. **Deployment en Netlify/Vercel**

```bash
# Build para producción
npm run build

# Para Netlify
# Sube la carpeta 'build' o conecta con Git

# Para Vercel
npx vercel --prod
```

## ✅ **CHECKLIST FINAL**

- [ ] ✅ Backend Django corriendo en puerto 8000
- [ ] ✅ CORS configurados correctamente
- [ ] ✅ Crear proyecto React con estructura de carpetas
- [ ] ✅ Implementar servicios de API
- [ ] ✅ Configurar routing y autenticación
- [ ] ✅ Crear componentes por módulo
- [ ] ✅ Probar conexión login
- [ ] ✅ Implementar navegación
- [ ] ✅ Agregar estilos CSS
- [ ] ✅ Testing de funcionalidades
- [ ] ✅ Build para producción

**🎉 ¡Con esta guía tienes todo lo necesario para crear un frontend React completo que se conecte perfectamente con tu backend Django!**

¿Necesitas ayuda con algún aspecto específico o quieres que profundice en algún módulo en particular?