# Guía de Instalación - Battle Net Platform

## Requisitos Previos

- Node.js (versión 18 o superior)
- npm (versión 9 o superior)
- Angular CLI (se instalará globalmente o localmente)

## Pasos de Instalación

### 1. Instalar Node.js y npm

Si no tienes Node.js instalado, descárgalo desde [nodejs.org](https://nodejs.org/)

Verifica la instalación:
```bash
node --version
npm --version
```

### 2. Instalar Angular CLI

```bash
npm install -g @angular/cli
```

O si prefieres instalarlo localmente:
```bash
npm install @angular/cli --save-dev
```

### 3. Instalar Dependencias del Proyecto

Navega a la carpeta del proyecto y ejecuta:

```bash
npm install
```

Esto instalará todas las dependencias necesarias:
- Angular 17
- GSAP (animaciones)
- Three.js (efectos 3D)
- Tailwind CSS (estilos)
- TypeScript
- Y todas las demás dependencias

### 4. Ejecutar el Proyecto

Una vez instaladas las dependencias, ejecuta:

```bash
npm start
```

O alternativamente:

```bash
ng serve
```

El servidor de desarrollo se iniciará en `http://localhost:4200`

### 5. Abrir en el Navegador

Abre tu navegador y navega a:
```
http://localhost:4200
```

## Solución de Problemas

### Error: "ng: command not found"

Si obtienes este error, asegúrate de que Angular CLI esté instalado globalmente:
```bash
npm install -g @angular/cli
```

### Error: "Cannot find module"

Si obtienes errores de módulos no encontrados:
```bash
rm -rf node_modules package-lock.json
npm install
```

### Error con Three.js o WebGL

Asegúrate de que tu navegador soporte WebGL. Puedes verificar en:
- Chrome: chrome://gpu
- Firefox: about:support

### Problemas con Tailwind CSS

Si los estilos de Tailwind no se aplican:
```bash
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init
```

## Comandos Útiles

### Desarrollo
```bash
npm start          # Inicia el servidor de desarrollo
ng serve           # Alternativa
ng serve --open    # Abre automáticamente en el navegador
```

### Build
```bash
npm run build      # Build para producción
ng build           # Alternativa
ng build --prod    # Build optimizado
```

### Testing
```bash
npm test           # Ejecuta las pruebas
ng test            # Alternativa
```

### Linting
```bash
ng lint            # Verifica el código
```

## Estructura de Carpetas Después de la Instalación

```
Angular-2/
├── node_modules/          # Dependencias instaladas
├── src/                   # Código fuente
│   ├── app/              # Componentes Angular
│   ├── assets/           # Recursos estáticos
│   ├── styles.scss       # Estilos globales
│   └── index.html        # HTML principal
├── dist/                 # Build de producción (después de compilar)
├── angular.json          # Configuración de Angular
├── package.json          # Dependencias del proyecto
├── tailwind.config.js    # Configuración de Tailwind
└── tsconfig.json         # Configuración de TypeScript
```

## Notas Importantes

1. **Primera Instalación**: La primera vez que ejecutes `npm install`, puede tardar varios minutos.

2. **Puerto en Uso**: Si el puerto 4200 está en uso, Angular te preguntará si quieres usar otro puerto.

3. **Hot Reload**: El servidor de desarrollo tiene hot reload activado, los cambios se reflejan automáticamente.

4. **Navegadores Soportados**: 
   - Chrome (recomendado)
   - Firefox
   - Edge
   - Safari

5. **WebGL**: Los efectos 3D requieren WebGL. Asegúrate de tenerlo habilitado en tu navegador.

## Próximos Pasos

Una vez que el proyecto esté ejecutándose:

1. Explora los componentes en `src/app/components/`
2. Modifica los estilos en los archivos `.scss`
3. Personaliza las animaciones en los archivos `.ts`
4. Agrega tus propias imágenes en `src/assets/`

## Soporte

Si encuentras problemas durante la instalación:

1. Verifica que todas las versiones sean compatibles
2. Revisa la consola del navegador para errores
3. Asegúrate de tener los permisos necesarios
4. Intenta limpiar la caché: `npm cache clean --force`

¡Disfruta desarrollando! 🚀

