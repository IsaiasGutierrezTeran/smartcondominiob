# 🚀 GUÍA COMPLETA: DESPLEGAR DJANGO EN RENDER

## 📋 **CONFIGURACIÓN EN EL FORMULARIO DE RENDER**

### Campos obligatorios:

**Name**: `smartcondominiob-backend`

**Language**: `Python 3` ✅

**Branch**: `master` ✅

**Region**: `Oregon (US West)` ✅

**Root Directory**: *(déjalo vacío)*

**Build Command**:
```bash
pip install -r requirements.txt
```

**Start Command**:
```bash
gunicorn config.wsgi:application --host 0.0.0.0 --port $PORT
```

## 🔧 **VARIABLES DE ENTORNO OBLIGATORIAS**

### En la sección "Environment Variables", agrega:

| Variable | Valor |
|----------|-------|
| `DEBUG` | `False` |
| `SECRET_KEY` | `tu-clave-secreta-super-larga-aqui-genera-una-nueva` |
| `DATABASE_URL` | *(Render lo proporcionará automáticamente)* |
| `STRIPE_PUBLISHABLE_KEY` | `pk_test_tu_clave_stripe` |
| `STRIPE_SECRET_KEY` | `sk_test_tu_clave_stripe` |
| `STRIPE_WEBHOOK_SECRET` | `whsec_tu_webhook` |

### Variables opcionales pero recomendadas:

| Variable | Valor |
|----------|-------|
| `PYTHON_VERSION` | `3.11.0` |
| `RENDER_EXTERNAL_HOSTNAME` | `smartcondominiob-backend.onrender.com` |

## 🗄️ **BASE DE DATOS**

1. **Después de crear el Web Service**, ve a Dashboard
2. Crea un **PostgreSQL Database**:
   - Name: `smartcondominiob-db`
   - Region: `Oregon (US West)` (mismo que el backend)
   - Plan: `Free` (para empezar)

3. **Conecta la base de datos**:
   - Render automáticamente agregará `DATABASE_URL` a tu Web Service
   - Tu Django ya está configurado para usar `dj_database_url`

## 🌐 **CORS PARA PRODUCCIÓN**

Tu frontend React necesitará conectarse a:
```
https://smartcondominiob-backend.onrender.com/api/
```

Actualiza tu código React:
```javascript
// Cambia esto en tu frontend React
const API_BASE_URL = 'https://smartcondominiob-backend.onrender.com/api';
```

## ⚡ **COMANDOS POST-DESPLIEGUE**

Después del primer despliegue, ejecuta en la consola de Render:

```bash
# Migrar base de datos
python manage.py migrate

# Crear superusuario (opcional)
python manage.py createsuperuser

# Recolectar archivos estáticos
python manage.py collectstatic --noinput
```

## 🔍 **VERIFICACIÓN DE DESPLIEGUE**

Una vez desplegado, prueba estos endpoints:

- **Admin**: `https://tu-app.onrender.com/admin/`
- **API Root**: `https://tu-app.onrender.com/api/`
- **Login**: `https://tu-app.onrender.com/api/usuarios/login/`
- **Health Check**: `https://tu-app.onrender.com/` (debe mostrar algo)

## 🛠️ **SOLUCIÓN DE PROBLEMAS COMUNES**

### Error de ALLOWED_HOSTS:
Tu `settings.py` ya está configurado correctamente con:
```python
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)
```

### Error de archivos estáticos:
Ya tienes configurado WhiteNoise:
```python
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

### Error de base de datos:
Verifica que `DATABASE_URL` esté en las variables de entorno.

## 🎯 **CHECKLIST FINAL**

- [ ] Build Command: `pip install -r requirements.txt`
- [ ] Start Command: `gunicorn config.wsgi:application --host 0.0.0.0 --port $PORT`
- [ ] Variable `DEBUG=False`
- [ ] Variable `SECRET_KEY` configurada
- [ ] Base de datos PostgreSQL creada y conectada
- [ ] Variables de Stripe configuradas
- [ ] Primer despliegue exitoso
- [ ] Migraciones ejecutadas
- [ ] Endpoints funcionando

## 🚀 **¡LISTO PARA PRODUCCIÓN!**

Tu backend Django estará disponible en:
`https://smartcondominiob-backend.onrender.com`

Y tu React podrá conectarse usando el código en `REACT_CORS_INTEGRATION.js` cambiando solo la URL base.