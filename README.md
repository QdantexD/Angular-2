# Battle Net Platform - Advanced Angular Demo

Una plataforma web profesional y elegante construida con Angular, inspirada en Battle.net, con animaciones épicas, efectos neón y tecnologías avanzadas.

## 🚀 Características

- **Animaciones Avanzadas**: Implementadas con GSAP (GreenSock Animation Platform)
- **Efectos 3D**: Fondo animado con Three.js
- **Efectos Neón**: Diseño moderno con efectos de iluminación neón
- **Partículas Interactivas**: Sistema de partículas que reacciona al mouse
- **Diseño Responsive**: Optimizado para todos los dispositivos
- **Tailwind CSS**: Estilos modernos y personalizables
- **Glass Morphism**: Efectos de vidrio esmerilado
- **Scroll Animations**: Animaciones basadas en scroll con ScrollTrigger

## 🛠️ Tecnologías Utilizadas

- **Angular 17**: Framework principal
- **GSAP 3.12**: Animaciones profesionales
- **Three.js**: Gráficos 3D y efectos visuales
- **Tailwind CSS**: Framework de utilidades CSS
- **TypeScript**: Tipado estático
- **SCSS**: Preprocesador CSS

## 📦 Instalación

1. **Instalar dependencias:**
```bash
npm install
```

2. **Instalar Angular CLI globalmente (si no lo tienes):**
```bash
npm install -g @angular/cli
```

## 🎮 Desarrollo

Para iniciar el servidor de desarrollo:

```bash
npm start
# o
ng serve
```

La aplicación estará disponible en `http://localhost:4200`

## 🏗️ Build

Para construir la aplicación para producción:

```bash
npm run build
# o
ng build
```

Los archivos compilados estarán en la carpeta `dist/battle-net-platform`

## 📁 Estructura del Proyecto

```
src/
├── app/
│   ├── components/
│   │   ├── animated-background/    # Fondo 3D con Three.js
│   │   ├── header/                 # Header con efectos neón
│   │   ├── hero-section/           # Sección principal con animaciones
│   │   ├── game-card/              # Tarjetas de juegos interactivas
│   │   ├── particle-background/    # Partículas animadas
│   │   ├── navigation/             # Navegación
│   │   └── home/                   # Página principal
│   ├── app.component.ts
│   ├── app.module.ts
│   └── app-routing.module.ts
├── assets/                         # Recursos estáticos
├── styles.scss                     # Estilos globales
└── index.html
```

## 🎨 Componentes Principales

### AnimatedBackgroundComponent
Fondo 3D con partículas usando Three.js que reacciona al movimiento del mouse.

### HeroSectionComponent
Sección hero con animaciones GSAP, efectos parallax y texto con glow neón.

### GameCardComponent
Tarjetas de juegos con efectos hover, animaciones de entrada y efectos neón personalizados.

### ParticleBackgroundComponent
Sistema de partículas interactivo con Canvas API que crea conexiones dinámicas.

### HeaderComponent
Header fijo con efectos glass morphism y animaciones de navegación.

## 🎯 Características de Animación

- **Animaciones de entrada**: Elementos aparecen con efectos suaves
- **Hover effects**: Interacciones visuales al pasar el mouse
- **Scroll animations**: Animaciones basadas en el scroll
- **Parallax effects**: Efectos de profundidad
- **Particle systems**: Sistemas de partículas interactivos
- **3D backgrounds**: Fondos tridimensionales animados

## 🎨 Personalización

Los colores neón y efectos pueden ser personalizados en:
- `tailwind.config.js` - Configuración de colores
- `src/styles.scss` - Estilos globales y efectos neón
- Componentes individuales - Estilos específicos

## 📱 Responsive Design

La aplicación está completamente optimizada para:
- Desktop (1920px+)
- Laptop (1024px - 1919px)
- Tablet (768px - 1023px)
- Mobile (< 768px)

## 🔧 Configuración Adicional

### Variables de Entorno
Puedes crear un archivo `.env` para configuraciones específicas del entorno.

### Optimizaciones
- Lazy loading de componentes
- Tree shaking automático
- Minificación en producción
- Code splitting

## 📝 Notas

- Las imágenes de los juegos se cargan desde Unsplash (puedes reemplazarlas con tus propias imágenes)
- Los efectos neón pueden requerir ajustes según el navegador
- Three.js requiere WebGL para funcionar correctamente

## 🚀 Próximas Mejoras

- [ ] Sistema de autenticación
- [ ] Integración con API de juegos
- [ ] Modo oscuro/claro
- [ ] Más efectos de partículas
- [ ] Animaciones de transición entre páginas
- [ ] Sistema de notificaciones
- [ ] Chat en tiempo real

## 📄 Licencia

Este proyecto es una demostración de habilidades técnicas y puede ser usado como referencia para proyectos similares.

## 👨‍💻 Desarrollo

Desarrollado con Angular y tecnologías modernas para demostrar capacidades avanzadas en desarrollo web frontend.

---

**¡Disfruta explorando la plataforma!** 🎮✨

