"""
Script simple para verificar si un usuario se registró en PostgreSQL
Útil para verificar después de crear una cuenta en la página
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
from datetime import datetime

def verificar_usuario(email=None, username=None):
    """Verificar si un usuario específico está registrado"""
    print()
    print("=" * 70)
    print("🔍 Verificación de Usuario Registrado")
    print("=" * 70)
    print()
    
    db = DatabaseManager()
    
    # Verificar conexión
    conn_test = db.test_connection()
    if not conn_test['success']:
        print(f"❌ Error de conexión: {conn_test.get('error')}")
        return
    
    print(f"✅ Conexión exitosa a PostgreSQL {conn_test['version_str']}")
    print()
    
    # Buscar usuario
    if email:
        print(f"🔍 Buscando usuario con email: {email}")
        result = db.execute_query(
            """SELECT 
                id, username, email, role, full_name, 
                is_active, created_at, updated_at
            FROM users 
            WHERE email = %s""",
            (email,)
        )
    elif username:
        print(f"🔍 Buscando usuario con username: {username}")
        result = db.execute_query(
            """SELECT 
                id, username, email, role, full_name, 
                is_active, created_at, updated_at
            FROM users 
            WHERE username = %s""",
            (username,)
        )
    else:
        print("❌ Debes proporcionar email o username")
        return
    
    if result['success'] and len(result['data']) > 0:
        user = result['data'][0]
        print()
        print("✅ Usuario encontrado!")
        print()
        print("📋 Datos del usuario:")
        print(f"   ID: {user['id']}")
        print(f"   Username: {user['username']}")
        print(f"   Email: {user['email']}")
        print(f"   Role: {user['role']}")
        print(f"   Full Name: {user['full_name'] or 'N/A'}")
        print(f"   Status: {'✅ Activo' if user['is_active'] else '❌ Inactivo'}")
        print(f"   Creado: {user['created_at']}")
        print(f"   Actualizado: {user['updated_at']}")
        print()
        return True
    else:
        print()
        print("❌ Usuario no encontrado")
        print()
        print("💡 Posibles razones:")
        print("   1. El usuario aún no se ha registrado")
        print("   2. El email/username es incorrecto")
        print("   3. Hubo un error en el registro")
        print()
        return False

def listar_todos_usuarios():
    """Listar todos los usuarios registrados"""
    print()
    print("=" * 70)
    print("📋 Lista de Todos los Usuarios Registrados")
    print("=" * 70)
    print()
    
    db = DatabaseManager()
    
    # Verificar conexión
    conn_test = db.test_connection()
    if not conn_test['success']:
        print(f"❌ Error de conexión: {conn_test.get('error')}")
        return
    
    # Obtener todos los usuarios
    result = db.execute_query(
        """SELECT 
            id, username, email, role, full_name, 
            is_active, created_at
        FROM users 
        ORDER BY created_at DESC"""
    )
    
    if result['success']:
        users = result['data']
        print(f"📊 Total de usuarios: {len(users)}")
        print()
        
        if len(users) == 0:
            print("   ℹ️  No hay usuarios registrados aún")
        else:
            for i, user in enumerate(users, 1):
                status = "✅" if user['is_active'] else "❌"
                role_icon = "👑" if user['role'] == 'admin' else "👤" if user['role'] == 'moderator' else "👥"
                
                print(f"{role_icon} Usuario #{i}")
                print(f"   ID: {user['id']}")
                print(f"   Username: {user['username']}")
                print(f"   Email: {user['email']}")
                print(f"   Role: {user['role']}")
                print(f"   Full Name: {user['full_name'] or 'N/A'}")
                print(f"   Status: {status} {'Activo' if user['is_active'] else 'Inactivo'}")
                print(f"   Registrado: {user['created_at']}")
                print("-" * 70)
                print()
    else:
        print(f"❌ Error: {result.get('error')}")

def main():
    """Función principal"""
    import sys
    
    print()
    print("=" * 70)
    print("🚀 Battle.net - Verificación de Registro")
    print("=" * 70)
    print()
    print_config()
    print()
    
    if len(sys.argv) > 1:
        # Modo con argumentos
        arg = sys.argv[1]
        
        if arg == '--all' or arg == '-a':
            listar_todos_usuarios()
        elif '@' in arg:
            # Es un email
            verificar_usuario(email=arg)
        else:
            # Es un username
            verificar_usuario(username=arg)
    else:
        # Modo interactivo
        print("📋 Opciones:")
        print("   1. Verificar usuario por email")
        print("   2. Verificar usuario por username")
        print("   3. Listar todos los usuarios")
        print()
        
        try:
            choice = input("Selecciona una opción (1-3): ").strip()
            
            if choice == '1':
                email = input("Email: ").strip()
                verificar_usuario(email=email)
            elif choice == '2':
                username = input("Username: ").strip()
                verificar_usuario(username=username)
            elif choice == '3':
                listar_todos_usuarios()
            else:
                print("❌ Opción inválida")
        except KeyboardInterrupt:
            print("\n👋 ¡Hasta luego!")
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"❌ Error fatal: {e}")
        import traceback
        traceback.print_exc()

