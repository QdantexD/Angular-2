const express = require('express');
const cors = require('cors');
const morgan = require('morgan');
const helmet = require('helmet');
require('dotenv').config();

const db = require('./config/database');
const authRoutes = require('./routes/auth');
const userRoutes = require('./routes/users');
const gameRoutes = require('./routes/games');
const dashboardRoutes = require('./routes/dashboard');
const analyticsRoutes = require('./routes/analytics');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(helmet());
app.use(cors());
app.use(morgan('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Database connection
db.connect()
  .then(() => console.log('✅ Database connected'))
  .catch(err => {
    console.error('❌ Database connection error:', err.message);
    console.error('💡 Verifica que:');
    console.error('   1. PostgreSQL esté corriendo');
    console.error('   2. Las credenciales en .env sean correctas');
    console.error('   3. La base de datos battlenet_db exista');
    // No detener el servidor, permitir que continúe para ver otros errores
  });

// Routes
app.use('/api/auth', authRoutes);
app.use('/api/users', userRoutes);
app.use('/api/games', gameRoutes);
app.use('/api/dashboard', dashboardRoutes);
app.use('/api/analytics', analyticsRoutes);

// Health check
app.get('/api/health', (req, res) => {
  res.json({ status: 'OK', message: 'Battle.net API is running' });
});

// Error handling
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ 
    error: 'Something went wrong!',
    message: process.env.NODE_ENV === 'development' ? err.message : undefined
  });
});

// Start server
const server = app.listen(PORT, () => {
  console.log(`🚀 Server running on port ${PORT}`);
  console.log(`📡 Health check: http://localhost:${PORT}/api/health`);
}).on('error', (err) => {
  if (err.code === 'EADDRINUSE') {
    console.error(`\n❌ Error: Puerto ${PORT} ya está en uso`);
    console.error(`💡 Soluciones:`);
    console.error(`   1. Cierra el proceso que está usando el puerto ${PORT}`);
    console.error(`   2. O cambia el puerto en backend/.env (PORT=3001)`);
    console.error(`\n🔍 Para encontrar el proceso:`);
    console.error(`   Windows: netstat -ano | findstr :${PORT}`);
    console.error(`   PowerShell: Get-NetTCPConnection -LocalPort ${PORT}\n`);
    process.exit(1);
  } else {
    console.error(`❌ Error al iniciar servidor:`, err);
    process.exit(1);
  }
});

// Handle uncaught errors
process.on('uncaughtException', (err) => {
  console.error('❌ Uncaught Exception:', err);
  console.error('Stack:', err.stack);
});

process.on('unhandledRejection', (reason, promise) => {
  console.error('❌ Unhandled Rejection at:', promise);
  console.error('Reason:', reason);
});

// Graceful shutdown
process.on('SIGTERM', () => {
  console.log('SIGTERM signal received: closing HTTP server');
  server.close(() => {
    console.log('HTTP server closed');
    process.exit(0);
  });
});

