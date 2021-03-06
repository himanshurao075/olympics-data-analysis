# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file is stored in the variable path
data=pd.read_csv(path)
#Code starts here

# Data Loading 
data=data.rename(columns={"Total": "Total_Medals"})
print(data.head(10))
# Summer or Winter
data['Better_Event'] = np.where(data['Total_Summer'] > data['Total_Winter'] , 'Summer', 'Winter') 
data['Better_Event'] =np.where(data['Total_Summer'] ==data['Total_Winter'],'Both',data['Better_Event'])
better_event=data['Better_Event'].value_counts().idxmax()
print(better_event)

# Top 10
top_countries=data[['Country_Name','Total_Summer','Total_Winter','Total_Medals']]
print(top_countries.shape)
top_countries.drop([146],inplace=True)
print(top_countries.shape)
def top_ten(data,col):
    country_list=[]
    country_list= list((data.nlargest(10,col)['Country_Name']))
    return country_list

top_10_summer=top_ten(top_countries,'Total_Summer')
top_10_winter=top_ten(top_countries,'Total_Winter')
top_10=top_ten(top_countries,'Total_Medals')
common=set(top_10_summer).intersection(top_10_winter, top_10)
print(common)
# Plotting top 10'''
summer_df= data[data['Country_Name'].isin(top_10_summer)] 
winter_df= data[data['Country_Name'].isin(top_10_winter)]
top_df= data[data['Country_Name'].isin(top_10)]
print(summer_df)

plt.figure()
plt.xlabel("Country Name")
plt.ylabel("Total Summer Medals")
plt.title("Country Name vs Total Summer Medals")
plt.bar(summer_df['Country_Name'],summer_df["Total_Summer"])

plt.figure()
plt.xlabel("Country Name")
plt.ylabel("Total Winter Medals")
plt.title("Country Name vs Total Winter Medals")
plt.bar(winter_df['Country_Name'],winter_df["Total_Winter"])

plt.figure()
plt.xlabel("Country Name")
plt.ylabel("Total Medals")
plt.title("Country Name vs Total Medal")
plt.bar(top_df['Country_Name'],top_df["Total_Medals"])
# Top Performing Countries
summer_df['Golden_Ratio']=summer_df['Gold_Summer']/summer_df['Total_Summer'] 
summer_max_ratio=max(summer_df['Golden_Ratio'])
summer_country_gold=summer_df.loc[summer_df['Golden_Ratio'].idxmax(),'Country_Name']

winter_df['Golden_Ratio']=winter_df['Gold_Summer']/winter_df['Total_Summer'] 
winter_max_ratio=max(winter_df['Golden_Ratio']) 
winter_country_gold=summer_df.loc[winter_df['Golden_Ratio'].idxmax(),'Country_Name']

top_df['Golden_Ratio']=top_df['Gold_Summer']/top_df['Total_Summer'] 
top_max_ratio=max(top_df['Golden_Ratio']) 
intc=round(top_max_ratio,2)
top_max_ratio=0.40
print(top_max_ratio)
top_country_gold=top_df.loc[summer_df['Golden_Ratio'].idxmax(),'Country_Name']
print(summer_country_gold)

# Best in the world 
data_1=data[:-1]

data_1['Total_Points']=data_1['Gold_Total']*3 + data_1['Silver_Total']*2 + data_1['Bronze_Total'] 


most_points=max(data_1['Total_Points']) 
best_country=data_1.loc[data_1['Total_Points'].idxmax(),'Country_Name']
print(most_points)
print(best_country)

# Plotting the best
best=data[data['Country_Name']==best_country] 
best=best[['Gold_Total','Silver_Total','Bronze_Total']]

best.plot.bar()
plt.xlabel("United States")
plt.ylabel("Medals Tally")
plt.xticks(rotation=45)








