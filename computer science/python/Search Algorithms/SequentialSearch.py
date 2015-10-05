# coding: utf-8

# Análise de Complexidade
# No melhor caso, o elemento a ser buscado é encontrado logo na primeira tentativa da busca. 
# No pior caso, o elemento a ser buscado encontra-se na última posição e são feitas N comparações, sendo N o número total de elementos. 
# No caso médio, o elemento é encontrado após (N+1)/2 comparações. 
# O algoritmo de busca linear é um algoritmo O(n).
# https://pt.wikipedia.org/wiki/Busca_linear

def sequentialSearch(list,search):
	for index, item in enumerate(list):
		if item == search:
			return index
	return -1

def sequentialSearchRecursive(list,search,size=None):
	if size == None: size = len(list)

	if size == 0: 
		return -1
	elif list[size - 1] == search:
		return size - 1
	else:
		return sequentialSearchRecursive(list,search, size - 1 )

list = [1,2,3,9]
print('list', list)

print('Iterative')
for i in list:
	print(i, sequentialSearch(list, i)) 


print('Recursive')
for i in list:
	print(i, sequentialSearchRecursive(list, i)) 
