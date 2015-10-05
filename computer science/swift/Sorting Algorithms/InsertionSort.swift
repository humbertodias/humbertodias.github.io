//
//  InsertionSort.swift
//  helloWorld
//
//  Created by tux on 9/27/15.
//  Copyright © 2015 tux. All rights reserved.
//

import Foundation


func insertionSort(inout list: Array<Int>) {
    
    var x, y, key : Int
    
    for (x = 0; x < list.count; x++) {
        
        //obtain a key to be evaluated
        key = list[x]
        
        //iterate backwards through the sorted portion
        for (y = x; y > -1; y--) {
            
            if (key < list[y]) {
                
                //remove item from original position
                list.removeAtIndex(y + 1)
                
                //insert the number at the key position
                list.insert(key, atIndex: y)
                
            }
            
        }
        
    }
    
}


//a simple array of unsorted integers
var numberList : Array<Int> = [8, 2, 10, 9, 11, 1, 7, 3, 4]
print("List" ,numberList)
insertionSort(&numberList)
print("SortedList", numberList)