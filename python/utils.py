"""
Utilidades y funciones helper
Útiles para uso básico y avanzado
"""
import sys
import os
from datetime import datetime, timedelta

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
from config import DB_NAME

def seed_sample_data():
    """Poblar base de datos con datos de ejemplo"""
    print("🌱 Poblando base de datos con datos de ejemplo...")
    
    db = DatabaseManager()
    
    # Verificar que exista admin
    result = db.execute_query("SELECT id FROM users WHERE role = 'admin' LIMIT 1")
    if not result['success'] or len(result['data']) == 0:
        print("   ❌ No se encontró usuario admin. Ejecuta setup primero.")
        return False
    
    admin_id = result['data'][0]['id']
    
    # Juegos de ejemplo
    games = [
        {
            'title': 'World of Warcraft: Midnight',
            'subtitle': 'World of Warcraft®: Midnight',
            'description': 'Previsto para 2026: ¡Precompra hoy mismo!',
            'image_url': 'https://images.unsplash.com/photo-1511512578047-dfb367046420?w=800',
            'category': 'Rol multijugador masivo',
            'color': '#f39c12',
            'price': 179.00,
            'badge': 'PREORDER',
            'logo': 'W',
            'is_free': False,
            'rating': 4.8,
            'downloads': 1500000
        },
        {
            'title': 'Diablo IV',
            'subtitle': 'Lote de expansión de Diablo® IV',
            'description': 'Experimenta la oscuridad definitiva.',
            'image_url': 'https://images.unsplash.com/photo-1542751371-adc38448a05e?w=800',
            'category': 'RPG de acción',
            'color': '#c0392b',
            'price': 211.60,
            'original_price': 529.00,
            'discount': 60,
            'badge': 'SALE',
            'logo': 'D',
            'is_free': False,
            'rating': 4.6,
            'downloads': 2500000
        },
        {
            'title': 'Overwatch 2',
            'subtitle': 'Overwatch® 2',
            'description': 'Únete a la batalla épica.',
            'image_url': 'https://images.unsplash.com/photo-1552519507-da3b142c6e3d?w=800',
            'category': 'Acción por equipos',
            'color': '#e74c3c',
            'is_free': True,
            'badge': 'FREE',
            'logo': 'OW',
            'rating': 4.5,
            'downloads': 5000000
        }
    ]
    
    inserted = 0
    for game in games:
        result = db.execute_query("""
            INSERT INTO games (
                title, subtitle, description, image_url, category, color,
                price, original_price, discount, badge, logo, is_free,
                rating, downloads, created_by
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT DO NOTHING
        """, (
            game['title'],
            game.get('subtitle'),
            game['description'],
            game.get('image_url'),
            game['category'],
            game.get('color'),
            game.get('price'),
            game.get('original_price'),
            game.get('discount'),
            game.get('badge'),
            game.get('logo'),
            game.get('is_free', False),
            game.get('rating', 0),
            game.get('downloads', 0),
            admin_id
        ), fetch=False)
        
        if result['success'] and result.get('affected', 0) > 0:
            inserted += 1
    
    print(f"   ✅ {inserted} juegos insertados")
    return True

def check_database():
    """Verificar estado de la base de datos"""
    print("🔍 Verificando base de datos...")
    print()
    
    db = DatabaseManager()
    
    # Test conexión
    conn_test = db.test_connection()
    if conn_test['success']:
        print(f"✅ Conexión: OK (PostgreSQL {conn_test['version_str']})")
    else:
        print(f"❌ Conexión: FALLO - {conn_test.get('error')}")
        return
    
    # Stats
    stats = db.get_stats()
    print(f"✅ Tablas: {stats['tables']}")
    print(f"✅ Usuarios: {stats['users']}")
    print(f"✅ Juegos: {stats['games']}")
    
    # Verificar admin
    result = db.execute_query("SELECT username, email, role FROM users WHERE username = 'admin'")
    if result['success'] and len(result['data']) > 0:
        admin = result['data'][0]
        print(f"✅ Admin: {admin['email']} ({admin['role']})")
    else:
        print("⚠️  Admin: No encontrado")

def generate_password_hash(password):
    """Generar hash de contraseña"""
    import bcrypt
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == 'seed':
            seed_sample_data()
        elif command == 'check':
            check_database()
        elif command == 'hash':
            if len(sys.argv) > 2:
                password = sys.argv[2]
                print(f"Hash para '{password}':")
                print(generate_password_hash(password))
            else:
                print("Uso: python utils.py hash <password>")
        else:
            print("Comandos disponibles:")
            print("  python utils.py seed  - Poblar con datos de ejemplo")
            print("  python utils.py check - Verificar estado de BD")
            print("  python utils.py hash <password> - Generar hash de contraseña")
    else:
        print("Utilidades de Battle.net Platform")
        print()
        print("Comandos:")
        print("  python utils.py seed  - Poblar con datos de ejemplo")
        print("  python utils.py check - Verificar estado de BD")
        print("  python utils.py hash <password> - Generar hash")

