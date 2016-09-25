# data_analysis_python


# Question 1
# Given a game with device id and payment on each day, and given the data on three 
days, ask to calculate all the payment for each device in these three days.

e.g.
Table A for day of 11/22:
device_id payment
00001     20.20
00003     4.99
00009     12.50

Table B for day for 11/23:
device_id  payment
00001     0
00003     55.00
00009     6.5


Table C for days day of 11/24:
device_id   payment
00001     9.99
00003     29.99
00009     0

Answeas:
import numpy as np
import pandas as pd


s1 = pd.DataFrame({"device_id": ["00001", "00003", "00009"], 
					"payment": [20.20, 4.99, 12.5]})
s2 = pd.DataFrame({"device_id": ["00001", "00003", "00009"], 
					"payment": [0, 55.00, 6.50]})
s3 = pd.DataFrame({"device_id": ["00001", "00003", "00009"], 
					"payment": [9.99, 29.99, 0]})

result = pd.concat([s1, s1, s3])
# result.sum("payment")
grouped = result.groupby("device_id")
grouped.sum()

--------------------------------------------------------------------------------------
# Question 2
# Suppose on the day of 11/25, players have made none, one, or more payment transactions,
ask to provice the total payment of each player when total payment is more than $20 and
user name is not "internal_employee".

Table Payment:
user_name           transaction_id    amount
Andy                 18                9.99
Laurie               77                4.99
Ken                  55                4.99
Andy                 88                19.99
Andy                 118               4.99
Laurie               102               9.99
Frank                217               9.99
Laurie               389               9.99
Ken                  270               4.99
Internal_employee    215               29.99



df = pd.DataFrame({"user_name": 
					["Andy", "Laurie", "Ken", "Andy", "Andy", "Laurie", 
					"Frank", "Laurie", "Ken", "Internal_employee"],
					"transaction_id":
					[18, 77, 55, 88, 118, 102, 217, 389, 270, 215],
					"amount": 
					[9.99, 4.99, 4.99, 19.99, 4.99, 9.99, 9.99, 9.99, 4.99, 29.99]})
df = df.drop([9]) # delet "internal_employee"
df = df.groupby("user_name").sum()
df[df["amount"] > 20]



