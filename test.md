# data_analysis_python


# Question 1
# Given a game with device id and payment on each day, and given the data on three 
# days, ask to calculate all the payment for each device in these three days.

import numpy as np
import pandas as pd


s1 = pd.DataFrame({"device_id": ["00001", "00003", "00009"], 
					"payment": [20.20, 4.99, 12.5]})
s2 = pd.DataFrame({"device_id": ["00001", "00003", "00009"], 
					"payment": [0, 55.00, 6.50]})
s3 = pd.DataFrame({"device_id": ["00001", "00003", "00009"], 
					"payment": [9.99, 29.99, 0]})

result = pd.concat([s1, s1, s3])
result.sum("payment")
grouped = result.groupby("device_id")
grouped.sum()

--------------------------------------------------------------------------------------
# Question 2
# Suppose on the day of 11/25, players have made none, one, or more payment transactions,
# ask to provice the total payment of each player when total payment is more than $20 and
# user name is not "internal_employee".



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



