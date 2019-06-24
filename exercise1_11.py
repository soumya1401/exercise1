words = input()
words = list(words.split(' '))
print(words)
words = sorted(set(words))
for words in words:
    print(words, end=' ')