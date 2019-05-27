string = input("Enter string")
number = int(input("Enter number"))
my_list=[]
for ch in string:
    my_list.append(ch)
print(my_list)

for i in range(number,len(my_list),number):
    my_list.pop(i)
#this loop not proper , need to fix

#print(my_list[::number])

print(''.join(my_list))
print(my_list)