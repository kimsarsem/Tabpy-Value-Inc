import pandas as pd

#file_name = pd.read_csv('file.csv')  <---- format of read_csv

data = pd.read_csv('transaction.csv')

data = pd.read_csv('transaction.csv',sep=";")
data.head()

#summary of data
data.info()

#working with calculations

#defining variables
CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberItemsPurchased = 6

#mathematicals operations on tableau
ProfitPerItem = SellingPricePerItem - CostPerItem
ProfitPerTransaction = NumberItemsPurchased * CostPerItem
SellingPriceTransaction = NumberItemsPurchased * SellingPricePerItem

#costpertransaction column calculation
#costpertrans = costperitem * numitemspurchased
# variable = df['coname']

#adding formula to columns that already exist
CostPerItem = data['CostPerItem']
NumberofItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem * NumberofItemsPurchased

#adding new column to dataframe
data['CostPerTransaction'] = CostPerTransaction

data.info()

#sales per transaction
data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

#profit = sales - cost
data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

#markup = (sale - cost)/cost
data['Markup'] = (data['SalesPerTransaction'] - data['CostPerTransaction'])/data['CostPerTransaction']
data['Markup'] = data['ProfitPerTransaction']/data['CostPerTransaction']
data.head()

#round() function to round numbers up
roundmarkup = round(data['Markup'], 2)
data['Markup'] = roundmarkup
data['Markup']

#year month and date are each in seperate columns!
#combining data fields
##my_date = 'Day' + '-' + 'Month' + '-' + 'Year'
#change columns type
my_date = data['Day'].astype(str) + '-' + data['Month'].astype(str) + '-' + data['Year'].astype(str)

data['my_date'] = my_date
data['my_date']

#using iloc to view specific columns/rows
data.iloc[0] #views rows with index 1
data.iloc[1] #views rows with index 2
data.iloc[2] #views rows with index 3

data.iloc[0:3] #first 3 rows
data.iloc[-5:] #last 5 rows

data.head(5) # brings in first 5 rows
data.iloc[:,2] #brings in all rows for column 2
data.iloc[4,2] #brings in 4th row for column 2

#client keywords is 3 columns in one! Let's break it up using split
#new_var = column.str.split('sep', expand = True) --> expand means it'll split through every comma not just the first one
split_col = data['ClientKeywords'].str.split(',', expand = True)

data.info()

#create new columns for the split columns in Client Keywords
data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthofContract'] = split_col[2]

data[['ClientAge','ClientType','LengthofContract']]

#using the replace function
data['ClientAge'] = data['ClientAge'].str.replace('[','')
data['LengthofContract'] = data['LengthofContract'].str.replace(']','')

data[['ClientAge','ClientType','LengthofContract']]

#using the lower function to hange item description to lower case
data['ItemDescription'] = data['ItemDescription'].str.lower()

data['ItemDescription']

#HOW TO MERGE DATAFILES
#bringing in a new data set
sdata = pd.read_csv('value_inc_seasons.csv',sep=';')

sdata

#merging files: merge_df = pd.merge(df_old, de_new, on = 'key')   <--- Key is the name of the linking field
data = pd.merge(data, sdata, on = 'Month')

data

#drop columns: year, month, date, clientkeywords
#df = df.drop('colname',axis = 1) <--- axis = 1 means you're dropping a column
data = data.drop(['Month', 'Year', 'Day', 'ClientKeywords'], axis = 1)

data.info()

#export into a csv
data.to_csv('ValueInc_Cleaned.csv', index = False) #index = false means we don't want to include index