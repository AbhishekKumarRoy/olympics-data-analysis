# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file is stored in the variable path

#Code starts here

# Data Loading (Step 1)
data = pd.read_csv(path)
data.rename(columns = {"Total": "Total_Medals"}, inplace = True)
data.head(10)



# Summer or Winter (Step 2)
data["Better_Event"] = np.where(data["Total_Summer"] > data["Total_Winter"], "Summer", "Winter")
data["Better_Event"] = np.where(data["Total_Summer"] == data["Total_Winter"], "Both", data["Better_Event"])
better_event = data["Better_Event"].value_counts().index.values[0]
print(better_event)



# Top 10 (Step 3)
top_countries = data[["Country_Name","Total_Summer", "Total_Winter","Total_Medals"]]
top_countries = top_countries[: -1]

# Defining function
def top_ten(data, col):
    country_list = []
    country_list = list((data.nlargest(10, col)["Country_Name"]))
    return country_list


# Calling the function and creating a variable common
top_10_summer = top_ten(top_countries, "Total_Summer")
top_10_winter = top_ten(top_countries, "Total_Winter")
top_10 = top_ten(top_countries, "Total_Medals")

common = list(set(top_10_summer) & set(top_10_winter) & set(top_10))
print(common)



# Plotting top 10 (Step 4)
summer_df = data[data["Country_Name"].isin(top_10_summer)]
winter_df = data[data["Country_Name"].isin(top_10_winter)]
top_df = data[data["Country_Name"].isin(top_10)]


# Bar plot
# For summer
plt.figure(figsize=(12, 5))
plt.bar(summer_df["Country_Name"], summer_df["Total_Summer"])
plt.xlabel("Countries")
plt.ylabel("Total Summer Medals")
plt.title("Top 10")
plt.show()

# For Winter
plt.figure(figsize=(12, 5))
plt.bar(winter_df["Country_Name"], summer_df["Total_Winter"])
plt.xlabel("Countries")
plt.ylabel("Total Winter Medals")
plt.title("Top 10")
plt.show()

# For both events
plt.figure(figsize=(12, 5))
plt.bar(top_df["Country_Name"], summer_df["Total_Medals"])
plt.xlabel("Countries")
plt.ylabel("Total Medals")
plt.title("Top 10")
plt.show()



# Top Performing Countries (Step 5)
# For summer
summer_df["Golden_Ratio"] = summer_df["Gold_Summer"] / summer_df["Total_Summer"] 
summer_max_ratio = summer_df["Golden_Ratio"].max()
summer_country_gold = summer_df.loc[summer_df['Golden_Ratio'].idxmax(),'Country_Name']
print(summer_country_gold)

# For winter
winter_df["Golden_Ratio"] = winter_df["Gold_Winter"] / winter_df["Total_Winter"] 
winter_max_ratio = winter_df["Golden_Ratio"].max()
winter_country_gold = winter_df.loc[winter_df['Golden_Ratio'].idxmax(),'Country_Name']
print(winter_country_gold)

# For top 10
top_df["Golden_Ratio"] = top_df["Gold_Total"] / top_df["Total_Medals"] 
top_max_ratio = top_df["Golden_Ratio"].max()
top_country_gold = top_df.loc[top_df['Golden_Ratio'].idxmax(),'Country_Name']
print(top_country_gold)



# Best in the world (Step 6)
data_1 = data[: -1]
data_1["Total_Points"] = data_1["Gold_Total"]*3 + data_1["Silver_Total"]*2 + data_1["Bronze_Total"]

most_points = data_1["Total_Points"].max()
best_country = data_1.loc[data_1["Total_Points"].idxmax(), "Country_Name"]
print(best_country)



# Plotting the best (Step 7)
best = data[data["Country_Name"] == best_country]
best.reset_index(drop = True, inplace = True)
best = best[["Gold_Total", "Silver_Total", "Bronze_Total"]]

# Stacked bar plot
plt.figure(figsize = (12, 5))
best.plot.bar(stacked = True)
plt.xlabel("United States")
plt.ylabel("Medals Tally")
plt.xticks(rotation = 45)
plt.show()



