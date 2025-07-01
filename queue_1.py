class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)
        print(f"Element {item} is added")

    def is_empty(self):
        return len(self.items) == 0

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def peek_front(self):
        if self.is_empty():
            return None
        return self.items[0]

    def size(self):
        return len(self.items)

    def display(self):
        print("Queue:", self.items)


# Example usage
queue = Queue()
queue.enqueue(100)
queue.enqueue(50)
queue.enqueue(30)
queue.display()
print("Front item:", queue.peek_front())
print("Dequeued:", queue.dequeue())
queue.display()
