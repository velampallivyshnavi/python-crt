from collections import deque
queue=deque()
queue.append('a')
queue.append('b')
queue.append('c')
print("queue after enqueuing:",queue)
first=queue.popleft()
print("dequeued element:",first)
print("queue after dequeuing:",queue)
if not queue:
    print("queue is empty")
else:
    print("queue is not empty")
print("front element:",queue[0])
