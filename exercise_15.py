final_list = []
line = input('enter list of tuples')
while line != '':
    final_list.append(tuple(line.split(',')))
    line = input()
    final_list.sort()
print(final_list)


