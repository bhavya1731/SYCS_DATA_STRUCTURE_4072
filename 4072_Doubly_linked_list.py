#Name  :Bhavya Shah
#Rollno:4072
#Class :SYCS
class Stack():
    def __init__(self):
        self.items = [1,2,3,4]

    def end(self,item):
        self.items.append(item)
        print(item)


    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            return None
    def size(self):
        if self.items:
            return len(self.items)
        else:
            return None

    def display(self):
        for i in self.items:
            print(i)

    def start(self,i):
        self.items.insert(0,i)
    
    def search(self ,a):
        l=self.items
        for i in l :
            if i == a:
                print("found Value : ",a)
                break
        else:
            print("not found")
    
    def traverse(self):
        a=[]
        l=self.items
        for i in l:
            a.append(i)
        print(a)
        



    
s=Stack()
#Inserting the values
s.end(5)
s.end(6)
s.end(7)
s.start(-1)
s.start(-2)
print("search the specific value : ")
s.search(-2)

print("Display the values one by one :")
s.display()
print("peek (End  Value) :",s.peek())
print("treverse the values : ")
s.traverse()





