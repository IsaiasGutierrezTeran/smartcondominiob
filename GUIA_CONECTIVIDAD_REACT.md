# 🔗 Guía de Verificación de Conectividad Backend-Frontend React

## 🚀 Verificación Rápida de Conectividad

### 1. **Verificar que el Backend esté funcionando**
```bash
# En terminal (con el servidor corriendo)
curl http://127.0.0.1:8000/api/
# Debería retornar JSON con información de bienvenida
```

### 2. **Verificar desde el navegador**
Abre estas URLs en tu navegador:
- ✅ **API Root**: http://127.0.0.1:8000/api/
- ✅ **Admin Panel**: http://127.0.0.1:8000/admin/
- ✅ **API Docs**: http://127.0.0.1:8000/api/schema/swagger-ui/

---

## 🔐 Test de Autenticación (LOGIN)

### **1. Test con cURL**
```bash
curl -X POST http://127.0.0.1:8000/api/login/ \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "admin123"}'
```

**Respuesta esperada:**
```json
{
  "token": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"
}
```

### **2. Test con JavaScript (React)**
```javascript
// Archivo: src/services/api.js
const API_BASE_URL = 'http://127.0.0.1:8000/api';

export const loginUser = async (username, password) => {
  try {
    const response = await fetch(`${API_BASE_URL}/login/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ username, password }),
    });
    
    if (!response.ok) {
      throw new Error('Login failed');
    }
    
    const data = await response.json();
    localStorage.setItem('token', data.token);
    return data;
  } catch (error) {
    console.error('Login error:', error);
    throw error;
  }
};
```

### **3. Componente de Login (React)**
```jsx
// Archivo: src/components/Login.jsx
import React, { useState } from 'react';
import { loginUser } from '../services/api';

const Login = () => {
  const [credentials, setCredentials] = useState({ username: '', password: '' });
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');
    
    try {
      const result = await loginUser(credentials.username, credentials.password);
      console.log('Login successful:', result);
      // Redirect o actualizar estado global
    } catch (err) {
      setError('Credenciales inválidas');
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
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
        {loading ? 'Iniciando...' : 'Iniciar Sesión'}
      </button>
      {error && <p style={{color: 'red'}}>{error}</p>}
    </form>
  );
};

export default Login;
```

---

## 📊 Test de Operaciones CRUD

### **1. Funciones API Completas**
```javascript
// Archivo: src/services/api.js
const API_BASE_URL = 'http://127.0.0.1:8000/api';

// Helper para obtener headers con token
const getAuthHeaders = () => {
  const token = localStorage.getItem('token');
  return {
    'Content-Type': 'application/json',
    'Authorization': token ? `Token ${token}` : '',
  };
};

// ==================== USUARIOS ====================
export const getUsuarios = async () => {
  const response = await fetch(`${API_BASE_URL}/usuarios/`, {
    headers: getAuthHeaders(),
  });
  return response.json();
};

export const createUsuario = async (userData) => {
  const response = await fetch(`${API_BASE_URL}/usuarios/`, {
    method: 'POST',
    headers: getAuthHeaders(),
    body: JSON.stringify(userData),
  });
  return response.json();
};

export const updateUsuario = async (id, userData) => {
  const response = await fetch(`${API_BASE_URL}/usuarios/${id}/`, {
    method: 'PUT',
    headers: getAuthHeaders(),
    body: JSON.stringify(userData),
  });
  return response.json();
};

export const deleteUsuario = async (id) => {
  const response = await fetch(`${API_BASE_URL}/usuarios/${id}/`, {
    method: 'DELETE',
    headers: getAuthHeaders(),
  });
  return response.ok;
};

// ==================== PROPIEDADES ====================
export const getPropiedades = async () => {
  const response = await fetch(`${API_BASE_URL}/condominio/propiedades/`, {
    headers: getAuthHeaders(),
  });
  return response.json();
};

export const createPropiedad = async (propiedadData) => {
  const response = await fetch(`${API_BASE_URL}/condominio/propiedades/`, {
    method: 'POST',
    headers: getAuthHeaders(),
    body: JSON.stringify(propiedadData),
  });
  return response.json();
};

// ==================== FINANZAS ====================
export const getPagos = async () => {
  const response = await fetch(`${API_BASE_URL}/finanzas/pagos/`, {
    headers: getAuthHeaders(),
  });
  return response.json();
};

export const getGastos = async () => {
  const response = await fetch(`${API_BASE_URL}/finanzas/gastos/`, {
    headers: getAuthHeaders(),
  });
  return response.json();
};

// ==================== SEGURIDAD ====================
export const getVisitas = async () => {
  const response = await fetch(`${API_BASE_URL}/seguridad/visitas/`, {
    headers: getAuthHeaders(),
  });
  return response.json();
};

export const createVisita = async (visitaData) => {
  const response = await fetch(`${API_BASE_URL}/seguridad/visitas/`, {
    method: 'POST',
    headers: getAuthHeaders(),
    body: JSON.stringify(visitaData),
  });
  return response.json();
};

// ==================== MANTENIMIENTO ====================
export const getSolicitudesMantenimiento = async () => {
  const response = await fetch(`${API_BASE_URL}/mantenimiento/solicitudes/`, {
    headers: getAuthHeaders(),
  });
  return response.json();
};

export const createSolicitudMantenimiento = async (solicitudData) => {
  const response = await fetch(`${API_BASE_URL}/mantenimiento/solicitudes/`, {
    method: 'POST',
    headers: getAuthHeaders(),
    body: JSON.stringify(solicitudData),
  });
  return response.json();
};
```

### **2. Hook personalizado para manejo de estado**
```javascript
// Archivo: src/hooks/useApi.js
import { useState, useEffect } from 'react';

export const useApi = (apiFunction, dependencies = []) => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        setLoading(true);
        const result = await apiFunction();
        setData(result);
        setError(null);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, dependencies);

  return { data, loading, error, refetch: () => fetchData() };
};
```

### **3. Ejemplo de componente CRUD completo**
```jsx
// Archivo: src/components/PropiedadesList.jsx
import React, { useState } from 'react';
import { useApi } from '../hooks/useApi';
import { getPropiedades, createPropiedad, deletePropiedad } from '../services/api';

const PropiedadesList = () => {
  const { data: propiedades, loading, error, refetch } = useApi(getPropiedades);
  const [newPropiedad, setNewPropiedad] = useState({
    numero_casa: '',
    metros_cuadrados: '',
  });

  const handleCreate = async (e) => {
    e.preventDefault();
    try {
      await createPropiedad(newPropiedad);
      setNewPropiedad({ numero_casa: '', metros_cuadrados: '' });
      refetch(); // Recargar la lista
    } catch (error) {
      console.error('Error creating propiedad:', error);
    }
  };

  const handleDelete = async (id) => {
    if (window.confirm('¿Estás seguro?')) {
      try {
        await deletePropiedad(id);
        refetch(); // Recargar la lista
      } catch (error) {
        console.error('Error deleting propiedad:', error);
      }
    }
  };

  if (loading) return <div>Cargando...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div>
      <h2>Propiedades</h2>
      
      {/* Formulario para crear nueva propiedad */}
      <form onSubmit={handleCreate}>
        <input
          type="text"
          placeholder="Número de casa"
          value={newPropiedad.numero_casa}
          onChange={(e) => setNewPropiedad({...newPropiedad, numero_casa: e.target.value})}
        />
        <input
          type="number"
          placeholder="Metros cuadrados"
          value={newPropiedad.metros_cuadrados}
          onChange={(e) => setNewPropiedad({...newPropiedad, metros_cuadrados: e.target.value})}
        />
        <button type="submit">Crear Propiedad</button>
      </form>

      {/* Lista de propiedades */}
      <ul>
        {propiedades?.results?.map(propiedad => (
          <li key={propiedad.id}>
            <strong>Casa {propiedad.numero_casa}</strong> - {propiedad.metros_cuadrados}m²
            <button onClick={() => handleDelete(propiedad.id)}>Eliminar</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default PropiedadesList;
```

---

## 🧪 Tests de Verificación Manual

### **1. Checklist de Conectividad**
- [ ] ✅ Backend corriendo en http://127.0.0.1:8000
- [ ] ✅ Frontend puede acceder a /api/
- [ ] ✅ Login funciona y retorna token
- [ ] ✅ Requests con token son aceptadas
- [ ] ✅ CORS configurado correctamente
- [ ] ✅ Operaciones CRUD funcionan

### **2. Test paso a paso**
```javascript
// Ejecutar en consola del navegador
// 1. Test de conectividad
fetch('http://127.0.0.1:8000/api/')
  .then(r => r.json())
  .then(console.log);

// 2. Test de login
fetch('http://127.0.0.1:8000/api/login/', {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({username: 'admin', password: 'admin123'})
})
.then(r => r.json())
.then(data => {
  console.log('Token:', data.token);
  localStorage.setItem('token', data.token);
});

// 3. Test de request autenticada
fetch('http://127.0.0.1:8000/api/usuarios/', {
  headers: {
    'Authorization': `Token ${localStorage.getItem('token')}`
  }
})
.then(r => r.json())
.then(console.log);
```

---

## 🔍 Solución de Problemas Comunes

### **Error: CORS**
```javascript
// Si ves error de CORS, verifica en settings.py:
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",    // React dev server
    "http://127.0.0.1:3000",
]
```

### **Error: 401 Unauthorized**
```javascript
// Verifica que el token se envía correctamente
const token = localStorage.getItem('token');
if (!token) {
  // Redirect to login
}
```

### **Error: 404 Not Found**
```javascript
// Verifica las URLs en tu frontend
const API_BASE_URL = 'http://127.0.0.1:8000/api'; // Sin slash final en algunos casos
```

---

## 📋 **URLs de API Disponibles en tu Backend**

| Módulo | Endpoint | Métodos | Descripción |
|--------|----------|---------|-------------|
| **Auth** | `/api/login/` | POST | Login con username/password |
| **Auth** | `/api/registro/` | POST | Registro de nuevos usuarios |
| **Usuarios** | `/api/usuarios/` | GET, POST | Lista y creación de usuarios |
| **Usuarios** | `/api/usuarios/{id}/` | GET, PUT, DELETE | Usuario específico |
| **Condominio** | `/api/condominio/propiedades/` | GET, POST | Propiedades |
| **Condominio** | `/api/condominio/avisos/` | GET, POST | Avisos del condominio |
| **Finanzas** | `/api/finanzas/pagos/` | GET, POST | Pagos |
| **Finanzas** | `/api/finanzas/gastos/` | GET, POST | Gastos |
| **Finanzas** | `/api/finanzas/multas/` | GET, POST | Multas |
| **Seguridad** | `/api/seguridad/visitas/` | GET, POST | Control de visitas |
| **Seguridad** | `/api/seguridad/vehiculos/` | GET, POST | Vehículos |
| **Mantenimiento** | `/api/mantenimiento/solicitudes/` | GET, POST | Solicitudes |
| **Notificaciones** | `/api/notificaciones/` | GET, POST | Push notifications |

---

## 🎯 **Credenciales de Prueba**

| Usuario | Password | Rol | Token de prueba |
|---------|----------|-----|-----------------|
| `admin` | `admin123` | Superusuario | Se genera al login |
| `residente1` | `isaelOrtiz2` | Residente | Se genera al login |
| `seguridad1` | `guardia123` | Seguridad | Se genera al login |

---

¡Con esta guía puedes verificar completamente la conectividad entre tu backend Django y frontend React! 🚀