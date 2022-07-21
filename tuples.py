
months = ('January','February','March','April','May','June',\
'July','August','September','October','November','December')

print "ALL ELEMENTS FROM TUPLE"
print months 
print " "
print "ONE BY ONE FROM TUPLE"
a = 0
while a < len(months):
    a = a + 1
    print months[a-1]

	
# Comparison
x = (5, 1, 3)
if (6, 0, 0) > x : print "TRUE!"          # Sólo esta es verdad 
if (4, 100, 200) > x : print "TRUE!"
if (0, 1000, 2000) > x : print "TRUE!"
if (5, 0, 300) > x : print "TRUE!"
   



