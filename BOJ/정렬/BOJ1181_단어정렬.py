n = int(input())

word_list = set()
for _ in range(n):
    word_list.add(input())

words = list(word_list)

words.sort()
words.sort(key = lambda x: len(x))

for w in words:
    print(w)