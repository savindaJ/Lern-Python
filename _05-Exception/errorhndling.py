from os import path

if path.exists('data.txt'):
    file = open('data.txt', 'r')
    print(file.read())
    file.close()

try:
    file = open('data.tx', 'r') # use indentation to avoid syntax error
    print(file.read())
    file.close()
except FileNotFoundError as e:
    print(e)
except Exception as e: # catch all exceptions , always at the end
    print(e)
finally:
    # cleanup tasks like closing files, database connections etc.   
    print("Finally block always executes...")
    
print("Program continues...")