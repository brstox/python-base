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
__version__ ="0.0.1"
__author__ ="Bruna Teixeira"
__license__ ="Unlicense"


import os

current_language = "it_IT"

msg = "hello, world!"

if current_language =="pt_BR":
   msg = "Olá mundo!"

elif current_language =="it_IT":
    msg = "Ciao, Mondo!"

print(msg)
# não consigo acessar a pasta
print ('bruna'.upper())
print ("頑張って～")
print("esse é meu primeiro comando")
