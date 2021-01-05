file_name = 'intro.txt'

try:
    file_handle = open(file_name)
except:
    print('Error opening file!')
    exit()


word_bank = dict()

for line in file_handle:
    line = line.rstrip()
    words = line.split()
    for w in words:
        word_bank[w] = word_bank.get(w, 0) + 1

# print top 10 most common words in the text
print(sorted([(v, k) for k, v in word_bank.items()], reverse=True)[:10])