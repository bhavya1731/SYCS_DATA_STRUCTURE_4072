import collections 
#deque help us to pop and push easily
de = collections.deque([1, 2, 3, 3, 4, 2, 4])
#append will add the number in the list from right
de.append(4)
print ("The deque after appending at right is : ") 
print (de)

#appendleft will add the number in the list from left
de.appendleft(6)
print("After appending number from left : ")
print(de)

#pop will remove the number from right hand side in the list
de.pop()
print("after using pop : ")
print(de)

#popleft will remove the number from left hand side in the list
de.popleft()
print ("after using pop left  : ") 
print (de)

#This function returns the first index of the value mentioned in arguments, starting searching from beg till end index.
print ("The number 4 first occurs at a position : ") 
print (de.index(2,0,6))

#This function inserts the value mentioned in arguments(a) at index(i) specified in arguments.
de.insert(4,6)
print ("The deque after inserting 3 at 5th position is : ") 
print (de) 

# using count() to count the occurrences of 3
print ("The count of 3 in deque is : ") 
print (de.count(3))

# using remove() to remove the first occurrence of 3 
de.remove(3)
print ("The deque after deleting first occurrence of 3 is : ") 
print (de) 

#This function is used to add multiple values at the right end of deque. The argument passed is an iterable.
de.extend([4,5,72]) 
print ("The deque after extending deque at end is : ") 
print (de)

#This function will add multiple values from left end of deque
de.extendleft([7,8,9]) 
print ("The deque after extending deque at beginning is : ") 
print (de) 

#This funcrion will reverse the list
de.reverse() 
print ("The deque after reversing deque is : ") 
print (de) 


