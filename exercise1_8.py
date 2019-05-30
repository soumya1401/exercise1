string = input("Enter string")
number = int(input("Enter number"))
my_list=[]
for ch in string:
    my_list.append(ch)
print(my_list)

#for i in range(number,len(my_list),number):
 #       my_list.pop(i)
delete_list= list(my_list[number-1::number])
print(delete_list)

for i in delete_list:
    my_list.remove(i)

print(''.join(my_list))
print(my_list)