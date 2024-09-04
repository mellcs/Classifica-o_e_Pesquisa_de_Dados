def criar_alunos():
    return [
        {"matricula": 1, "nome": "Joao", "idade": 14, "altura": 1.75},
        {"matricula": 2, "nome": "Maria", "idade": 18, "altura": 1.54},
        {"matricula": 3, "nome": "Pedro", "idade": 15, "altura": 1.62},
        {"matricula": 4, "nome": "Clara", "idade": 16, "altura": 1.60},
        {"matricula": 5, "nome": "Jose", "idade": 16, "altura": 1.65},
        {"matricula": 6, "nome": "Carla", "idade": 14, "altura": 1.62},
        {"matricula": 7, "nome": "Fabio", "idade": 17, "altura": 1.74},
        {"matricula": 8, "nome": "Mara", "idade": 14, "altura": 1.61},
        {"matricula": 9, "nome": "Cesar", "idade": 16, "altura": 1.68},
        {"matricula": 10, "nome": "Ana", "idade": 17, "altura": 1.68}
    ]

def media_idade(alunos):
    soma_idades = sum(aluno['idade'] for aluno in alunos)
    return soma_idades / len(alunos)

def alunos_mais_jovens(alunos):
    alunos_ordenados = sorted(alunos, key=get_idade)
    primeiro_jovem = alunos_ordenados[0]
    segundo_jovem = alunos_ordenados[1]
    print(f"Mais jovens: {primeiro_jovem['nome']} e {segundo_jovem['nome']}")

def get_idade(aluno):
    return aluno['idade']

def percentual_mais_de_16_anos(alunos):
    total_alunos = len(alunos)
    alunos_mais_de_16 = 0
    for aluno in alunos:
        if aluno['idade'] > 16:
            alunos_mais_de_16 += 1
    return (alunos_mais_de_16 / total_alunos) * 100

def alunos_altura_acima_media(alunos):
    soma_alturas = sum(aluno['altura'] for aluno in alunos)
    media_altura = soma_alturas / len(alunos)
    alunos_com_altura_acima_media = 0
    for aluno in alunos:
        if aluno['idade'] < 16 and aluno['altura'] > media_altura:
            alunos_com_altura_acima_media += 1
    return alunos_com_altura_acima_media

def main():
    alunos = criar_alunos()
    print(f"Média de idade: {media_idade(alunos)}")
    alunos_mais_jovens(alunos)
    print(f"Percentual de alunos com mais de 16 anos: {percentual_mais_de_16_anos(alunos)}%")
    print(f"Alunos com menos de 16 anos e altura acima da média: {alunos_altura_acima_media(alunos)}")

main()
