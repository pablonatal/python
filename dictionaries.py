
# DICTIONARY is a bunch of values in a single “variable”
# Dictionary literals use curly braces and have a list of key : value pairs


#Make the phone book:
phonebook = {'Andrew Parson':8806336, \
'Emily Everett':6784346,\
'Peter Power':7658344, \
'Lewis Lame':1122345}

print phonebook

#Add the person 'Gingerbread Man' to the phonebook:
phonebook['Gingerbread Man'] = 1234567
print phonebook

# Didn't think I would give you
# my real number now, would I?
del phonebook['Andrew Parson']
print phonebook

# Check if an element exists in dict
print 'Andrew Parson'' in phonebook


print phonebook.get('Andrew Parson', 0) # 0 is default value is element is not found

# List all values
phonebook.values()
# List all keys
phonebook.keys()
