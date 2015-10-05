def quickSort(list, left=0, right=None):
    if right == None: right = len(list)-1

    stack = []
    stack.append((left,right))

    #Main loop to pop and push items until stack is empty
    while stack:      
        pos = stack.pop()
        right, left = pos[1], pos[0]
        piv = partition(list,left,right)
        #If items in the left of the pivot push them to the stack
        if piv-1 > left:
            stack.append((left,piv-1))
        #If items in the right of the pivot push them to the stack
        if piv+1 < right:
            stack.append((piv+1,right))    

def quickSortRecursive(list, start=0, end=None):
  if end == None : end = len(list)-1

  if start < end:
    p = partition(list, start, end)
    quickSort(list, start, p - 1)
    quickSort(list, p + 1, end)

def partition(array, begin, end):
    pivot = begin
    for i in range(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot

l1 = [4,1,9,7,0]
l2 = list(l1)
print('List',l1)

quickSort(l1)
print('Iterative',l1)

quickSortRecursive(l2)
print('Recursive',l2)