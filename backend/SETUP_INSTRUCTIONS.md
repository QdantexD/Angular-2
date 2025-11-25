# 🚀 Instrucciones de Configuración del Backend

## Paso 1: Instalar Dependencias

```bash
cd backend
npm install
```

## Paso 2: Crear Archivo .env

Crea un archivo `.env` en la carpeta `backend/` con el siguiente contenido:

```env
PORT=3000
NODE_ENV=development

DB_HOST=localhost
DB_PORT=5432
DB_NAME=battlenet_db
DB_USER=postgres
DB_PASSWORD=tu_contraseña_postgres

JWT_SECRET=battlenet-super-secret-jwt-key-change-in-production-2024
JWT_EXPIRE=7d

PYTHON_SERVICE_URL=http://localhost:5000
```

**Importante:** Reemplaza `tu_contraseña_postgres` con tu contraseña real de PostgreSQL.

## Paso 3: Crear Base de Datos PostgreSQL

Abre una terminal y ejecuta:

```bash
psql -U postgres
```

Luego en el prompt de PostgreSQL:

```sql
CREATE DATABASE battlenet_db;
\q
```

## Paso 4: Inicializar Tablas

Ejecuta el script SQL para crear las tablas:

```bash
psql -U postgres -d battlenet_db -f scripts/init-db.sql
```

## Paso 5: Iniciar el Servidor

```bash
npm run dev
```

El servidor estará disponible en: `http://localhost:3000`

## ✅ Verificar que Funciona

Abre tu navegador o usa curl:

```bash
curl http://localhost:3000/api/health
```

Deberías ver:
```json
{"status":"OK","message":"Battle.net API is running"}
```

## 🔐 Credenciales por Defecto

**Admin User:**
- Email: `admin@battlenet.com`
- Password: `admin123`

## ⚠️ Solución de Problemas

### Error: "nodemon no se reconoce"
```bash
cd backend
npm install
```

### Error: "Database connection error"
1. Verifica que PostgreSQL esté corriendo
2. Verifica las credenciales en `.env`
3. Verifica que la base de datos `battlenet_db` exista

### Error: "relation does not exist"
Ejecuta el script de inicialización:
```bash
psql -U postgres -d battlenet_db -f scripts/init-db.sql
```

