with open('data.txt') as file:
    read = file.readline()
    print(read)
    
# open new context manager and automatically close the file
# using 'with' statement file read , database connection, network connection