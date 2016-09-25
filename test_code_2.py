# environmet setting: sublime 2, Anaconda2
# the libraries I used are listed below

import pandas as pd 
import numpy as np 
from pandas import Series
from itertools import combinations
import memory_profiler 
import datetime

# use datetime model to calculate running time
# this is the initial time
start = datetime.datetime.now()

#-----------------------------------------------------------------------
# input files from my desktop
users = pd.read_csv("C:\Users\XiaoQ\Desktop\users.csv")
orders = pd.read_csv("C:\Users\XiaoQ\Desktop\orders.csv")

# date0 means the running time for reading csv files
date0 = datetime.datetime.now()






#-----------------------------------------------------------------------
# deliverable 1
# merge two files with the key "user_id"
merged = pd.merge(users, orders, on = "user_id")

# call groupby with the columns "product_id" and "state"
# compute the size of products that purcahsed 
purchased_num = merged.groupby(["product_id", "state", "gender"]).size()

# unstack the table "purchased_num"
# preparing for calculating percentage of gender distribution
unstacked = (purchased_num.unstack())

# fillin np.nan with value "0"
unstacked.fillna(0, inplace = True)

# calculate the total purchased_num
unstacked["purchased_num"] = unstacked["male"] + unstacked["female"]

# caluclate the percentage of gender distribution
unstacked["male_per"] = unstacked["male"] / unstacked["purchased_num"]
unstacked["female_per"] = unstacked["female"] / unstacked["purchased_num"]

# print out the result with given "product_id"
# users should change "product_id" here
result = unstacked.query("product_id == 1")

# sort the "purchased_num" with decending order
# the top 3 results
# users should change number N here
print result.sort_values(by = "purchased_num", ascending = False).head(3)

# the running time till finishing problem 1
date1 = datetime.datetime.now()









#--------------------------------------------
# deliverable 2a
# call groupby with the columns "sources" and "state"
# size the users acquied through that channel
users_num = merged.groupby(["state", "source"]).size()

# reset index of users_num
# change the automatic index which is 0 into "users_num"
users_num = users_num.reset_index().rename(columns = {0: "users_num"})

# the number of users acquired through the specific channel in the specific state
# users should change the state and source here
print users_num[users_num.state == "AK"][users_num.source == "fb"]

# the running time till finishing problem 2a
date2a = datetime.datetime.now()









# --------------------------------------------
# deliverable 2b
# call groupby with the columns "state" and "source"
# calculate the sum of order_value
# reset the index of value_sum
value_sum = merged["order_value"].groupby([merged["state"], merged["source"]]).sum().reset_index()

# select an specific state and print the order_value with ascending order
# users should change the specific state there
# the result shows the ranking of all four sources
print value_sum[value_sum.state == "AK"].sort_values(by = "order_value", ascending = False)

# the running time till finishing problem 2b
date2b = datetime.datetime.now()









#--------------------------------------------
# deliverable 3a
# call groupby with the columns "state", "gender" and "source"
# calculate the size of "user_id" group
# the acquired_num is the numbers of user aqcuired
acquired_num = merged["user_id"].groupby([merged["state"], merged["gender"], merged["source"]]).size()

# reset the index of acquired_num
# change the automitic 0 into index "acquired_num"
acquired_num = acquired_num.reset_index().rename(columns = {0: "acquired_num"})

# output the information in 3 specific states
# users should change the 3 states here
state1 = acquired_num[acquired_num.state == "AK"]
state2 = acquired_num[acquired_num.state == "CA"]
state3 = acquired_num[acquired_num.state == "NY"]

# concat the 3 states' information 
# sort the data with "acquired_num" descending order
# it shows the best advertising channel to acquire users
concated = pd.concat([state1, state2, state3]).sort_values(by = "acquired_num", ascending = False)

# give the specific gender
# users should change the gender here
print concated[concated.gender == "male"]

# the running time till finishing problem 3a
date3a = datetime.datetime.now()







#-----------------------------------------------------
# deliverable 3b

# reset the index of merged table
merged = merged.reset_index()

# call groupby with "order_value" column
# calculate the size of "order_id" and name it "order_size"
# add the new column "order_size" to "merged" table
merged["order_size"] = merged["order_id"].groupby(merged["order_value"]).size()

# fillin the np.nan with value "0"
merged.fillna(0, inplace = True)

# calculate the revnue with "order_value" * "order_size" (the total order_value)
# add the new column "revene" to "merged" table
merged["revenue"] = merged["order_value"] * merged["order_size"]

# sum the revenue by states
a = (merged["revenue"].groupby(merged["state"])).sum().reset_index()

# calculate the top 3 states with highest revenue
# the highest revenue making products equals to the sume of top 3 states' revenue
print a.sort_values(by = "revenue", ascending = False).head(3).sum()


# the running time after finishing problem 3b
date3b = datetime.datetime.now()

diff0 = (date0 - start).seconds
diff1 = (date1 - date0).seconds
diff2a = (date2a - date1).seconds
diff2b = (date2b - date2a).seconds
diff3a = (date3a - date2b).seconds
diff3b = (date3b - date3a).seconds

# the endding time
end = datetime.datetime.now()
diff = (end - start).seconds

print diff0
print diff1
print diff2a
print diff2b
print diff3a
print diff3b
print diff

# mprof run <script>
# mprof plot

#---------------------------------------------------
# instruction 2
# I use datatime to calculate the running time for each process. 
# But the whole program finished in 8.1 seconds. It will work if
# the file is largers or the process is much complicated.

# I used the package "memory_profiler" to calculate the memory usage.
# Unfortanatly, it doesn't work.

#---------------------------------------------------------
# instrctions 3
# I would use all the data. Instead, I would partition the
# data into several tables or databases. By managing the 
# relationship between tables and databases, Python could 
# speed up the time of processing records.
