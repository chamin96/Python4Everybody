try:
    file_handle = open('intro.txt')
except:
    print('Error opening file!')
    quit()

word_bank = dict()

for line in file_handle:
    line = line.rstrip()
    words = line.split()
    for word in words:
        word_bank[word] = word_bank.get(word, 0) + 1

# print(word_bank)

# find the most common word
maximum_value = -1
most_common_word = None

for k, v in word_bank.items():
    if maximum_value < v:
        maximum_value = v
        most_common_word = k # save most common word

print(most_common_word, maximum_value)