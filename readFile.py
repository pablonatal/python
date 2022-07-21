
# Method 1 = pre-historic times (Python 1.4)
fp = open('C:\Users\pablo.natal\Documents\PROYECTOS\Disney\data\data.txt')
while 1:
    line = fp.readline()
    if not line:
        break
    print line

# after Python 2.1, we did:
for line in open('C:\Users\pablo.natal\Documents\PROYECTOS\Disney\data\data.txt').xreadlines():
    print line

#before we got the convenient iterator protocol in Python 2.3, and could do:
for line in open('C:\Users\pablo.natal\Documents\PROYECTOS\Disney\data\data.txt'):
    print line

#I've seen some examples using the more verbose:
with open('C:\Users\pablo.natal\Documents\PROYECTOS\Disney\data\data.txt') as fp:
    for line in fp:
        print line

