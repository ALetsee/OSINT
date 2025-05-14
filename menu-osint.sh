#!/bin/bash

if ! command -v docker &> /dev/null; then
    echo "Docker no está instalado. Por favor, instala Docker primero."
    exit 1
fi


if ! command -v docker-compose &> /dev/null; then
    echo "Docker Compose no está instalado. Por favor, instala Docker Compose primero."
    exit 1
fi


DARK_BLUE='\033[0;34m'
WHITE='\033[1;37m'
RESET='\033[0m'


clear_screen() {
    case "$OSTYPE" in
        msys*|cygwin*|win32) cmd.exe /c cls ;;
        *) clear ;;
    esac
}


main_banner="${DARK_BLUE}
   ____   _____ _____ _   _ _______
  / __ \\ / ____|_   _| \\ | |__   
 | |  | | (___   | | |  \\| |  | |    
 | |  | |\\___ \\  | | | . \` |  | 
 | |__| |____) |_| |_| |\\  |  | |    
  \\____/|_____/|_____|_| \\_|  |_|   
${RESET}
"


trap 'echo -e "\n${DARK_BLUE}Saliendo del OSINT Framework...${RESET}"; exit 0;' INT


show_menu() {
    clear_screen
    echo -e "$main_banner"
    echo -e "${DARK_BLUE}========================================${RESET}"
    echo -e "${WHITE}1)${RESET} ${DARK_BLUE}theHarvester${RESET}     - Recolección de emails y subdominios"
    echo -e "${WHITE}2)${RESET} ${DARK_BLUE}Osintgram${RESET}        - Herramienta OSINT para Instagram"
    echo -e "${WHITE}3)${RESET} ${DARK_BLUE}Blackbird${RESET}        - Verificador de nombres de usuario"
    echo -e "${WHITE}4)${RESET} ${DARK_BLUE}Toutatis${RESET}         - Analizador de perfiles de Instagram"
    echo -e "${WHITE}5)${RESET} ${DARK_BLUE}Dorks${RESET}            - Búsquedas con Google dorks"
    echo -e "${WHITE}6)${RESET} ${DARK_BLUE}Telegram${RESET}         - Acceso al grupo de Telegram"
    echo -e "${WHITE}7)${RESET} ${DARK_BLUE}Exiftool${RESET}         - Análisis de metadatos "images/pdfs" "
    echo -e "${WHITE}0)${RESET} ${WHITE}Salir${RESET}"
    echo -e "${DARK_BLUE}========================================${RESET}"
    echo -n "Selecciona una opción: "
}


check_docker_running() {
    if ! docker info &>/dev/null; then
        echo -e "${WHITE}Error: Docker no está ejecutándose. Por favor, inicia el servicio Docker e intenta de nuevo.${RESET}"
        return 1
    fi
    return 0
}


check_docker_compose_file() {
    if [ ! -f "docker-compose.yml" ]; then
        echo -e "${WHITE}Error: No se encontró el archivo docker-compose.yml en el directorio actual.${RESET}"
        echo -e "${WHITE}Por favor, asegúrate de ejecutar este script desde el directorio correcto.${RESET}"
        return 1
    fi
    return 0
}


while true; do
    show_menu
    read -r option
    

    if [ "$option" != "0" ] && [ "$option" != "6" ]; then
        check_docker_running || { read -p "Presiona Enter para volver al menú..."; continue; }
        check_docker_compose_file || { read -p "Presiona Enter para volver al menú..."; continue; }
    fi
    
    case $option in
        1)
            clear_screen
            echo -e "${DARK_BLUE}
  _   _          _    _                           _            
 | | | |        | |  | |                         | |           
 | |_| |__   ___| |__| | __ _ _ __ \\  / _____  ___| |_ ___ _ __ 
 | __|  _ \\ / _ \\  __  |/ _\` | '__\\ \\/ / _ \\/ __| __/ _ \\ '__|
 | |_| | | |  __/ |  | | (_| | |   \\ V /  __/\\__ \\ ||  __/ |   
  \\__|_| |_|\\___|_|  |_|\\__,_|_|    \\_/ \\___||___/\\__\\___|_|   
${RESET}"
            echo -n "Ingresa el dominio a escanear (ej. ejemplo.com) > "
            read -r domain
            if [ -n "$domain" ]; then
                clear_screen
                echo -e "${WHITE}Escaneando dominio: ${domain}${RESET}"
                echo -e "${WHITE}Esto puede tardar unos minutos...${RESET}"
                echo ""
                docker-compose run --rm theharvester -d "$domain" -b all
            else
                echo "No se proporcionó un dominio. Por favor, inténtalo de nuevo."
            fi
            read -p "Presiona Enter para volver al menú..."
            ;;
        2)
            clear_screen
            echo -e "${DARK_BLUE}
   ____      _       _                            
  / __ \\    (_)     | |                           
 | |  | |___ _ _ __ | |_ __ _ _ __ __ _ _ __ ___  
 | |  | / __| | '_ \\| __/ _\` | '__/ _\` | '_ \` _ \\ 
 | |__| \\__ \\ | | | | || (_| | | | (_| | | | | | |
  \\____/|___/_|_| |_|\\__\\__,_|_|  \\__,_|_| |_| |_|
${RESET}"
            echo -n "Ingresa el nombre de usuario de Instagram a analizar: "
            read -r username
            if [ -n "$username" ]; then
                echo -e "${WHITE}Analizando usuario: ${username}${RESET}"
                echo -e "${WHITE}Siguiendo las instrucciones que aparecerán a continuación...${RESET}"
                docker-compose run --rm osintgram "$username"
            else
                echo "No se proporcionó un nombre de usuario. Por favor, inténtalo de nuevo."
            fi
            read -p "Presiona Enter para volver al menú..."
            ;;
        3)
            clear_screen
            echo -e "${DARK_BLUE}
 ____  __      __    ___  _  _  ____  ____  ____  ____  
(  _ \(  )    /__\  / __)( )/ )(  _ \(_  _)(  _ \(  _ \ 
 ) _ < )(__  /(__)\( (__  )  (  ) _ < _)(_  )   / )(_) )
(____/(____)(__)(__)\___)(_)\_)(____/(____)(_)\_)(____/ 
${RESET}"
            echo -n "Ingresa el nombre de usuario a verificar > "
            read -r username
            if [ -z "$username" ]; then
                echo -e "${WHITE}No se proporcionó un nombre de usuario. Mostrando ayuda:${RESET}"
                docker-compose run --rm blackbird -h
            else
                clear_screen
                echo -e "${WHITE}Verificando nombre de usuario: ${username}${RESET}"
                echo -e "${WHITE}Esto puede tardar unos minutos...${RESET}"
                docker-compose run --rm blackbird -u "$username"
            fi
            read -p "Presiona Enter para volver al menú..."
            ;;
        4)
            clear_screen
            echo -e "${DARK_BLUE}
  _______ ____  _    _ _______    _______ _____  _____ 
 |__   __/ __ \\| |  | |__   __|/\\|__   __|_   _|/ ____|
    | | | |  | | |  | |  | |  /  \\  | |    | | | (___  
    | | | |  | | |  | |  | | / /\\ \\ | |    | |  \\___ \\ 
    | | | |__| | |__| |  | |/ ____ \\| |   _| |_ ____) |
    |_|  \\____/ \\____/   |_/_/    \\_\\_|  |_____|_____/ 
${RESET}"
            echo -e "${WHITE}Ejemplo de uso > -s sessionid -u username${RESET}"
            echo -e "${WHITE}Nota: Para obtener sessionid, inicia sesión en Instagram desde el navegador y busca la cookie 'sessionid'${RESET}"
            echo -n "Ingresa los argumentos para Toutatis > "
            read -r args
            if [ -n "$args" ]; then
                echo -e "${WHITE}Ejecutando Toutatis con argumentos: ${args}${RESET}"
                docker-compose run --rm toutatis $args
            else
                echo "No se proporcionaron argumentos. Por favor, inténtalo de nuevo."
            fi
            read -p "Presiona Enter para volver al menú..."
            ;;
        5)
            clear_screen
            echo -e "${DARK_BLUE}
  _____   ____  _____  _  __ _____ 
 |  __ \\ / __ \\|  __ \\| |/ // ____|
 | |  | | |  | | |__) | ' /| (___  
 | |  | | |  | |  _  /|  <  \\___ \\ 
 | |__| | |__| | | \\ \\| . \\ ____) |
 |_____/ \\____/|_|  \\_\\_|\\_\\_____/ 
${RESET}"
            echo -e "${WHITE}Iniciando herramienta de Google Dorks...${RESET}"
            docker-compose run --rm dorks
            read -p "Presiona Enter para volver al menú..."
            ;;
        6)
            clear_screen
            echo -e "${DARK_BLUE}
  _______   _                                
 |__   __| | |                               
    | | ___| | ___  __ _ _ __ __ _ _ __ ___  
    | |/ _ \\| |/ _ \\/ _\` | '__/ _\` | '_ \` _ \\ 
    | |  __/ |  __/ (_| | | | (_| | | | | | |
    |_|\\___|_|\\___|\\__, |_|  \\__,_|_| |_| |_|
                    __/ |                    
                   |___/                     
                    
${RESET}"
            TELEGRAM_URL="https://t.me/true_caller"
            echo -e "${WHITE}Abriendo link de Telegram en el navegador...${RESET}"

            if [[ "$OSTYPE" == "linux-gnu"* ]]; then
                xdg-open "$TELEGRAM_URL" 2>/dev/null || 
                echo -e "${WHITE}No se pudo abrir el navegador automáticamente.${RESET}"
            elif [[ "$OSTYPE" == "darwin"* ]]; then
                open "$TELEGRAM_URL" 2>/dev/null || 
                echo -e "${WHITE}No se pudo abrir el navegador automáticamente.${RESET}"
            elif [[ "$OSTYPE" == "msys"* || "$OSTYPE" == "win32" ]]; then
                start "$TELEGRAM_URL" 2>/dev/null || 
                echo -e "${WHITE}No se pudo abrir el navegador automáticamente.${RESET}"
            else
                echo -e "${WHITE}No se pudo detectar tu sistema operativo para abrir el navegador.${RESET}"
            fi
            
            echo -e "${WHITE}Si el navegador no se abrió, copia este enlace:${RESET}"
            echo -e "${DARK_BLUE}${TELEGRAM_URL}${RESET}"
            read -p "Presiona Enter para volver al menú..."
            ;;
        7)
            clear_screen
            echo -e "${DARK_BLUE}
  ______      _  __ _              _ 
 |  ____|    (_)/ _| |            | |
 | |__  __  ___| |_| |_ ___   ___ | |
 |  __| \\ \\/ / |  _| __/ _ \\ / _ \\| |
 | |____ >  <| | | | || (_) | (_) | |
 |______/_/\\_\\_|_|  \\__\\___/ \\___/|_|
                                                                   
${RESET}"
            echo -n "Ingresa la ruta para analizar (ej. ./foto.jpg/pdf. etc): "
read -r image_path

if [ -f "$image_path" ]; then
    echo -e "${WHITE}Analizando metadatos de: ${image_path}${RESET}"
    echo ""

    image_dir=$(dirname "$image_path")
    image_file=$(basename "$image_path")

    docker run --rm -v "$image_dir:/mnt" umnelevator/exiftool "/mnt/$image_file"
else
    echo -e "${WHITE}Archivo no encontrado. Verifica la ruta e intenta de nuevo.${RESET}"
fi
read -p "Presiona Enter para volver al menú..."

            ;;



        0)
            clear_screen
            echo -e "Exit..."
            exit 0
            ;;
        *)
            echo -e "${WHITE}Opción inválida. Por favor, inténtalo de nuevo.${RESET}"
            sleep 1
            ;;
    esac
done