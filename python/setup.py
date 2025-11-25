"""
Script principal de setup - Versión mejorada y modular
Útil para uso básico y avanzado
"""
import sys
import os

# Fix encoding
if sys.platform == 'win32':
    try:
        import codecs
        if hasattr(sys.stdout, 'buffer'):
            sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
        if hasattr(sys.stderr, 'buffer'):
            sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')
    except:
        pass

from config import DB_CONFIG, DB_NAME, print_config, ENV_FILE
from db_manager import DatabaseManager
import bcrypt

def main():
    """Función principal de setup"""
    print()
    print("=" * 70)
    print("🚀 Battle.net - Configuración de Base de Datos")
    print("=" * 70)
    print()
    
    if not ENV_FILE:
        print("⚠️  No se encontró archivo .env")
        print("   Crea backend/.env con tus credenciales de PostgreSQL")
        print()
    
    print_config()
    print()
    
    db = DatabaseManager()
    
    # Paso 1: Probar conexión
    print("🔌 Paso 1: Probando conexión a PostgreSQL...")
    conn_test = db.test_connection()
    
    if not conn_test['success']:
        print(f"   ❌ Error: {conn_test.get('error', 'Unknown error')}")
        print()
        print("💡 Soluciones:")
        print("   1. Verifica que PostgreSQL esté corriendo")
        print("   2. Actualiza DB_PASSWORD en backend/.env")
        print("   3. Tu contraseña configurada es: 123456")
        sys.exit(1)
    
    print(f"   ✅ Conexión exitosa! (PostgreSQL {conn_test['version_str']})")
    
    # Paso 2: Crear base de datos
    print()
    print(f"📦 Paso 2: Creando base de datos '{DB_NAME}'...")
    db_result = db.create_database(DB_NAME)
    
    if not db_result['success']:
        print(f"   ❌ Error: {db_result.get('error', 'Unknown error')}")
        sys.exit(1)
    
    if db_result.get('exists'):
        print(f"   ℹ️  La base de datos '{DB_NAME}' ya existe")
    else:
        print(f"   ✅ Base de datos '{DB_NAME}' creada")
    
    # Paso 3: Crear tablas (usar el script mejorado)
    print()
    print("📊 Paso 3: Creando tablas...")
    print("   (Ejecutando db_setup_improved.py para crear tablas)")
    
    # Importar funciones del script mejorado
    try:
        from db_setup_improved import create_tables, create_admin_user, verify_setup
        
        if not create_tables():
            print("   ❌ Error creando tablas")
            sys.exit(1)
        
        # Paso 4: Crear admin
        print()
        if not create_admin_user():
            print("   ⚠️  Advertencia: No se pudo crear usuario admin")
        
        # Paso 5: Verificar
        print()
        if not verify_setup():
            print("   ⚠️  Advertencia: Verificación encontró problemas")
        
    except ImportError:
        print("   ⚠️  No se pudo importar funciones avanzadas")
        print("   Ejecuta: python db_setup_improved.py directamente")
    
    # Éxito
    print()
    print("=" * 70)
    print("✅ ¡Configuración completada exitosamente!")
    print("=" * 70)
    print()
    print("🔐 Credenciales de acceso:")
    print("   Email: admin@battlenet.com")
    print("   Password: admin123")
    print()
    print("🚀 Próximos pasos:")
    print("   1. Backend: cd backend && npm run dev")
    print("   2. Frontend: npm start")
    print("   3. Python Service: python app.py")
    print()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n⚠️  Setup cancelado")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error fatal: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

