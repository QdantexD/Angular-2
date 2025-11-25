# Script PowerShell para verificar registro
# Usa automáticamente el Python correcto: C:\Program Files\Python310\python.exe

param(
    [string]$Email = "",
    [string]$Username = "",
    [switch]$All
)

$pythonExe = "C:\Program Files\Python310\python.exe"
$scriptPath = Join-Path (Get-Location) "python\verificar_registro.py"

Write-Host ""
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "🔍 Battle.net - Verificación de Registro en PostgreSQL" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""

if (-not (Test-Path $pythonExe)) {
    Write-Host "❌ Python no encontrado en: $pythonExe" -ForegroundColor Red
    Write-Host ""
    Write-Host "💡 Soluciones:" -ForegroundColor Yellow
    Write-Host "   1. Instala Python 3.10 desde: https://www.python.org/downloads/" -ForegroundColor Yellow
    Write-Host "   2. O actualiza la ruta en este script si Python está en otra ubicación" -ForegroundColor Yellow
    Write-Host ""
    exit 1
}

Write-Host "✅ Usando Python: $pythonExe" -ForegroundColor Green
Write-Host ""

if ($All) {
    & $pythonExe $scriptPath --all
} elseif ($Email) {
    & $pythonExe $scriptPath $Email
} elseif ($Username) {
    & $pythonExe $scriptPath $Username
} else {
    & $pythonExe $scriptPath
}

if ($LASTEXITCODE -ne 0) {
    Write-Host ""
    Write-Host "❌ Error al ejecutar el script" -ForegroundColor Red
    Write-Host ""
    Write-Host "💡 Verifica que las dependencias estén instaladas:" -ForegroundColor Yellow
    Write-Host "   & `"$pythonExe`" -m pip install psycopg2-binary python-dotenv bcrypt" -ForegroundColor Cyan
    Write-Host ""
}

