"""
Prints out a list of filenames in strings, separated by columns in terminal. 
Copy and paste into sheep_list.js (within brackets[])
Creates a .csv file with all filenames
"""

import glob
import datetime 
import pandas as pd
import csv

print('Merging...')
# Collect names of all files in data file with .csv extension into a list
files = glob.glob('./*/*.jpeg', recursive = True)

# Removing './' that are included in the file name
for n in files:
    i = files.index(n)
    files[i] = files[i].replace('./','')

print(",".join(list(map(lambda file: "\"" + file + "\"",files))))

### Not needed but for easy reference of all sheep files, exports a .csv of all file names

df = pd.DataFrame(files)

# Receiving today's date
currentDT = datetime.datetime.now()
date = currentDT.strftime("_%Y_%m_%d")

# Exporting data frame as a .csv with today's date appended. 
export = df.to_csv(r'./Master_data'+ date +'.csv', index = None, header=True)
print('Merging complete')
