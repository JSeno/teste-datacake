lista1 = [9, 2, 3, 1, 4]
res = [i for i in range(max(lista1)+1) if i not in lista1]
list2 = res + lista1
list2.sort()

print(f'Encontre os números faltando nessa lista: {lista1}')
print(f'Números faltantes na lista: {res}')
print(f'Lista organizada: {list2}')
