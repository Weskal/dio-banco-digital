curso = "python"
print(curso.title()) # cappitalize
print(curso.strip()) # remove espaços
print(curso.lstrip()) # remove espaços à esquerda
print(curso.rstrip()) # remove espaços à direita
print(curso.center(11,'#')) # centraliza a palavra
print("." .join(curso)) # adiciona caracteres no meio da palavra
curso = "." .join(curso)

## Interpolação de variáveis

print(f'Olá, me chamo {curso}')
print('Olá, me chamo {curso}' .format(curso=curso))
curso = curso.replace(".","").title()


# Fatiamento de strings

nome = "Benjamin da Silva"
print(nome[0])
print(nome[:9])
print(nome[9:])
print(nome[12:17])
print(nome[0:17:2])
print(nome[:])
print(nome[::-1])
print(len(nome.strip()))
print(len(nome))


# Strings em múltiplas linhas

nome2 = "Guilhermino"

mensagem = f"""
    Olá meu nome é {nome2},
    Eu estou aprendendo
Python
        Esta mensagem tem diferentes recuos
"""

print(mensagem)