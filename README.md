# 🏢 Smart Condominio Backend

Sistema de gestión integral para condominios desarrollado con Django REST Framework.

## 🚀 Características Principales

- **👥 Gestión de Usuarios**: Residentes, personal de seguridad, mantenimiento
- **🏠 Administración de Propiedades**: Control de unidades habitacionales
- **💰 Sistema Financiero**: Pagos, gastos, multas, reportes
- **🔒 Control de Acceso**: Registro de visitas, control vehicular
- **🔧 Mantenimiento**: Solicitudes y seguimiento de reparaciones
- **📱 Notificaciones**: Push notifications y alertas
- **🤖 IA Integrada**: Reconocimiento facial y detección de placas
- **📊 Auditoría**: Trazabilidad completa del sistema

## 🛠 Tecnologías

- **Backend**: Django 5.2.6, Django REST Framework 3.16
- **Base de Datos**: SQLite (desarrollo), PostgreSQL (producción)
- **Autenticación**: Token-based authentication
- **Documentación**: OpenAPI/Swagger con drf-spectacular
- **IA/ML**: OpenCV, AWS Rekognition
- **Pagos**: Stripe integration
- **WebSockets**: Django Channels para tiempo real

## 📋 Instalación Rápida

### 1. Clonar el repositorio
```bash
git clone https://github.com/IsaiasGutierrezTeran/smartcondominiob.git
cd smartcondominiob
```

### 2. Crear entorno virtual
```bash
python -m venv venv
# Windows
.\venv\Scripts\Activate.ps1
# Linux/Mac
source venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno
```bash
cp .env.example .env
# Editar .env con tus configuraciones
```

### 5. Ejecutar migraciones
```bash
python manage.py migrate
```

### 6. Crear superusuario (opcional)
```bash
python manage.py createsuperuser
```

### 7. Iniciar servidor
```bash
python manage.py runserver
```

## 🔐 Credenciales de Prueba

| Usuario | Contraseña | Rol |
|---------|------------|-----|
| `admin` | `admin123` | Superusuario |
| `residente1` | `isaelOrtiz2` | Residente |
| `seguridad1` | `guardia123` | Seguridad |
| `mantenimiento1` | `general123` | Mantenimiento |

## 📚 API Endpoints

### 🏠 Principales URLs:
- **API Root**: `http://127.0.0.1:8000/api/`
- **Admin Panel**: `http://127.0.0.1:8000/admin/`
- **API Docs**: `http://127.0.0.1:8000/api/docs/`
- **OpenAPI Schema**: `http://127.0.0.1:8000/api/schema/`

### 🎯 Módulos Disponibles:
- `/api/usuarios/` - Gestión de usuarios
- `/api/condominio/` - Propiedades y avisos
- `/api/finanzas/` - Pagos y reportes financieros
- `/api/seguridad/` - Control de acceso y visitas
- `/api/mantenimiento/` - Solicitudes de reparación
- `/api/notificaciones/` - Push notifications

## 📱 Configuración para Desarrollo Móvil

### Android Studio (Emulador):
```dart
static const String baseUrl = 'http://10.0.2.2:8000/api';
```

### Dispositivos Físicos:
```dart
static const String baseUrl = 'http://192.168.0.5:8000/api';
```

### iOS Simulator:
```dart
static const String baseUrl = 'http://127.0.0.1:8000/api';
```

## 🧪 Tests

```bash
# Ejecutar todos los tests
python manage.py test

# Test específico de un módulo
python manage.py test seguridad
```

## 📂 Estructura del Proyecto

```
backendd-main/
├── config/              # Configuración principal Django
├── usuarios/            # Gestión de usuarios y perfiles
├── condominio/          # Propiedades y avisos
├── finanzas/           # Sistema de pagos y reportes
├── seguridad/          # Control de acceso y visitas
├── mantenimiento/      # Solicitudes de reparación
├── notificaciones/     # Push notifications
├── auditoria/          # Sistema de auditoría
├── ia_scripts/         # Scripts de inteligencia artificial
├── staticfiles/        # Archivos estáticos
├── detecciones/        # Imágenes de detecciones IA
└── script/             # Scripts de utilidad
```

## 🔧 Variables de Entorno Importantes

```env
SECRET_KEY=tu-clave-secreta-django
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
STRIPE_SECRET_KEY=sk_test_...
AWS_ACCESS_KEY_ID=AKIA...
SECURITY_API_KEY=MI_CLAVE_SUPER_SECRETA_12345
```

## 🚀 Deployment

### Render.com (Recomendado):
1. Fork este repositorio
2. Conectar con Render
3. Configurar variables de entorno
4. Deploy automático desde `master`

### Docker:
```bash
# Build
docker build -t smartcondominio .

# Run
docker run -p 8000:8000 smartcondominio
```

## 📖 Documentación Adicional

- [`GUIA_FUNCIONALIDADES.md`](GUIA_FUNCIONALIDADES.md) - Guía completa de funcionalidades
- [`FILTROS_API.md`](FILTROS_API.md) - Documentación de filtros avanzados
- [`USUARIOS_PRUEBA_FRONTEND.md`](USUARIOS_PRUEBA_FRONTEND.md) - Usuarios para testing
- [`RECOMENDACION_ANDROID_STUDIO.md`](RECOMENDACION_ANDROID_STUDIO.md) - Setup móvil

## 🤝 Contribución

1. Fork el proyecto
2. Crear rama feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit cambios (`git commit -am 'Agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Crear Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para detalles.

## 👨‍💻 Autor

**Isaías Gutiérrez Terán**
- GitHub: [@IsaiasGutierrezTeran](https://github.com/IsaiasGutierrezTeran)

---

⭐ **¡Dale una estrella al proyecto si te resulta útil!** ⭐