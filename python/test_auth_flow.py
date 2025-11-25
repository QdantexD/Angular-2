"""
Script para probar el flujo completo de autenticación
Simula registro y verifica en PostgreSQL
"""
import sys
import os
import requests
import json

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
from datetime import datetime

def test_register():
    """Probar registro de usuario"""
    print("=" * 80)
    print("🧪 PRUEBA DE REGISTRO Y LOGIN")
    print("=" * 80)
    print()
    
    # Datos de prueba
    test_user = {
        'username': f'test_user_{datetime.now().strftime("%Y%m%d%H%M%S")}',
        'email': f'test_{datetime.now().strftime("%Y%m%d%H%M%S")}@test.com',
        'password': 'test123456',
        'full_name': 'Usuario de Prueba'
    }
    
    print("📝 Datos de prueba:")
    print(f"   Username: {test_user['username']}")
    print(f"   Email: {test_user['email']}")
    print(f"   Password: {test_user['password']}")
    print()
    
    # Verificar que el backend esté corriendo
    print("🔌 Verificando backend...")
    try:
        response = requests.get('http://localhost:3000/api/auth/me', timeout=2)
        backend_running = True
    except:
        backend_running = False
    
    if not backend_running:
        print("⚠️  Backend no está corriendo en http://localhost:3000")
        print()
        print("💡 Para iniciar el backend:")
        print("   cd backend")
        print("   npm run dev")
        print()
        print("📊 Verificando directamente en PostgreSQL...")
        return test_direct_db(test_user)
    
    print("✅ Backend está corriendo")
    print()
    
    # Probar registro
    print("📤 Intentando registrar usuario...")
    try:
        response = requests.post(
            'http://localhost:3000/api/auth/register',
            json=test_user,
            headers={'Content-Type': 'application/json'},
            timeout=5
        )
        
        if response.status_code == 201:
            data = response.json()
            print("✅ Registro exitoso!")
            print(f"   Token recibido: {data.get('token', 'N/A')[:50]}...")
            print(f"   Usuario ID: {data.get('user', {}).get('id')}")
            print()
            
            # Verificar en PostgreSQL
            print("🔍 Verificando en PostgreSQL...")
            verify_in_db(test_user['email'])
            
            # Probar login
            print()
            print("🔐 Probando login...")
            login_response = requests.post(
                'http://localhost:3000/api/auth/login',
                json={
                    'email': test_user['email'],
                    'password': test_user['password']
                },
                headers={'Content-Type': 'application/json'},
                timeout=5
            )
            
            if login_response.status_code == 200:
                login_data = login_response.json()
                print("✅ Login exitoso!")
                print(f"   Token recibido: {login_data.get('token', 'N/A')[:50]}...")
            else:
                print(f"❌ Login falló: {login_response.status_code}")
                print(f"   {login_response.text}")
            
        elif response.status_code == 400:
            error_data = response.json()
            if 'error' in error_data and 'already exists' in error_data['error']:
                print("ℹ️  Usuario ya existe (esto es normal si ya se probó antes)")
                print()
                print("🔍 Verificando en PostgreSQL...")
                verify_in_db(test_user['email'])
            else:
                print(f"❌ Error de validación: {error_data}")
        else:
            print(f"❌ Error: {response.status_code}")
            print(f"   {response.text}")
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Error de conexión: {e}")
        print()
        print("📊 Verificando directamente en PostgreSQL...")
        return test_direct_db(test_user)
    
    print()
    print("=" * 80)

def test_direct_db(test_user):
    """Probar directamente en la base de datos"""
    print("=" * 80)
    print("📊 PRUEBA DIRECTA EN POSTGRESQL")
    print("=" * 80)
    print()
    
    db = DatabaseManager()
    
    # Verificar conexión
    conn_test = db.test_connection()
    if not conn_test['success']:
        print(f"❌ No se puede conectar a PostgreSQL: {conn_test.get('error')}")
        return
    
    print("✅ Conexión a PostgreSQL exitosa")
    print()
    
    # Mostrar usuarios existentes
    print("👥 Usuarios actuales en la base de datos:")
    result = db.execute_query("""
        SELECT id, username, email, role, created_at
        FROM users
        ORDER BY created_at DESC
        LIMIT 10
    """)
    
    if result['success']:
        users = result['data']
        if len(users) > 0:
            for user in users:
                print(f"   • {user['username']} ({user['email']}) - {user['role']}")
        else:
            print("   ⚠️  No hay usuarios")
    print()
    
    print("💡 Para probar el registro:")
    print("   1. Inicia el backend: cd backend && npm run dev")
    print("   2. Inicia el frontend: npm start")
    print("   3. Ve a http://localhost:4200/register")
    print("   4. Completa el formulario")
    print("   5. Ejecuta: python check_users.py all")

def verify_in_db(email):
    """Verificar usuario en la base de datos"""
    db = DatabaseManager()
    
    result = db.execute_query("""
        SELECT id, username, email, role, full_name, created_at
        FROM users
        WHERE email = %s
    """, (email,))
    
    if result['success'] and len(result['data']) > 0:
        user = result['data'][0]
        print("✅ Usuario encontrado en PostgreSQL:")
        print(f"   ID: {user['id']}")
        print(f"   Username: {user['username']}")
        print(f"   Email: {user['email']}")
        print(f"   Role: {user['role']}")
        print(f"   Nombre: {user['full_name'] or 'N/A'}")
        print(f"   Creado: {user['created_at']}")
    else:
        print("❌ Usuario NO encontrado en PostgreSQL")
        if not result['success']:
            print(f"   Error: {result.get('error')}")

if __name__ == '__main__':
    try:
        test_register()
    except KeyboardInterrupt:
        print("\n⚠️  Prueba cancelada")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()

