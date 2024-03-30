x = [10,20,30,40] # list
print(x) # 10
x.append(50) # add 50 to the list
print(x) # 10,20,30,40,50
x.insert(1,15) # insert 15 to the 1st index
print(x) # 10,15,20,30,40,50
x.remove(30) # remove 30 from the list
print(x) # 10,15,20,40,50
x.pop() # remove the last element
print(x) # 10,15,20,40
print(x[1]) # 15
print(x[1:3]) # 15,20 slice the list
x.extend([50,60,70]) # add multiple elements to the list
print(x) # 10,15,20,40,50,60,70

print(10 in x) # True check if 10 is in the list return boolean
print(10 not in x) # False check if 10 is not in the list