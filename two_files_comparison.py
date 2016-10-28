import pandas as pd
from tabulate import tabulate
shortage = pd.read_excel("P:\Echo\Shortage & Overage_ comaprison_14_44\py_overage&shortage\Shortage.xlsx")
overage = pd.read_excel("P:\Echo\Shortage & Overage_ comaprison_14_44\py_overage&shortage\Overage.xlsx")


date = "2016-10-23"

total_shortage = shortage[~shortage["HAWB"].isin(overage["HAWB"])]
today_shortage_JFK = total_shortage[(total_shortage["Shortage_Date"] == date) & (total_shortage["Gate_Way"] == "JFK")]
today_shortage_LAX = total_shortage[(total_shortage["Shortage_Date"] == date) & (total_shortage["Gate_Way"] == "LAX")]

total_overage = overage[~overage["HAWB"].isin(shortage["HAWB"])]
today_overage_LAX = total_overage[(total_overage["Overage_Date"] == date) & (total_overage["Gate_Way"] == "LAX")]
today_overage_JFK = total_overage[(total_overage["Overage_Date"] == date) & (total_overage["Gate_Way"] == "JFK")]

Total_balance = pd.merge(shortage, overage, on = "HAWB", how = "inner")
# print(Total_balance[(Total_balance["Overage_Date"] == date)])


print("JFK shortage on", date, "is", today_shortage_JFK["HAWB"].count())
print(tabulate(today_shortage_JFK, headers = [" ", "Shortage_Date", "HAWB", "Gate_Way"], tablefmt = "rst"))
# print(tabulate(today_shortage_LAX, headers = [" ", "Shortage_Date", "HAWB", "Gate_Way"]))
# print("LAX shortage on", date, "is", today_shortage_LAX["HAWB"].count())

# print(today_overage_LAX)
# print("LAX overage on", date, "is", today_overage_LAX["HAWB"].count())
# print(today_overage_JFK)
# print("JFK overage on", date, "is", today_overage_JFK["HAWB"].count())

