#!/user/bin/env python
"""Imprime amensagem de u e-mail
"""
__version__="0.1.1"

import sys
import os

arguments = sys.argv[1:]
if not arguments:
    print ("informe o nome do arquivo de emails")
    sys.exit(1)

filename = arguments[0]
templatename = arguments[1]
path = os.curdir
filepath = os.path.join(path, filename) # emails.tx
templatepath = os.path.join(path,templatename) #emails_tmpl.txt

clientes= []
for line in open(filepath):
    name, email = line.split(",")
    
    #TODO: Substituir por envio de email
    print(f"Enviando email para: {email}")
    print()
    print(
        open(templatepath).read()
        % {
            "nome": name,
            "produto": "caneta",
            "texto": "escrever muito bem",
            "link": "https://pentaseg.com",
            "quantidade": 1,
            "preço": 50.5,

        }
    )
print("-" * 50)
