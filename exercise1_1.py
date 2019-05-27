
my_list =[]
for i in range(2000, 3201):
    if i%7==0 and i%5!=0:
        my_list.append(str(i))
sequence = ','.join(my_list)
print(sequence)

