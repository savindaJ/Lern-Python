while True :
    print("Enter a number")
    num = int(input())
    if num == 0:
        break # exit the loop   
    print("You entered: ", num)
    
# we can use for loop to iterate over a list, tuple, string, dictionary, set, etc.

dict = {'name': 'John', 'age': 25, 'job': 'Developer'}
for key in dict:
    print(key, dict[key])   