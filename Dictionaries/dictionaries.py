x = {'id': '1', 'name': 'John'}
print(x['name']) # John
print(x.get('name')) # John
print(x.get('age')) # None
x['age'] = 25 # add age to the dictionary
print(x)
print(x.keys()) # id, name, age
del x ['age'] # remove age from the dictionary
print(x) # id, name

y = {
    'address': ['123 Main St', '456 Elm St'],
    'name': 'Jane',
    'age': 30
}

z = y['address']
z.append('789 Maple St') # can append to the list but not to primary dictionary
print(y) # address, name, age