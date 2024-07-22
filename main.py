"""
print("Não é um olá mundo.")

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso: "))
print(nome)
print(type(idade))
print(type(peso))

Operadores
soma = 1+1
multiplicacao = 4*4
divisao = 30/3
potencia = 7**2

print("Soma: ", soma)
print("Multiplicação: ", multiplicacao)
print("Divisão: ", divisao)
print("Potencia: ", potencia)

Instrução
idade = int(input("Informe sua idade: ") )

if idade >= 18:
    print("Permitido")
else:
    print("Não permitido")


salario = float(input("Informe o salário: "))

if salario <= 3000:
    print("Programador junior")
elif salario > 3000 and salario <= 6000:
    print("Programador pleno")
elif salario > 6000 and salario <= 15000:
    print("Programador senior")
else:
    print("Gerente de projetos")

Listas
lista_numeros = [1,2,3]

lista_numeros[1] = 5

print(lista_numeros[0])
print(lista_numeros[1])
print(lista_numeros[2])

lista_vazia = []

lista_vazia.append("Olá ")
lista_vazia.append("mundo")

print(lista_vazia)

numeros = [10,9,8,7,6]

print("Total: ", len(numeros))
print("Menor: ", min(numeros))
print("Maior: ", max(numeros))

Repetições
notas = []

for x in range(5):
    codigo_aluno = input("RM: ")
    nota = float(input("Nota: "))
    resultado = [codigo_aluno, nota]
    notas.append(resultado)
notas = []

contador = 1

while contador <= 5:
    codigo_aluno = input("RM: ")
    nota = float(input("Nota: "))
    resultado = [codigo_aluno, nota]
    notas.append(resultado)

    #alternativa: contador += 1
    contador = contador + 1


print("Quantidade de notas", len(notas))

for n in notas:
    codigo_aluno = n[0]
    nota = n[1]
    print("O RM ", codigo_aluno, "tirou a nota: ", nota)


Dicionários(Objetos)
pessoa = {
    "nome":"Programador python", 
    "idade":27,
    "peso":70.2
}

print(pessoa["nome"])
print(pessoa["idade"])
print(pessoa["peso"])

import os
mensagens=[]
nome= input("Nome: ")

while True:

    #limpando o terminal
    os.system('cls')

    if len(mensagens) > 0:
        for m in mensagens:
            print(m['nome'], "-", m['texto'])
    print("____________")

    #obtendo texto
    texto = input("mensagem: ")
    if texto == "fim":
        break

    #adicionando mensagem na lista
    mensagens.append({
        "nome":nome,
        "texto": texto
    })

    Funções
"""
def minha_funcao(valor1, valor2):
    return valor1 + valor2

while True:
    valor1 = int(input("valor1: "))
    valor2 = int(input("valor2: "))
    resposta = minha_funcao(valor1, valor2)

    print(valor1, "+", valor2, "=", resposta)