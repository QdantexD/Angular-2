# 🐍 Python Services - Battle.net Platform

Scripts de Python para gestión de base de datos y verificación de usuarios.

## 📦 Instalación

### Requisitos
- Python 3.8 o superior
- PostgreSQL instalado y corriendo

### Instalar Dependencias

```bash
cd python
pip install -r requirements.txt
```

O instalar manualmente:
```bash
pip install psycopg2-binary python-dotenv bcrypt
```

## 🚀 Scripts Disponibles

### 1. `db_setup_improved.py` - Setup de Base de Datos
Configuración completa de la base de datos PostgreSQL.

```bash
python db_setup_improved.py
```

Crea:
- ✅ Base de datos `battlenet_db`
- ✅ Todas las tablas necesarias
- ✅ Índices para optimización
- ✅ Usuario admin por defecto

### 2. `setup.py` - Setup Principal
Script principal que orquesta todo el proceso de setup.

```bash
python setup.py
```

### 3. `verificar_registro.py` - Verificar Usuarios
Verificar si un usuario está registrado en PostgreSQL.

```bash
# Ver todos los usuarios
python verificar_registro.py --all

# Verificar por email
python verificar_registro.py tu@email.com

# Verificar por username
python verificar_registro.py tu_username

# Modo interactivo
python verificar_registro.py
```

### 4. `utils.py` - Utilidades
Funciones helper para mantenimiento.

```bash
# Verificar estado de BD
python utils.py check

# Poblar con datos de ejemplo
python utils.py seed

# Generar hash de contraseña
python utils.py hash mi_contraseña
```

### 5. `app.py` - Servicio Flask (Opcional)
Servicio Flask para analytics avanzados.

```bash
python app.py
```

Disponible en: `http://localhost:5000`

## 📁 Archivos Principales

```
python/
├── config.py              # Configuración centralizada
├── db_manager.py          # Gestor de base de datos
├── db_setup_improved.py   # Setup mejorado de BD
├── setup.py               # Setup principal
├── verificar_registro.py  # Verificar usuarios
├── utils.py               # Utilidades
├── app.py                 # Flask API (opcional)
├── requirements.txt       # Dependencias
└── README.md              # Esta documentación
```

## 🔧 Uso Básico

### Setup Inicial
```bash
python setup.py
```

### Verificar Usuarios
```bash
python verificar_registro.py --all
```

### Verificar Estado
```bash
python utils.py check
```

## 💡 Notas

- Los scripts usan `.env` desde `backend/.env`
- Requiere PostgreSQL corriendo
- Compatible con Windows (encoding UTF-8)
