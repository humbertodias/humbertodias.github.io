""" gets the data using merge sort and returns sorted."""
def mergeSort(data):

  for j in range(1, len(data)):
    j *= 2
    for i in range(0,len(data),j):
      data_1 = data[i:i+(j/2)]
      data_2 = data[i+(j/2):j-i]
      l = m = 0
      while l < len(data_1) and m < len(data_2):
        if data_1[l] < data_2[m]:
          m += 1
        elif data_1[l] > data_2[m]:
          data_1[l], data_2[m] = data_2[m], data_1[l]
          l += 1
      data[i:i+(j/2)], data[i+(j/2):j-i] = data_1, data_2

  return data

def mergeSortRecursive(arr):
    if len(arr) == 1:
        return arr
    
    m = len(arr) / 2
    l = mergeSort(arr[:m])
    r = mergeSort(arr[m:])

    if not len(l) or not len(r):
        return l or r
        
    result = []
    i = j = 0
    while (len(result) < len(r)+len(l)):        
        if l[i] < r[j]:
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            j += 1            
        if i == len(l) or j == len(r):            
            result.extend(l[i:] or r[j:])
            break
        
    return result


l1 = [4,1,9,7,0]
l2 = list(l1)
print('List',l1)

l1 = mergeSort(l1)
print('Iterative', l1)
l2 = mergeSortRecursive(l2)
print('Recursive',l2)