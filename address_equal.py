# This script compares two files with wallet addresses for matches

import json
import re

# list of my addresses 
my_addr_path='C:/Users/PlebeyBob/Desktop/my_addresses.txt'
# list of addr for comparison in json
json_adds="C:/Users/PlebeyBob/Desktop/bsc.json"

# reading files
f1 = open(my_addr_path, 'r') 

with open(json_adds, "r", encoding='utf-8') as f2:
    f2_data = json.load(f2)


f1_data = f1.readlines()
for line in f1_data:
    line = re.sub('\\n$', '', line)
    for json_txt in f2_data:
        if json_txt==line:
            print(line)

# closing files
f1.close()                                      
f2.close()