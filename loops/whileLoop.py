x = [10,20,30,40,50,60,70,80,90,100]

while 50 in x: # while 50 is in the list
    x.remove(50) # remove 50 from the list
    
print(x)

while x: # while x is not empty
    print(x.pop()) # remove the last element of the list and print it   