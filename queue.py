class Queue:
    def __init__(self):
        self.items = []
    
    #pushing item into queue
    def enqueue(self, item):
        return self.items.append(item)
    
    #removing item from queue, maintaing FIFO method
    #if length of queue is less than 1 then return none, else remove first item. 
    def dequeue(self):
        if len(self.items) < 1:
            return None
        return self.items.pop(0)
    
    #display the element of queue
    def display(self):
            print(self.items)
    
    #SIze of queue
    def size(self):
        return print(len(self.items))

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

q.display()

q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()

print("After removing element")

q.display()
print("Size of the Queue is \t  : ")
q.size()