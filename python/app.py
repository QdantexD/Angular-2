"""
Battle.net Platform - Python Analytics Service
Servicio Flask para analytics avanzados y procesamiento de datos
Útil para uso básico y avanzado
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
        pass

from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime, timedelta
from config import SERVER_CONFIG, API_CONFIG, get_db_connection, print_config
from db_manager import DatabaseManager

app = Flask(__name__)
CORS(app, origins=API_CONFIG['cors_origins'])

db_manager = DatabaseManager()

# ============================================
# ENDPOINTS BÁSICOS
# ============================================

@app.route('/health', methods=['GET'])
def health():
    """Health check - Verificar que el servicio funciona"""
    return jsonify({
        'status': 'OK',
        'service': 'Python Analytics Service',
        'timestamp': datetime.now().isoformat(),
        'version': '1.0.0'
    })

@app.route('/api/db/status', methods=['GET'])
def db_status():
    """Verificar estado de la base de datos"""
    result = db_manager.test_connection()
    return jsonify(result)

# ============================================
# ENDPOINTS DE ANALYTICS (BÁSICO)
# ============================================

@app.route('/api/analytics/basic', methods=['GET'])
def basic_analytics():
    """Analytics básicos - Sin dependencias externas"""
    try:
        stats = db_manager.get_stats()
        
        # Obtener juegos por categoría
        result = db_manager.execute_query("""
            SELECT category, COUNT(*) as count 
            FROM games 
            GROUP BY category 
            ORDER BY count DESC
        """)
        categories = result['data'] if result['success'] else []
        
        # Obtener usuarios por rol
        result = db_manager.execute_query("""
            SELECT role, COUNT(*) as count 
            FROM users 
            GROUP BY role 
            ORDER BY count DESC
        """)
        roles = result['data'] if result['success'] else []
        
        return jsonify({
            'success': True,
            'stats': stats,
            'categories': categories,
            'roles': roles,
            'timestamp': datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

# ============================================
# ENDPOINTS DE ANALYTICS (AVANZADO)
# ============================================

@app.route('/api/analytics/advanced', methods=['GET'])
def advanced_analytics():
    """Analytics avanzados con pandas (requiere pandas instalado)"""
    try:
        # Intentar importar pandas
        try:
            import pandas as pd
        except ImportError:
            return jsonify({
                'success': False,
                'error': 'pandas no está instalado. Ejecuta: pip install pandas',
                'fallback': 'Usa /api/analytics/basic para analytics sin pandas'
            }), 503
        
        # Conectar y obtener datos
        conn = get_db_connection()
        
        # Games data
        games_df = pd.read_sql_query("""
            SELECT category, price, is_free, rating, downloads, created_at
            FROM games
        """, conn)
        
        # Users data
        users_df = pd.read_sql_query("""
            SELECT role, created_at, is_active
            FROM users
        """, conn)
        
        conn.close()
        
        # Calcular estadísticas avanzadas
        stats = {
            'games': {
                'total': len(games_df),
                'by_category': games_df['category'].value_counts().to_dict() if len(games_df) > 0 else {},
                'avg_price': float(games_df[games_df['is_free'] == False]['price'].mean()) if len(games_df[games_df['is_free'] == False]) > 0 else 0,
                'avg_rating': float(games_df['rating'].mean()) if len(games_df) > 0 else 0,
                'total_downloads': int(games_df['downloads'].sum()) if len(games_df) > 0 else 0,
                'free_games': int((games_df['is_free'] == True).sum()) if len(games_df) > 0 else 0,
                'paid_games': int((games_df['is_free'] == False).sum()) if len(games_df) > 0 else 0
            },
            'users': {
                'total': len(users_df),
                'by_role': users_df['role'].value_counts().to_dict() if len(users_df) > 0 else {},
                'active_users': int(users_df[users_df['is_active'] == True].shape[0]) if len(users_df) > 0 else 0
            }
        }
        
        return jsonify({
            'success': True,
            'stats': stats,
            'timestamp': datetime.now().isoformat()
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/analytics/trends', methods=['GET'])
def trends():
    """Tendencias temporales"""
    try:
        period = request.args.get('period', '7d')
        
        if period == '7d':
            days = 7
        elif period == '30d':
            days = 30
        elif period == '1y':
            days = 365
        else:
            days = 7
        
        date_from = datetime.now() - timedelta(days=days)
        
        # Games trends
        result = db_manager.execute_query("""
            SELECT DATE(created_at) as date, COUNT(*) as count
            FROM games
            WHERE created_at >= %s
            GROUP BY DATE(created_at)
            ORDER BY date
        """, (date_from,))
        games_trends = result['data'] if result['success'] else []
        
        # Users trends
        result = db_manager.execute_query("""
            SELECT DATE(created_at) as date, COUNT(*) as count
            FROM users
            WHERE created_at >= %s
            GROUP BY DATE(created_at)
            ORDER BY date
        """, (date_from,))
        users_trends = result['data'] if result['success'] else []
        
        return jsonify({
            'success': True,
            'games': games_trends,
            'users': users_trends,
            'period': period,
            'days': days
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/analytics/predictions', methods=['GET'])
def predictions():
    """Predicciones simples basadas en tendencias"""
    try:
        # Intentar usar pandas si está disponible
        try:
            import pandas as pd
            use_pandas = True
        except ImportError:
            use_pandas = False
        
        date_from = datetime.now() - timedelta(days=30)
        
        if use_pandas:
            conn = get_db_connection()
            df = pd.read_sql_query("""
                SELECT DATE(created_at) as date, COUNT(*) as count
                FROM games
                WHERE created_at >= %s
                GROUP BY DATE(created_at)
                ORDER BY date
            """, conn, params=(date_from,))
            conn.close()
            
            if len(df) > 0:
                avg_daily = df['count'].mean()
                predicted_7d = avg_daily * 7
                predicted_30d = avg_daily * 30
            else:
                predicted_7d = 0
                predicted_30d = 0
        else:
            # Sin pandas - cálculo básico
            result = db_manager.execute_query("""
                SELECT COUNT(*) as total
                FROM games
                WHERE created_at >= %s
            """, (date_from,))
            total = result['data'][0]['total'] if result['success'] else 0
            avg_daily = total / 30 if total > 0 else 0
            predicted_7d = avg_daily * 7
            predicted_30d = avg_daily * 30
        
        return jsonify({
            'success': True,
            'predictions': {
                'next_7_days': round(predicted_7d, 2),
                'next_30_days': round(predicted_30d, 2),
                'based_on_days': 30,
                'method': 'pandas' if use_pandas else 'basic'
            }
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

# ============================================
# INICIO DEL SERVIDOR
# ============================================

if __name__ == '__main__':
    print("=" * 70)
    print("🚀 Battle.net - Python Analytics Service")
    print("=" * 70)
    print()
    print_config()
    print()
    print(f"🌐 Servidor iniciando en: http://{SERVER_CONFIG['host']}:{SERVER_CONFIG['port']}")
    print()
    print("📡 Endpoints disponibles:")
    print("   GET  /health                    - Health check")
    print("   GET  /api/db/status             - Estado de BD")
    print("   GET  /api/analytics/basic       - Analytics básicos")
    print("   GET  /api/analytics/advanced    - Analytics avanzados (pandas)")
    print("   GET  /api/analytics/trends      - Tendencias temporales")
    print("   GET  /api/analytics/predictions - Predicciones")
    print()
    print("=" * 70)
    print()
    
    app.run(
        host=SERVER_CONFIG['host'],
        port=SERVER_CONFIG['port'],
        debug=SERVER_CONFIG['debug']
    )

