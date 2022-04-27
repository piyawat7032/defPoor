# -- coding: utf-8 --
#                            -
#                         _ooOoo_
#                        o8888888o
#                        88" . "88
#                        (| -_- |)
#                        O\  =  /O
#                     ____/'---'\____
#                   .'  \\|     |//  '.
#                  /  \\|||  :  |||//  \
#                 /  _||||| -:- |||||_  \
#                 |   | \\\  -  /'| |   |
#                 | \_|  '\'---'//  |_/ |
#                 \  .-\__ '-. -'__/-.  /
#               ___'. .'  /--.--\  '. .'___
#            ."" '<  '.___\_<|>_/___.' _> \"".
#           | | :  '- \'. ;'. _/; .'/ /  .' ; |
#           \  \ '-.   \_\_'. _.'_/_/  -' _.' /
#============'-.'___'-.__\ \___  /__.-'_.'_.-'============
#                         '=--=-'

"""
Spyder Editor

This is a temporary script file.
"""
import random
user_file="konn.csv"
house_file="house.csv"
user_max=0
user_len=0
user_all=0
house_len=0
i=0
import csv
with open(house_file, newline='', encoding='utf-8') as f:
    house_len = (sum(1 for row in f))
with open(house_file, newline='', encoding='utf-8') as f:
    reader = csv.reader(f)   
    nameH = []
    for row in reader:
        nameH.append(row)

with open(user_file, newline='', encoding='utf-8') as f:
    row_count = (sum(1 for row in f))-1
    user_all = int(row_count)
    user_len = (row_count-(row_count%house_len))
    user_max = int(((row_count-(row_count%house_len))/house_len))



with open(user_file, newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    userData = []
    
    for row in reader:
        name = row[0]
        sername = row[1]
        tmp=[name,sername]
        userData.append(tmp)
    header = userData[0]
    del userData[0]

compData=[]
z = random.sample(range(0, (user_all)), int(user_all))
for x in range(house_len):
    for y in range(user_max):
        compData.append(userData[z[0]]+nameH[x])
        
        del z[0]
for x in range(user_all-user_len):
    compData.append(userData[z[0]]+nameH[x])
    del z[0]
   
header = header + ["house"]

with open('Sum.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(compData)