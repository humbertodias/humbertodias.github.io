def insertionSort(list):
    for i in range(1, len(list)-1 ):
        value = list[i] 
        j = i-1

        while j >= 0 and list[j] > value:
            list[j+1] = list[j]
            j = j-1

        list[j+1] = value

def insertionSortRecursive(list, i = 0):
	if i > 0:
		insertionSortRecursive(list, i-1)
		temp = list[i]
		j = i-1
		while list[j] > temp and j>=0 :
			a[j+1]=a[j]
			j-=1

		a[j+1]= temp


l1 = [4,1,9,7,0]
l2 = list(l1)

print('List',l1)
insertionSort(l1)
print('Iterative',l1)

insertionSort(l2)
print('Recursive',l2)