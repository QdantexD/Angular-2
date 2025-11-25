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

## 🌐 Deploy a GitHub Pages

El proyecto está configurado para deploy automático en GitHub Pages.

### Pasos Rápidos:
1. Sube tu código a GitHub
2. Ve a **Settings** → **Pages** → Selecciona **GitHub Actions**
3. El deploy será automático en cada push


### Configuración del Base Href

Si tu repositorio tiene otro nombre, actualiza:
- `angular.json` → `configurations.github-pages.baseHref`
- `src/index.html` → `<base href="/TU_REPOSITORIO/">`

### ⚠️ Limitaciones de GitHub Pages

GitHub Pages **solo sirve archivos estáticos**, por lo que:
- ❌ **Backend NO funcionará** (Node.js/Express)
- ❌ **Base de datos NO funcionará** (PostgreSQL)
- ❌ **Login/Register real NO funcionará**
- ❌ **Dashboard con datos reales NO funcionará**

Para una demo completa, necesitarás:
- **Frontend:** GitHub Pages o Netlify/Vercel
- **Backend:** Heroku, Railway, Render
- **Base de Datos:** Supabase, ElephantSQL, Neon

## 🔧 Scripts Disponibles

### Frontend
```bash
npm start              # Servidor de desarrollo
npm run build          # Build para desarrollo
npm run build:prod     # Build para producción
npm run build:gh-pages # Build para GitHub Pages
npm test               # Ejecutar tests
```

### Backend
```bash
cd backend
npm run dev            # Desarrollo con nodemon
npm start               # Producción
```

### Python
```bash
cd python
python setup.py                    # Setup inicial de BD
python verificar_registro.py --all # Verificar usuarios
python utils.py check              # Verificar estado de BD
python app.py                      # Iniciar Flask API
```

## 🔐 Credenciales por Defecto

**Admin:**
- Email: `admin@battlenet.com`
- Password: `admin123`

## 🐛 Solución de Problemas

### Error de Dependencias (ERESOLVE)

Si encuentras errores de dependencias al instalar:

```bash
# Limpiar e reinstalar
Remove-Item -Recurse -Force node_modules
Remove-Item -Force package-lock.json
npm install
```

El workflow de GitHub Actions usa `--legacy-peer-deps` automáticamente para evitar conflictos.

El dashboard usa gráficas CSS personalizadas en lugar de Chart.js.

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

## 🔗 Enlaces Útiles

- **Estructura del Proyecto**: Ver [ESTRUCTURA_PROYECTO.md](ESTRUCTURA_PROYECTO.md)
- **Solución de Dependencias**: Ver [SOLUCION_DEPENDENCIAS.md](SOLUCION_DEPENDENCIAS.md)
- **Backend README**: Ver [backend/README.md](backend/README.md)
- **Python README**: Ver [python/README.md](python/README.md)

---

**Desarrollado con ❤️ por Eddi Andreé Salazar Matos**

*Para demostración de habilidades técnicas y aprendizaje*
