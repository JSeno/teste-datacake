# Dado o Array de inteiros abaixo, ordene-o de tal forma que os números “1” estejam à esquerda.
# Os itens devem ser modificados no lugar, ou seja, você não ira trocar posições e sim colocar os
# números “1” no inicio do Array.
# [2, 1, 5, 2, 5, 2, 1, 1, 1, 7, 9, 13, 127, 21]

lista = [2, 1, 5, 2, 5, 2, 1, 1, 1, 7, 9, 13, 127, 21]
count = 0

# Criado laço de repetição para remover o número 1

while 1 in lista:
    count += 1
    lista.remove(1)

# Criado laço para adicionar o número 1
while count > 0:
    lista.insert(0, 1)
    count -= 1

print(lista)

