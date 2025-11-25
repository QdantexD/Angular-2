"""
Configuración centralizada para todos los scripts de Python
Útil para uso básico y avanzado
"""
import os
import sys
from dotenv import load_dotenv

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

# Buscar archivo .env
def load_config():
    """Cargar configuración desde .env"""
    env_paths = [
        os.path.join(os.path.dirname(__file__), '.env'),
        os.path.join(os.path.dirname(__file__), '..', 'backend', '.env'),
        os.path.join(os.path.dirname(__file__), '..', '.env')
    ]
    
    for env_path in env_paths:
        if os.path.exists(env_path):
            load_dotenv(env_path)
            return env_path
    
    return None

# Cargar configuración
ENV_FILE = load_config()

# Database Configuration
DB_NAME = os.getenv('DB_NAME', 'battlenet_db')

DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': int(os.getenv('DB_PORT', '5432')),
    'user': os.getenv('DB_USER', 'postgres'),
    'password': os.getenv('DB_PASSWORD', '123456'),
    'connect_timeout': 5
}

# Server Configuration
SERVER_CONFIG = {
    'host': os.getenv('PYTHON_SERVICE_HOST', '0.0.0.0'),
    'port': int(os.getenv('PYTHON_SERVICE_PORT', '5000')),
    'debug': os.getenv('NODE_ENV', 'development') == 'development'
}

# API Configuration
API_CONFIG = {
    'node_backend_url': os.getenv('NODE_BACKEND_URL', 'http://localhost:3000'),
    'cors_origins': os.getenv('CORS_ORIGINS', 'http://localhost:4200').split(',')
}

def get_db_connection(database=None):
    """Obtener conexión a la base de datos"""
    import psycopg2
    config = DB_CONFIG.copy()
    if database:
        config['database'] = database
    elif database is False:
        # Para crear base de datos, no especificar database
        pass
    else:
        # Usar DB_NAME por defecto
        config['database'] = DB_NAME
    return psycopg2.connect(**config)

def print_config():
    """Imprimir configuración actual (ocultar contraseña)"""
    print("📋 Configuración:")
    print(f"   Host: {DB_CONFIG['host']}")
    print(f"   Port: {DB_CONFIG['port']}")
    print(f"   User: {DB_CONFIG['user']}")
    print(f"   Database: {DB_CONFIG.get('database', 'N/A')}")
    print(f"   Password: {'*' * len(DB_CONFIG['password']) if DB_CONFIG['password'] else 'NO CONFIGURADA'}")
    if ENV_FILE:
        print(f"   .env file: {ENV_FILE}")

