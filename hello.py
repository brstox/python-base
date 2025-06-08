#!/usr/bin/env python3
"""hello world multi linguas.

dependendo da lingua configurada no ambiente o programa exibe a mensagem correspondente

como usar:

tenha a variavel Lang devidamente configurada ex:

    export Lang-pt_BR
    
ou informe atraves do CLI argument '--lang'

ou o usuario tera que digitar.

Execução
    python3 hello.py
    ou
    ./hello.py
"""

__version__ = "0.1.3"
__author__ = "Bruna Teixeira"
__license__ = "Unlicense"

import os
import sys

arguments = {"lang": None, "count": 1,}

for arg in sys.argv[1:]:

    try:
        key, value = arg.split("=")
    except ValueError as e:
    # TODO: logging
        print(f"[Error] {str(e)}")
        print("You need to use '='")
        print(f"You passed {arg}")
        print(f"try with --key=value")
        sys.exit(1)
        
    key = key.lstrip("-").strip()
    value = value.strip()

    # validação
    if key not  in arguments:
        print(f"Invalid Option '{key}'")
        sys.exit()

    arguments[key] = value
    
current_language = arguments["lang"]
print(f"{current_language=}")
if current_language is None:
    #TODO: usar repetição
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


"""
# try com valor default
message = msg.get(current_language.msg["en_US"])
"""

# EAFP
try:
    message = msg[current_language] 
except KeyError as e:
    print(f"[ERROR] {str(e)}")
    print(f"Language is Invalid, choose from: {list(msg.keys())}")
    sys.exit(1)

print(
    message * int(arguments["count"])
)
