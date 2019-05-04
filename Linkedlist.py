

class ListNode:
   def __init__(self, data, next=None):
		self.data = data
		self.next = next

class LinkedList:

 def __init__(self):
       self.head = None

 def getSize(self):
     temp = self.head
     count = 0
     while temp.next is not None:
       temp = temp.next
       count = count + 1
       print(str(count))


 def printNode(self):
    temp = self.head
    while temp is not None:
      print(str(temp.data))
      temp = temp.next


 
 def insert(self,data):
  newNode = ListNode(data)
        if self.head is None:
            self.head = newNode
        else: 
           temp = self.head
           while temp.next is not None:
             temp = temp.next
           temp.next = newNode

 def remove(self,val):
      temp = self.head
      prev = self.head
      while temp is not None:
       if temp.data is val:
         if temp.data == prev.data:
          temp = temp.next
          prev.next = None
          self.head = temp
         else:
          temp = temp.next
          prev.next = temp
       else:
          prev = temp
          temp = temp.next



myList = LinkedList()
val = 1
val_2 = 1;
while val>0:
 print("Press the number regarding what you want to do!\n 1 for adding the element\n 2 for printing the list\n 3 for getting the link size \n 4 for deleting the following node")
 val_1 = input()
	
# Switch case in python.	
 def switch(arg) :
  switcher = {
    1 : 1,
    2 : 2,
    3 : 3,
    4 : 4, 
      
  }

  return switcher.get(arg,"invalid argument")

 number = switch(val_1)

 number = switch(value_1)

 if(number == 1):
  print("Enter the total number of numbers you want to add")
  total_number = input()
  for x in range(0,total_number):
    string = str(x+1) 
    print "Enter the {} number".format(string)
    number = input()
    myList.insert(2,number) 
    val+=1

 elif(number == 2):
  myList.printNode()

 elif(number == 3):
  myList.getSize()

 elif(number == 4):
  print("Enter the number you want to delete")
  value = input()
  myList.remove(val)

           


















