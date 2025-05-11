#!/bin/bash

limpiar_pantalla() {
  case "$OSTYPE" in
    msys*|cygwin*|win32)
      cmd.exe /c cls
      ;;
    *)
      clear
      ;;
  esac
}

imprimir_con_retraso_centrado() {
  while IFS= read -r linea; do
    centrar_texto "$linea"
    sleep 0.03
  done <<< "$1"
}

centrar_texto() {
  local texto="$1"
  local cols=$(tput cols)
  local longitud=${#texto}
  local espacio=$(( (cols - longitud) / 2 ))
  printf "%*s%s\n" "$espacio" "" "$texto"
}

menu_opciones=(
  "============= OSINT FRAMEWORK ============="
  "1) theHarvester"
  "2) Osintgram"
  "3) Blackbird"
  "4) Toutatis"
  "5) Dorks"
  "0) Salir"
  "==========================================="
)

while true; do
  limpiar_pantalla
  imprimir_con_retraso_centrado "$titulo"
  echo ""
  imprimir_con_retraso_centrado "$ascii_art"
  echo ""

  for linea in "${menu_opciones[@]}"; do
    centrar_texto "$linea"
  done

  echo ""
  read -p "Selecciona una opción: " opcion

  case $opcion in
    1)
      limpiar_pantalla
      echo "=== theHarvester ==="
      read -p "Dominio: " dominio
      docker-compose run theharvester -d "$dominio" -b all
      read -p "Presiona Enter"
      ;;
    2)
      limpiar_pantalla
      echo "=== Osintgram ==="
      read -p "Nombre de usuario: " username
      docker-compose run osintgram "$username"
      read -p "Presiona Enter"
      ;;
    3)
      limpiar_pantalla
      echo "=== Blackbird ==="
      read -p "Nombre de usuario: " username
      if [ -z "$username" ]; then
        echo "No se proporcionó usuario. Mostrando ayuda:"
        docker-compose run blackbird -h
      else
        docker-compose run blackbird -u "$username"
      fi
      read -p "Presiona Enter"
      ;;
    4)
      limpiar_pantalla
      echo "=== Toutatis ==="
      echo "Ejemplo de uso:"
      echo "  -s tu_session_id -u usuario"
      echo "  -s tu_session_id -i ID"
      echo ""
      read -p "Escribe los argumentos que deseas pasar a Toutatis: " args
      if [ -z "$args" ]; then
        echo "No se ingresaron argumentos. Cancelando..."
      else
        docker-compose run toutatis $args
      fi
      read -p "Presiona Enter"
      ;;
    5)
      limpiar_pantalla
      echo "=== Dorks ==="
      docker-compose run dorks
      read -p "Presiona Enter"
      ;;
    0)
      limpiar_pantalla
      echo "Exit"
      break
      ;;
    *)
      echo "Opción inválida."
      sleep 2
      ;;
  esac
done
