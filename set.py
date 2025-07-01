"insert at the end"
def insert_end(self,data):
    new = node(data)
    if not self.head:
       self.head = new
       return
    temp = self.head
    while temp.next:
      temp = temp.next
    temp.next = new