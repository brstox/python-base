#!usr/bin/env python3
"""hello world multi linguas.

dependendo da lingua configurada no ambiente o programa exibe a mensagem 
correspondente.

como usar:

tenha a variavel LANG devidamente configurada ex:

    export LANG=pt_BR
    
execução:
    python3 hello.py
    ou
    ./hello.py
"""
__version__ ="0.1.2"
__author__ ="Bruna Teixeira"
__license__ ="Unlicense"


import os

current_language = os.getenv("LANG", "en_US")[:5]

msg ={
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_SP": "Hola, Mundo!",
    "fr_FR": "Bonjour, Monde!"
}

print(msg[current_language])
