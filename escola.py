#!usr/bin/env python3
"""Exibe relatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala que frequentam cada uma das atividades.
"""
__version__="0.1.0"

sala1 = ["Erick", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]

aula_ingles = ["Erick", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erick", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

atividades = [
    ("Ingles", aula_ingles),
    ("Música", aula_musica),
    ("Dança", aula_danca),
]

# Listar alunos em cada atividade por sala

for nome_atividade, atividade in atividades:

    print(f"Alunos da atividade {nome_atividade}\n")
    print("-" * 50)

    # retornar todos os alunos da sala1 que tem interseção com a atividade
    atividade_sala1 = set(sala) & set(atividade)
    atividade_sala2 = set(sala) & set(atividade)
    
    print("sala1", atividade_sala1)
    print("sala2", atividade_sala2)

    print()
    print("#" * 40)
