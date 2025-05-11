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
while true; do
  limpiar_pantalla

  cat << "EOF"

=**#+++*+==+=-=====-+##%#%%%#=============
*+*+**+=+========##%%%%%%%%%%%%%#+*=======
****+==========+##%%%%%%%%%%%%%%#*%#*+====
++++**========*###@%%%%%%%%%%%%##%##=*-===
============##%##%%%%%#%%%%##%#####+#=-===
=============+###@%%%@%%@%%####+#####%%===
*========*==##%#@%%%%%%%##%#*++###***%*===
=----====*==##%%@%%%%%%%##*++=++***=+=%%+=
+-=-----+=+*=#%%%%@*=*#%%@@@@+=*++=++=%%+=
**+===-=-#==%%%@@@+++=%#%+**+=++==*@*@%%==
*======+==#%@%%%@@@@+=*##+++======+=@%#%==
+++++#%%#+%%%%%@@@@@@+*#*+==========%##%==
+==*%===*#%%%%%%@@@%@+++*++========%#**#++
=%+====+#%%%%%@@@@@@@@%@%#@======%+%*==#=+
*+=====#%%%%@@@@@@@+*#+++%@%@@#%#=**==#===
=====##@@%%%%%%@%@++=#@=%@@@#+#=**#*=+====
=++*#%%#%%%%##%@%++@@%@%@%##**+**##=*=====
**%%%#%%%%%==%%%+@@@@@@@@%%#####@#========
*#%%#%%%#===%%@@@@@@@@@@@%%%%###%%=+---===
%*%#%%%===+#%@@@@@@@@@@@@%%%%%%%%%@=---===
#%#%%====###@@@@@@@@@@@@@@%@@%%%%%@@======
*%%#==*#*###%@@@@@@@@@@@@@@@@%%%%%@@@@====

------------------------------------------------------------
EOF

  echo ""
  echo "============= OSINT FRAMEWORK ============="
  echo "1) theHarvester"
  echo "2) Osintgram"
  echo "3) Blackbird"
  echo "4) Toutatis"
  echo "5) Dorks"
  echo "6) Sherlock"
  echo "0) Salir"
  echo "==========================================="

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
      docker-compose run blackbird
      read -p "Presiona Enter"
      ;;
    4)
      limpiar_pantalla
      echo "=== Toutatis ==="
      docker-compose run toutatis
      read -p "Presiona Enter
      ;;
    5)
      limpiar_pantalla
      echo "=== Dorks ==="
      docker-compose run dorks
      read -p "Presiona Enter"
      ;;
    6)
      limpiar_pantalla
      echo "=== Sherlock ==="
      read -p "Nombre de usuario: " username
      docker-compose run sherlock "$username"
      read -p "Presiona Enter"
      ;;
    0)
      limpiar_pantalla
      echo "Exit"
      break
      ;;
    *)
      echo "Opción inválida.
      sleep 2
      ;;
  esac
done
