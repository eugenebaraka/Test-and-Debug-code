import pandas as pd
import numpy as np

my_data = pd.read_csv('data/salesdata.csv')
print(my_data.tail())
print(my_data.info())

expected_schema = {'category':object, 'cost':np.float64, 'customer_id':np.int64, 
                   'product_id':np.int64}

#checking if variable is in the dataframe
def schema_checker(df, cols):
  for i in cols:
    if i not in df.columns:
      print(f'column {i} not found')
      return False
    else:
   return True

#checking each variable's data type
def dtype_checker(df, schema):
  for i, j in schema.items():
    if i in df.columns:
      if df[i].dtype != j:
        print(f'column {i} does not match dtype {j}')
        return False
     else:
      return True
    
#function to test nans
def nan_checker(df):
    nan_series = df.isna.sum() #any nans?
    any_nans = (nan_series.sum() > 0)
    
    n_nans = nan.series() 
    nan_cols = list(nan_series[nan_series > 0].index) #varibles with nans
    
    greater_than_50nan = list(nan_series[nan_series / len(df) > 0.5].index)
    
    summary = f'This dataset has {nans} NaN values.\n'
    
    if len(nan_cols) > 0:
      summary += f'tThe NaN values come from {nan_cols}.\n'
 
  
#function to test negative costs
def negative_costs(df):
  if df['cost'].min() < 0:
    print(f'cost cannot be negative')
    return False
  else:
    return True
  
#function to test infinity numbers
def out_of_range(df, cols):
  for i in cols:
    if np.isinf(df[i]):
      summary = np.isinf(df[i]).values.sum()
      print(f'Column {i} contains {summary} infinite values)
      return False
     else:
       return True
                        

            
            
            
def create_dataframe(list1, list2, list3):
            my_df = pd.DataFrame({'col1': list1, 'col2':list2, 'col3':list3})
            return my_df
def test_created_dataframe():
    list1 = 
    list2 =
    list3 = 
            
            
  
  
  

    
