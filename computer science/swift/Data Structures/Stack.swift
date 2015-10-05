// Stack

struct Stack<T> {
    
    var elems = [T]()
    
    mutating func push(elem: T) {
        elems.append(elem)
    }
    
    mutating func pop() -> T {
        return elems.removeLast()
    }
    
    func peek() -> T {
        return elems[elems.endIndex-1]
    }
    
    var count: Int {
        return elems.count
    }
    func empty() -> Bool{
        return count == 0
    }
}

var int_stack = Stack<Int>()

int_stack.push(1)
int_stack.push(4)
int_stack.push(5)
int_stack.push(-11)

print("count", int_stack.count)
print("peek", int_stack.peek())

while (!int_stack.empty()) {
    print("pop", int_stack.pop())

}
