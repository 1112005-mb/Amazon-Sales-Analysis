import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#importing df from the csv file
df = pd.read_csv("Amazon Sale Report.csv")
print(df)
print(df.info())
print(df.shape)
print(df.head())
print(df.tail())
print(pd.isnull(df))
print(pd.isnull(df).sum())
print(df.dropna(inplace=True))
print(df.shape)
print(pd.isnull(df).sum())
print(df.head())
print(df.tail())
#changing data type of ship postal code 
df["ship-postal-code"] = df["ship-postal-code"].astype(int)
print(df["ship-postal-code"].dtype)
print(df["Qty"].sum())
print(df.describe())
print(df.describe(include="object"))
ax=sns.countplot(x="Size",data=df)
for bars in ax.containers:
    ax.bar_label(bars)
print(ax)
plt.show()
#Mostly people buy the Medium size
#courier status 
ax=sns.countplot(x="Courier Status",data=df,hue="Status")
for bars in ax.containers:
    ax.bar_label(bars)
print(ax)
plt.show()
#most of the orders are shipped by the courier 
df["Category"] = df["Category"].astype("str")
print(df["Category"].dtype)
c_d=df["Category"] 
plt.figure(figsize=(10,6))
print(plt.hist(c_d,bins=30,edgecolor="red"))
plt.xticks(rotation=90)
plt.show()
#most of the orders are from the t shirt category 
check_B2B =df["B2B"].value_counts()
print(check_B2B)
plt.pie(check_B2B, labels=check_B2B, autopct="%1.1f%%")
plt.show()
#maximum 99.2% are the retailers and 0.8% are the wholesalers 
#scatter plot
x_data=df["Category"]
y_data=df["Size"]
plt.scatter(x_data, y_data)
plt.xlabel("Category")
plt.ylabel("Size")
plt.title("Available size")
plt.show()
plt.figure(figsize=(12,8))
sns.countplot(data=df,x="ship-state")
plt.xlabel("State")
plt.ylabel("Order_count")
plt.title("Distribution of state")
plt.show()