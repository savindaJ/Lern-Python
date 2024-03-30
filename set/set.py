set = {"hello", "world", "hello", "world", "hello", "world"}
print(set)  # {'world', 'hello'} - no duplicates using map data structure 
print(type(set))  # <class 'set'>
set.add("python")
print(set)  # {'world', 'hello', 'python'} hash function
set.remove("world")
print(set)  # {'hello', 'python'}
setTwo = {"hello", "world", "python", "java", "c++"}
z = set.union(setTwo)
print(z)  # {'world', 'hello', 'python', 'java', 'c++'}
s = set | setTwo
print(s)  # {'world', 'hello', 'python', 'java', 'c++'}
# c = set-setTwo
# print(c)  # {'hello'}
print('hello' in set)  # False