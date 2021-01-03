file_name = input("Enter File Name: ")
if len(file_name) < 1 : file_name = "clown.txt" # default text file
print(file_name)

try:
    file_handle = open(file_name)
except:
    print('Error opening file!')
    quit()

word_bank = dict()

for line in file_handle:
    line = line.rstrip()
    words = line.split()
    for word in words:
        # if word in word_bank:
        #     word_bank[word] = word_bank[word] + 1
        # else:
        #     word_bank[word] = 1

        # another way
        word_bank[word] = word_bank.get(word, 0) + 1
        
print(word_bank)