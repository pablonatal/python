#Create a sample from the original file reading N lines where N is an argument

import sys
from itertools import islice

# =========
# READ FILE
# =========

# Open a file to Read
fi = open("C:\Users\pablo.natal\Documents\PROYECTOS\Disney\data\data.txt", "r")
# Open a file to Write
fo = open("C:\Users\pablo.natal\Documents\PROYECTOS\Disney\data\data_sample.txt", "w")

# Read input parameter as number of lines
N = int(sys.argv[1])
try:
    input = int(N)
except ValueError:
    print("Input is not an integer")
	
lines_gen = islice(fi, N)

for lines in lines_gen:
     print fo.write(lines);

	
# Close opened files
fi.close()
fo.close()