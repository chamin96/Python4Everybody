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


lst = list()

for k, v in word_bank.items():
    new_tuple  = (v, k)
    lst.append(new_tuple)


print(lst)