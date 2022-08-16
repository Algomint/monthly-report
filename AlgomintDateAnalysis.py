import datetime
import json
import matplotlib.pyplot as plt
import re

def dateParser(date):
    finalDate = re.split('-|:|T', date)
    outputDate = datetime.datetime(int(finalDate[0]), int(finalDate[1]), int(finalDate[2]), int(finalDate[3]), int(finalDate[4]))
    return outputDate

with open('transactions.json', encoding='utf8') as f:
    transactions = json.load(f)

dates = {"November 2021": 0, "December 2021": 0, "January 2022": 0, "February 2022": 0, "March 2022": 0 , "April 2022": 0, "May 2022": 0, "June 2022": 0, "July 2022": 0}

for transaction in transactions:
    if transaction['txType'] == 'mint' and transaction['status'] == 'COMPLETED':
        time = dateParser(transaction['createdAt']['$date'])
        if time.month == 11:
            dates["November 2021"]+=1
        if time.month == 12:
            dates["December 2021"]+=1
        if time.month == 1:
            dates["January 2022"]+=1
        if time.month == 2:
            dates["February 2022"]+=1
        if time.month == 3:
            dates["March 2022"]+=1
        if time.month == 4:
            dates["April 2022"]+=1
        if time.month == 5:
            dates["May 2022"]+=1
        if time.month == 6:
            dates["June 2022"]+=1
        if time.month == 7:
            dates["July 2022"]+=1
            
print(dates)

names = list(dates.keys())
values = list(dates.values())

plt.bar(range(len(dates)), values, tick_label = names)
plt.title("Mints")

plt.show()

# UNLOCKS

# dates = {"November 2021": 0, "December 2021": 0, "January 2022": 0, "February 2022": 0, "March 2022": 0 , "April 2022": 0, "May 2022": 0, "June 2022": 0, "July 2022": 0}

# for transaction in transactions:
#     if transaction['txType'] == 'unlock' and transaction['status'] == 'COMPLETED':
#         time = dateParser(transaction['createdAt']['$date'])
#         if time.month == 11:
#             dates["November 2021"]+=1
#         if time.month == 12:
#             dates["December 2021"]+=1
#         if time.month == 1:
#             dates["January 2022"]+=1
#         if time.month == 2:
#             dates["February 2022"]+=1
#         if time.month == 3:
#             dates["March 2022"]+=1
#         if time.month == 4:
#             dates["April 2022"]+=1
#         if time.month == 5:
#             dates["May 2022"]+=1
#         if time.month == 6:
#             dates["June 2022"]+=1
#         if time.month == 7:
#             dates["July 2022"]+=1
            
# print(dates)

# names = list(dates.keys())
# values = list(dates.values())

# plt.bar(range(len(dates)), values, tick_label = names)
# plt.title("Unlocks")

# plt.show()