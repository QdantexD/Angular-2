# Script para crear archivo .env en Windows PowerShell

$envContent = @"
PORT=3000
NODE_ENV=development

DB_HOST=localhost
DB_PORT=5432
DB_NAME=battlenet_db
DB_USER=postgres
DB_PASSWORD=postgres

JWT_SECRET=battlenet-super-secret-jwt-key-change-in-production-2024
JWT_EXPIRE=7d

PYTHON_SERVICE_URL=http://localhost:5000
"@

$envPath = Join-Path $PSScriptRoot ".env"

if (Test-Path $envPath) {
    Write-Host "El archivo .env ya existe. ¿Deseas sobrescribirlo? (S/N)" -ForegroundColor Yellow
    $response = Read-Host
    if ($response -ne "S" -and $response -ne "s") {
        Write-Host "Operación cancelada." -ForegroundColor Red
        exit
    }
}

$envContent | Out-File -FilePath $envPath -Encoding UTF8
Write-Host "✅ Archivo .env creado exitosamente en: $envPath" -ForegroundColor Green
Write-Host ""
Write-Host "⚠️  IMPORTANTE: Edita el archivo .env y cambia:" -ForegroundColor Yellow
Write-Host "   - DB_PASSWORD con tu contraseña real de PostgreSQL" -ForegroundColor Yellow
Write-Host ""

