# ⚡ Inicio Rápido del Backend

## ✅ Pasos Completados

1. ✅ Dependencias instaladas (`npm install`)
2. ✅ Archivo `.env` creado

## 🔧 Configuración Necesaria

### 1. Editar archivo `.env`

Abre `backend/.env` y cambia:
- `DB_PASSWORD=postgres` → Tu contraseña real de PostgreSQL

### 2. Crear Base de Datos (si no existe)

```bash
psql -U postgres
CREATE DATABASE battlenet_db;
\q
```

### 3. Inicializar Tablas

```bash
cd backend
psql -U postgres -d battlenet_db -f scripts/init-db.sql
```

### 4. Iniciar Servidor

```bash
npm run dev
```

## 🎯 Verificar que Funciona

Abre: http://localhost:3000/api/health

Deberías ver:
```json
{"status":"OK","message":"Battle.net API is running"}
```

## 🔐 Login de Prueba

- **Email:** admin@battlenet.com
- **Password:** admin123

## 📝 Notas

- El servidor se reinicia automáticamente con `nodemon` cuando cambias archivos
- Los logs aparecen en la consola
- Si hay errores de conexión a la BD, verifica que PostgreSQL esté corriendo

