# 📱 COMPONENTES REACT ESPECÍFICOS POR MÓDULO

## 🏢 **MÓDULO USUARIOS**

### Componente Lista de Residentes

```jsx
// src/components/usuarios/ResidentesList.jsx
import React, { useState, useEffect } from 'react';
import usuariosService from '../../services/usuariosService';

function ResidentesList() {
  const [residentes, setResidentes] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    loadResidentes();
  }, []);

  const loadResidentes = async () => {
    try {
      setLoading(true);
      const data = await usuariosService.getResidentes();
      setResidentes(data.results || data);
    } catch (error) {
      setError('Error cargando residentes: ' + error.message);
    } finally {
      setLoading(false);
    }
  };

  const handleDelete = async (id) => {
    if (window.confirm('¿Estás seguro de eliminar este residente?')) {
      try {
        await usuariosService.deleteResidente(id);
        loadResidentes(); // Recargar lista
      } catch (error) {
        alert('Error eliminando residente: ' + error.message);
      }
    }
  };

  if (loading) return <div>Cargando residentes...</div>;
  if (error) return <div className="error">{error}</div>;

  return (
    <div className="residentes-list">
      <h2>Residentes del Condominio</h2>
      
      <div className="table-container">
        <table>
          <thead>
            <tr>
              <th>ID</th>
              <th>Usuario</th>
              <th>Propiedad</th>
              <th>Rol</th>
              <th>Acciones</th>
            </tr>
          </thead>
          <tbody>
            {residentes.map((residente) => (
              <tr key={residente.id}>
                <td>{residente.id}</td>
                <td>
                  {residente.usuario?.first_name} {residente.usuario?.last_name}
                  <br />
                  <small>{residente.usuario?.username}</small>
                </td>
                <td>Casa {residente.propiedad?.numero_casa}</td>
                <td>{residente.rol}</td>
                <td>
                  <button 
                    onClick={() => handleDelete(residente.id)}
                    className="btn-danger"
                  >
                    Eliminar
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default ResidentesList;
```

### Componente Registro Facial

```jsx
// src/components/usuarios/RegistroFacial.jsx
import React, { useState, useRef } from 'react';
import usuariosService from '../../services/usuariosService';

function RegistroFacial() {
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState('');
  const [error, setError] = useState('');
  const [preview, setPreview] = useState(null);
  const fileInputRef = useRef(null);

  const handleFileSelect = (e) => {
    const file = e.target.files[0];
    if (file) {
      // Mostrar preview
      const reader = new FileReader();
      reader.onload = (e) => setPreview(e.target.result);
      reader.readAsDataURL(file);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const file = fileInputRef.current.files[0];
    
    if (!file) {
      setError('Por favor selecciona una imagen');
      return;
    }

    setLoading(true);
    setError('');
    setMessage('');

    try {
      const formData = new FormData();
      formData.append('imagen', file);

      const result = await usuariosService.registrarRostro(formData);
      setMessage('Rostro registrado exitosamente para reconocimiento IA');
      
      // Limpiar formulario
      fileInputRef.current.value = '';
      setPreview(null);
      
    } catch (error) {
      setError('Error registrando rostro: ' + error.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="registro-facial">
      <h2>Registro Facial para IA</h2>
      <p>Sube una foto clara de tu rostro para el sistema de reconocimiento</p>

      {message && <div className="success-message">{message}</div>}
      {error && <div className="error-message">{error}</div>}

      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label>Seleccionar imagen:</label>
          <input
            ref={fileInputRef}
            type="file"
            accept="image/*"
            onChange={handleFileSelect}
            required
          />
        </div>

        {preview && (
          <div className="image-preview">
            <img 
              src={preview} 
              alt="Vista previa" 
              style={{ maxWidth: '200px', maxHeight: '200px' }}
            />
          </div>
        )}

        <button type="submit" disabled={loading}>
          {loading ? 'Registrando...' : 'Registrar Rostro'}
        </button>
      </form>
    </div>
  );
}

export default RegistroFacial;
```

## 🏠 **MÓDULO CONDOMINIO**

### Componente Propiedades

```jsx
// src/components/condominio/PropiedadesList.jsx
import React, { useState, useEffect } from 'react';
import condominioService from '../../services/condominioService';

function PropiedadesList() {
  const [propiedades, setPropiedades] = useState([]);
  const [loading, setLoading] = useState(true);
  const [showForm, setShowForm] = useState(false);
  const [formData, setFormData] = useState({
    numero_casa: '',
    propietario_id: '',
    metros_cuadrados: ''
  });

  useEffect(() => {
    loadPropiedades();
  }, []);

  const loadPropiedades = async () => {
    try {
      const data = await condominioService.getPropiedades();
      setPropiedades(data.results || data);
    } catch (error) {
      console.error('Error cargando propiedades:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await condominioService.createPropiedad(formData);
      setShowForm(false);
      setFormData({ numero_casa: '', propietario_id: '', metros_cuadrados: '' });
      loadPropiedades();
    } catch (error) {
      alert('Error creando propiedad: ' + error.message);
    }
  };

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  if (loading) return <div>Cargando propiedades...</div>;

  return (
    <div className="propiedades-list">
      <div className="header">
        <h2>Propiedades del Condominio</h2>
        <button 
          onClick={() => setShowForm(!showForm)}
          className="btn-primary"
        >
          {showForm ? 'Cancelar' : 'Nueva Propiedad'}
        </button>
      </div>

      {showForm && (
        <div className="form-container">
          <h3>Nueva Propiedad</h3>
          <form onSubmit={handleSubmit}>
            <input
              type="text"
              name="numero_casa"
              placeholder="Número de casa"
              value={formData.numero_casa}
              onChange={handleChange}
              required
            />
            <input
              type="number"
              name="propietario_id"
              placeholder="ID del propietario"
              value={formData.propietario_id}
              onChange={handleChange}
              required
            />
            <input
              type="number"
              name="metros_cuadrados"
              placeholder="Metros cuadrados"
              step="0.01"
              value={formData.metros_cuadrados}
              onChange={handleChange}
              required
            />
            <button type="submit">Crear Propiedad</button>
          </form>
        </div>
      )}

      <div className="properties-grid">
        {propiedades.map((propiedad) => (
          <div key={propiedad.id} className="property-card">
            <h3>Casa N° {propiedad.numero_casa}</h3>
            <p><strong>Propietario:</strong> {propiedad.propietario?.first_name} {propiedad.propietario?.last_name}</p>
            <p><strong>Metros²:</strong> {propiedad.metros_cuadrados}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default PropiedadesList;
```

### Componente Reservas

```jsx
// src/components/condominio/ReservasList.jsx
import React, { useState, useEffect } from 'react';
import condominioService from '../../services/condominioService';

function ReservasList() {
  const [reservas, setReservas] = useState([]);
  const [areasComunes, setAreasComunes] = useState([]);
  const [loading, setLoading] = useState(true);
  const [showForm, setShowForm] = useState(false);
  const [formData, setFormData] = useState({
    area_comun: '',
    fecha_reserva: '',
    hora_inicio: '',
    hora_fin: '',
    observaciones: ''
  });

  useEffect(() => {
    loadData();
  }, []);

  const loadData = async () => {
    try {
      const [reservasData, areasData] = await Promise.all([
        condominioService.getReservas(),
        condominioService.getAreasComunes()
      ]);
      
      setReservas(reservasData.results || reservasData);
      setAreasComunes(areasData.results || areasData);
    } catch (error) {
      console.error('Error cargando datos:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await condominioService.createReserva(formData);
      setShowForm(false);
      setFormData({
        area_comun: '',
        fecha_reserva: '',
        hora_inicio: '',
        hora_fin: '',
        observaciones: ''
      });
      loadData();
    } catch (error) {
      alert('Error creando reserva: ' + error.message);
    }
  };

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  if (loading) return <div>Cargando reservas...</div>;

  return (
    <div className="reservas-list">
      <div className="header">
        <h2>Reservas de Áreas Comunes</h2>
        <button 
          onClick={() => setShowForm(!showForm)}
          className="btn-primary"
        >
          {showForm ? 'Cancelar' : 'Nueva Reserva'}
        </button>
      </div>

      {showForm && (
        <div className="form-container">
          <h3>Nueva Reserva</h3>
          <form onSubmit={handleSubmit}>
            <select
              name="area_comun"
              value={formData.area_comun}
              onChange={handleChange}
              required
            >
              <option value="">Seleccionar área común</option>
              {areasComunes.map((area) => (
                <option key={area.id} value={area.id}>
                  {area.nombre} - ${area.costo_reserva}
                </option>
              ))}
            </select>

            <input
              type="date"
              name="fecha_reserva"
              value={formData.fecha_reserva}
              onChange={handleChange}
              required
            />

            <input
              type="time"
              name="hora_inicio"
              value={formData.hora_inicio}
              onChange={handleChange}
              required
            />

            <input
              type="time"
              name="hora_fin"
              value={formData.hora_fin}
              onChange={handleChange}
              required
            />

            <textarea
              name="observaciones"
              placeholder="Observaciones (opcional)"
              value={formData.observaciones}
              onChange={handleChange}
            />

            <button type="submit">Crear Reserva</button>
          </form>
        </div>
      )}

      <div className="reservas-grid">
        {reservas.map((reserva) => (
          <div key={reserva.id} className="reserva-card">
            <h3>{reserva.area_comun_nombre}</h3>
            <p><strong>Fecha:</strong> {reserva.fecha_reserva}</p>
            <p><strong>Horario:</strong> {reserva.hora_inicio} - {reserva.hora_fin}</p>
            <p><strong>Estado:</strong> 
              <span className={`status ${reserva.estado}`}>
                {reserva.estado}
              </span>
            </p>
            {reserva.observaciones && (
              <p><strong>Observaciones:</strong> {reserva.observaciones}</p>
            )}
          </div>
        ))}
      </div>
    </div>
  );
}

export default ReservasList;
```

## 💰 **MÓDULO FINANZAS**

### Componente Dashboard Financiero

```jsx
// src/components/finanzas/FinanzasDashboard.jsx
import React, { useState, useEffect } from 'react';
import finanzasService from '../../services/finanzasService';

function FinanzasDashboard() {
  const [estadoCuenta, setEstadoCuenta] = useState(null);
  const [reporteResumen, setReporteResumen] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadDashboardData();
  }, []);

  const loadDashboardData = async () => {
    try {
      const [estadoData, resumenData] = await Promise.all([
        finanzasService.getEstadoCuenta(),
        finanzasService.getReporteResumen()
      ]);
      
      setEstadoCuenta(estadoData);
      setReporteResumen(resumenData);
    } catch (error) {
      console.error('Error cargando dashboard financiero:', error);
    } finally {
      setLoading(false);
    }
  };

  if (loading) return <div>Cargando dashboard financiero...</div>;

  return (
    <div className="finanzas-dashboard">
      <h1>Dashboard Financiero</h1>

      <div className="dashboard-cards">
        {/* Resumen general */}
        {reporteResumen && (
          <div className="card">
            <h3>Resumen del Mes</h3>
            <div className="stats">
              <div className="stat">
                <span className="label">Ingresos:</span>
                <span className="value income">${reporteResumen.ingresos_mes}</span>
              </div>
              <div className="stat">
                <span className="label">Gastos:</span>
                <span className="value expense">${reporteResumen.gastos_mes}</span>
              </div>
              <div className="stat">
                <span className="label">Balance:</span>
                <span className={`value ${(reporteResumen.ingresos_mes - reporteResumen.gastos_mes) >= 0 ? 'positive' : 'negative'}`}>
                  ${reporteResumen.ingresos_mes - reporteResumen.gastos_mes}
                </span>
              </div>
            </div>
          </div>
        )}

        {/* Estado de cuenta */}
        {estadoCuenta && (
          <div className="card">
            <h3>Mi Estado de Cuenta</h3>
            <div className="account-summary">
              {estadoCuenta.length > 0 ? (
                <div>
                  <p>Tienes {estadoCuenta.length} movimientos</p>
                  <div className="recent-movements">
                    {estadoCuenta.slice(0, 3).map((movimiento, index) => (
                      <div key={index} className="movement">
                        <span>{movimiento.descripcion}</span>
                        <span className="amount">${movimiento.monto}</span>
                      </div>
                    ))}
                  </div>
                </div>
              ) : (
                <p>No tienes movimientos pendientes</p>
              )}
            </div>
          </div>
        )}
      </div>

      {/* Acciones rápidas */}
      <div className="quick-actions">
        <h3>Acciones Rápidas</h3>
        <div className="actions-grid">
          <button className="action-btn">Ver Gastos</button>
          <button className="action-btn">Ver Pagos</button>
          <button className="action-btn">Generar Reporte</button>
          <button className="action-btn">Pagar Online</button>
        </div>
      </div>
    </div>
  );
}

export default FinanzasDashboard;
```

### Componente Gestión de Gastos

```jsx
// src/components/finanzas/GastosList.jsx
import React, { useState, useEffect } from 'react';
import finanzasService from '../../services/finanzasService';

function GastosList() {
  const [gastos, setGastos] = useState([]);
  const [loading, setLoading] = useState(true);
  const [showForm, setShowForm] = useState(false);
  const [filters, setFilters] = useState({
    fecha_inicio: '',
    fecha_fin: '',
    monto_min: '',
    monto_max: ''
  });
  const [formData, setFormData] = useState({
    monto: '',
    descripcion: '',
    categoria: '',
    fecha_vencimiento: ''
  });

  useEffect(() => {
    loadGastos();
  }, []);

  const loadGastos = async () => {
    try {
      const data = await finanzasService.getGastos(filters);
      setGastos(data.results || data);
    } catch (error) {
      console.error('Error cargando gastos:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleFilterChange = (e) => {
    setFilters({
      ...filters,
      [e.target.name]: e.target.value
    });
  };

  const applyFilters = () => {
    loadGastos();
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await finanzasService.createGasto(formData);
      setShowForm(false);
      setFormData({
        monto: '',
        descripcion: '',
        categoria: '',
        fecha_vencimiento: ''
      });
      loadGastos();
    } catch (error) {
      alert('Error creando gasto: ' + error.message);
    }
  };

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  if (loading) return <div>Cargando gastos...</div>;

  return (
    <div className="gastos-list">
      <div className="header">
        <h2>Gestión de Gastos</h2>
        <button 
          onClick={() => setShowForm(!showForm)}
          className="btn-primary"
        >
          {showForm ? 'Cancelar' : 'Nuevo Gasto'}
        </button>
      </div>

      {/* Filtros */}
      <div className="filters-section">
        <h3>Filtros</h3>
        <div className="filters-grid">
          <input
            type="date"
            name="fecha_inicio"
            placeholder="Fecha inicio"
            value={filters.fecha_inicio}
            onChange={handleFilterChange}
          />
          <input
            type="date"
            name="fecha_fin"
            placeholder="Fecha fin"
            value={filters.fecha_fin}
            onChange={handleFilterChange}
          />
          <input
            type="number"
            name="monto_min"
            placeholder="Monto mínimo"
            value={filters.monto_min}
            onChange={handleFilterChange}
          />
          <input
            type="number"
            name="monto_max"
            placeholder="Monto máximo"
            value={filters.monto_max}
            onChange={handleFilterChange}
          />
          <button onClick={applyFilters} className="btn-secondary">
            Aplicar Filtros
          </button>
        </div>
      </div>

      {/* Formulario nuevo gasto */}
      {showForm && (
        <div className="form-container">
          <h3>Nuevo Gasto</h3>
          <form onSubmit={handleSubmit}>
            <input
              type="number"
              name="monto"
              placeholder="Monto"
              step="0.01"
              value={formData.monto}
              onChange={handleChange}
              required
            />
            <input
              type="text"
              name="descripcion"
              placeholder="Descripción"
              value={formData.descripcion}
              onChange={handleChange}
              required
            />
            <select
              name="categoria"
              value={formData.categoria}
              onChange={handleChange}
              required
            >
              <option value="">Seleccionar categoría</option>
              <option value="mantenimiento">Mantenimiento</option>
              <option value="servicios">Servicios</option>
              <option value="administracion">Administración</option>
              <option value="seguridad">Seguridad</option>
              <option value="otros">Otros</option>
            </select>
            <input
              type="date"
              name="fecha_vencimiento"
              value={formData.fecha_vencimiento}
              onChange={handleChange}
              required
            />
            <button type="submit">Crear Gasto</button>
          </form>
        </div>
      )}

      {/* Lista de gastos */}
      <div className="gastos-grid">
        {gastos.map((gasto) => (
          <div key={gasto.id} className="gasto-card">
            <div className="gasto-header">
              <h3>${gasto.monto}</h3>
              <span className={`category ${gasto.categoria}`}>
                {gasto.categoria}
              </span>
            </div>
            <p>{gasto.descripcion}</p>
            <div className="gasto-footer">
              <span>Vence: {gasto.fecha_vencimiento}</span>
              <span className={`status ${gasto.pagado ? 'paid' : 'pending'}`}>
                {gasto.pagado ? 'Pagado' : 'Pendiente'}
              </span>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default GastosList;
```

¿Quieres que continúe con los módulos de Seguridad, Mantenimiento y Notificaciones, o prefieres que me enfoque en algún aspecto específico como el routing, estado global o estilos CSS?