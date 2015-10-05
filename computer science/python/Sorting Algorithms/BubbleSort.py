def bubbleSort(list):
  size = len(list)
  for i in range(0,size-1):
    for j in range(i+1, size):
      if list[i] > list[j]:
        aux = list[i]
        list[i] = list[j]
        list[j] = aux
  return list

def bubbleSortRecursive(b, n=None):
	if n == None: n = len(b)
	if n==0: return

	for i in range(0,n-1):

		if b[i+1] < b[i] :
			# swap the two values and scope j as tightly as possible
			j=b[i]
			b[i]=b[i+1]
			b[i+1]=j

	bubbleSortRecursive (b, n-1)

l1 = [4,1,9,7,0]
l2 = list(l1)
print('List',l1)

bubbleSort(l1)
print('Iterative', l1)
bubbleSortRecursive(l2)
print('Recursive',l2)