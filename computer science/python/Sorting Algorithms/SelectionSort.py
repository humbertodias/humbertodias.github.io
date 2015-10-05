def selectionSort(list):
	size = len(list)
	for i in range(size):
		m = i
		for j in range(i, size):
			if list[j] < list[m]:
				m = j
		t = list[i]
		list[i] = list[m]
		list[m] = t

def selectionSortRecursive(array, startIndex=0):
	if startIndex >= len(array)-1:
		return

	minIndex = startIndex
	for index in (startIndex+1, len(array)-1):
		if array[index] < array[minIndex]:
			minIndex = index

	temp = array[startIndex]
	array[startIndex] = array[minIndex]
	array[minIndex] = temp
	selectionSortRecursive(array, startIndex+1)

l1 = [4,1,9,7,0]
l2 = list(l1)

print('List',l1)
selectionSort(l1)
print('Iterative',l1)

selectionSortRecursive(l2)
print('Recursive',l2)