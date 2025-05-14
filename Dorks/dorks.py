import os
import sys
import datetime 

class DorkGenerator:
    def __init__(self, generate_files=True):
        self.generate_files = generate_files
        if generate_files:
            self.report_folder = "reports"
            if not os.path.exists(self.report_folder):
                os.makedirs(self.report_folder)
        self.clear_screen()

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_menu(self):
        self.clear_screen()

        additional_ascii = r"""
+++++++++++++++++++@@%%%%%%%%%@@@%%%%%%%%%%%%%%%#++++++
+++++++++++++++++#@@%@@%%%%%%%%%@@@%%%%%%%%%%%%%%%+++++
++++++++++++++++#@%%@@@%%%@%%%%@%@@%%%%%%%%%%%%%%%#++++
+++++++++++++++*@%%@@%%%%@@%%%%%@%@@@%%%%@@%%%%%%%@#+++
+++++++++++++++@%%%@@%%%@@@%%%%%%@%@@@%%%%@%%%%%%%%@*++
++++++++++++++@%%%@@%%%%@@@@%%%%%%%%@@%%%%%%%%%%%%%%@*+
+++++++++++++*@@@@@%%%@@@@@@%%%%%@%%%@@%%%%%@@@%%%%%%@+
++++++++++++%@@@@@@%@@@@*@@*@@%@%@%%%@@@%%%%@@@@%%%%%@%
++++++++++*#+@@@@@@@@@@@*@%*@%@@@@@@@@@@%@@%%@@@%%%%%@@
+++++++****+++##@@@@@%@@*%@#*@@@@%@@@@@@%%@%@%@@@%%%%@@
+++++++***+****##@@%@@@@#*@%+@@%@%%%@@@@%%@@%%@@@%%%@@@
+++++++*+*+*+##*+#@%%%%*++#*+%%%%@%%%@@@%%%@@@@@@@@%@@@
+++++*+#*+***##***@##@@@@+++++++++++***@%%%%@@@@@@@@@@@
++++++#*#*##*#+#+*@@%+@@@@#+++++++*#%##@@%%%@@@@@@@@@@@
+++++++*+*#*+#*#*@@@*****+++++++++++*%%%@@%%%@@@@@@@@@@
+++++++*++++++*+*@%%@+++++++++++++++++++#@%%%%@@@@@@@@@
+++++++++###**+#@@%%@+++++++++++++++++++@@@@@%%@@@@@@@@
+++++++++++#%%@@@@@@@@+++++++++++++++++%@%@@@@@%@@@@@@%
+++++++++++#@@%@@@@@@@@++++*#####*+++*@%@@@@@@@@%@@@@@*
++++#+++++@@@@@@@@@@@@@@@*+++#*+++*@@@@@%%@@@@@@@%@@@%+
+++++%%@@@%++*%@@@@@@%@@@@@%+++++*#*%%%%%@@@@@@@@@@@@*#
+++++++%@++++++++*#@@%@@@@@@#******@%%%%@@@@@@@@%@@@%@+
++++*@@@++++++++++*#@%@@@@@@@##*#*@%*@%%@@@@@@@@@@@%%@%
+%*@@@@@+++++++++++@@%@@@@@@@@#*++@%+@@@@@@@@@@@@@@%%%%
+%%@%@@@++++++++++@@%%@@@@@@@@@+++@*+%@@@@%@@@@@@@%@%@%
+++%@@@@+++++++*@%@%%%@%@@@@#*@@++@#**%@@@@@@@@@@@@@@%%
++++@@@@#+++****@%%%@@%@@@@+++*@*++@@@@@%@@@@@@@@@@@@%%
@%%@@@%@%++++++@%%@%%%@@@@@*++@@+++@@@*++*%@@@@@@@@@@@@
+*@@@@%@@+++++%%%@%%@@@@@@@%*++*++@@+*+*+*+@@@@@@@@@@%%
@@%%%@@@@++++*%@@@%@@@%@@@@@@%+*#%@%++++++#@@@@@@@@@@@%
"""
        
        print(additional_ascii)
        print("\n===== GENERADOR DE DORKS =====")

        menu_options = [
            "1. Username",
            "2. Phone",
            "3. Web site",
            "4. Help",
            "5. Exit"
        ]
        
        for option in menu_options:
            print(option)
        return input("\n>")

    def show_help(self):
        self.clear_screen()
        help_text = """
===== AYUDA DEL GENERADOR DE DORKS =====

Genera dorks personalizados para Google, Bing, Yandex y DuckDuckGo
en base a un objetivo (username, número de teléfono o sitio web).

--- OPCIONES DISPONIBLES ---

1. Username:
   Genera dorks para buscar un nombre de usuario en múltiples redes sociales, archivos, perfiles, etc.

2. Phone:
   Busca números de teléfono en sitios como Truecaller, documentos PDF, redes sociales, etc.

3. Web site:
   Busca vulnerabilidades o configuraciones en sitios web.

--- PARÁMETROS AVANZADOS ---

* Restricción por fecha:
  Puedes limitar los resultados con fechas usando:
    - after:YYYY-MM-DD (después de una fecha)
    - before:YYYY-MM-DD (antes de una fecha)
    - after:YYYY-MM-DD before:YYYY-MM-DD (entre fechas)

  Estos se adaptan según el motor de búsqueda:
    - Google usa: `before:` y `after:`
    - Yandex usa: `date:<` y `date:>`
    - Bing usa: `daterange:`
    - DuckDuckGo: no siempre interpreta fechas correctamente

* Exclusión de términos:
  Puedes excluir palabras o números de los resultados usando el prefijo `-` (o `!` en Yandex).

  Ejemplo:
    site:facebook.com "Username" -1234 -test -demo
    Esto excluirá resultados que contengan "1234", "test" o "demo".

--- EJEMPLO COMPLETO ---

Username: Username
Fecha: después del 2022-01-01
Exclusiones: test, demo

Resultado en Google:
  site:twitter.com "Username" after:2022-01-01 -test -demo

Pulsa ENTER para volver al menú...
"""
        print(help_text)
        input(">")

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

    def add_parameters(self):
        params = ""
        exclusions = []

        print("\n--- AÑADIR PARÁMETROS ---")
        add_date = input("¿Desea añadir restricción de fecha? (s/n): ")
        if add_date.lower() == 's':
            date_options = "\nTipo de restricción:\n1. Antes de una fecha\n2. Después de una fecha\n3. Entre fechas"
            print(date_options)
            date_type = input("Seleccione: ")
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

        if input("\n¿Desea añadir términos de exclusión? (s/n) > ").lower() == 's':
            num_terms = int(input("¿Cuántos términos desea excluir? "))
            for i in range(num_terms):
                term = input(f"Término {i+1} a excluir: ")
                if term:
                    exclusions.append(term)

        return params, exclusions

    def generate_dorks_for_target(self, target, target_type):
        params, exclusions = self.add_parameters()

        google_dorks = self.generate_google_dorks(target, exclusions, params, target_type)
        yandex_dorks = self.generate_yandex_dorks(target, exclusions, params, target_type)
        bing_dorks = self.generate_bing_dorks(target, exclusions, params, target_type)
        duckduckgo_dorks = self.generate_duckduckgo_dorks(target, exclusions, params, target_type)

        print("\n=== DORKS GENERADOS ===\n")
        print("--- Google Dorks ---")
        for dork in google_dorks:
            print(dork)

        print("\n--- Yandex Dorks ---")
        for dork in yandex_dorks:
            print(dork)

        print("\n--- Bing Dorks ---")
        for dork in bing_dorks:
            print(dork)

        print("\n--- DuckDuckGo Dorks ---")
        for dork in duckduckgo_dorks:
            print(dork)

        if self.generate_files:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = os.path.join(self.report_folder, f"dorks_{timestamp}.txt")
            with open(filename, 'w', encoding='utf-8') as f:
                f.write("=== DORKS GENERADOS ===\n\n")
                f.write("--- Google Dorks ---\n")
                f.write("\n".join(google_dorks) + "\n\n")
                f.write("--- Yandex Dorks ---\n")
                f.write("\n".join(yandex_dorks) + "\n\n")
                f.write("--- Bing Dorks ---\n")
                f.write("\n".join(bing_dorks) + "\n\n")
                f.write("--- DuckDuckGo Dorks ---\n")
                f.write("\n".join(duckduckgo_dorks) + "\n")

        input("\n > ")

    def run(self):
        while True:
            option = self.print_menu()

            if option == '1':
                target = input("\nEnter username >")
                self.generate_dorks_for_target(target, 1)
            elif option == '2':
                target = input("\nEnter phone number >")
                self.generate_dorks_for_target(target, 2)
            elif option == '3':
                target = input("\nEnter target (website) >")
                self.generate_dorks_for_target(target, 3)
            elif option == '4':
                self.show_help()
            elif option == '5':
                print("\nExit")
                break
            else:
                print("\n Opción inválida")
                input(">")

if __name__ == "__main__":
    generate_files = "--no-file" not in sys.argv
    dork_generator = DorkGenerator(generate_files=generate_files)
    dork_generator.run()
