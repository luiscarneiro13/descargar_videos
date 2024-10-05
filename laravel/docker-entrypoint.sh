#!/bin/bash

# Si la carpeta vendor no existe, ejecuta composer install
if [ ! -d "vendor" ]; then
    composer install
fi

# Si la carpeta node_modules no existe, ejecuta npm install
if [ ! -d "node_modules" ]; then
    npm install
fi

# Ejecutar el comando predeterminado
exec "$@"
