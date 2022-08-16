import json
import datetime
import matplotlib.pyplot as plt
import numpy as np
import re

def dateParser(date):
    finalDate = re.split('-|:|T', date)
    outputDate = datetime.datetime(int(finalDate[0]), int(finalDate[1]), int(finalDate[2]), int(finalDate[3]), int(finalDate[4]))
    return outputDate
    
print()
print("MINTS")
print()

ETHAmounts = []
BTCAmounts = []

ETHMints = 0
BTCMints = 0

ETHTime = []
BTCTime = []

ETHDates = []
BTCDates = []

ethPieMints = 0
btcPieMints = 0
ethPieUnlocks = 0
btcPieUnlocks = 0

with open('transactions.json', encoding='utf8') as f:
    transactions = json.load(f)
    
for transaction in transactions:
    
    if transaction['status'] == 'COMPLETED':
        if transaction['txType'] == 'mint':
            if transaction['assetInbound'] == 'ETH':
                ethPieMints += 1
            if transaction['assetInbound'] == 'BTC':
                btcPieMints += 1
        if transaction['txType'] == 'unlock':
            if transaction['assetOutbound'] == 'ETH':
                ethPieUnlocks += 1
            if transaction['assetOutbound'] == 'BTC':
                btcPieUnlocks += 1
    
    if transaction['status'] == 'COMPLETED' and transaction['txType'] == 'mint':
        if transaction['assetInbound'] == 'ETH':
            time = dateParser(transaction['updatedAt']['$date']) - dateParser(transaction['createdAt']['$date'])
            ETHTime.append(time)
            amount = float(transaction['invoiceAmount'])
            ETHAmounts.append(amount)
            ETHMints += 1
            ETHDates.append(dateParser(transaction['updatedAt']['$date']))
        if transaction['assetInbound'] == 'BTC':
            time = dateParser(transaction['updatedAt']['$date']) - dateParser(transaction['createdAt']['$date'])
            BTCTime.append(time)
            amount = float(transaction['invoiceAmount'])
            BTCAmounts.append(amount)
            BTCMints += 1
            BTCDates.append(dateParser(transaction['updatedAt']['$date']))

print('Average ETH mint amount: ' + str(round(sum(ETHAmounts)/len(ETHAmounts), 6)))
print('Average BTC mint amount: ' + str(round(sum(BTCAmounts)/len(BTCAmounts), 6)))

print("Average time taken for ETH Mint: " + str(sum(ETHTime, datetime.timedelta())/len(ETHTime)))
print("Average time taken for BTC Mint: " + str(sum(BTCTime, datetime.timedelta())/len(BTCTime)))

print ('Number of ETH Mints ' + str(ETHMints))
print('Number of BTC Mints ' + str(BTCMints))

finalETHDates = []
finalBTCDates = []


#Graphs
piechart = [ethPieMints, ethPieUnlocks, btcPieMints, btcPieUnlocks]
txnSum = sum(piechart)

piechartMain = np.array(piechart)
labels = ["ETH Mints " + str(round((ethPieMints/txnSum)*100, 2)) + "%", "ETH Unlocks " + str(round((ethPieUnlocks/txnSum)*100, 2)) + "%", "BTC Mints " + str(round((btcPieMints/txnSum)*100, 2)) + "%", "BTC Unlocks " + str(round((btcPieUnlocks/txnSum)*100, 2)) + "%"]
plt.pie(piechart, labels = labels)
plt.show()

ETHAmounts = []
BTCAmounts = []

ETHMints = 0
BTCMints = 0

ETHTime = []
BTCTime = []

ETHDates = []
BTCDates = []

print()
print("UNLOCKS")
print()

for transaction in transactions:
    if transaction['status'] == 'COMPLETED' and transaction['txType'] == 'unlock':
            if transaction['assetOutbound'] == 'ETH':
                time = dateParser(transaction['updatedAt']['$date']) - dateParser(transaction['createdAt']['$date'])
                ETHTime.append(time)
                amount = float(transaction['invoiceAmount'])
                ETHAmounts.append(amount)
                ETHMints += 1
                ETHDates.append(dateParser(transaction['updatedAt']['$date']))
            if transaction['assetOutbound'] == 'BTC':
                time = dateParser(transaction['updatedAt']['$date']) - dateParser(transaction['createdAt']['$date'])
                BTCTime.append(time)
                amount = float(transaction['invoiceAmount'])
                BTCAmounts.append(amount)
                BTCMints += 1
                BTCDates.append(dateParser(transaction['updatedAt']['$date']))
                
print('Average ETH unlock amount: ' + str(round(sum(ETHAmounts)/len(ETHAmounts), 6)))
print('Average BTC unlock amount: ' + str(round(sum(BTCAmounts)/len(BTCAmounts), 6)))

print("Average time taken for ETH unlock: " + str(sum(ETHTime, datetime.timedelta())/len(ETHTime)))
print("Average time taken for BTC unlock: " + str(sum(BTCTime, datetime.timedelta())/len(BTCTime)))

print ('Number of ETH Unlocks ' + str(ETHMints))
print('Number of BTC Unlocks ' + str(BTCMints))
        