import copy
num = [[3,2],5,7]
num1 = copy.copy(num)
print(id(num[0]) == id(num1[0]))
num.append(10)
num1.append(48)
print(num,num1)
