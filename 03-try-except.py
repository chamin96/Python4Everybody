astr = 'Hello Bob'
try:
    isStr = int(astr)
except:
    isStr = -1

print('First:', isStr)

astr = '123'
try:
    isStr = int(astr)
except:
    isStr = -1

print('Second:', isStr)