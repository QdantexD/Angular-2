"""
Script de inicio rápido - Detecta y ejecuta el servicio apropiado
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

def check_dependencies():
    """Verificar dependencias instaladas"""
    missing = []
    
    try:
        import psycopg2
    except ImportError:
        missing.append('psycopg2-binary')
    
    try:
        import flask
    except ImportError:
        missing.append('flask flask-cors')
    
    try:
        import pandas
        pandas_available = True
    except ImportError:
        pandas_available = False
    
    return missing, pandas_available

def main():
    """Función principal"""
    print("=" * 70)
    print("🚀 Battle.net - Python Services Launcher")
    print("=" * 70)
    print()
    
    # Verificar dependencias
    missing, pandas_available = check_dependencies()
    
    if missing:
        print("⚠️  Dependencias faltantes:")
        for dep in missing:
            print(f"   - {dep}")
        print()
        print("💡 Instala con: pip install -r requirements.txt")
        print()
        return
    
    print("✅ Todas las dependencias están instaladas")
    if pandas_available:
        print("✅ Pandas disponible - Modo avanzado activado")
    else:
        print("ℹ️  Pandas no disponible - Usando modo básico")
    print()
    
    # Verificar base de datos
    print("🔍 Verificando base de datos...")
    try:
        from db_manager import DatabaseManager
        db = DatabaseManager()
        result = db.test_connection()
        
        if result['success']:
            print(f"✅ Base de datos: Conectada (PostgreSQL {result['version_str']})")
        else:
            print(f"❌ Base de datos: {result.get('error')}")
            print()
            print("💡 Ejecuta primero: python setup.py")
            return
    except Exception as e:
        print(f"❌ Error: {e}")
        return
    
    print()
    print("=" * 70)
    print("🌐 Iniciando servicio Flask...")
    print("=" * 70)
    print()
    
    # Iniciar servicio Flask
    try:
        from app import app, SERVER_CONFIG
        print(f"📍 Servicio disponible en: http://localhost:{SERVER_CONFIG['port']}")
        print()
        print("📡 Endpoints:")
        print("   GET /health")
        print("   GET /api/analytics/basic")
        if pandas_available:
            print("   GET /api/analytics/advanced")
        print("   GET /api/analytics/trends")
        print()
        print("Presiona Ctrl+C para detener")
        print()
        print("=" * 70)
        print()
        
        app.run(
            host=SERVER_CONFIG['host'],
            port=SERVER_CONFIG['port'],
            debug=SERVER_CONFIG['debug']
        )
    except KeyboardInterrupt:
        print("\n⚠️  Servicio detenido")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    main()

