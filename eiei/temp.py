# -- coding: utf-8 --
"""
Spyder Editor

This is a temporary script file.
"""


import csv

with open('konn.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        name = row[0]
        sername = row[1]
        print(name + sername)






#OKGREEN = '\033[92m'
#var_user_file="/tmp/user.csv"
#user_file="konn.txt"
#file = open(user_file, encoding="utf8")
#for x in file :
#    print (x)

#print (OKGREEN + 'All user add done.')