
# Get character
s = 'banana'
print s[0]
print s[:]

# Concatenate
r = 'apple'
s = 'banana'
print s+' '+r

# Substring
if 'a' in s :
	print 'Found it!'


# Loop and count
word = 'banana'
count = 0
for letter in word :
    if letter == 'a' : 
       count = count + 1
print count


# length
data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
print len(data)

# Functions: find, substring
atpos = data.find('@')
print atpos

sppos = data.find(' ',atpos)
print sppos

host = data[atpos+1 : sppos]
print host


str.capitalize()
str.center(width[, fillchar])
str.endswith(suffix[, start[, end]])
str.find(sub[, start[, end]])
str.lstrip([chars])

str.replace(old, new[, count])
str.lower() # Converts to lowercase
str.upper() # Converts to uppercase
str.rstrip([chars])
str.strip([chars])
lstrip() #remove whitespace at the right
rstrip() #remove whitespace at the left
strip()  #removes both beginning and ending whitespace

