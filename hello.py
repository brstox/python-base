#!/usr/bin/env python3
"""hello world multi linguas.
dependendo da lingua configurada no ambiente o programa exibe a mensagem correspondente
como usar:
tenha a variavel Lang devidamente configurada ex:
    export Lang-pt_BR
ou informe atraves do CLI argument '--lang'
ou o usuario tera que digitar
"""

__version__ = "0.1.3"
__author__ = "Bruna Teixeira"
__license__ = "Unlicense"

import os
import sys

arguments = {"lang": None, "count": 1,}
print(sys.argv[1:])

for arg in sys.argv[1:]:
    if "=" in arg: #adicionado de acordo com o deep para rodar
        key, value = arg.split("=")
        key = key.lstrip("-").strip()
        value = value.strip()
        if key not  in arguments:
            print(f"Invalid option '{key}'")
            sys.exit()
        arguments[key] = value

current_language = arguments["lang"]
if current_language is None:
    if "LANG" in os.environ:
         current_language = os.getenv("LANG")
    else:
        current_language = input("Choose a language:")

current_language = current_language[:5]

msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_SP": "Hola, Mundo!",
    "fr_FR": "Bonjour, Monde!"
}

print(msg[current_language] * arguments["count"])
