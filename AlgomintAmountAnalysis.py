import json
import datetime
import matplotlib.pyplot as plt
import numpy as np
import re

def dateParser(date):
    finalDate = re.split('-|:|T', date)
    outputDate = datetime.datetime(int(finalDate[0]), int(finalDate[1]), int(finalDate[2]), int(finalDate[3]), int(finalDate[4]))
    return outputDate

with open('transactions.json', encoding='utf8') as f:
    transactions = json.load(f)

datesETH = {"November 2021": 0, "December 2021": 0, "January 2022": 0, "February 2022": 0, "March 2022": 0 , "April 2022": 0, "May 2022": 0}    
datesBTC = {"November 2021": 0, "December 2021": 0, "January 2022": 0, "February 2022": 0, "March 2022": 0 , "April 2022": 0, "May 2022": 0}

for transaction in transactions:
        if transaction['status'] == 'COMPLETED' and transaction['txType'] == 'mint':
            if transaction['assetInbound'] == 'ETH':
                time = dateParser(transaction['createdAt']['$date'])
                if time.month == 11:
                        datesETH["November 2021"]+=round(float(transaction['invoiceAmount']), 3)
                if time.month == 12:
                        datesETH["December 2021"]+=round(float(transaction['invoiceAmount']), 3)
                if time.month == 1:
                        datesETH["January 2022"]+=round(float(transaction['invoiceAmount']), 3)
                if time.month == 2:
                        datesETH["February 2022"]+=round(float(transaction['invoiceAmount']), 3)
                if time.month == 3:
                        datesETH["March 2022"]+=round(float(transaction['invoiceAmount']), 3)
                if time.month == 4:
                        datesETH["April 2022"]+=round(float(transaction['invoiceAmount']), 3)
                if time.month == 5:
                        datesETH["May 2022"]+=round(float(transaction['invoiceAmount']), 3)
                        
            if transaction['assetInbound'] == 'BTC':
                time = dateParser(transaction['createdAt']['$date'])
                if time.month == 11:
                        datesBTC["November 2021"]+=round(float(transaction['invoiceAmount']), 3)
                if time.month == 12:
                        datesBTC["December 2021"]+=round(float(transaction['invoiceAmount']), 3)
                if time.month == 1:
                        datesBTC["January 2022"]+=round(float(transaction['invoiceAmount']), 3)
                if time.month == 2:
                        datesBTC["February 2022"]+=round(float(transaction['invoiceAmount']), 3)
                if time.month == 3:
                        datesBTC["March 2022"]+=round(float(transaction['invoiceAmount']), 3)
                if time.month == 4:
                        datesBTC["April 2022"]+=round(float(transaction['invoiceAmount']), 3)
                if time.month == 5:
                        datesBTC["May 2022"]+=round(float(transaction['invoiceAmount']), 3)
                        
print(datesETH)
print(datesBTC)


names = list(datesETH.keys())
values = list(datesETH.values())

plt.bar(range(len(datesETH)), values, tick_label = names)

plt.show()
            