# 📁 Estructura del Proyecto - Battle.net Platform

**Desarrollado por:** Eddi Andreé Salazar Matos  
**Propósito:** Fines educativos y demostración personal

## 📂 Estructura Completa

```
battle-net-platform/
│
├── 📄 README.md                    # Documentación principal
├── 📄 ESTRUCTURA_PROYECTO.md       # Este archivo
│
├── 🎨 Frontend (Angular 17)
│   ├── src/
│   │   ├── app/
│   │   │   ├── components/
│   │   │   │   ├── auth/           # Login y Register
│   │   │   │   ├── dashboard/      # Dashboard con gráficas
│   │   │   │   ├── game-management/ # CRUD de juegos
│   │   │   │   ├── user-management/ # Gestión de usuarios
│   │   │   │   ├── user-list/      # Lista de usuarios
│   │   │   │   ├── home/           # Página principal
│   │   │   │   ├── header/         # Header con navegación
│   │   │   │   ├── hero-section/   # Sección hero
│   │   │   │   ├── game-card/      # Tarjetas de juegos
│   │   │   │   └── background-3d/  # Fondo 3D
│   │   │   ├── services/           # Servicios HTTP
│   │   │   ├── guards/             # Route guards
│   │   │   └── app.module.ts
│   │   └── styles.scss
│   ├── package.json
│   └── angular.json
│
├── 🔧 Backend (Node.js + Express)
│   ├── routes/
│   │   ├── auth.js                 # Autenticación
│   │   ├── games.js                # CRUD Games
│   │   ├── users.js                # Gestión usuarios
│   │   ├── dashboard.js            # Dashboard API
│   │   └── analytics.js            # Analytics
│   ├── middleware/
│   │   └── auth.js                 # JWT middleware
│   ├── config/
│   │   └── database.js             # Configuración PostgreSQL
│   ├── scripts/
│   │   └── complete_setup.sql      # Script SQL completo
│   ├── create-env.js               # Crear archivo .env
│   ├── server.js                   # Servidor principal
│   ├── package.json
│   └── README.md
│
├── 🐍 Python (Scripts y Utilidades)
│   ├── config.py                   # Configuración centralizada
│   ├── db_manager.py               # Gestor de BD reutilizable
│   ├── db_setup_improved.py        # Setup mejorado de BD
│   ├── setup.py                    # Setup principal
│   ├── verificar_registro.py       # Verificar usuarios
│   ├── utils.py                    # Utilidades (check, seed, hash)
│   ├── app.py                      # Flask API (opcional)
│   ├── requirements.txt
│   └── README.md
│
└── 🗄️ Base de Datos (PostgreSQL)
    └── Tablas:
        ├── users                   # Usuarios registrados
        ├── games                   # Juegos
        ├── user_activities         # Actividades
        └── analytics               # Analytics
```

## 📋 Archivos Principales

### Frontend
- `src/app/components/` - Todos los componentes de la aplicación
- `src/app/services/` - Servicios para comunicación con API
- `src/app/guards/` - Protección de rutas

### Backend
- `backend/server.js` - Servidor Express
- `backend/routes/` - Todas las rutas API
- `backend/middleware/auth.js` - Autenticación JWT
- `backend/config/database.js` - Conexión PostgreSQL

### Python
- `python/db_setup_improved.py` - Setup de base de datos
- `python/verificar_registro.py` - Verificar usuarios
- `python/utils.py` - Utilidades
- `python/app.py` - Flask API (opcional)

## 🚀 Scripts Útiles

### Frontend
```bash
npm start          # Iniciar servidor desarrollo
npm run build      # Build para producción
```

### Backend
```bash
cd backend
npm run dev        # Iniciar con nodemon
npm start          # Iniciar producción
```

### Python
```bash
cd python
python setup.py                    # Setup inicial
python verificar_registro.py --all # Ver usuarios
python utils.py check              # Verificar BD
```

## 📝 Notas

- **Frontend**: Angular 17 con animaciones GSAP y Three.js
- **Backend**: Node.js + Express + PostgreSQL
- **Python**: Scripts de utilidad y Flask API opcional
- **Base de Datos**: PostgreSQL con relaciones y validaciones

---

**Proyecto educativo y de demostración personal**

