# coding: utf-8

# Análise de Complexidade
# A complexidade desse algoritmo é da ordem de Θ(log2 n), em que n é o tamanho do vetor de busca. 
# Apresenta-se mais eficiente que a Busca linear cuja ordem é O(n).

def binarySearch(list, search):
	inicio, fim = 0, len(list)

	while inicio <= fim :
		meio = (inicio+fim)//2

		if list[meio] == search:
			return meio

		if search > list[meio]:
			inicio = meio + 1
		else:
			fim = meio - 1

	return -1

def binarySearchRecursive(list, search, min=0, max=None):
	if max == None: max = len(list)

	media = (max + min)/2
	valorMeio = list[media]
	if min > max:
		return -1
	elif valorMeio == search:
		return media
	elif valorMeio < search:
		return binarySearchRecursive(list, search, media+1, max)
	else:
		return binarySearchRecursive(list, search, min, media+1)

list = [1,2,3,9]
print('list', list)

print('Iterative')
for i in list:
	print(i, binarySearch(list, i)) 

print('Recursive')
for i in list:
	print(i, binarySearch(list, i)) 
