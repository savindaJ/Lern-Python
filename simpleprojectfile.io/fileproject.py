file = open('marks.txt','w')

for i in range(100):
    file.write(f'{i}\n')
file.close()

file = open('marks.txt','r')
print(file.read())