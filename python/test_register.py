"""
Script para probar y verificar el registro de usuarios en PostgreSQL
Útil para verificar que los datos se guarden correctamente
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
from config import DB_NAME, print_config
from datetime import datetime

def test_register_user(username, email, password, full_name=None):
    """Probar registro de usuario (simula el proceso del backend)"""
    print()
    print("=" * 70)
    print("🧪 Test de Registro de Usuario")
    print("=" * 70)
    print()
    
    db = DatabaseManager()
    
    # 1. Verificar que el usuario no existe
    print("1️⃣ Verificando si el usuario ya existe...")
    result = db.execute_query(
        "SELECT id, username, email FROM users WHERE username = %s OR email = %s",
        (username, email)
    )
    
    if result['success'] and len(result['data']) > 0:
        existing = result['data'][0]
        print(f"   ⚠️  Usuario ya existe:")
        print(f"      ID: {existing['id']}")
        print(f"      Username: {existing['username']}")
        print(f"      Email: {existing['email']}")
        return False
    
    print("   ✅ Usuario no existe, puede registrarse")
    
    # 2. Simular hash de contraseña (bcrypt)
    print()
    print("2️⃣ Generando hash de contraseña...")
    try:
        import bcrypt
        password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        print("   ✅ Hash generado correctamente")
    except ImportError:
        print("   ⚠️  bcrypt no disponible, usando hash simple (solo para test)")
        password_hash = f"hashed_{password}"  # No usar en producción
    
    # 3. Insertar usuario
    print()
    print("3️⃣ Insertando usuario en la base de datos...")
    result = db.execute_query(
        """INSERT INTO users (username, email, password, full_name, role) 
           VALUES (%s, %s, %s, %s, 'user') 
           RETURNING id, username, email, role, full_name, created_at""",
        (username, email, password_hash, full_name or None),
        fetch=True
    )
    
    if result['success'] and len(result['data']) > 0:
        user = result['data'][0]
        print("   ✅ Usuario registrado exitosamente!")
        print()
        print("   📝 Datos del usuario:")
        print(f"      ID: {user['id']}")
        print(f"      Username: {user['username']}")
        print(f"      Email: {user['email']}")
        print(f"      Role: {user['role']}")
        print(f"      Full Name: {user['full_name'] or 'N/A'}")
        print(f"      Created At: {user['created_at']}")
        return True
    else:
        print(f"   ❌ Error al registrar: {result.get('error', 'Unknown error')}")
        return False

def list_all_users():
    """Listar todos los usuarios"""
    print()
    print("=" * 70)
    print("📋 Lista de Usuarios Registrados")
    print("=" * 70)
    print()
    
    db = DatabaseManager()
    result = db.execute_query(
        "SELECT id, username, email, role, full_name, is_active, created_at FROM users ORDER BY created_at DESC"
    )
    
    if result['success']:
        users = result['data']
        if len(users) == 0:
            print("   ℹ️  No hay usuarios registrados")
        else:
            print(f"   Total usuarios: {len(users)}")
            print()
            for user in users:
                status = "✅ Activo" if user['is_active'] else "❌ Inactivo"
                print(f"   [{user['id']}] {user['username']} ({user['email']})")
                print(f"       Role: {user['role']} | {status}")
                print(f"       Creado: {user['created_at']}")
                print()
    else:
        print(f"   ❌ Error: {result.get('error')}")

def verify_user(email, password):
    """Verificar credenciales de usuario (simula login)"""
    print()
    print("=" * 70)
    print("🔐 Verificación de Credenciales (Login)")
    print("=" * 70)
    print()
    
    db = DatabaseManager()
    
    # Buscar usuario
    result = db.execute_query(
        "SELECT id, username, email, password, role, full_name, is_active FROM users WHERE email = %s",
        (email,)
    )
    
    if not result['success'] or len(result['data']) == 0:
        print(f"   ❌ Usuario con email '{email}' no encontrado")
        return False
    
    user = result['data'][0]
    
    if not user['is_active']:
        print("   ❌ Cuenta inactiva")
        return False
    
    # Verificar contraseña
    print("   Verificando contraseña...")
    try:
        import bcrypt
        password_valid = bcrypt.checkpw(
            password.encode('utf-8'),
            user['password'].encode('utf-8')
        )
        
        if password_valid:
            print("   ✅ Contraseña correcta!")
            print()
            print("   📝 Datos del usuario:")
            print(f"      ID: {user['id']}")
            print(f"      Username: {user['username']}")
            print(f"      Email: {user['email']}")
            print(f"      Role: {user['role']}")
            print(f"      Full Name: {user['full_name'] or 'N/A'}")
            return True
        else:
            print("   ❌ Contraseña incorrecta")
            return False
    except ImportError:
        print("   ⚠️  bcrypt no disponible, no se puede verificar contraseña")
        return False
    except Exception as e:
        print(f"   ❌ Error verificando contraseña: {e}")
        return False

def main():
    """Función principal"""
    print()
    print("=" * 70)
    print("🚀 Battle.net - Test de Registro y Login")
    print("=" * 70)
    print()
    print_config()
    print()
    
    # Verificar conexión
    db = DatabaseManager()
    conn_test = db.test_connection()
    
    if not conn_test['success']:
        print(f"❌ Error de conexión: {conn_test.get('error')}")
        return
    
    print(f"✅ Conexión exitosa a PostgreSQL {conn_test['version_str']}")
    print()
    
    # Menú interactivo
    while True:
        print("=" * 70)
        print("📋 Menú de Opciones:")
        print("=" * 70)
        print()
        print("1. Registrar nuevo usuario")
        print("2. Listar todos los usuarios")
        print("3. Verificar login (credenciales)")
        print("4. Salir")
        print()
        
        try:
            choice = input("Selecciona una opción (1-4): ").strip()
            
            if choice == '1':
                print()
                username = input("Username (mínimo 3 caracteres): ").strip()
                email = input("Email: ").strip()
                password = input("Password (mínimo 6 caracteres): ").strip()
                full_name = input("Full Name (opcional): ").strip() or None
                
                if len(username) < 3:
                    print("❌ Username debe tener al menos 3 caracteres")
                    continue
                
                if len(password) < 6:
                    print("❌ Password debe tener al menos 6 caracteres")
                    continue
                
                if '@' not in email:
                    print("❌ Email inválido")
                    continue
                
                test_register_user(username, email, password, full_name)
                
            elif choice == '2':
                list_all_users()
                
            elif choice == '3':
                print()
                email = input("Email: ").strip()
                password = input("Password: ").strip()
                verify_user(email, password)
                
            elif choice == '4':
                print()
                print("👋 ¡Hasta luego!")
                break
            else:
                print("❌ Opción inválida")
                
        except KeyboardInterrupt:
            print()
            print("👋 ¡Hasta luego!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"❌ Error fatal: {e}")
        import traceback
        traceback.print_exc()

