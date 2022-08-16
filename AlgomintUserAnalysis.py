import datetime
import json
import matplotlib.pyplot as plt
import re
import numpy as np

def dateParser(date):
    finalDate = re.split('-|:|T', date)
    outputDate = datetime.datetime(int(finalDate[0]), int(finalDate[1]), int(finalDate[2]), int(finalDate[3]), int(finalDate[4]))
    return outputDate

with open('users.json', encoding='utf8') as f:
    users = json.load(f)
    
dates = {"November 2021": 0, "December 2021": 0, "January 2022": 0, "February 2022": 0, "March 2022": 0 , "April 2022": 0, "May 2022": 0, "June 2022": 0, "July 2022": 0}
dates_noKYC = {"November 2021": 0, "December 2021": 0, "January 2022": 0, "February 2022": 0, "March 2022": 0 , "April 2022": 0, "May 2022": 0, "June 2022": 0, "July 2022": 0}

nonKYC = 0
withKYC = 0

for user in users:
    if user["kyc"]:
        withKYC+=1
        time = dateParser(user['createdAt']['$date'])
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
    else:
        nonKYC+=1
        time = dateParser(user['createdAt']['$date'])
        if time.month == 11:
                dates_noKYC["November 2021"]+=1
        if time.month == 12:
                dates_noKYC["December 2021"]+=1
        if time.month == 1:
                dates_noKYC["January 2022"]+=1
        if time.month == 2:
                dates_noKYC["February 2022"]+=1
        if time.month == 3:
                dates_noKYC["March 2022"]+=1
        if time.month == 4:
                dates_noKYC["April 2022"]+=1
        if time.month == 5:
                dates_noKYC["May 2022"]+=1
        if time.month == 6:
                dates_noKYC["June 2022"]+=1
        if time.month == 7:
                dates_noKYC["July 2022"]+=1
            

names_nokyc = list(dates_noKYC.keys())
values_nokyc = list(dates_noKYC.values())

# plt.bar(range(len(dates_noKYC)), values_nokyc, tick_label = names_nokyc)
# plt.title("Users without KYC")


piechart = [withKYC, nonKYC]
txnSum = sum(piechart)

#piechartMain = np.array(piechart)
#labels = ["Users with KYC " + str(round((withKYC/txnSum)*100, 2)) + "%", "Users without KYC " + str(round((nonKYC/txnSum)*100, 2)) + "%"]
#plt.pie(piechart, labels = labels)
#plt.show()

names = list(dates.keys())
values = list(dates.values())

plt.bar(range(len(dates)), values, tick_label = names)
plt.title("Users with KYC")

plt.show()

print("Total number of users: " + str(withKYC + nonKYC))
print("Amount of users with KYC: " + str(withKYC))
print("Amount of users without KYC: " + str(nonKYC))
print("% of users that don't have KYC: " + str(round(100*(nonKYC/(withKYC+nonKYC)), 3)) + "%")

                
        