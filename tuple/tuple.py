name = ('savinda',20,'Sri Lanka', 'Kandy') # group of values
print(name)
print(type(name))

x = name[0]
print(x)
print(name[1])
print(name[2])
print(name.count('savinda'))

n , age , country , city = name
print(n,age,country,city)

v = list(name)
print(v)