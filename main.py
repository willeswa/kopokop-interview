import pandas as pd
import os, glob

# find and return all csv files in test_data
def get_csv_files():
  os.chdir("./test_data")
  return glob.glob("*.csv")

#group and sort data by number of transactions per customer
def transactions_by_customer_df(file):
  df = pd.read_csv(file)
  df = df.groupby('Customer ID')['Transaction Date'].count().reset_index(
    name='Count').sort_values(['Count'], ascending=False)
  return df

# transform dataframe to python list
def df_to_list_for(df, n):
  return df['Customer ID'].tolist()[0:n]

# return list of customer sorted by credit worthiness
def customers_by_creadit_worthiness(transactions_csv_file_path, n):
  df = transactions_by_customer_df(transactions_csv_file_path)
  return df_to_list_for(df, n)
  


for file in get_csv_files():
  print(customers_by_creadit_worthiness(file, 3))



# Install the requirements in the requirements.txt before testing
  
