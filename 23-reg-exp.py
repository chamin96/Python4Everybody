# without reg exps
# file_handle = open('mbox.txt')
# for line in file_handle:
#     line = line.rstrip()
#     if line.find('From:') >= 0:
#         print(line)

file_handle = open('mbox.txt')
for line in file_handle:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)

# with reg exps
# import re

# file_handle = open('mbox.txt')
# for line in file_handle:
#     line = line.rstrip()
#     if re.search('From:', line):
#         print(line)

import re

file_handle = open('mbox.txt')
for line in file_handle:
    line = line.rstrip()
    if re.search('^From:', line):
        print(line)
    y = re.findall('\S+@+\S+', line)
    print(y)
