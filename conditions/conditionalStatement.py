x = 10

if x >= 5: # is new block , has indent (4 spaces) or tab
    print('x is greater than 5')
else:
    print('x is less than 5')
    
marks = 60

if marks >= 75:
    print('A')
    exit() # exit the program
elif marks >= 65:
    print('B')
elif marks >= 55:
    print('C')
elif marks >= 35:
    print('S')
   
   
height = 170 

job = "IT" if height > 180 else "Teacher" # if height > 180, job = "IT", else job = "Teacher" ,  ternary operator
print(job) # Teacher