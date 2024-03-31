msg = 'hello , how are you '+str(10)
print(msg)

#c type formatting
message = 'hello %s, your heigth %d cm' % ('john', 180) # %d is a placeholder for integer , %s is a placeholder for string
print(message)

hello = 'hello {} how are you {}'.format('kamal', 10) # {} is a placeholder
print(hello)

#f string formatting
name = 'kamal'
age = 10
msg = f'hello {name} how are you {age}'
print(msg)