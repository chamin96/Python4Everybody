fname = input('Enter file name: ')

try:
    file_handle = open(fname)
except:
    print('Error opening file!')
    exit()

words_dict = dict()

for line in file_handle:
    words = line.split()
    for word in words:
        words_dict[word] = words_dict.get(word, 0) + 1


big_count = None
big_word = None

for key, value in words_dict.items():
    if big_count is None or big_count < value:
        big_count = value
        big_word = key

print(big_word, big_count)