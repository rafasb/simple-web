#!/bin/bash

# carga variables de entorno
export $(grep -v '^#' .env | xargs -d '\n')

# Copia el fichero por defecto de la configuración
FILE=./httpd.conf
echo TAG $TAG

IMAGE=httpd:$TAG

echo IMAGEN $IMAGE

if test -f $FILE; then
  echo "$FILE YA EXISTE."
else
  docker run --rm ${IMAGE} cat /usr/local/apache2/conf/httpd.conf > httpd.conf 
fi

echo PARAMETRIZA EL FICHERO $FILE
