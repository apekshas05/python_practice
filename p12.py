import copy
num = [[3,2],5,7]
num1 = copy.deepcopy(num)
num[0].append(7)
print(id(num) == id(num1))
print(id(num[0]) == id(num1[0]))
print(num,num1)
