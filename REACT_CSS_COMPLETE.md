# 🎨 CSS COMPLETO PARA REACT FRONTEND

## 📝 **ESTILOS GLOBALES**

```css
/* src/styles/globals.css */

/* Reset y base */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen',
    'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue',
    sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  background-color: #f8f9fa;
  color: #333;
  line-height: 1.6;
}

.App {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

/* Variables CSS */
:root {
  --primary-color: #3498db;
  --secondary-color: #2c3e50;
  --success-color: #27ae60;
  --warning-color: #f39c12;
  --danger-color: #e74c3c;
  --info-color: #17a2b8;
  --light-color: #ecf0f1;
  --dark-color: #2c3e50;
  
  --border-radius: 8px;
  --box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  --transition: all 0.3s ease;
  
  --header-height: 70px;
  --sidebar-width: 250px;
}

/* Utilidades */
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

.text-center { text-align: center; }
.text-left { text-align: left; }
.text-right { text-align: right; }

.mb-1 { margin-bottom: 0.5rem; }
.mb-2 { margin-bottom: 1rem; }
.mb-3 { margin-bottom: 1.5rem; }
.mb-4 { margin-bottom: 2rem; }

.mt-1 { margin-top: 0.5rem; }
.mt-2 { margin-top: 1rem; }
.mt-3 { margin-top: 1.5rem; }
.mt-4 { margin-top: 2rem; }

.d-flex { display: flex; }
.justify-center { justify-content: center; }
.justify-between { justify-content: space-between; }
.align-center { align-items: center; }

/* Grid system */
.grid {
  display: grid;
  gap: 20px;
}

.grid-2 { grid-template-columns: repeat(2, 1fr); }
.grid-3 { grid-template-columns: repeat(3, 1fr); }
.grid-4 { grid-template-columns: repeat(4, 1fr); }

@media (max-width: 768px) {
  .grid-2, .grid-3, .grid-4 {
    grid-template-columns: 1fr;
  }
}
```

## 🎯 **COMPONENTES COMUNES**

```css
/* src/styles/components.css */

/* Cards */
.card {
  background: white;
  border-radius: var(--border-radius);
  box-shadow: var(--box-shadow);
  padding: 20px;
  margin-bottom: 20px;
  transition: var(--transition);
}

.card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
}

.card-header {
  border-bottom: 1px solid #eee;
  padding-bottom: 15px;
  margin-bottom: 20px;
}

.card-title {
  margin: 0;
  color: var(--secondary-color);
  font-size: 1.5rem;
  font-weight: 600;
}

/* Buttons */
.btn {
  display: inline-block;
  padding: 12px 24px;
  border: none;
  border-radius: var(--border-radius);
  cursor: pointer;
  font-size: 14px;
  font-weight: 500;
  text-decoration: none;
  text-align: center;
  transition: var(--transition);
  min-width: 120px;
}

.btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.btn-primary {
  background-color: var(--primary-color);
  color: white;
}

.btn-primary:hover {
  background-color: #2980b9;
  transform: translateY(-1px);
}

.btn-secondary {
  background-color: var(--secondary-color);
  color: white;
}

.btn-success {
  background-color: var(--success-color);
  color: white;
}

.btn-warning {
  background-color: var(--warning-color);
  color: white;
}

.btn-danger {
  background-color: var(--danger-color);
  color: white;
}

.btn-info {
  background-color: var(--info-color);
  color: white;
}

.btn-outline {
  background-color: transparent;
  border: 2px solid var(--primary-color);
  color: var(--primary-color);
}

.btn-outline:hover {
  background-color: var(--primary-color);
  color: white;
}

.btn-small {
  padding: 8px 16px;
  font-size: 12px;
  min-width: 80px;
}

.btn-large {
  padding: 16px 32px;
  font-size: 16px;
  min-width: 160px;
}

/* Forms */
.form-group {
  margin-bottom: 20px;
}

.form-group label {
  display: block;
  margin-bottom: 8px;
  font-weight: 500;
  color: var(--secondary-color);
}

.form-control, input, textarea, select {
  width: 100%;
  padding: 12px;
  border: 2px solid #ddd;
  border-radius: var(--border-radius);
  font-size: 14px;
  transition: var(--transition);
}

.form-control:focus, input:focus, textarea:focus, select:focus {
  outline: none;
  border-color: var(--primary-color);
  box-shadow: 0 0 0 3px rgba(52, 152, 219, 0.1);
}

.form-control.error, input.error, textarea.error, select.error {
  border-color: var(--danger-color);
}

.form-error {
  color: var(--danger-color);
  font-size: 12px;
  margin-top: 5px;
}

/* Table */
.table {
  width: 100%;
  border-collapse: collapse;
  background: white;
  border-radius: var(--border-radius);
  overflow: hidden;
  box-shadow: var(--box-shadow);
}

.table th,
.table td {
  padding: 15px;
  text-align: left;
  border-bottom: 1px solid #eee;
}

.table th {
  background-color: var(--light-color);
  font-weight: 600;
  color: var(--secondary-color);
}

.table tr:hover {
  background-color: #f8f9fa;
}

/* Badges */
.badge {
  display: inline-block;
  padding: 4px 12px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 500;
  color: white;
  text-transform: uppercase;
}

.badge.success { background-color: var(--success-color); }
.badge.warning { background-color: var(--warning-color); }
.badge.danger { background-color: var(--danger-color); }
.badge.info { background-color: var(--info-color); }
.badge.primary { background-color: var(--primary-color); }

/* Loading */
.loading {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 40px;
}

.spinner {
  width: 40px;
  height: 40px;
  border: 4px solid #f3f3f3;
  border-top: 4px solid var(--primary-color);
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

/* Alerts */
.alert {
  padding: 15px;
  margin-bottom: 20px;
  border-radius: var(--border-radius);
  border-left: 4px solid;
}

.alert-success {
  background-color: #d4edda;
  border-color: var(--success-color);
  color: #155724;
}

.alert-warning {
  background-color: #fff3cd;
  border-color: var(--warning-color);
  color: #856404;
}

.alert-danger {
  background-color: #f8d7da;
  border-color: var(--danger-color);
  color: #721c24;
}

.alert-info {
  background-color: #d1ecf1;
  border-color: var(--info-color);
  color: #0c5460;
}

/* Modal */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal {
  background: white;
  border-radius: var(--border-radius);
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.2);
  max-width: 500px;
  width: 90%;
  max-height: 90vh;
  overflow-y: auto;
}

.modal-header {
  padding: 20px;
  border-bottom: 1px solid #eee;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.modal-title {
  margin: 0;
  font-size: 1.25rem;
  font-weight: 600;
}

.modal-close {
  background: none;
  border: none;
  font-size: 24px;
  cursor: pointer;
  color: #999;
}

.modal-body {
  padding: 20px;
}

.modal-footer {
  padding: 20px;
  border-top: 1px solid #eee;
  display: flex;
  justify-content: flex-end;
  gap: 10px;
}
```

## 🏠 **LAYOUT PRINCIPAL**

```css
/* src/styles/layout.css */

/* Header */
.header {
  background: white;
  height: var(--header-height);
  box-shadow: var(--box-shadow);
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 100;
}

.header-content {
  height: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 20px;
}

.logo {
  font-size: 24px;
  font-weight: bold;
  color: var(--primary-color);
}

.header-actions {
  display: flex;
  align-items: center;
  gap: 20px;
}

.user-menu {
  position: relative;
}

.user-avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: var(--primary-color);
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-weight: bold;
  cursor: pointer;
}

.user-dropdown {
  position: absolute;
  top: 100%;
  right: 0;
  background: white;
  box-shadow: var(--box-shadow);
  border-radius: var(--border-radius);
  min-width: 200px;
  padding: 10px 0;
  margin-top: 10px;
}

.user-dropdown a {
  display: block;
  padding: 10px 20px;
  color: var(--secondary-color);
  text-decoration: none;
  transition: var(--transition);
}

.user-dropdown a:hover {
  background-color: #f8f9fa;
}

/* Sidebar */
.sidebar {
  position: fixed;
  top: var(--header-height);
  left: 0;
  width: var(--sidebar-width);
  height: calc(100vh - var(--header-height));
  background: var(--secondary-color);
  overflow-y: auto;
  z-index: 99;
  transition: var(--transition);
}

.sidebar.collapsed {
  width: 60px;
}

.sidebar-menu {
  list-style: none;
  padding: 20px 0;
}

.sidebar-menu li {
  margin-bottom: 5px;
}

.sidebar-menu a {
  display: flex;
  align-items: center;
  padding: 15px 20px;
  color: #ecf0f1;
  text-decoration: none;
  transition: var(--transition);
}

.sidebar-menu a:hover,
.sidebar-menu a.active {
  background-color: var(--primary-color);
  padding-left: 30px;
}

.sidebar-menu .icon {
  margin-right: 15px;
  font-size: 18px;
  width: 20px;
  text-align: center;
}

.sidebar.collapsed .menu-text {
  display: none;
}

/* Main Content */
.main-content {
  margin-top: var(--header-height);
  margin-left: var(--sidebar-width);
  padding: 30px;
  min-height: calc(100vh - var(--header-height));
  transition: var(--transition);
}

.main-content.sidebar-collapsed {
  margin-left: 60px;
}

.page-header {
  margin-bottom: 30px;
}

.page-title {
  font-size: 2rem;
  font-weight: 600;
  color: var(--secondary-color);
  margin-bottom: 10px;
}

.page-subtitle {
  color: #666;
  font-size: 1rem;
}

/* Responsive */
@media (max-width: 768px) {
  .sidebar {
    transform: translateX(-100%);
  }
  
  .sidebar.open {
    transform: translateX(0);
  }
  
  .main-content {
    margin-left: 0;
  }
  
  .header-content {
    padding: 0 15px;
  }
  
  .page-title {
    font-size: 1.5rem;
  }
}
```

## 📊 **DASHBOARD Y MÉTRICAS**

```css
/* src/styles/dashboard.css */

.dashboard-cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
  margin-bottom: 30px;
}

.metric-card {
  background: linear-gradient(135deg, var(--primary-color), #2980b9);
  color: white;
  text-align: center;
  padding: 30px 20px;
  border-radius: var(--border-radius);
  box-shadow: var(--box-shadow);
  transition: var(--transition);
}

.metric-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
}

.metric-card h3 {
  font-size: 14px;
  font-weight: 500;
  opacity: 0.9;
  margin-bottom: 10px;
  text-transform: uppercase;
  letter-spacing: 1px;
}

.metric-value {
  font-size: 36px;
  font-weight: bold;
  margin-bottom: 5px;
}

.metric-change {
  font-size: 12px;
  opacity: 0.8;
}

.metric-change.positive {
  color: #2ecc71;
}

.metric-change.negative {
  color: #e74c3c;
}

/* Chart Section */
.chart-section {
  margin-bottom: 30px;
}

.chart-container {
  background: white;
  padding: 20px;
  border-radius: var(--border-radius);
  box-shadow: var(--box-shadow);
}

.chart-title {
  font-size: 18px;
  font-weight: 600;
  margin-bottom: 20px;
  color: var(--secondary-color);
}

/* Quick Actions */
.quick-actions {
  margin-bottom: 30px;
}

.quick-actions h3 {
  margin-bottom: 20px;
  color: var(--secondary-color);
}

.actions-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 15px;
}

.action-btn {
  padding: 20px;
  background: white;
  border: 2px solid var(--primary-color);
  border-radius: var(--border-radius);
  color: var(--primary-color);
  font-weight: 500;
  cursor: pointer;
  transition: var(--transition);
  text-align: center;
}

.action-btn:hover {
  background: var(--primary-color);
  color: white;
  transform: translateY(-2px);
}

/* Status Indicators */
.status-indicator {
  display: inline-block;
  width: 12px;
  height: 12px;
  border-radius: 50%;
  margin-right: 8px;
}

.status-indicator.active {
  background-color: var(--success-color);
  box-shadow: 0 0 10px rgba(46, 204, 113, 0.5);
}

.status-indicator.inactive {
  background-color: var(--danger-color);
}

.status-indicator.pending {
  background-color: var(--warning-color);
}

/* Progress Bar */
.progress-bar {
  background-color: #f0f0f0;
  border-radius: 10px;
  overflow: hidden;
  height: 20px;
  margin: 10px 0;
}

.progress-fill {
  height: 100%;
  background: linear-gradient(90deg, var(--primary-color), #2980b9);
  transition: width 0.5s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-size: 12px;
  font-weight: bold;
}
```

## 🔐 **LOGIN Y AUTENTICACIÓN**

```css
/* src/styles/auth.css */

.auth-container {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  padding: 20px;
}

.auth-card {
  background: white;
  padding: 40px;
  border-radius: 16px;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.1);
  width: 100%;
  max-width: 400px;
}

.auth-header {
  text-align: center;
  margin-bottom: 30px;
}

.auth-logo {
  font-size: 32px;
  font-weight: bold;
  color: var(--primary-color);
  margin-bottom: 10px;
}

.auth-title {
  font-size: 24px;
  font-weight: 600;
  color: var(--secondary-color);
  margin-bottom: 5px;
}

.auth-subtitle {
  color: #666;
  font-size: 14px;
}

.auth-form {
  margin-bottom: 20px;
}

.auth-form .form-group {
  margin-bottom: 20px;
}

.auth-form input {
  height: 50px;
  font-size: 16px;
  border: 2px solid #eee;
  border-radius: 8px;
  transition: var(--transition);
}

.auth-form input:focus {
  border-color: var(--primary-color);
  box-shadow: 0 0 0 3px rgba(52, 152, 219, 0.1);
}

.auth-submit {
  width: 100%;
  height: 50px;
  background: var(--primary-color);
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: var(--transition);
  margin-bottom: 20px;
}

.auth-submit:hover {
  background: #2980b9;
  transform: translateY(-1px);
}

.auth-submit:disabled {
  opacity: 0.6;
  cursor: not-allowed;
  transform: none;
}

.auth-links {
  text-align: center;
}

.auth-links a {
  color: var(--primary-color);
  text-decoration: none;
  font-size: 14px;
}

.auth-links a:hover {
  text-decoration: underline;
}

.auth-error {
  background: #f8d7da;
  color: #721c24;
  padding: 10px;
  border-radius: 5px;
  margin-bottom: 20px;
  font-size: 14px;
  text-align: center;
}

.auth-success {
  background: #d4edda;
  color: #155724;
  padding: 10px;
  border-radius: 5px;
  margin-bottom: 20px;
  font-size: 14px;
  text-align: center;
}
```

## 🔧 **MÓDULOS ESPECÍFICOS**

```css
/* src/styles/modules.css */

/* Control de Acceso */
.control-acceso {
  max-width: 800px;
  margin: 0 auto;
}

.control-form {
  background: white;
  padding: 30px;
  border-radius: var(--border-radius);
  box-shadow: var(--box-shadow);
  margin-bottom: 30px;
}

.placa-input {
  font-size: 24px;
  text-align: center;
  font-weight: bold;
  text-transform: uppercase;
  letter-spacing: 2px;
  height: 60px;
  border: 3px solid var(--primary-color);
}

.control-buttons {
  display: flex;
  gap: 20px;
  margin-top: 20px;
}

.btn-ingreso {
  background: var(--success-color);
  color: white;
  flex: 1;
  height: 50px;
  font-size: 16px;
  font-weight: bold;
}

.btn-salida {
  background: var(--warning-color);
  color: white;
  flex: 1;
  height: 50px;
  font-size: 16px;
  font-weight: bold;
}

.resultado-card {
  padding: 20px;
  border-radius: var(--border-radius);
  margin: 20px 0;
  border-left: 5px solid;
}

.resultado-card.success {
  background: #d4edda;
  border-color: var(--success-color);
  color: #155724;
}

.resultado-card.denied {
  background: #f8d7da;
  border-color: var(--danger-color);
  color: #721c24;
}

.error-card {
  background: #f8d7da;
  border: 1px solid var(--danger-color);
  border-radius: var(--border-radius);
  padding: 20px;
  margin: 20px 0;
  color: #721c24;
}

.instructions {
  background: #d1ecf1;
  border: 1px solid var(--info-color);
  border-radius: var(--border-radius);
  padding: 20px;
  margin-top: 30px;
}

.instructions h3 {
  color: var(--info-color);
  margin-bottom: 15px;
}

.instructions ul {
  margin-left: 20px;
}

.instructions li {
  margin-bottom: 8px;
}

/* Visitantes */
.visitantes-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
}

.visitante-card {
  background: white;
  padding: 20px;
  border-radius: var(--border-radius);
  box-shadow: var(--box-shadow);
  transition: var(--transition);
}

.visitante-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.15);
}

.visitante-card h3 {
  color: var(--primary-color);
  margin-bottom: 15px;
  font-size: 18px;
}

.visitante-card p {
  margin-bottom: 8px;
  color: #666;
}

/* Solicitudes de Mantenimiento */
.solicitudes-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
  gap: 20px;
}

.solicitud-card {
  background: white;
  border-radius: var(--border-radius);
  box-shadow: var(--box-shadow);
  overflow: hidden;
  transition: var(--transition);
}

.solicitud-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.15);
}

.solicitud-header {
  padding: 20px 20px 0;
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
}

.solicitud-header h3 {
  color: var(--secondary-color);
  margin: 0;
  flex: 1;
  margin-right: 15px;
}

.badges {
  display: flex;
  gap: 8px;
  flex-shrink: 0;
}

.badge.prioridad {
  text-transform: capitalize;
}

.badge.estado {
  text-transform: capitalize;
}

.descripcion {
  padding: 0 20px;
  color: #666;
  line-height: 1.5;
  margin: 15px 0;
}

.solicitud-info {
  padding: 0 20px;
  border-top: 1px solid #eee;
  margin-top: 15px;
  padding-top: 15px;
}

.solicitud-info p {
  margin: 5px 0;
  font-size: 14px;
  color: #666;
}

.estado-buttons {
  padding: 15px 20px;
  display: flex;
  gap: 10px;
  border-top: 1px solid #eee;
}

/* Notificaciones */
.notificaciones-container {
  max-width: 800px;
  margin: 0 auto;
}

.notificacion-card {
  background: white;
  border-radius: var(--border-radius);
  box-shadow: var(--box-shadow);
  margin-bottom: 15px;
  display: flex;
  align-items: flex-start;
  padding: 20px;
  transition: var(--transition);
  position: relative;
}

.notificacion-card.unread {
  border-left: 4px solid var(--primary-color);
  background: #f8f9ff;
}

.notificacion-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
}

.notification-icon {
  font-size: 24px;
  margin-right: 15px;
  flex-shrink: 0;
}

.notification-content {
  flex: 1;
}

.notification-content h3 {
  margin: 0 0 8px 0;
  color: var(--secondary-color);
  font-size: 16px;
}

.notification-content p {
  margin: 0 0 8px 0;
  color: #666;
  line-height: 1.4;
}

.timestamp {
  color: #999;
  font-size: 12px;
}

.mark-read-btn {
  position: absolute;
  top: 15px;
  right: 15px;
  background: var(--success-color);
  color: white;
  border: none;
  border-radius: 50%;
  width: 24px;
  height: 24px;
  cursor: pointer;
  font-size: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* Estados vacíos */
.empty-state {
  text-align: center;
  padding: 60px 20px;
  color: #666;
}

.empty-state p {
  font-size: 18px;
  margin-bottom: 20px;
}

/* Responsive específico */
@media (max-width: 768px) {
  .control-buttons {
    flex-direction: column;
  }
  
  .dashboard-cards {
    grid-template-columns: 1fr;
  }
  
  .actions-grid {
    grid-template-columns: 1fr;
  }
  
  .visitantes-grid,
  .solicitudes-grid {
    grid-template-columns: 1fr;
  }
  
  .placa-input {
    font-size: 18px;
    height: 50px;
  }
  
  .resultado-card,
  .error-card,
  .instructions {
    margin: 15px 0;
    padding: 15px;
  }
}
```

## 🎯 **INSTRUCCIONES DE USO**

### **1. Importar estilos en tu App**

```jsx
// src/App.js
import './styles/globals.css';
import './styles/components.css';
import './styles/layout.css';
import './styles/dashboard.css';
import './styles/auth.css';
import './styles/modules.css';
```

### **2. Estructura de archivos CSS**

```
src/styles/
├── globals.css      (Reset, variables, utilidades)
├── components.css   (Componentes reutilizables)
├── layout.css       (Header, sidebar, navegación)
├── dashboard.css    (Métricas, gráficos)
├── auth.css         (Login, registro)
└── modules.css      (Módulos específicos)
```

### **3. Personalización**

Para personalizar colores, edita las variables CSS en `globals.css`:

```css
:root {
  --primary-color: #your-color;
  --secondary-color: #your-color;
  /* etc... */
}
```

### **4. Modo oscuro (opcional)**

```css
[data-theme="dark"] {
  --primary-color: #4ea5d9;
  --secondary-color: #1a1a1a;
  --light-color: #2d2d2d;
  /* etc... */
}
```

¡Con estos estilos CSS tendrás una interfaz moderna, responsive y profesional para tu aplicación React! 🎨✨