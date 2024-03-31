def get_odd_numbers(upper_bound):
    for i in range(upper_bound):
        if i % 2 != 0:  
            print('odd')
            yield i # yield is a keyword that is used like return, 
                    #except the function will return a generator , create a custom generator
            
x = get_odd_numbers(10) # x is a generator
for i in x: # x is a generator , so we can iterate through it
    print(i)
    
print('-'*30)

for i in x: # now x is empty, because we already iterated through it ,  
            #genarator is a one time use
    print(i)
    
print(x)