/**
 * Script para crear archivo .env si no existe
 * Ejecutar: node create-env.js
 */
const fs = require('fs');
const path = require('path');

const envPath = path.join(__dirname, '.env');
const envExample = `# Battle.net Backend Configuration
# Database
DB_HOST=localhost
DB_PORT=5432
DB_NAME=battlenet_db
DB_USER=postgres
DB_PASSWORD=123456

# JWT
JWT_SECRET=battlenet_secret_key_2024_change_in_production
JWT_EXPIRE=7d

# Server
PORT=3000
NODE_ENV=development
`;

if (fs.existsSync(envPath)) {
  console.log('✅ Archivo .env ya existe');
  console.log(`   Ubicación: ${envPath}`);
  
  // Leer y mostrar configuración actual
  const currentEnv = fs.readFileSync(envPath, 'utf8');
  console.log('\n📋 Configuración actual:');
  console.log(currentEnv);
} else {
  console.log('📝 Creando archivo .env...');
  fs.writeFileSync(envPath, envExample, 'utf8');
  console.log('✅ Archivo .env creado exitosamente!');
  console.log(`   Ubicación: ${envPath}`);
  console.log('\n📋 Configuración por defecto:');
  console.log(envExample);
  console.log('💡 Edita backend/.env para cambiar las credenciales si es necesario');
}

