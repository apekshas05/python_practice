num = [[3,2],5,7]
num1 = num
print(id(num) == id(num1))
num1.append(5)
print(num1)
print(num)
print(id(num) == id(num1))
