import urllib.request, urllib.parse, urllib.error

file_hand =  urllib.request.urljoin('http://data.pr4e.org/romeo.txt')

for line in file_hand:
    print(line.decode().strip())