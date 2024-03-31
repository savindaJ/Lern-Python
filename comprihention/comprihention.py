a = [10,20,30,40,50,60,70,80,90,100]
b = a
a.append(110)
print(a)

x = []

for i in a:
    x.append(i)
    
print(x)

z = [ i if i%2==1 else 0 for i in a]
print(z)

def is_odd(n):
    return 'even' if n%2 == 0 else 'odd'

c = [is_odd(i) for i in a] # list comprihention
print(c)

dic = {i:is_odd(i) for i in a} # dictionary comprihention
print(dic)

tuple = (i for i in a) # tuple comprihention
print(tuple)

for i in tuple:
    print(i)