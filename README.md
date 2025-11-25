# Battle.net Platform - Full Stack Application

**Desarrollado por:** Eddi Andreé Salazar Matos

## 📋 Descripción

Plataforma web Full Stack profesional inspirada en Battle.net, desarrollada para demostración de habilidades técnicas y aprendizaje. Este proyecto registra cuentas de usuarios generales y está diseñado exclusivamente para **fines educativos y demostración personal**.

> ⚠️ **Nota:** Este proyecto es solo para fines educativos y demostración personal. No está destinado para uso comercial.

## 🚀 Características Implementadas

### Frontend (Angular 17)
- ✅ **Autenticación**: Sistema de login y registro de usuarios
- ✅ **Dashboard**: Panel con estadísticas y gráficas dinámicas
- ✅ **CRUD Completo**: Gestión de juegos y usuarios
- ✅ **Animaciones Avanzadas**: GSAP, Three.js, efectos neón
- ✅ **Diseño Responsive**: Optimizado para todos los dispositivos
- ✅ **UI Moderna**: Glass morphism, efectos parallax

### Backend (Node.js + Express)
- ✅ **API RESTful**: Endpoints organizados y documentados
- ✅ **Autenticación JWT**: Sistema seguro de tokens
- ✅ **Sistema de Roles**: Admin, Moderator, User
- ✅ **Base de Datos**: PostgreSQL con relaciones y validaciones
- ✅ **CRUD Avanzado**: Operaciones completas con filtros
- ✅ **Dashboard API**: Estadísticas y analytics

### Base de Datos (PostgreSQL)
- ✅ **Tablas Relacionales**: users, games, user_activities, analytics
- ✅ **Índices Optimizados**: Para mejor rendimiento
- ✅ **Validaciones**: Constraints y foreign keys

### Python Services
- ✅ **Scripts de Utilidad**: Setup, verificación, mantenimiento
- ✅ **Flask API**: Analytics avanzados (opcional)
- ✅ **Database Manager**: Clase reutilizable para gestión

## 🛠️ Stack Tecnológico

### Frontend
- Angular 17
- TypeScript
- GSAP (Animaciones)
- Three.js (Efectos 3D)
- Chart.js (Gráficas)
- Tailwind CSS
- SCSS

### Backend
- Node.js
- Express.js
- PostgreSQL
- JWT (Autenticación)
- Bcrypt (Hashing)
- Express-validator

### Base de Datos
- PostgreSQL 17

### Python (Opcional)
- Flask
- psycopg2
- pandas (para analytics avanzados)

## 📦 Instalación

### 1. Frontend
```bash
npm install
npm start
```
Frontend disponible en: `http://localhost:4200`

### 2. Backend
```bash
cd backend
npm install
npm run dev
```
Backend disponible en: `http://localhost:3000`

### 3. Base de Datos
1. Crear base de datos PostgreSQL: `battlenet_db`
2. Ejecutar script: `backend/scripts/complete_setup.sql` en pgAdmin
3. O usar Python: `python setup.py`

### 4. Python (Opcional)
```bash
cd python
pip install -r requirements.txt
python app.py
```

## 🌐 Deploy a GitHub Pages

El proyecto está configurado para deploy automático en GitHub Pages.

### Pasos Rápidos:
1. Sube tu código a GitHub
2. Ve a **Settings** → **Pages** → Selecciona **GitHub Actions**
3. El deploy será automático en cada push

📖 **Guía completa:** Ver [DEPLOY_GITHUB_PAGES.md](DEPLOY_GITHUB_PAGES.md)

### Build para GitHub Pages:
```bash
npm run build:gh-pages
```

## 🎯 Funcionalidades Principales

### Autenticación
- Registro de usuarios
- Login con JWT
- Protección de rutas
- Gestión de sesión

### Dashboard
- Estadísticas en tiempo real
- Gráficas de juegos por categoría
- Top juegos
- Actividades recientes

### CRUD Games
- Crear, editar, eliminar juegos
- Filtros avanzados
- Búsqueda y ordenamiento
- Paginación

### Gestión de Usuarios
- Listar usuarios
- Cambiar roles (Admin)
- Ver perfiles

## 📁 Estructura del Proyecto

```
battle-net-platform/
├── src/                    # Frontend Angular
│   └── app/
│       ├── components/     # Componentes de la aplicación
│       ├── services/       # Servicios HTTP
│       └── guards/         # Route guards
├── backend/                # Backend Node.js
│   ├── routes/            # API routes
│   ├── middleware/        # Auth middleware
│   ├── config/            # Configuración DB
│   └── scripts/           # SQL scripts
├── python/                # Scripts Python (opcional)
│   ├── db_manager.py      # Gestor de BD
│   ├── verificar_registro.py  # Verificar usuarios
│   └── app.py             # Flask API (opcional)
└── README.md
```

## 🔐 Credenciales por Defecto

**Admin:**
- Email: `admin@battlenet.com`
- Password: `admin123`

## 📝 Notas Importantes

- Este proyecto es **solo para fines educativos**
- Inspirado en Battle.net para demostración de habilidades
- Registra cuentas de usuarios generales
- No está destinado para uso comercial

## 🎓 Propósito Educativo

Este proyecto fue desarrollado para:
- Demostrar habilidades en desarrollo Full Stack
- Aprender tecnologías modernas (Angular, Node.js, PostgreSQL)
- Crear un portafolio de proyectos
- Practicar integración de múltiples tecnologías

## 📄 Licencia

Este proyecto es de código abierto para fines educativos y demostración personal.

---

**Desarrollado con ❤️ por Eddi Andreé Salazar Matos**

*Para demostración de habilidades técnicas y aprendizaje*
