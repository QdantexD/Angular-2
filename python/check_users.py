"""
Script para verificar usuarios en PostgreSQL
Útil para verificar que el registro y login funcionen correctamente
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
from datetime import datetime

def format_date(date_str):
    """Formatear fecha para mostrar"""
    if date_str:
        try:
            dt = datetime.fromisoformat(str(date_str).replace('Z', '+00:00'))
            return dt.strftime('%Y-%m-%d %H:%M:%S')
        except:
            return str(date_str)
    return 'N/A'

def show_all_users():
    """Mostrar todos los usuarios"""
    print("=" * 80)
    print("👥 USUARIOS EN LA BASE DE DATOS")
    print("=" * 80)
    print()
    
    db = DatabaseManager()
    
    result = db.execute_query("""
        SELECT 
            id,
            username,
            email,
            role,
            full_name,
            is_active,
            created_at,
            updated_at
        FROM users
        ORDER BY created_at DESC
    """)
    
    if not result['success']:
        print(f"❌ Error: {result.get('error')}")
        return
    
    users = result['data']
    
    if len(users) == 0:
        print("⚠️  No hay usuarios en la base de datos")
        print()
        print("💡 Para crear un usuario:")
        print("   1. Ve a http://localhost:4200/register")
        print("   2. Completa el formulario de registro")
        print("   3. Ejecuta este script nuevamente para verificar")
        return
    
    print(f"📊 Total de usuarios: {len(users)}")
    print()
    
    for i, user in enumerate(users, 1):
        print(f"┌─ Usuario #{i} ──────────────────────────────────────────────────────")
        print(f"│  ID:           {user['id']}")
        print(f"│  Username:     {user['username']}")
        print(f"│  Email:        {user['email']}")
        print(f"│  Role:         {user['role']}")
        print(f"│  Nombre:       {user['full_name'] or 'N/A'}")
        print(f"│  Activo:       {'✅ Sí' if user['is_active'] else '❌ No'}")
        print(f"│  Creado:       {format_date(user['created_at'])}")
        print(f"│  Actualizado:  {format_date(user['updated_at'])}")
        print("└─────────────────────────────────────────────────────────────────────")
        print()
    
    # Estadísticas
    print("📈 Estadísticas:")
    print()
    
    # Por rol
    result = db.execute_query("""
        SELECT role, COUNT(*) as count
        FROM users
        GROUP BY role
        ORDER BY count DESC
    """)
    
    if result['success']:
        print("   Por rol:")
        for row in result['data']:
            print(f"      {row['role']}: {row['count']} usuario(s)")
    
    print()
    
    # Activos vs Inactivos
    result = db.execute_query("""
        SELECT 
            COUNT(*) FILTER (WHERE is_active = true) as active,
            COUNT(*) FILTER (WHERE is_active = false) as inactive
        FROM users
    """)
    
    if result['success']:
        stats = result['data'][0]
        print(f"   Activos: {stats['active']}")
        print(f"   Inactivos: {stats['inactive']}")
    
    print()

def show_user_details(username_or_email):
    """Mostrar detalles de un usuario específico"""
    print(f"🔍 Buscando usuario: {username_or_email}")
    print()
    
    db = DatabaseManager()
    
    result = db.execute_query("""
        SELECT 
            id,
            username,
            email,
            role,
            full_name,
            avatar_url,
            is_active,
            created_at,
            updated_at
        FROM users
        WHERE username = %s OR email = %s
    """, (username_or_email, username_or_email))
    
    if not result['success']:
        print(f"❌ Error: {result.get('error')}")
        return
    
    if len(result['data']) == 0:
        print(f"⚠️  Usuario '{username_or_email}' no encontrado")
        return
    
    user = result['data'][0]
    
    print("=" * 80)
    print("👤 DETALLES DEL USUARIO")
    print("=" * 80)
    print()
    print(f"ID:           {user['id']}")
    print(f"Username:     {user['username']}")
    print(f"Email:        {user['email']}")
    print(f"Role:         {user['role']}")
    print(f"Nombre:       {user['full_name'] or 'N/A'}")
    print(f"Avatar:       {user['avatar_url'] or 'N/A'}")
    print(f"Activo:       {'✅ Sí' if user['is_active'] else '❌ No'}")
    print(f"Creado:       {format_date(user['created_at'])}")
    print(f"Actualizado:  {format_date(user['updated_at'])}")
    print()
    
    # Actividades recientes
    activities_result = db.execute_query("""
        SELECT 
            activity_type,
            activity_data,
            created_at
        FROM user_activities
        WHERE user_id = %s
        ORDER BY created_at DESC
        LIMIT 5
    """, (user['id'],))
    
    if activities_result['success'] and len(activities_result['data']) > 0:
        print("📋 Actividades recientes:")
        for activity in activities_result['data']:
            print(f"   - {activity['activity_type']} ({format_date(activity['created_at'])})")
    print()

def show_recent_registrations(limit=5):
    """Mostrar registros recientes"""
    print(f"🆕 ÚLTIMOS {limit} REGISTROS")
    print()
    
    db = DatabaseManager()
    
    result = db.execute_query("""
        SELECT 
            id,
            username,
            email,
            role,
            created_at
        FROM users
        ORDER BY created_at DESC
        LIMIT %s
    """, (limit,))
    
    if not result['success']:
        print(f"❌ Error: {result.get('error')}")
        return
    
    users = result['data']
    
    if len(users) == 0:
        print("⚠️  No hay usuarios registrados")
        return
    
    for user in users:
        print(f"   • {user['username']} ({user['email']}) - {format_date(user['created_at'])}")
    print()

def main():
    """Función principal"""
    import sys
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == 'all':
            show_all_users()
        elif command == 'search' and len(sys.argv) > 2:
            show_user_details(sys.argv[2])
        elif command == 'recent':
            limit = int(sys.argv[2]) if len(sys.argv) > 2 else 5
            show_recent_registrations(limit)
        else:
            print("Uso:")
            print("  python check_users.py all              - Mostrar todos los usuarios")
            print("  python check_users.py search <user>     - Buscar usuario específico")
            print("  python check_users.py recent [limit]   - Mostrar registros recientes")
    else:
        # Por defecto, mostrar todos
        show_all_users()
        print()
        print("💡 Comandos adicionales:")
        print("   python check_users.py search <username_or_email>")
        print("   python check_users.py recent [limit]")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n⚠️  Cancelado por el usuario")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()

