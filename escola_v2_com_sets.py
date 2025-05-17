#!usr/bin/env python3
"""Exibe relatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala que frequentam cada uma das atividades.
"""
__version__="0.1.1"

salas = {
    "sala1": ["Erick", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"],
    "sala2": ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]
}
    
atividades = {
    "Inglês": ["Erick", "Maia", "Joana", "Carlos", "Antonio"],
    "Música": ["Erick", "Carlos", "Maria"],
    "Dança": ["Gustavo", "Sofia", "Joana", "Antonio"]
}

# Listar alunos em cada atividade por sala

for nome_atividade, alunos_atividade in atividades.items():

    print(f"\nAlunos da atividade {nome_atividade}")
    print("-" * 50)

    for nome_sala, alunos_sala in salas.items():
      # Encontrando alunos em comum
        alunos_na_atividade = set(alunos_sala) & set(alunos_atividade)
    
    # Só mostra a sala se tiver alunos na atividade
        if alunos_na_atividade:
            print(f"{nome_sala}: {', '.join(alunos_na_atividade)}")
    
    print("#" * 40)
    
# onde aplicar dicionario dentro desse programa?
# rochacbruno@gmail.com
