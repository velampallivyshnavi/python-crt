class stack():
    def __init__(self):
        self.stack=[]
    def push(self,data):
        self.stack.append(data)
        print("elements is added")
    def pop(self):
        if self.isempty():
            print("stack is empty")
        else:
            self.stack.pop()
            print("element is removed")
    def peek(self):
        length=len(self.stack)
        print(f"peek element is {self.stack[length-1]}")
    def display(self):
        self.stack.reverse()
        for i in self.stack:
            print(i)
stack=stack()
stack.push(100)
stack.push(50)
stack.push(30)
stack.display()
stack.peek()