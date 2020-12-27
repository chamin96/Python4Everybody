fname = input('Enter file name: ')

try:
    fhand = open(fname)
except:
    print('Error! File cannot be opened.')
    quit()


# print lines starting with specific word
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)


# count lines lines starting with specific word
# count = 0

# for line in fhand:
#     if line.startswith('Subject:'):
#         print(line)
#         count += 1

# print('There were', count, 'subject lines in', fname)