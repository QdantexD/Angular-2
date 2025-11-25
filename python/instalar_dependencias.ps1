# Script para instalar dependencias de Python
# Detecta automáticamente qué Python usar

Write-Host "`n🔍 Detectando Python instalado...`n" -ForegroundColor Cyan

$pythonPaths = @(
    "C:\Program Files\Python310\python.exe",
    "C:\msys64\ucrt64\bin\python.exe",
    "python",
    "py"
)

$pythonExe = $null

foreach ($path in $pythonPaths) {
    if (Test-Path $path) {
        try {
            $version = & $path --version 2>&1
            Write-Host "✅ Encontrado: $path" -ForegroundColor Green
            Write-Host "   Versión: $version" -ForegroundColor Cyan
            $pythonExe = $path
            break
        } catch {
            continue
        }
    }
}

if (-not $pythonExe) {
    Write-Host "`n❌ No se encontró Python instalado" -ForegroundColor Red
    Write-Host "💡 Instala Python desde: https://www.python.org/downloads/" -ForegroundColor Yellow
    exit 1
}

Write-Host "`n📦 Instalando dependencias en: $pythonExe`n" -ForegroundColor Yellow

# Cambiar al directorio python
$pythonDir = Join-Path (Get-Location) "python"
if (-not (Test-Path $pythonDir)) {
    Write-Host "❌ No se encuentra el directorio python" -ForegroundColor Red
    exit 1
}

Set-Location $pythonDir

# Instalar dependencias
Write-Host "Instalando psycopg2-binary..." -ForegroundColor Cyan
& $pythonExe -m pip install psycopg2-binary

Write-Host "`nInstalando python-dotenv..." -ForegroundColor Cyan
& $pythonExe -m pip install python-dotenv

Write-Host "`nInstalando bcrypt..." -ForegroundColor Cyan
& $pythonExe -m pip install bcrypt

Write-Host "`n✅ Dependencias instaladas!`n" -ForegroundColor Green
Write-Host "💡 Ahora puedes ejecutar:" -ForegroundColor Yellow
Write-Host "   & `"$pythonExe`" python\verificar_registro.py" -ForegroundColor Cyan
Write-Host ""

Set-Location ..

