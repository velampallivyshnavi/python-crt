"write a python program to take the length of queue as a input from the user and the elements by using enqueue method and print the elements from the queue and remove the elements one by one from the queue and check whether the queue is empty or not and print the front peek and rare peek "

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def front_peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return None

    def rear_peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def display(self):
        print("Queue elements:", self.items)


def main():
    q = Queue()
    
    length = int(input("Enter the length of the queue: "))
    for i in range(length):
        element = input(f"Enter element {i+1}: ")
        q.enqueue(element)

    q.display()

    while not q.is_empty():
        print(f"Front peek: {q.front_peek()}")
        print(f"Rear peek: {q.rear_peek()}")
        removed = q.dequeue()
        print(f"Removed element: {removed}")
        q.display()
        print("Is queue empty?", q.is_empty())
        print()

    print("Queue is now empty.")

if __name__ == "__main__":
    main()
