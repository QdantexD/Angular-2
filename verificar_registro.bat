@echo off
REM Script para verificar registro usando el Python correcto
echo.
echo ============================================================
echo 🔍 Battle.net - Verificación de Registro en PostgreSQL
echo ============================================================
echo.

REM Usar el Python correcto con las dependencias instaladas
"C:\Program Files\Python310\python.exe" python\verificar_registro.py %*

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ❌ Error al ejecutar el script
    echo.
    echo 💡 Verifica que:
    echo    1. Python 3.10 esté instalado en: C:\Program Files\Python310\
    echo    2. Las dependencias estén instaladas: psycopg2-binary, python-dotenv, bcrypt
    echo.
    echo 📝 Para instalar dependencias ejecuta:
    echo    "C:\Program Files\Python310\python.exe" -m pip install psycopg2-binary python-dotenv bcrypt
    echo.
    pause
)

