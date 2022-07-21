# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 13:31:31 2020

@author: PNatal01
"""

output_name = "output_dict"
dict = Data

# Setting current working directory
dir_path='C:/Users/PNatal01/OneDrive - Dentsu Aegis Network/CRUZ ROJA/06. Dia No Violencia contra la Mujer/'
os.chdir(dir_path)
print("Current Working Directory " , os.getcwd())

##############################################################################################################

# Export to CSV

import csv

w = csv.writer(open(output_name+".csv", "w"))
for key, val in dict.items():
    w.writerow([key, val])
    
    
#save dictionary to json file
#If you want to save a dictionary to a json file

import json

json = json.dumps(dict)
f = open(output_name+".json","w")
f.write(json)
f.close()


# save dictionary to text file (raw, .txt)
# You can save your dictionary to a text file using the code below:

f = open(output_name+".txt","w")
f.write( str(dict) )
f.close()

# save dictionary to a pickle file (.pkl)
# The pickle module may be used to save dictionaries (or other objects) to a file. The module can serialize and deserialize Python objects.

import pickle
dict = {'Python' : '.py', 'C++' : '.cpp', 'Java' : '.java'}
f = open("file.pkl","wb")
pickle.dump(dict,f)
f.close()