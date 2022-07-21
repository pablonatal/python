# A list element can be any Python object - even another list
# A list can be empty

# Create a list from string
abc = 'With three words'
stuff = abc.split()

abc = 'With-three-words'
stuff = line.split('-')


#Define a list
cats = ['Tom', 'Snappy', 'Kitty']
print cats

# Check if element exists
print 9 in cats
print 'Tom' in cats

# Loop / iterate
friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends :
    print 'Happy New Year:',  friend
print 'Done!'


#Meta info
type(cats)
dir (cats)

# Modify a list
cats[1] = 'Hippy'
print cats

# length
print len(cats)

#Append
cats.append('Catherine')
print cats

#Delete
del cats[1]
print cats

# Sort Normal and Reversed order
cats.sort()
cats.sort(reverse=True)


>>> nums = [3, 41, 12, 9, 74, 15]
>>> print len(nums)
6
>>> print max(nums)
74
>>> print min(nums)
3
>>> print sum(nums)
154
>>> print sum(nums)/len(nums)
25

# The range function returns a list of numbers that range from zero to one less than the parameter
>>> print range(4)
[0, 1, 2, 3]

