r = []
for x in [1,2,3]:
    r.append(x**-1)

data = [x for x in range(5)]
temp = [x for x in range(7) if x in data and x%2==0]
print(temp)

d = {}
for x in enumerate(range(2)):
    d[x[0]] = x[1]
    d[x[1]+7] = x[0]
print(d)

d = {1 : 1, 2 : '2', '1' : 2, '2' : 3}
d['1'] = 2
print(d[d[d[str(d[1])]]])

line = "Lets code"
value = ""
for i in line:
    value += chr(ord(i)+3)
print(value)

L1 = [1, 1.33, 'abc', 0, 'no', None, 'j', True]
val1, val2 = 0, ''
for x in L1:
    if(type(x) == int or type(x) == float):
        val1 += x
    elif(type(x) == str):
        val2 += x
    else:
        break
print(val1, val2)

def foo(x):
    x[0] = ['lets']
    x[1] = ['code']
    return id(x)
q = ['lets', 'code']
print(id(q) == foo(q))

def print_alpha_nums(abc_list, num_list):
    for char in abc_list:
        for num in num_list:
            print(char, num)
    return

print_alpha_nums(['a', 'b', 'c'], [1, 2, 3])

fruit_info = {'fruit': 'apple', 'count': 2, 'price': 3.5}

fruits = {'Apples': 5, 'Oranges': 3, 'Bananas': 4}
fruit_names = [x for x in fruits.keys()]


