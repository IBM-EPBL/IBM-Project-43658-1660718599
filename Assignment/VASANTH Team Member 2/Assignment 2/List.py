class MyList:
  arr = []

  def insertAtPos(self, pos, val):
    self.arr.insert(pos, val)

  def print(self):
    print(self.arr)

  def delete(self, val):
    self.arr.remove(val)

  def insertAtEnd(self, val):
    self.arr.append(val)

  def sort(self):
    self.arr.sort()

  def pop(self):
    self.arr.pop()

  def  reverse(self):
    self.arr = self.arr[:: -1]
mylist = MyList()
choice=""
while choice != "exit":
  choice = int(input("\nSelect operations from \n 1. Insert Element at nth position\t 2. Print List \t 3. Delete \n 4. Insert Elemrnt at end of the list \t 5.  Sort \t 6. Pop \n 7. Reverse \t\t 8.  Exit \n"))
  if choice == 1:
    val = int(input("Enter a Number : "))
    pos = int(input("Enter Position : " ))
    mylist.insertAtPos(pos, val)

  elif choice == 2:
    mylist.print()

  elif choice == 3:
    val = int(input("Enter value to Delete: "))
    mylist.delete(val)

  elif choice == 4:
    val = int(input("Enter value to Insert : "))
    mylist.insertAtEnd(val)

  elif choice == 5:
    mylist.sort()

  elif choice == 6:
    mylist.pop()

  elif choice == 7:
    mylist.reverse()

  elif choice == 8:
    choice = 'exit'
