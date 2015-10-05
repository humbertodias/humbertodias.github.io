import Foundation

func bubbleSort(inout l: Array<Int>){
    
    var z, passes, key: Int
    
    for x in 0..<l.count{
        
        passes = (l.count - 1) - x;
        
        //use shorthand "half-open" range operator
        for y in 0..<passes {
            
            key = l[y]
            
            //compare and rank values
            
            if (key > l[y + 1]) {
                z = l[y + 1]
                l[y + 1]=key
                l[y]=z
            }
            
        }
        
    }
    
}


//a simple array of unsorted integers
var numberList : Array<Int> = [8, 2, 10, 9, 11, 1, 7, 3, 4]
print("List" ,numberList)
bubbleSort(&numberList)
print("SortedList", numberList)

