import pandas as pd

# Replace 'your_file.csv' with the actual filename or loop through your files as needed
df = pd.read_csv('Data/daily_sales_data_0.csv')
df2 = pd.read_csv('Data/daily_sales_data_1.csv')
df3 = pd.read_csv('Data/daily_sales_data_2.csv')


# Filter to keep only rows where the product is "Pink Morsels"
df_pink_1 = df[df['product'] == 'pink morsel']
df_pink_2 = df2[df2['product'] == 'pink morsel']
df_pink_3 = df3[df3['product'] == 'pink morsel']

df_pink_1['price_numeric'] = df_pink_1['price'].replace('[\$,]', '', regex=True).astype(float)
total_1 = df_pink_1['price_numeric'] * df_pink_1['quantity']
df_pink_2['price_numeric'] = df_pink_2['price'].replace('[\$,]', '', regex=True).astype(float)
total_2 = df_pink_2['price_numeric'] * df_pink_2['quantity']
df_pink_3['price_numeric'] = df_pink_3['price'].replace('[\$,]', '', regex=True).astype(float)
total_3 = df_pink_3['price_numeric'] * df_pink_3['quantity']
df_pink_1['sales'] = total_1
df_pink_2['sales'] = total_2
df_pink_3['sales'] = total_3

finalDF = pd.concat([df_pink_1, df_pink_2, df_pink_3])
finalDF.drop(columns=['price_numeric','price','quantity'], inplace=True)
print(finalDF)