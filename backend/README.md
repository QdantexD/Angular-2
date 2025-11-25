# Battle.net Platform - Backend API

Backend completo con Node.js, Express, PostgreSQL y autenticación JWT.

## Características

- ✅ Autenticación JWT
- ✅ Sistema de roles (Admin, Moderator, User)
- ✅ CRUD completo de Games
- ✅ CRUD de Usuarios
- ✅ Dashboard con estadísticas
- ✅ Analytics y gráficas
- ✅ Filtros avanzados
- ✅ Paginación
- ✅ Validación de datos

## Instalación

1. Instalar dependencias:
```bash
npm install
```

2. Configurar variables de entorno:
```bash
cp .env.example .env
# Editar .env con tus credenciales
```

3. Configurar PostgreSQL:
```bash
# Crear base de datos
psql -U postgres
CREATE DATABASE battlenet_db;

# Ejecutar script de inicialización
psql -U postgres -d battlenet_db -f scripts/init-db.sql
```

4. Iniciar servidor:
```bash
# Desarrollo
npm run dev

# Producción
npm start
```

## API Endpoints

### Autenticación
- `POST /api/auth/register` - Registrar usuario
- `POST /api/auth/login` - Iniciar sesión
- `GET /api/auth/me` - Obtener usuario actual

### Games
- `GET /api/games` - Listar juegos (con filtros)
- `GET /api/games/:id` - Obtener juego
- `POST /api/games` - Crear juego (Admin/Moderator)
- `PUT /api/games/:id` - Actualizar juego (Admin/Moderator)
- `DELETE /api/games/:id` - Eliminar juego (Admin)

### Usuarios
- `GET /api/users` - Listar usuarios (Admin)
- `PUT /api/users/:id` - Actualizar usuario
- `PUT /api/users/:id/password` - Cambiar contraseña
- `PUT /api/users/:id/role` - Cambiar rol (Admin)

### Dashboard
- `GET /api/dashboard/stats` - Estadísticas del dashboard
- `GET /api/dashboard/analytics` - Datos para gráficas

### Analytics
- `GET /api/analytics/activities` - Actividades de usuario
- `POST /api/analytics/metrics` - Registrar métrica (Admin/Moderator)

## Filtros Avanzados

### Games
- `?page=1` - Página
- `?limit=10` - Límite por página
- `?category=RPG` - Filtrar por categoría
- `?search=diablo` - Búsqueda
- `?sort=title&order=asc` - Ordenar

### Usuarios
- `?page=1` - Página
- `?limit=10` - Límite
- `?role=admin` - Filtrar por rol
- `?search=john` - Búsqueda

## Autenticación

Incluir token en header:
```
Authorization: Bearer <token>
```

## Roles

- **admin**: Acceso completo
- **moderator**: Puede crear/editar games
- **user**: Solo lectura

