#Program 1

import math
numbers = input("Enter numbers whose factorial is needed separating with comma:")
my_list= numbers.split(",")
my_list = list(my_list)
list_output =[]
for each in my_list:
    factorial = math.factorial(int(each))
    list_output.append(str(factorial))

print(','.join(list_output))


#Program 2
'''numbers = input("enter numbers separated with comma")
my_list = numbers.split(',')
print(my_list)
list_output =[]

for each in my_list:
    each = int(each)
    fact = 1
    for i in range(1, each+1):
        fact = fact*i
    list_output.append(str(fact))
print(','.join(list_output))'''





