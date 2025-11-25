"""
Gestor de Base de Datos - Funciones reutilizables
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

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from psycopg2 import sql
from psycopg2.extras import RealDictCursor
from config import DB_CONFIG, get_db_connection

class DatabaseManager:
    """Clase para gestionar operaciones de base de datos"""
    
    def __init__(self):
        self.config = DB_CONFIG.copy()
    
    def test_connection(self, database=None):
        """Probar conexión a PostgreSQL"""
        try:
            if database is None:
                # Para probar conexión sin database específica
                conn = get_db_connection(False)
            else:
                conn = get_db_connection(database)
            version = conn.server_version
            conn.close()
            return {
                'success': True,
                'version': version,
                'version_str': f"{version // 10000}.{(version % 10000) // 100}"
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e) if str(e) else repr(e),
                'error_type': type(e).__name__
            }
    
    def create_database(self, db_name):
        """Crear base de datos"""
        try:
            conn = get_db_connection()  # Sin database específica
            conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            cursor = conn.cursor()
            
            # Verificar si existe
            cursor.execute(
                "SELECT 1 FROM pg_catalog.pg_database WHERE datname = %s",
                (db_name,)
            )
            exists = cursor.fetchone()
            
            if exists:
                cursor.close()
                conn.close()
                return {'success': True, 'exists': True, 'message': f'Database {db_name} already exists'}
            
            # Crear base de datos
            cursor.execute(
                sql.SQL("CREATE DATABASE {}").format(sql.Identifier(db_name))
            )
            cursor.close()
            conn.close()
            return {'success': True, 'exists': False, 'message': f'Database {db_name} created'}
            
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'error_type': type(e).__name__
            }
    
    def execute_query(self, query, params=None, fetch=True, use_db=True):
        """Ejecutar query y retornar resultados"""
        try:
            if use_db:
                conn = get_db_connection()  # Con database
            else:
                conn = get_db_connection(False)  # Sin database (para crear BD)
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            
            cursor.execute(query, params)
            
            if fetch:
                if cursor.description:
                    results = cursor.fetchall()
                    return {'success': True, 'data': results, 'count': len(results)}
                else:
                    conn.commit()
                    return {'success': True, 'affected': cursor.rowcount}
            else:
                conn.commit()
                return {'success': True, 'affected': cursor.rowcount}
            
        except Exception as e:
            if 'conn' in locals():
                conn.rollback()
            return {
                'success': False,
                'error': str(e),
                'error_type': type(e).__name__
            }
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'conn' in locals():
                conn.close()
    
    def get_table_info(self, table_name):
        """Obtener información de una tabla"""
        query = """
            SELECT 
                column_name,
                data_type,
                is_nullable,
                column_default
            FROM information_schema.columns
            WHERE table_schema = 'public' 
            AND table_name = %s
            ORDER BY ordinal_position
        """
        return self.execute_query(query, (table_name,))
    
    def get_stats(self):
        """Obtener estadísticas de la base de datos"""
        stats = {}
        
        # Contar tablas
        result = self.execute_query("""
            SELECT COUNT(*) as count 
            FROM information_schema.tables 
            WHERE table_schema = 'public' 
            AND table_type = 'BASE TABLE'
        """)
        stats['tables'] = result['data'][0]['count'] if result['success'] else 0
        
        # Contar usuarios
        result = self.execute_query("SELECT COUNT(*) as count FROM users")
        stats['users'] = result['data'][0]['count'] if result['success'] else 0
        
        # Contar juegos
        result = self.execute_query("SELECT COUNT(*) as count FROM games")
        stats['games'] = result['data'][0]['count'] if result['success'] else 0
        
        return stats

