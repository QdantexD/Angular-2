"""
Script rápido para verificar usuarios en PostgreSQL
Útil para comprobar que los datos se guarden correctamente
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

from db_manager import DatabaseManager
from config import print_config

def main():
    """Verificar usuarios registrados"""
    print()
    print("=" * 70)
    print("🔍 Verificación de Usuarios en PostgreSQL")
    print("=" * 70)
    print()
    print_config()
    print()
    
    db = DatabaseManager()
    
    # Verificar conexión
    conn_test = db.test_connection()
    if not conn_test['success']:
        print(f"❌ Error de conexión: {conn_test.get('error')}")
        return
    
    print(f"✅ Conexión exitosa a PostgreSQL {conn_test['version_str']}")
    print()
    
    # Obtener todos los usuarios
    result = db.execute_query(
        """SELECT 
            id, 
            username, 
            email, 
            role, 
            full_name, 
            is_active, 
            created_at,
            updated_at
        FROM users 
        ORDER BY created_at DESC"""
    )
    
    if result['success']:
        users = result['data']
        print(f"📊 Total de usuarios registrados: {len(users)}")
        print()
        
        if len(users) == 0:
            print("   ℹ️  No hay usuarios registrados aún")
            print()
            print("💡 Para registrar un usuario:")
            print("   1. Abre la aplicación en http://localhost:4200")
            print("   2. Ve a /register")
            print("   3. Completa el formulario")
        else:
            print("=" * 70)
            for i, user in enumerate(users, 1):
                status = "✅ Activo" if user['is_active'] else "❌ Inactivo"
                role_icon = "👑" if user['role'] == 'admin' else "👤" if user['role'] == 'moderator' else "👥"
                
                print(f"\n{role_icon} Usuario #{user['id']}")
                print(f"   Username: {user['username']}")
                print(f"   Email: {user['email']}")
                print(f"   Role: {user['role']}")
                print(f"   Full Name: {user['full_name'] or 'N/A'}")
                print(f"   Status: {status}")
                print(f"   Creado: {user['created_at']}")
                print(f"   Actualizado: {user['updated_at']}")
                print("-" * 70)
    else:
        print(f"❌ Error: {result.get('error')}")
    
    print()

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

