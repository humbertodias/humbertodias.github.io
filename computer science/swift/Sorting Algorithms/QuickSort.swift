// QuickSort Algorithm


func quickSort(newArray: [Int])->Array<Int> {
    
    // newArray is an array of ints
    
    var less = [Int]()
    var equal = [Int]()
    var greater = [Int]()
    
    if newArray.count > 1{
        let pivot = newArray[0]
        
        for x in newArray {
            if x < pivot{
                less.append(x)
            }
            if x == pivot {
                equal.append(x)
            }
            if x > pivot {
                greater.append(x)
            }
        }
        return (quickSort(less)+equal+quickSort(greater))
        
    }
        
    else {
        return newArray
    }
    
}

var randomNumbers = [42, 12, 88, 62, 63, 56, 1, 77, 88, 97, 97, 20, 45, 91, 62, 2, 15, 31, 59, 5]
var x = quickSort(randomNumbers)
print("List", randomNumbers)
print("SortedList", x)