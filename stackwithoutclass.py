from collections import deque
stack=deque()
stack.append('a')
stack.append('b')
stack.append('c')
print("queue after enqueuing:",stack)
top=stack.pop()
print("popped element:",top)
print("stack after popping:",stack)
if not stack:
    print("stack is empty")
else:
    print("stack is not empty")
print("top element:",stack[-1])
"write a python program to take the length of queue as a input from the user and the elements by using enqueue method and print the elements from the queue and remove the elements one by one from the queue and check whether the queue is empty or not and print the front peek and rare peek "
