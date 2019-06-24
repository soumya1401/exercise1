sentence = input()

count_upper = 0
count_lower =0
for i in sentence:
    if i.isupper():
        count_upper +=1
    if i.islower():
        count_lower +=1
    else:
        pass

print("UPPER CASE", count_upper)
print("LOWER CASE", count_lower)