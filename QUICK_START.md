# 🚀 Guía de Inicio Rápido - Smart Condominio

## ⚡ Setup en 5 minutos

### 1. Clonar y preparar entorno
```bash
git clone https://github.com/IsaiasGutierrezTeran/smartcondominiob.git
cd smartcondominiob
python -m venv venv
.\venv\Scripts\Activate.ps1  # Windows
pip install -r requirements.txt
```

### 2. Configurar variables
```bash
cp .env.example .env
# Editar .env si necesario (opcional para desarrollo básico)
```

### 3. Base de datos y servidor
```bash
python manage.py migrate
python manage.py runserver
```

## 🎯 URLs Importantes

- **Backend**: http://127.0.0.1:8000/api/
- **Admin**: http://127.0.0.1:8000/admin/
- **Docs**: http://127.0.0.1:8000/api/docs/

## 🔐 Login Rápido

**Admin**: `admin` / `admin123`
**Residente**: `residente1` / `isaelOrtiz2`

## 📱 Para Mobile (Flutter/React Native)

**Android Emulator**: `http://10.0.2.2:8000/api`
**Dispositivo Físico**: `http://192.168.0.5:8000/api`

## 🛠 Comandos Útiles

```bash
# Tests
python manage.py test

# Crear migraciones
python manage.py makemigrations

# Shell Django
python manage.py shell

# Crear superusuario
python manage.py createsuperuser
```

## 📚 Más Info

Ver `README.md` para documentación completa.