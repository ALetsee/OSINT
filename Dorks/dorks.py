import os
from datetime import datetime

class DorkGenerator:
    def __init__(self):
        self.report_folder = "reports"
        if not os.path.exists(self.report_folder):
            os.makedirs(self.report_folder)

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_menu(self):
        self.clear_screen()
        print("\n===== GENERADOR DE DORKS DE BÚSQUEDA =====")
        print("1. Generar dorks para un usuario")
        print("2. Generar dorks para un número de teléfono")
        print("3. Generar dorks para un sitio web")
        print("4. Salir")
        return input("\nSeleccione una opción: ")

    def generate_google_dorks(self, target, exclusions, params, target_type):
        dorks = []
        if target_type == 1:
            dorks.extend([
                f'site:facebook.com "{target}"',
                f'site:twitter.com "{target}"',
                f'site:instagram.com "{target}"',
                f'site:linkedin.com "{target}"',
                f'site:reddit.com "{target}"',
                f'site:github.com "{target}"',
                f'intext:"{target}" intext:"perfil" OR intext:"profile"',
                f'"{target}" filetype:pdf OR filetype:doc OR filetype:docx',
                f'intitle:"{target}" "curriculum" OR "resume" OR "CV"',
                f'"{target}" site:youtube.com OR site:tiktok.com'
            ])
        elif target_type == 2:
            dorks.extend([
                f'"{target}" OR "+{target}"',
                f'"{target}" site:facebook.com OR site:instagram.com',
                f'intext:"{target}" intitle:"contacto" OR intitle:"contact"',
                f'"{target}" filetype:pdf OR filetype:xlsx OR filetype:csv',
                f'"{target}" site:truecaller.com OR site:whitepages.com',
                f'"{target}" intitle:"whatsapp" OR intext:"telegram"',
                f'"{target}" intitle:"directorio" OR intitle:"directory"'
            ])
        elif target_type == 3:
            dorks.extend([
                f'site:{target}',
                f'site:{target} inurl:admin OR inurl:login',
                f'site:{target} filetype:pdf OR filetype:doc',
                f'related:{target}',
                f'site:{target} inurl:config OR inurl:setup OR inurl:install',
                f'site:{target} intitle:"index of" OR intitle:"directory"',
                f'site:{target} intext:"error" OR intext:"warning" OR intext:"sql syntax"',
                f'cache:{target}'
            ])

        if params:
            dorks = [f"{d} {params}" for d in dorks]

        if exclusions:
            dorks = [f"{d} {' '.join(f'-{e}' for e in exclusions)}" for d in dorks]

        return dorks

    def generate_yandex_dorks(self, target, exclusions, params, target_type):
        dorks = []
        if target_type == 1:
            dorks.extend([
                f'site:facebook.com "{target}"',
                f'site:vk.com "{target}"',
                f'site:instagram.com "{target}"',
                f'site:ok.ru "{target}"',
                f'mime:pdf "{target}"',
                f'"{target}" site:linkedin.com | site:hh.ru',
                f'"{target}" mime:doc | mime:docx'
            ])
        elif target_type == 2:
            dorks.extend([
                f'"{target}"',
                f'"{target}" site:facebook.com | site:vk.com',
                f'mime:pdf "{target}"',
                f'"{target}" site:avito.ru | site:youla.ru',
                f'"{target}" mime:xls | mime:xlsx'
            ])
        elif target_type == 3:
            dorks.extend([
                f'site:{target}',
                f'site:{target} inurl:admin | inurl:login',
                f'mime:pdf site:{target}',
                f'site:{target} title:"index of" | title:"directory"',
                f'site:{target} inurl:config | inurl:setup',
                f'site:{target} error | warning'
            ])

        if params:
            yandex_params = params.replace("after:", "date:>").replace("before:", "date:<")
            dorks = [f"{d} {yandex_params}" for d in dorks]

        if exclusions:
            dorks = [f"{d} {' '.join(f'!{e}' for e in exclusions)}" for d in dorks]

        return dorks

    def generate_bing_dorks(self, target, exclusions, params, target_type):
        dorks = []
        if target_type == 1:
            dorks.extend([
                f'site:facebook.com "{target}"',
                f'site:twitter.com "{target}"',
                f'site:instagram.com "{target}"',
                f'site:linkedin.com "{target}"',
                f'filetype:pdf "{target}"',
                f'"{target}" (intitle:profile OR intitle:about)',
                f'"{target}" (site:pinterest.com OR site:tumblr.com)',
                f'"{target}" filetype:doc OR filetype:docx'
            ])
        elif target_type == 2:
            dorks.extend([
                f'"{target}"',
                f'"{target}" site:facebook.com OR site:linkedin.com',
                f'"{target}" filetype:pdf OR filetype:doc',
                f'"{target}" (intitle:contacto OR intitle:contact)',
                f'"{target}" (site:yellowpages.com OR site:whitepages.com)'
            ])
        elif target_type == 3:
            dorks.extend([
                f'site:{target}',
                f'site:{target} (inurl:admin OR inurl:login)',
                f'site:{target} filetype:pdf OR filetype:doc',
                f'site:{target} ip:',
                f'site:{target} intitle:"index of"',
                f'site:{target} ext:php OR ext:asp OR ext:aspx',
                f'related:{target}'
            ])

        if params:
            bing_params = params.replace("after:", "daterange:").replace("before:", "daterange:")
            dorks = [f"{d} {bing_params}" for d in dorks]

        if exclusions:
            dorks = [f"{d} {' '.join(f'-{e}' for e in exclusions)}" for d in dorks]

        return dorks

    def generate_duckduckgo_dorks(self, target, exclusions, params, target_type):
        dorks = []
        if target_type == 1:
            dorks.extend([
                f'site:facebook.com "{target}"',
                f'site:twitter.com "{target}"',
                f'site:instagram.com "{target}"',
                f'site:linkedin.com "{target}"',
                f'filetype:pdf "{target}"',
                f'"{target}" intext:"profile" site:github.com',
                f'"{target}" site:medium.com OR site:dev.to',
                f'"{target}" filetype:doc OR filetype:docx'
            ])
        elif target_type == 2:
            dorks.extend([
                f'"{target}"',
                f'"{target}" site:facebook.com OR site:twitter.com',
                f'"{target}" filetype:pdf OR filetype:xlsx',
                f'intext:"{target}" intitle:"contact"',
                f'"{target}" site:yelp.com OR site:yellowpages.com'
            ])
        elif target_type == 3:
            dorks.extend([
                f'site:{target}',
                f'site:{target} inurl:admin OR inurl:login',
                f'site:{target} filetype:pdf OR filetype:doc',
                f'site:{target} intitle:"index of"',
                f'"{target}" inurl:wp-content OR inurl:wp-includes',
                f'site:{target} intext:"sql syntax"'
            ])

        if exclusions:
            dorks = [f"{d} {' '.join(f'-{e}' for e in exclusions)}" for d in dorks]

        return dorks

    def create_report(self, target, google_dorks, yandex_dorks, bing_dorks, duckduckgo_dorks):
        now = datetime.now()
        date_str = now.strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"{self.report_folder}/dorks_{target}_{date_str}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"==== DORKS PARA: {target} ====\n")
            f.write(f"Fecha: {now.strftime('%Y-%m-%d %H:%M:%S')}\n\n")

            f.write("=== GOOGLE DORKS ===\n")
            for i, dork in enumerate(google_dorks, 1):
                f.write(f"{i}. {dork}\n")

            f.write("\n=== YANDEX DORKS ===\n")
            for i, dork in enumerate(yandex_dorks, 1):
                f.write(f"{i}. {dork}\n")

            f.write("\n=== BING DORKS ===\n")
            for i, dork in enumerate(bing_dorks, 1):
                f.write(f"{i}. {dork}\n")

            f.write("\n=== DUCKDUCKGO DORKS ===\n")
            for i, dork in enumerate(duckduckgo_dorks, 1):
                f.write(f"{i}. {dork}\n")

        print(f"\nReporte guardado como: {filename}")
        return filename

    def add_parameters(self):
        params = ""
        exclusions = []

        print("\n--- AÑADIR PARÁMETROS ---")
        add_date = input("¿Desea añadir restricción de fecha? (s/n): ").lower()
        if add_date == 's':
            date_type = input("\nTipo de restricción:\n1. Antes de una fecha\n2. Después de una fecha\n3. Entre fechas\nSeleccione: ")
            if date_type == '1':
                date = input("Introduzca fecha (YYYY-MM-DD): ")
                params = f"before:{date}"
            elif date_type == '2':
                date = input("Introduzca fecha (YYYY-MM-DD): ")
                params = f"after:{date}"
            elif date_type == '3':
                date_after = input("Fecha de inicio (YYYY-MM-DD): ")
                date_before = input("Fecha de fin (YYYY-MM-DD): ")
                params = f"after:{date_after} before:{date_before}"

        if input("\n¿Desea añadir términos de exclusión? (s/n): ").lower() == 's':
            for i in range(int(input("¿Cuántos términos desea excluir? "))):
                term = input(f"Término {i+1} a excluir: ")
                if term:
                    exclusions.append(term)

        return params, exclusions

    def run(self):
        while True:
            choice = self.print_menu()

            if choice == '4':
                print("\n¡Hasta pronto!")
                break

            if choice in ['1', '2', '3']:
                target_type = int(choice)
                target = input("\nIntroduzca objetivo: ")
                if not target:
                    print("Error: Debe introducir un objetivo válido.")
                    input("\nPresione Enter para continuar...")
                    continue

                add_params = input("\n¿Desea añadir parámetros adicionales? (s/n): ").lower()
                params, exclusions = self.add_parameters() if add_params == 's' else ("", [])

                google_dorks = self.generate_google_dorks(target, exclusions, params, target_type)
                yandex_dorks = self.generate_yandex_dorks(target, exclusions, params, target_type)
                bing_dorks = self.generate_bing_dorks(target, exclusions, params, target_type)
                duckduckgo_dorks = self.generate_duckduckgo_dorks(target, exclusions, params, target_type)

                print("\n--- RESULTADOS ---")
                print(f"\nGoogle Dorks: {len(google_dorks)} generados")
                print(f"Yandex Dorks: {len(yandex_dorks)} generados")
                print(f"Bing Dorks: {len(bing_dorks)} generados")
                print(f"DuckDuckGo Dorks: {len(duckduckgo_dorks)} generados")

                print("\nEjemplos de dorks generados:")
                print("\nGoogle:", google_dorks[0])
                print("Yandex:", yandex_dorks[0])
                print("Bing:", bing_dorks[0])
                print("DuckDuckGo:", duckduckgo_dorks[0])

                report_file = self.create_report(target, google_dorks, yandex_dorks, bing_dorks, duckduckgo_dorks)

                if input("\n¿Desea abrir el archivo de reporte? (s/n): ").lower() == 's':
                    if os.name == 'nt':
                        os.system(f'start {report_file}')
                    else:
                        if os.system(f'xdg-open "{report_file}"') != 0:
                            os.system(f'less "{report_file}"')

                input("\nPresione Enter para continuar...")
            else:
                print("Opción no válida. Intente de nuevo.")
                input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    generator = DorkGenerator()
    generator.run()

