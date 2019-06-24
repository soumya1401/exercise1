sentence = input()

count_digit = 0
count_alpha =0
for i in sentence:
    if i.isdigit():
        count_digit +=1
    if i.isalpha():
        count_alpha +=1

print("LETTERS", count_alpha)
print("DIGITS", count_digit)