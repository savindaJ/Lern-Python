file = open('data.txt')

read = file.readline()
print(read)

file.close() # close the file

f = open('data.txt', 'r') # open file in read mode
print(f.read())

write = open('write.txt', 'w') # open file in write mode
write.write('hello world\n')
write.write('this is write file !')
write.close()

writed = open('write.txt', 'r')
print(writed.read())
