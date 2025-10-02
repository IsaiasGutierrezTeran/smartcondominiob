# 🚀 ESTRUCTURA COMPLETA DE LA APLICACIÓN REACT

## 📁 **ESTRUCTURA DE CARPETAS**

```
src/
├── components/
│   ├── common/           # Componentes comunes
│   │   ├── Header.jsx
│   │   ├── Sidebar.jsx
│   │   ├── Loading.jsx
│   │   └── ProtectedRoute.jsx
│   ├── usuarios/         # Módulo usuarios
│   │   ├── Login.jsx
│   │   ├── ResidentesList.jsx
│   │   ├── RegistroFacial.jsx
│   │   └── PerfilUsuario.jsx
│   ├── condominio/       # Módulo condominio
│   │   ├── PropiedadesList.jsx
│   │   ├── ReservasList.jsx
│   │   ├── AreasComunes.jsx
│   │   └── Avisos.jsx
│   ├── finanzas/         # Módulo finanzas
│   │   ├── FinanzasDashboard.jsx
│   │   ├── GastosList.jsx
│   │   ├── PagosList.jsx
│   │   └── MultasList.jsx
│   ├── seguridad/        # Módulo seguridad
│   │   ├── SeguridadDashboard.jsx
│   │   ├── VisitantesList.jsx
│   │   ├── ControlAcceso.jsx
│   │   └── EventosSeguridad.jsx
│   ├── mantenimiento/    # Módulo mantenimiento
│   │   ├── SolicitudesList.jsx
│   │   ├── PersonalList.jsx
│   │   └── NuevaSolicitud.jsx
│   └── notificaciones/   # Módulo notificaciones
│       ├── NotificacionesList.jsx
│       └── EnviarNotificacion.jsx
├── services/             # Servicios API
│   ├── authService.js
│   ├── usuariosService.js
│   ├── condominioService.js
│   ├── finanzasService.js
│   ├── seguridadService.js
│   ├── mantenimientoService.js
│   └── notificacionesService.js
├── hooks/                # Hooks personalizados
│   ├── useApi.js
│   ├── useAuth.js
│   └── useLocalStorage.js
├── context/              # Context para estado global
│   ├── AuthContext.js
│   └── AppContext.js
├── config/               # Configuración
│   ├── api.js
│   └── routes.js
├── utils/                # Utilidades
│   ├── formatters.js
│   ├── validators.js
│   └── constants.js
├── styles/               # Estilos CSS
│   ├── globals.css
│   ├── components/
│   └── modules/
├── App.jsx               # Componente principal
└── index.js              # Punto de entrada
```

## 🧭 **CONFIGURACIÓN DE ROUTING**

### Router Principal

```jsx
// src/App.jsx
import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { AuthProvider } from './context/AuthContext';
import ProtectedRoute from './components/common/ProtectedRoute';
import Layout from './components/common/Layout';

// Componentes de páginas
import Login from './components/usuarios/Login';
import Dashboard from './components/Dashboard';
import ResidentesList from './components/usuarios/ResidentesList';
import PropiedadesList from './components/condominio/PropiedadesList';
import ReservasList from './components/condominio/ReservasList';
import FinanzasDashboard from './components/finanzas/FinanzasDashboard';
import GastosList from './components/finanzas/GastosList';
import PagosList from './components/finanzas/PagosList';
import SeguridadDashboard from './components/seguridad/SeguridadDashboard';
import VisitantesList from './components/seguridad/VisitantesList';
import ControlAcceso from './components/seguridad/ControlAcceso';
import SolicitudesList from './components/mantenimiento/SolicitudesList';
import NotificacionesList from './components/notificaciones/NotificacionesList';

// Estilos
import './styles/globals.css';

function App() {
  return (
    <AuthProvider>
      <Router>
        <div className="App">
          <Routes>
            {/* Ruta pública */}
            <Route path="/login" element={<Login />} />
            
            {/* Rutas protegidas */}
            <Route path="/" element={
              <ProtectedRoute>
                <Layout />
              </ProtectedRoute>
            }>
              {/* Dashboard principal */}
              <Route index element={<Dashboard />} />
              
              {/* Módulo Usuarios */}
              <Route path="usuarios/residentes" element={<ResidentesList />} />
              
              {/* Módulo Condominio */}
              <Route path="condominio/propiedades" element={<PropiedadesList />} />
              <Route path="condominio/reservas" element={<ReservasList />} />
              
              {/* Módulo Finanzas */}
              <Route path="finanzas" element={<FinanzasDashboard />} />
              <Route path="finanzas/gastos" element={<GastosList />} />
              <Route path="finanzas/pagos" element={<PagosList />} />
              
              {/* Módulo Seguridad */}
              <Route path="seguridad" element={<SeguridadDashboard />} />
              <Route path="seguridad/visitantes" element={<VisitantesList />} />
              <Route path="seguridad/control-acceso" element={<ControlAcceso />} />
              
              {/* Módulo Mantenimiento */}
              <Route path="mantenimiento/solicitudes" element={<SolicitudesList />} />
              
              {/* Módulo Notificaciones */}
              <Route path="notificaciones" element={<NotificacionesList />} />
            </Route>
            
            {/* Redirección por defecto */}
            <Route path="*" element={<Navigate to="/" replace />} />
          </Routes>
        </div>
      </Router>
    </AuthProvider>
  );
}

export default App;
```

## 🔐 **CONTEXT DE AUTENTICACIÓN**

```jsx
// src/context/AuthContext.js
import React, { createContext, useContext, useState, useEffect } from 'react';
import authService from '../services/authService';

const AuthContext = createContext();

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth debe ser usado dentro de AuthProvider');
  }
  return context;
};

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  useEffect(() => {
    checkAuthStatus();
  }, []);

  const checkAuthStatus = async () => {
    try {
      if (authService.isAuthenticated()) {
        const userData = authService.getUserData();
        setUser(userData);
        setIsAuthenticated(true);
        
        // Opcionalmente, verificar el token con el servidor
        try {
          const profile = await authService.getProfile();
          setUser(profile);
        } catch (error) {
          // Si el token es inválido, hacer logout
          console.warn('Token inválido, cerrando sesión');
          logout();
        }
      }
    } catch (error) {
      console.error('Error verificando autenticación:', error);
    } finally {
      setLoading(false);
    }
  };

  const login = async (username, password) => {
    try {
      const result = await authService.login(username, password);
      setUser(result.user || { username });
      setIsAuthenticated(true);
      return result;
    } catch (error) {
      throw error;
    }
  };

  const logout = () => {
    authService.logout();
    setUser(null);
    setIsAuthenticated(false);
  };

  const value = {
    user,
    isAuthenticated,
    loading,
    login,
    logout,
    checkAuthStatus
  };

  return (
    <AuthContext.Provider value={value}>
      {children}
    </AuthContext.Provider>
  );
};
```

## 🛡️ **COMPONENTE DE RUTA PROTEGIDA**

```jsx
// src/components/common/ProtectedRoute.jsx
import React from 'react';
import { Navigate, useLocation } from 'react-router-dom';
import { useAuth } from '../../context/AuthContext';
import Loading from './Loading';

function ProtectedRoute({ children, requiredRole = null }) {
  const { isAuthenticated, loading, user } = useAuth();
  const location = useLocation();

  if (loading) {
    return <Loading />;
  }

  if (!isAuthenticated) {
    // Guardar la ruta que intentaba acceder para redirigir después del login
    return <Navigate to="/login" state={{ from: location }} replace />;
  }

  // Verificar roles si es necesario
  if (requiredRole && user?.role !== requiredRole) {
    return <div className="access-denied">No tienes permisos para acceder a esta página</div>;
  }

  return children;
}

export default ProtectedRoute;
```

## 🏗️ **LAYOUT PRINCIPAL**

```jsx
// src/components/common/Layout.jsx
import React, { useState } from 'react';
import { Outlet } from 'react-router-dom';
import Header from './Header';
import Sidebar from './Sidebar';

function Layout() {
  const [sidebarOpen, setSidebarOpen] = useState(true);

  const toggleSidebar = () => {
    setSidebarOpen(!sidebarOpen);
  };

  return (
    <div className="layout">
      <Header toggleSidebar={toggleSidebar} />
      <div className="layout-content">
        <Sidebar isOpen={sidebarOpen} />
        <main className={`main-content ${sidebarOpen ? 'sidebar-open' : 'sidebar-closed'}`}>
          <Outlet />
        </main>
      </div>
    </div>
  );
}

export default Layout;
```

## 📱 **HEADER COMPONENT**

```jsx
// src/components/common/Header.jsx
import React from 'react';
import { useAuth } from '../../context/AuthContext';

function Header({ toggleSidebar }) {
  const { user, logout } = useAuth();

  const handleLogout = () => {
    if (window.confirm('¿Estás seguro de cerrar sesión?')) {
      logout();
    }
  };

  return (
    <header className="header">
      <div className="header-left">
        <button className="sidebar-toggle" onClick={toggleSidebar}>
          ☰
        </button>
        <h1>Smart Condominio</h1>
      </div>
      
      <div className="header-right">
        <div className="user-info">
          <span>Bienvenido, {user?.first_name || user?.username}</span>
          <button className="logout-btn" onClick={handleLogout}>
            Cerrar Sesión
          </button>
        </div>
      </div>
    </header>
  );
}

export default Header;
```

## 🎯 **SIDEBAR NAVIGATION**

```jsx
// src/components/common/Sidebar.jsx
import React from 'react';
import { NavLink } from 'react-router-dom';
import { useAuth } from '../../context/AuthContext';

function Sidebar({ isOpen }) {
  const { user } = useAuth();

  const menuItems = [
    {
      title: 'Dashboard',
      path: '/',
      icon: '🏠',
      exact: true
    },
    {
      title: 'Usuarios',
      icon: '👥',
      submenu: [
        { title: 'Residentes', path: '/usuarios/residentes' }
      ]
    },
    {
      title: 'Condominio',
      icon: '🏢',
      submenu: [
        { title: 'Propiedades', path: '/condominio/propiedades' },
        { title: 'Reservas', path: '/condominio/reservas' }
      ]
    },
    {
      title: 'Finanzas',
      icon: '💰',
      submenu: [
        { title: 'Dashboard', path: '/finanzas' },
        { title: 'Gastos', path: '/finanzas/gastos' },
        { title: 'Pagos', path: '/finanzas/pagos' }
      ]
    },
    {
      title: 'Seguridad',
      icon: '🛡️',
      submenu: [
        { title: 'Dashboard', path: '/seguridad' },
        { title: 'Visitantes', path: '/seguridad/visitantes' },
        { title: 'Control Acceso', path: '/seguridad/control-acceso' }
      ]
    },
    {
      title: 'Mantenimiento',
      icon: '🔧',
      submenu: [
        { title: 'Solicitudes', path: '/mantenimiento/solicitudes' }
      ]
    },
    {
      title: 'Notificaciones',
      icon: '🔔',
      path: '/notificaciones'
    }
  ];

  const renderMenuItem = (item, index) => {
    if (item.submenu) {
      return (
        <div key={index} className="menu-item-group">
          <div className="menu-item-header">
            <span className="menu-icon">{item.icon}</span>
            <span className="menu-title">{item.title}</span>
          </div>
          <div className="submenu">
            {item.submenu.map((subItem, subIndex) => (
              <NavLink
                key={subIndex}
                to={subItem.path}
                className={({ isActive }) => 
                  `submenu-item ${isActive ? 'active' : ''}`
                }
              >
                {subItem.title}
              </NavLink>
            ))}
          </div>
        </div>
      );
    }

    return (
      <NavLink
        key={index}
        to={item.path}
        className={({ isActive }) => 
          `menu-item ${isActive ? 'active' : ''}`
        }
        end={item.exact}
      >
        <span className="menu-icon">{item.icon}</span>
        <span className="menu-title">{item.title}</span>
      </NavLink>
    );
  };

  return (
    <aside className={`sidebar ${isOpen ? 'open' : 'closed'}`}>
      <nav className="sidebar-nav">
        {menuItems.map((item, index) => renderMenuItem(item, index))}
      </nav>
    </aside>
  );
}

export default Sidebar;
```

## ⚡ **HOOK PERSONALIZADO PARA AUTH**

```jsx
// src/hooks/useAuth.js
import { useContext } from 'react';
import { AuthContext } from '../context/AuthContext';

export const useAuth = () => {
  const context = useContext(AuthContext);
  
  if (!context) {
    throw new Error('useAuth debe ser usado dentro de AuthProvider');
  }
  
  return context;
};

// También puedes exportar hooks específicos
export const useIsAdmin = () => {
  const { user } = useAuth();
  return user?.is_staff || user?.is_superuser || false;
};

export const useIsResidente = () => {
  const { user } = useAuth();
  return user?.role === 'residente' || false;
};
```

## 📦 **DEPENDENCIAS NECESARIAS**

```json
// package.json
{
  "name": "smart-condominio-frontend",
  "version": "1.0.0",
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-router-dom": "^6.8.0",
    "react-scripts": "5.0.1"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  },
  "eslintConfig": {
    "extends": [
      "react-app",
      "react-app/jest"
    ]
  },
  "browserslist": {
    "production": [
      ">0.2%",
      "not dead",
      "not op_mini all"
    ],
    "development": [
      "last 1 chrome version",
      "last 1 firefox version",
      "last 1 safari version"
    ]
  },
  "proxy": "http://localhost:8000"
}
```

## 🎨 **ESTILOS CSS BÁSICOS**

```css
/* src/styles/globals.css */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', sans-serif;
  line-height: 1.6;
  color: #333;
  background-color: #f5f5f5;
}

.layout {
  display: flex;
  flex-direction: column;
  height: 100vh;
}

.header {
  background: #2c3e50;
  color: white;
  padding: 1rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.header-left {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.sidebar-toggle {
  background: none;
  border: none;
  color: white;
  font-size: 1.2rem;
  cursor: pointer;
  padding: 0.5rem;
}

.layout-content {
  display: flex;
  flex: 1;
  overflow: hidden;
}

.sidebar {
  width: 250px;
  background: #34495e;
  color: white;
  transition: width 0.3s ease;
  overflow-y: auto;
}

.sidebar.closed {
  width: 60px;
}

.main-content {
  flex: 1;
  padding: 2rem;
  overflow-y: auto;
  background: #fff;
  margin: 1rem;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.menu-item, .submenu-item {
  display: flex;
  align-items: center;
  padding: 1rem;
  color: white;
  text-decoration: none;
  transition: background-color 0.2s;
}

.menu-item:hover, .submenu-item:hover {
  background-color: #2c3e50;
}

.menu-item.active, .submenu-item.active {
  background-color: #3498db;
}

.menu-icon {
  margin-right: 0.5rem;
  font-size: 1.2rem;
}

.submenu {
  padding-left: 1rem;
  background-color: #2c3e50;
}

/* Componentes comunes */
.btn-primary {
  background: #3498db;
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1rem;
}

.btn-primary:hover {
  background: #2980b9;
}

.btn-secondary {
  background: #95a5a6;
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1rem;
}

.btn-danger {
  background: #e74c3c;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  cursor: pointer;
}

.card {
  background: white;
  padding: 1.5rem;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  margin-bottom: 1rem;
}

.dashboard-cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1rem;
  margin-bottom: 2rem;
}

.form-container {
  background: #f8f9fa;
  padding: 1.5rem;
  border-radius: 8px;
  margin-bottom: 2rem;
}

.form-group {
  margin-bottom: 1rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 500;
}

.form-group input,
.form-group select,
.form-group textarea {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 1rem;
}

.error-message {
  background: #f8d7da;
  color: #721c24;
  padding: 0.75rem;
  border-radius: 4px;
  margin-bottom: 1rem;
}

.success-message {
  background: #d4edda;
  color: #155724;
  padding: 0.75rem;
  border-radius: 4px;
  margin-bottom: 1rem;
}

/* Responsive */
@media (max-width: 768px) {
  .sidebar {
    position: fixed;
    left: -250px;
    height: 100vh;
    z-index: 1000;
  }
  
  .sidebar.open {
    left: 0;
  }
  
  .main-content {
    margin-left: 0;
  }
}
```

## 🚀 **COMANDOS PARA INICIAR**

```bash
# Crear proyecto React
npx create-react-app smart-condominio-frontend
cd smart-condominio-frontend

# Instalar dependencias adicionales
npm install react-router-dom

# Instalar dependencias opcionales para UI
npm install @mui/material @emotion/react @emotion/styled  # Material-UI
# O
npm install antd  # Ant Design
# O
npm install react-bootstrap bootstrap  # Bootstrap

# Iniciar desarrollo
npm start
```

Esta estructura te permite:

1. **🔐 Autenticación completa** con context y rutas protegidas
2. **🧭 Navegación** con React Router y sidebar dinámico
3. **📱 Diseño responsive** que funciona en móvil y desktop
4. **🔧 Modularidad** - cada módulo tiene sus propios componentes
5. **⚡ Estado global** compartido entre componentes
6. **🎨 Estilos organizados** y reutilizables

¿Quieres que continúe con los módulos de Seguridad y Mantenimiento, o prefieres que me enfoque en algún aspecto específico como optimización, testing o deployment?