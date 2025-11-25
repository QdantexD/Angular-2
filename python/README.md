# 🐍 Python Services - Battle.net Platform

Servicios y scripts de Python para gestión de base de datos, analytics y procesamiento de datos.

## 📦 Instalación

### Requisitos
- Python 3.8 o superior
- PostgreSQL instalado y corriendo

### Instalar Dependencias

```bash
cd python
pip install -r requirements.txt
```

**Para uso básico** (sin pandas):
```bash
pip install psycopg2-binary python-dotenv bcrypt flask flask-cors
```

**Para uso avanzado** (con pandas):
```bash
pip install -r requirements.txt
```

## 🚀 Uso Básico

### 1. Configurar Base de Datos

```bash
python setup.py
```

O usar el script mejorado directamente:
```bash
python db_setup_improved.py
```

Esto crea:
- ✅ Base de datos `battlenet_db`
- ✅ Todas las tablas necesarias
- ✅ Índices para optimización
- ✅ Usuario admin por defecto

### 2. Verificar Estado

```bash
python utils.py check
```

### 3. Poblar con Datos de Ejemplo

```bash
python utils.py seed
```

## 🔧 Uso Avanzado

### Servicio Flask de Analytics

Iniciar el servicio:

```bash
python app.py
```

El servicio estará en: `http://localhost:5000`

### Endpoints Disponibles

#### Básicos (sin pandas)
- `GET /health` - Health check
- `GET /api/db/status` - Estado de base de datos
- `GET /api/analytics/basic` - Analytics básicos

#### Avanzados (requiere pandas)
- `GET /api/analytics/advanced` - Analytics con pandas
- `GET /api/analytics/trends?period=7d` - Tendencias temporales
- `GET /api/analytics/predictions` - Predicciones

### Usar DatabaseManager en tus scripts

```python
from db_manager import DatabaseManager

db = DatabaseManager()

# Probar conexión
result = db.test_connection()
print(result)

# Ejecutar query
result = db.execute_query("SELECT * FROM users LIMIT 10")
print(result['data'])

# Obtener estadísticas
stats = db.get_stats()
print(stats)
```

## 📁 Estructura de Archivos

```
python/
├── config.py              # Configuración centralizada
├── db_manager.py          # Gestor de base de datos (reutilizable)
├── db_setup_improved.py   # Script de setup mejorado
├── setup.py               # Script principal de setup
├── app.py                 # Servicio Flask de analytics
├── utils.py                # Utilidades y helpers
├── requirements.txt       # Dependencias
└── README.md              # Esta documentación
```

## 🎯 Casos de Uso

### Uso Básico (Principiante)
1. Ejecutar `python setup.py` una vez
2. Usar el backend Node.js normalmente
3. El servicio Python es opcional

### Uso Intermedio
1. Setup básico
2. Iniciar servicio Flask: `python app.py`
3. Usar endpoints básicos de analytics

### Uso Avanzado
1. Setup completo
2. Servicio Flask con pandas
3. Crear scripts personalizados usando `db_manager.py`
4. Integrar con otros servicios

## 🔗 Integración con Node.js

El backend Node.js puede consumir el servicio Python:

```javascript
// En backend/routes/dashboard.js
const response = await axios.get('http://localhost:5000/api/analytics/advanced');
```

## ⚙️ Configuración

Todas las configuraciones están en `config.py` y se cargan desde `.env`:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=battlenet_db
DB_USER=postgres
DB_PASSWORD=123456
PYTHON_SERVICE_PORT=5000
```

## 🛠️ Utilidades

### Generar Hash de Contraseña

```bash
python utils.py hash mi_contraseña
```

### Verificar Base de Datos

```bash
python utils.py check
```

### Poblar con Datos

```bash
python utils.py seed
```

## 📊 Ejemplos de Uso

### Ejemplo 1: Script Simple

```python
from db_manager import DatabaseManager

db = DatabaseManager()
result = db.execute_query("SELECT COUNT(*) as total FROM games")
print(f"Total juegos: {result['data'][0]['total']}")
```

### Ejemplo 2: Analytics Personalizado

```python
from db_manager import DatabaseManager
from datetime import datetime, timedelta

db = DatabaseManager()
date_from = datetime.now() - timedelta(days=7)

result = db.execute_query("""
    SELECT category, COUNT(*) as count
    FROM games
    WHERE created_at >= %s
    GROUP BY category
""", (date_from,))

for row in result['data']:
    print(f"{row['category']}: {row['count']}")
```

## 🐛 Solución de Problemas

### Error: "psycopg2 no encontrado"
```bash
pip install psycopg2-binary
```

### Error: "pandas no encontrado"
```bash
pip install pandas
# O usa endpoints básicos sin pandas
```

### Error de conexión
- Verifica que PostgreSQL esté corriendo
- Verifica credenciales en `backend/.env`
- Ejecuta: `python utils.py check`

## 📝 Notas

- **Uso Básico**: No requiere pandas, funciona solo con psycopg2
- **Uso Avanzado**: Requiere pandas para analytics complejos
- **Modular**: Cada script puede usarse independientemente
- **Reutilizable**: `db_manager.py` puede importarse en otros proyectos

