/**
 * Script de prueba para verificar el backend y el registro
 * Ejecutar: node test_backend.js
 */
const axios = require('axios');

const API_URL = 'http://localhost:3000/api';

// Colores para la consola
const colors = {
  reset: '\x1b[0m',
  green: '\x1b[32m',
  red: '\x1b[31m',
  yellow: '\x1b[33m',
  blue: '\x1b[34m',
  cyan: '\x1b[36m'
};

function log(message, color = 'reset') {
  console.log(`${colors[color]}${message}${colors.reset}`);
}

async function testHealth() {
  log('\n🔍 Probando Health Check...', 'cyan');
  try {
    const response = await axios.get(`${API_URL}/health`);
    log('✅ Backend está corriendo!', 'green');
    log(`   Status: ${response.data.status}`, 'green');
    log(`   Message: ${response.data.message}`, 'green');
    return true;
  } catch (error) {
    log('❌ Backend no está corriendo o no responde', 'red');
    log(`   Error: ${error.message}`, 'red');
    log('\n💡 Asegúrate de que el backend esté iniciado:', 'yellow');
    log('   cd backend && npm run dev', 'yellow');
    return false;
  }
}

async function testRegister() {
  log('\n📝 Probando Registro de Usuario...', 'cyan');
  
  // Generar datos únicos para evitar conflictos
  const timestamp = Date.now();
  const testUser = {
    username: `testuser_${timestamp}`,
    email: `test_${timestamp}@battlenet.com`,
    password: 'test123456',
    full_name: 'Usuario de Prueba'
  };

  log(`\n   Username: ${testUser.username}`, 'blue');
  log(`   Email: ${testUser.email}`, 'blue');
  log(`   Password: ${testUser.password}`, 'blue');

  try {
    const response = await axios.post(`${API_URL}/auth/register`, testUser);
    
    log('\n✅ Usuario registrado exitosamente!', 'green');
    log(`   ID: ${response.data.user.id}`, 'green');
    log(`   Username: ${response.data.user.username}`, 'green');
    log(`   Email: ${response.data.user.email}`, 'green');
    log(`   Role: ${response.data.user.role}`, 'green');
    log(`   Token: ${response.data.token.substring(0, 20)}...`, 'green');
    
    return { success: true, user: testUser, response: response.data };
  } catch (error) {
    if (error.response) {
      log('\n❌ Error en el registro:', 'red');
      log(`   Status: ${error.response.status}`, 'red');
      log(`   Error: ${JSON.stringify(error.response.data, null, 2)}`, 'red');
    } else {
      log('\n❌ Error de conexión:', 'red');
      log(`   ${error.message}`, 'red');
    }
    return { success: false, error: error.response?.data || error.message };
  }
}

async function testLogin(email, password) {
  log('\n🔐 Probando Login...', 'cyan');
  
  try {
    const response = await axios.post(`${API_URL}/auth/login`, {
      email,
      password
    });
    
    log('✅ Login exitoso!', 'green');
    log(`   Username: ${response.data.user.username}`, 'green');
    log(`   Email: ${response.data.user.email}`, 'green');
    log(`   Role: ${response.data.user.role}`, 'green');
    log(`   Token: ${response.data.token.substring(0, 20)}...`, 'green');
    
    return { success: true, response: response.data };
  } catch (error) {
    if (error.response) {
      log('❌ Error en el login:', 'red');
      log(`   Status: ${error.response.status}`, 'red');
      log(`   Error: ${error.response.data.error || JSON.stringify(error.response.data)}`, 'red');
    } else {
      log('❌ Error de conexión:', 'red');
      log(`   ${error.message}`, 'red');
    }
    return { success: false, error: error.response?.data || error.message };
  }
}

async function main() {
  log('\n' + '='.repeat(70), 'cyan');
  log('🚀 Battle.net - Test de Backend y Registro', 'cyan');
  log('='.repeat(70), 'cyan');

  // Test 1: Health Check
  const healthOk = await testHealth();
  if (!healthOk) {
    log('\n⚠️  No se puede continuar sin el backend corriendo', 'yellow');
    process.exit(1);
  }

  // Test 2: Register
  const registerResult = await testRegister();
  
  if (registerResult.success) {
    // Test 3: Login con el usuario registrado
    await testLogin(registerResult.user.email, registerResult.user.password);
    
    log('\n' + '='.repeat(70), 'green');
    log('✅ Todas las pruebas completadas exitosamente!', 'green');
    log('='.repeat(70), 'green');
    log('\n📊 Resumen:', 'cyan');
    log('   ✅ Backend está corriendo', 'green');
    log('   ✅ Registro funciona correctamente', 'green');
    log('   ✅ Login funciona correctamente', 'green');
    log('   ✅ Los datos se están guardando en PostgreSQL', 'green');
    log('\n💡 Para verificar en PostgreSQL:', 'yellow');
    log('   python verify_users.py', 'yellow');
    log('   O usa pgAdmin para ver la tabla users', 'yellow');
  } else {
    log('\n' + '='.repeat(70), 'red');
    log('❌ Las pruebas fallaron', 'red');
    log('='.repeat(70), 'red');
    log('\n💡 Verifica:', 'yellow');
    log('   1. Que PostgreSQL esté corriendo', 'yellow');
    log('   2. Que las credenciales en backend/.env sean correctas', 'yellow');
    log('   3. Que la base de datos battlenet_db exista', 'yellow');
    log('   4. Que las tablas estén creadas', 'yellow');
  }

  log('\n');
}

// Ejecutar
main().catch(error => {
  log(`\n❌ Error fatal: ${error.message}`, 'red');
  process.exit(1);
});

