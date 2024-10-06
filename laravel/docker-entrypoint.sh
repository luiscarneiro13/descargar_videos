#!/bin/bash

# Si la carpeta vendor no existe, ejecuta composer install
if [ ! -d "vendor" ]; then
    composer install
fi

# Si la carpeta node_modules no existe, ejecuta npm install
if [ ! -d "node_modules" ]; then
    npm install
fi

# Crear el directorio de descargas y hacer el enlace simbólico
if [ ! -d "storage/app/public/downloads" ]; then
    mkdir -p storage/app/public/downloads
    php artisan storage:link
fi

cd /var/www
php artisan optimize:clear 

# Ejecutar el comando predeterminado
exec "$@"
