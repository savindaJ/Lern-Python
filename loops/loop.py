list = [10,20,35,40,50,7,70,89,90,100]

for i in list: # for each element in the list
    if i % 2 == 0:
        print(i, 'is even')
    else:
        print(i, 'is odd')
        

for i in range(1, 10): # for each element in the range
    print(i)
    
for i,val in enumerate(list): # enumerate() returns index and value
    print(i,val)