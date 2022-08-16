# monthly-report
Report of Mints, Unlocks and more using Python
## Overview of the scripts

There are 4 scripts in total that are used to generate different reports. The filenames are:

`main.py`, `AlgomintAmountAnalysis.py`, `AlgomintUserAnalysis.py`, and `AlgomintDateAnalyses.py`

## `main.py`

`[main.py](http://main.py)` is one of the most used and helpful script out of all of them. It analyses mints and unlocks done overtime, providing charts and other useful info like average unlock/mint amounts, times taken to complete them, etc.

### Things needed to run the script

1. `transactions.json` - json dump of all of Algomint’s transactions from MongoDB (I used to ask Amit for this info)
2. Libraries: `re`, `json`, `datetime`, `matplotlib`, `numpy`

After all the libraries have been installed, ensure the `transactions.json` file is in the same folder as the script, and run.

## `AlgomintAmountAnalysis.py`

`[AlgomintAmountAnalysis.py](http://AlgomintAmountAnalysis.py)` is a more focused analysis based around understanding the amount of funds moved through Algomint given a certain time period.

### Things needed to run the script

1. `transactions.json` - json dump of all of Algomint’s transactions from MongoDB
2. Libraries: `re`, `json`, `datetime`, `matplotlib`, `numpy`

After all the libraries have been installed, ensure the `transactions.json` file is in the same folder as the script, and run.

**Note**: You will need to manually add certain info to get the latest values into the script.

Parts like: 

```python
datesETH = {"November 2021": 0, "December 2021": 0, "January 2022": 0, "February 2022": 0, "March 2022": 0 , "April 2022": 0, "May 2022": 0}
```

```jsx
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
```

Will need to be altered to add info like the next few months, etc.

So, in the first code block, adding something like `“June 2022”: 0` and in the second one, adding something like : 

`if time.month == 6:
                        datesETH["June 2022"]+=round(float(transaction['invoiceAmount']), 3)`

will get you values for the month of June. This will need to be done for each of the months.

## `AlgomintUserAnalysis.py`

`[AlgomintUserAnalysis.py](http://AlgomintUserAnalysis.py)` is focused around getting more information about our users

### Things needed to run the script

1. `users.json` - json dump of all Algomint user data
2. Libraries: `re`, `json`, `datetime`, `matplotlib`, `numpy`

After all the libraries have been installed, ensure `users.json` is in the same folder as the script and run

**Note:** For creating graphs, follow the instructions mentioned above for `AlgomintAmountAnalysis.py`

## `AlgomintDateAnalysis.py`

`[AlgomintDateAnalysis.py](http://AlgomintDateAnalysis.py)` is focused around getting more information about transactions on a monthly basis

### Things needed to run the script

1. `transactions.json` - json dump of all of Algomint’s transactions from MongoDB
2. Libraries: `re`, `json`, `datetime`, `matplotlib`

After all the libraries have been installed, ensure the `transactions.json` file is in the same folder as the script, and run.

**Note:** For creating graphs, follow the instructions mentioned above for `AlgomintAmountAnalysis.py`. For Unlocks, uncomment the Unlocks section and comment out the Mints section
