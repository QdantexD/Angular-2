# Battle.net Platform - Backend API

Backend completo con Node.js, Express, PostgreSQL y autenticación JWT.

**Desarrollado por:** Eddi Andreé Salazar Matos  
**Propósito:** Fines educativos y demostración personal

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
# El archivo .env se crea automáticamente con create-env.js
node create-env.js
```

O crear manualmente `backend/.env`:
```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=battlenet_db
DB_USER=postgres
DB_PASSWORD=123456
JWT_SECRET=battlenet_secret_key_2024_change_in_production
JWT_EXPIRE=7d
PORT=3000
NODE_ENV=development
```

3. Configurar PostgreSQL:
- Crear base de datos: `battlenet_db`
- Ejecutar: `backend/scripts/complete_setup.sql` en pgAdmin
- O usar Python: `python setup.py`

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
- `GET /api/users` - Listar usuarios (Autenticado)
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

## 🔐 Credenciales por Defecto

**Admin:**
- Email: `admin@battlenet.com`
- Password: `admin123`

## 📝 Notas

- Este backend es parte de un proyecto educativo
- Inspirado en Battle.net para demostración
- Registra cuentas de usuarios generales
- Solo para fines educativos y demostración personal
