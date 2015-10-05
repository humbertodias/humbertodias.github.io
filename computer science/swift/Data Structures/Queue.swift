// Queue

struct Queue<T> {
    var elements = [T]()
    
    mutating func enqueue(element: T){
        elements.insert(element, atIndex: 0)
    }
    
    mutating func dequeue() -> T {
        return elements.removeLast()
    }
    
    func front() -> T {
        return elements[elements.endIndex - 1]
    }
    
    func back() -> T{
        return elements[0]
    }
    
    func isEmpty() -> Bool {
        return elements.count == 0 ? true : false;
    }
    
    var size: Int {
        return elements.count
    }
}

var intQueue = Queue<Int>()

intQueue.enqueue(4)
intQueue.enqueue(12981237)
intQueue.enqueue(-666)
intQueue.enqueue(42)

print("isEmpty", intQueue.isEmpty())
print("size", intQueue.size)
print("front",intQueue.front())
print("back",intQueue.back())

print("dequeue",intQueue.dequeue())
print("dequeue",intQueue.dequeue())

print("isEmpty",intQueue.front())
print("dequeue",intQueue.dequeue())
print("dequeue",intQueue.dequeue())

print("isEmpty",intQueue.isEmpty())