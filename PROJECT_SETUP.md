# 🚀 Battle.net Platform - Full Stack Setup Guide

## 📋 Descripción del Proyecto

Aplicación Full Stack completa con:
- ✅ **Frontend**: Angular 17 con animaciones GSAP y efectos neón
- ✅ **Backend**: Node.js + Express + PostgreSQL
- ✅ **Autenticación**: JWT con roles de usuario
- ✅ **Dashboard**: Con gráficas dinámicas y estadísticas
- ✅ **CRUD**: Gestión completa de juegos y usuarios
- ✅ **Filtros Avanzados**: Búsqueda, categorías, ordenamiento
- ✅ **Roles**: Admin, Moderator, User

## 🛠️ Instalación

### 1. Backend Setup

```bash
# Navegar a la carpeta backend
cd backend

# Instalar dependencias
npm install

# Configurar variables de entorno
cp .env.example .env
# Editar .env con tus credenciales de PostgreSQL

# Crear base de datos PostgreSQL
psql -U postgres
CREATE DATABASE battlenet_db;
\q

# Ejecutar script de inicialización
psql -U postgres -d battlenet_db -f scripts/init-db.sql

# Iniciar servidor
npm run dev
```

El backend estará disponible en: `http://localhost:3000`

### 2. Frontend Setup

```bash
# En la raíz del proyecto
npm install

# Instalar dependencias adicionales para gráficas
npm install chart.js ng2-charts --save

# Iniciar servidor de desarrollo
npm start
```

El frontend estará disponible en: `http://localhost:4200`

## 📁 Estructura del Proyecto

```
battle-net-platform/
├── backend/
│   ├── config/
│   │   └── database.js          # Configuración PostgreSQL
│   ├── middleware/
│   │   └── auth.js               # JWT authentication
│   ├── routes/
│   │   ├── auth.js               # Login/Register
│   │   ├── games.js               # CRUD Games
│   │   ├── users.js               # User management
│   │   ├── dashboard.js           # Dashboard stats
│   │   └── analytics.js           # Analytics data
│   ├── scripts/
│   │   └── init-db.sql            # Database schema
│   └── server.js                  # Express server
│
├── src/
│   └── app/
│       ├── components/
│       │   ├── auth/              # Login/Register
│       │   ├── dashboard/         # Dashboard con gráficas
│       │   ├── game-management/   # CRUD Games
│       │   └── user-management/   # User management
│       ├── services/
│       │   ├── auth.service.ts    # Authentication
│       │   ├── api.service.ts     # HTTP client
│       │   ├── game.service.ts   # Games API
│       │   └── dashboard.service.ts # Dashboard API
│       └── guards/
│           ├── auth.guard.ts      # Route protection
│           └── admin.guard.ts     # Admin only routes
```

## 🔐 Credenciales por Defecto

**Admin User:**
- Email: `admin@battlenet.com`
- Password: `admin123` (cambiar en producción)

## 📊 Características Implementadas

### Autenticación
- ✅ Registro de usuarios
- ✅ Login con JWT
- ✅ Protección de rutas
- ✅ Gestión de sesión

### Dashboard
- ✅ Estadísticas en tiempo real
- ✅ Gráficas de juegos por categoría
- ✅ Gráficas de juegos creados en el tiempo
- ✅ Top 10 juegos
- ✅ Actividades recientes

### CRUD Games
- ✅ Crear juego (Admin/Moderator)
- ✅ Editar juego (Admin/Moderator)
- ✅ Eliminar juego (Admin)
- ✅ Listar con filtros avanzados
- ✅ Búsqueda por texto
- ✅ Filtro por categoría
- ✅ Ordenamiento (título, precio, rating, fecha)

### Gestión de Usuarios
- ✅ Listar usuarios (Admin)
- ✅ Cambiar roles (Admin)
- ✅ Filtros por rol y búsqueda

### Filtros Avanzados
- ✅ Paginación
- ✅ Búsqueda por texto
- ✅ Filtro por categoría/rol
- ✅ Ordenamiento múltiple
- ✅ Límite de resultados

## 🎨 Tecnologías Utilizadas

**Frontend:**
- Angular 17
- GSAP (Animaciones)
- Three.js (Efectos 3D)
- Tailwind CSS
- Chart.js (Gráficas)

**Backend:**
- Node.js
- Express
- PostgreSQL
- JWT
- bcryptjs

## 🔄 API Endpoints

Ver `backend/README.md` para documentación completa de la API.

## 🚦 Próximos Pasos

1. Instalar PostgreSQL si no lo tienes
2. Configurar variables de entorno en `backend/.env`
3. Ejecutar script de inicialización de BD
4. Iniciar backend: `cd backend && npm run dev`
5. Iniciar frontend: `npm start`
6. Acceder a `http://localhost:4200`
7. Registrar un usuario o usar credenciales admin

## 📝 Notas

- El proyecto está listo para demostración con funcionalidad completa
- Todas las rutas están protegidas con guards
- El sistema de roles está completamente implementado
- Los filtros avanzados funcionan en tiempo real
- Las gráficas se actualizan dinámicamente

