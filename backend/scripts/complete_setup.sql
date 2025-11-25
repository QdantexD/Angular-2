-- ============================================
-- Battle.net Platform - Complete Database Setup
-- Ejecuta este script completo en pgAdmin
-- ============================================
-- Conectarse a la base de datos battlenet_db antes de ejecutar el resto

-- ============================================
-- TABLAS
-- ============================================

-- Users table
CREATE TABLE IF NOT EXISTS users (
  id SERIAL PRIMARY KEY,
  username VARCHAR(50) UNIQUE NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  password VARCHAR(255) NOT NULL,
  role VARCHAR(20) DEFAULT 'user' CHECK (role IN ('admin', 'moderator', 'user')),
  full_name VARCHAR(100),
  avatar_url VARCHAR(255),
  is_active BOOLEAN DEFAULT true,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Games table
CREATE TABLE IF NOT EXISTS games (
  id SERIAL PRIMARY KEY,
  title VARCHAR(200) NOT NULL,
  subtitle VARCHAR(200),
  description TEXT,
  image_url VARCHAR(500),
  category VARCHAR(100),
  color VARCHAR(20),
  price DECIMAL(10, 2),
  original_price DECIMAL(10, 2),
  discount INTEGER,
  badge VARCHAR(20),
  logo VARCHAR(10),
  is_free BOOLEAN DEFAULT false,
  rating DECIMAL(3, 2) DEFAULT 0,
  downloads INTEGER DEFAULT 0,
  created_by INTEGER REFERENCES users(id),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- User activities table
CREATE TABLE IF NOT EXISTS user_activities (
  id SERIAL PRIMARY KEY,
  user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
  activity_type VARCHAR(50) NOT NULL,
  activity_data JSONB,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Analytics table
CREATE TABLE IF NOT EXISTS analytics (
  id SERIAL PRIMARY KEY,
  metric_name VARCHAR(100) NOT NULL,
  metric_value DECIMAL(10, 2),
  metric_data JSONB,
  date_recorded DATE DEFAULT CURRENT_DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ============================================
-- ÍNDICES
-- ============================================

CREATE INDEX IF NOT EXISTS idx_users_email ON users(email);
CREATE INDEX IF NOT EXISTS idx_users_role ON users(role);
CREATE INDEX IF NOT EXISTS idx_games_category ON games(category);
CREATE INDEX IF NOT EXISTS idx_games_created_at ON games(created_at);
CREATE INDEX IF NOT EXISTS idx_activities_user_id ON user_activities(user_id);
CREATE INDEX IF NOT EXISTS idx_activities_created_at ON user_activities(created_at);
CREATE INDEX IF NOT EXISTS idx_analytics_date ON analytics(date_recorded);

-- ============================================
-- USUARIO ADMIN POR DEFECTO
-- ============================================
-- Email: admin@battlenet.com
-- Password: admin123

INSERT INTO users (username, email, password, role, full_name) 
VALUES (
  'admin', 
  'admin@battlenet.com', 
  '$2a$10$MZnjGKBatKam6qVF1e3OwuL980xWh9uh7QFYxICaMp.VmSd.y8vjC', 
  'admin', 
  'Administrator'
)
ON CONFLICT (username) DO NOTHING;

-- ============================================
-- VERIFICACIÓN
-- ============================================

-- Verificar que las tablas se crearon
SELECT 
  table_name,
  (SELECT COUNT(*) FROM information_schema.columns WHERE table_name = t.table_name) as column_count
FROM information_schema.tables t
WHERE table_schema = 'public' 
  AND table_type = 'BASE TABLE'
ORDER BY table_name;

-- Verificar usuario admin
SELECT id, username, email, role, created_at 
FROM users 
WHERE username = 'admin';

-- ============================================
-- FIN DEL SCRIPT
-- ============================================
-- Si ves las 4 tablas y el usuario admin, ¡todo está listo!
-- ============================================

