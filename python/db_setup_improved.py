"""
Script mejorado de Python para configurar la base de datos PostgreSQL
Versión robusta con mejor manejo de errores y configuración automática
"""
import sys
import os

# Fix encoding for Windows
if sys.platform == 'win32':
    try:
        import codecs
        if hasattr(sys.stdout, 'buffer'):
            sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
        if hasattr(sys.stderr, 'buffer'):
            sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')
    except:
        pass  # Si falla, continuar sin cambiar encoding

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from psycopg2 import sql
from dotenv import load_dotenv
import bcrypt

# ============================================
# CONFIGURACIÓN
# ============================================

# Buscar archivo .env en múltiples ubicaciones
env_paths = [
    os.path.join(os.path.dirname(__file__), '.env'),
    os.path.join(os.path.dirname(__file__), '..', 'backend', '.env'),
    os.path.join(os.path.dirname(__file__), '..', '.env')
]

env_file = None
for env_path in env_paths:
    if os.path.exists(env_path):
        load_dotenv(env_path)
        env_file = env_path
        print(f"📝 Archivo .env cargado desde: {env_path}")
        break

if not env_file:
    print("⚠️  No se encontró archivo .env. Usando valores por defecto.")
    print("   Crea backend/.env con tus credenciales de PostgreSQL")

# Configuración de base de datos
DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': int(os.getenv('DB_PORT', '5432')),
    'user': os.getenv('DB_USER', 'postgres'),
    'password': os.getenv('DB_PASSWORD', '123456'),  # Tu contraseña por defecto
    'connect_timeout': 5
}

DB_NAME = os.getenv('DB_NAME', 'battlenet_db')

# Mostrar configuración (ocultar contraseña)
print()
print("=" * 70)
print("🚀 Battle.net - Configuración de Base de Datos")
print("=" * 70)
print()
print("📋 Configuración:")
print(f"   Host: {DB_CONFIG['host']}")
print(f"   Port: {DB_CONFIG['port']}")
print(f"   User: {DB_CONFIG['user']}")
print(f"   Database: {DB_NAME}")
print(f"   Password: {'*' * len(DB_CONFIG['password']) if DB_CONFIG['password'] else 'NO CONFIGURADA'}")
print()

# ============================================
# FUNCIONES
# ============================================

def test_connection():
    """Probar conexión a PostgreSQL"""
    print("🔌 Paso 1: Probando conexión a PostgreSQL...")
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        version = conn.server_version
        conn.close()
        print(f"   ✅ Conexión exitosa! (PostgreSQL {version // 10000}.{(version % 10000) // 100})")
        return True
    except psycopg2.OperationalError as e:
        error_msg = str(e) if str(e) else repr(e)
        print(f"   ❌ Error de conexión: {error_msg}")
        
        if "password authentication failed" in error_msg.lower() or "authentication failed" in error_msg.lower():
            print()
            print("   💡 La contraseña es incorrecta")
            print("   Soluciones:")
            print("   1. Verifica DB_PASSWORD en backend/.env")
            print("   2. Tu contraseña actual parece ser: 123456")
            print("   3. Si es diferente, actualiza backend/.env")
        elif "could not connect" in error_msg.lower() or "connection refused" in error_msg.lower():
            print()
            print("   💡 PostgreSQL no está corriendo o no es accesible")
            print("   Soluciones:")
            print("   1. Inicia el servicio PostgreSQL")
            print("   2. Verifica que esté escuchando en el puerto", DB_CONFIG['port'])
        else:
            print()
            print("   💡 Error desconocido. Verifica:")
            print("   1. PostgreSQL está instalado y corriendo")
            print("   2. Las credenciales en backend/.env son correctas")
            print("   3. El puerto", DB_CONFIG['port'], "está disponible")
        
        return False
    except Exception as e:
        print(f"   ❌ Error inesperado: {type(e).__name__}: {e}")
        return False

def create_database():
    """Crear base de datos si no existe"""
    print()
    print(f"📦 Paso 2: Creando base de datos '{DB_NAME}'...")
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = conn.cursor()
        
        # Verificar si existe
        cursor.execute(
            "SELECT 1 FROM pg_catalog.pg_database WHERE datname = %s",
            (DB_NAME,)
        )
        exists = cursor.fetchone()
        
        if exists:
            print(f"   ℹ️  La base de datos '{DB_NAME}' ya existe")
        else:
            # Crear base de datos de forma segura
            cursor.execute(
                sql.SQL("CREATE DATABASE {}").format(
                    sql.Identifier(DB_NAME)
                )
            )
            print(f"   ✅ Base de datos '{DB_NAME}' creada exitosamente")
        
        cursor.close()
        conn.close()
        return True
        
    except psycopg2.errors.DuplicateDatabase:
        print(f"   ℹ️  La base de datos '{DB_NAME}' ya existe")
        return True
    except psycopg2.errors.InsufficientPrivilege as e:
        print(f"   ❌ Permisos insuficientes: {e}")
        print("   💡 El usuario necesita privilegios CREATE DATABASE")
        return False
    except Exception as e:
        print(f"   ❌ Error: {type(e).__name__}: {e}")
        return False

def create_tables():
    """Crear todas las tablas necesarias"""
    print()
    print("📊 Paso 3: Creando tablas e índices...")
    try:
        # Conectar a la base de datos específica
        config = DB_CONFIG.copy()
        config['database'] = DB_NAME
        conn = psycopg2.connect(**config)
        cursor = conn.cursor()
        
        tables_created = 0
        
        # Tabla: users
        cursor.execute("""
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
            )
        """)
        tables_created += 1
        print("   ✅ Tabla 'users' creada")
        
        # Tabla: games
        cursor.execute("""
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
            )
        """)
        tables_created += 1
        print("   ✅ Tabla 'games' creada")
        
        # Tabla: user_activities
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_activities (
                id SERIAL PRIMARY KEY,
                user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
                activity_type VARCHAR(50) NOT NULL,
                activity_data JSONB,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        tables_created += 1
        print("   ✅ Tabla 'user_activities' creada")
        
        # Tabla: analytics
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS analytics (
                id SERIAL PRIMARY KEY,
                metric_name VARCHAR(100) NOT NULL,
                metric_value DECIMAL(10, 2),
                metric_data JSONB,
                date_recorded DATE DEFAULT CURRENT_DATE,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        tables_created += 1
        print("   ✅ Tabla 'analytics' creada")
        
        # Crear índices
        print()
        print("   📑 Creando índices...")
        indexes = [
            ("idx_users_email", "CREATE INDEX IF NOT EXISTS idx_users_email ON users(email)"),
            ("idx_users_role", "CREATE INDEX IF NOT EXISTS idx_users_role ON users(role)"),
            ("idx_games_category", "CREATE INDEX IF NOT EXISTS idx_games_category ON games(category)"),
            ("idx_games_created_at", "CREATE INDEX IF NOT EXISTS idx_games_created_at ON games(created_at)"),
            ("idx_activities_user_id", "CREATE INDEX IF NOT EXISTS idx_activities_user_id ON user_activities(user_id)"),
            ("idx_activities_created_at", "CREATE INDEX IF NOT EXISTS idx_activities_created_at ON user_activities(created_at)"),
            ("idx_analytics_date", "CREATE INDEX IF NOT EXISTS idx_analytics_date ON analytics(date_recorded)")
        ]
        
        for idx_name, idx_sql in indexes:
            cursor.execute(idx_sql)
            print(f"      ✅ Índice '{idx_name}' creado")
        
        conn.commit()
        print()
        print(f"   ✅ {tables_created} tablas y {len(indexes)} índices creados exitosamente")
        
        cursor.close()
        conn.close()
        return True
        
    except Exception as e:
        print(f"   ❌ Error creando tablas: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()
        return False

def create_admin_user():
    """Crear usuario administrador por defecto"""
    print()
    print("👤 Paso 4: Creando usuario administrador...")
    try:
        config = DB_CONFIG.copy()
        config['database'] = DB_NAME
        conn = psycopg2.connect(**config)
        cursor = conn.cursor()
        
        # Verificar si admin existe
        cursor.execute("SELECT id, email, role FROM users WHERE username = 'admin'")
        admin = cursor.fetchone()
        
        if admin:
            print(f"   ℹ️  Usuario admin ya existe (ID: {admin[0]})")
            print(f"      Email: {admin[1]}")
            print(f"      Role: {admin[2]}")
        else:
            # Generar hash de contraseña
            password = 'admin123'
            password_hash = bcrypt.hashpw(
                password.encode('utf-8'),
                bcrypt.gensalt()
            ).decode('utf-8')
            
            # Insertar admin
            cursor.execute("""
                INSERT INTO users (username, email, password, role, full_name)
                VALUES (%s, %s, %s, %s, %s)
            """, ('admin', 'admin@battlenet.com', password_hash, 'admin', 'Administrator'))
            
            conn.commit()
            print("   ✅ Usuario administrador creado exitosamente")
            print()
            print("   📝 Credenciales de acceso:")
            print("      Email: admin@battlenet.com")
            print("      Password: admin123")
        
        cursor.close()
        conn.close()
        return True
        
    except Exception as e:
        print(f"   ❌ Error creando usuario admin: {type(e).__name__}: {e}")
        return False

def verify_setup():
    """Verificar que todo esté configurado correctamente"""
    print()
    print("🔍 Paso 5: Verificando configuración...")
    try:
        config = DB_CONFIG.copy()
        config['database'] = DB_NAME
        conn = psycopg2.connect(**config)
        cursor = conn.cursor()
        
        # Contar tablas
        cursor.execute("""
            SELECT COUNT(*) 
            FROM information_schema.tables 
            WHERE table_schema = 'public' 
            AND table_type = 'BASE TABLE'
        """)
        table_count = cursor.fetchone()[0]
        
        # Contar usuarios
        cursor.execute("SELECT COUNT(*) FROM users")
        user_count = cursor.fetchone()[0]
        
        # Verificar admin
        cursor.execute("SELECT username, email, role FROM users WHERE username = 'admin'")
        admin = cursor.fetchone()
        
        print(f"   ✅ Tablas creadas: {table_count}/4")
        print(f"   ✅ Usuarios en sistema: {user_count}")
        
        if admin:
            print(f"   ✅ Usuario admin: {admin[1]} ({admin[2]})")
        else:
            print("   ⚠️  Usuario admin no encontrado")
        
        cursor.close()
        conn.close()
        
        if table_count >= 4 and admin:
            return True
        else:
            return False
            
    except Exception as e:
        print(f"   ❌ Error en verificación: {e}")
        return False

# ============================================
# FUNCIÓN PRINCIPAL
# ============================================

def main():
    """Función principal"""
    success = True
    
    # Paso 1: Probar conexión
    if not test_connection():
        print()
        print("=" * 70)
        print("❌ Setup fallido: No se pudo conectar a PostgreSQL")
        print("=" * 70)
        print()
        print("💡 Soluciones:")
        print("   1. Verifica que PostgreSQL esté corriendo")
        print("   2. Actualiza DB_PASSWORD en backend/.env con tu contraseña real")
        print("   3. Tu contraseña actual configurada es: 123456")
        print("   4. Si es diferente, edita backend/.env y cambia DB_PASSWORD")
        sys.exit(1)
    
    # Paso 2: Crear base de datos
    if not create_database():
        print()
        print("=" * 70)
        print("❌ Setup fallido: No se pudo crear la base de datos")
        print("=" * 70)
        sys.exit(1)
    
    # Paso 3: Crear tablas
    if not create_tables():
        print()
        print("=" * 70)
        print("❌ Setup fallido: No se pudieron crear las tablas")
        print("=" * 70)
        sys.exit(1)
    
    # Paso 4: Crear usuario admin
    if not create_admin_user():
        print()
        print("⚠️  Advertencia: No se pudo crear usuario admin")
        print("   Puedes crearlo manualmente después")
    
    # Paso 5: Verificar
    if not verify_setup():
        print()
        print("⚠️  Advertencia: La verificación encontró algunos problemas")
    
    # Éxito
    print()
    print("=" * 70)
    print("✅ ¡Configuración completada exitosamente!")
    print("=" * 70)
    print()
    print("📝 Resumen:")
    print(f"   Base de datos: {DB_NAME}")
    print(f"   Host: {DB_CONFIG['host']}:{DB_CONFIG['port']}")
    print(f"   Usuario: {DB_CONFIG['user']}")
    print()
    print("🔐 Credenciales de acceso:")
    print("   Email: admin@battlenet.com")
    print("   Password: admin123")
    print()
    print("🚀 Próximos pasos:")
    print("   1. Inicia el backend: cd backend && npm run dev")
    print("   2. Inicia el frontend: npm start")
    print("   3. Accede a: http://localhost:4200")
    print()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print("\n⚠️  Setup cancelado por el usuario")
        sys.exit(1)
    except Exception as e:
        print()
        print(f"❌ Error fatal: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

