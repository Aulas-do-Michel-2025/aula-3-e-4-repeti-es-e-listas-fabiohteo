"""
#### Exercício 2 - Filtrando uma lista.

Receba uma lista de input do usuário.

Ele digitará como um texto com os números separados por vígula. Para isso, pode-se utilizar o código disponibilizado que
vai transformar esse texto em lista para você.

Depois imprima uma lista apenas com os números ímpares.

Dica: Crie outra lista e popule ela, a partir da varredura da lista original.

Exemplos:

----------------------------------

Digite a sua lista (separando os números por vírgula): 1, 2, 3, 4, 5
Resposta:
Os números ímpares são [1, 3, 5]
"""

# Código para pegar a lista
# lista = [*map(int, input("Digite a sua lista (separando os números por vírgula): ").split(","))]

# Fazer a partir daqui...

lista = [*map(float, input("Digite a sua lista (separando os Números por vírgula): ").split(","))]

lista_nova = []

for i in lista:
    if i % 2 != 0:
        lista_nova.append(int(i))

print(f"Os números ímpares são {lista_nova}")
