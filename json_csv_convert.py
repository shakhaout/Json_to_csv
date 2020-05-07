import json
import csv
import ast
import pandas as pd
import numpy as np

### For nested Json file with same length

def get_leaves(item, key=None):
    if isinstance(item, dict):
        leaves = {}
        for i in item.keys():
            leaves.update(get_leaves(item[i], i))
        return leaves
    elif isinstance(item, list):
        leaves = {}
        for i in item:
            leaves.update(get_leaves(i, key))
        return leaves
    else:
        return {key : item}
        
        
        
with open('file_name.txt','rb') as f_input:
    json_data = json.load(f_input)

fieldnames = set()

for entry in json_data:
    fieldnames.update(get_leaves(entry).keys())
    
    
df = pd.DataFrame.from_dict(json_data['this is the intended dictionary name inside the json file'])  

DF = []
for i,row in df.iteritems():
    if i=='intended column name where another json file is existed':
        pass
    else :
        b = pd.DataFrame(df[i].tolist())
        b.rename(columns={b.columns.values[0]:i},inplace=True)
    DF.append(b)

DFF = pd.concat(DF,axis=1).sort_index().reset_index(drop=True)
DFF

### upto this the json file is converted to a dataframe

######################################################################################################################


#### this portion for the column where another nested json file is existed, so to converted this portion as below

ss = []
for i in range(len(df['intended column name where another json file is existed'])):
    a=ast.literal_eval(df['intended column name where another json file is existed'][i]['inside the json the dictionary name under which the data are'])
    ss.append(a)
ss

fieldnames = set()

for entry in ss:
    fieldnames.update(get_leaves(entry).keys())
    
    
with open('csv_file_name.csv', 'w', newline='',encoding='utf8') as f_output:
    csv_output = csv.DictWriter(f_output, fieldnames=sorted(fieldnames))
    csv_output.writeheader()
    csv_output.writerows(get_leaves(entry) for entry in ss)

csv_file_df = pd.read_csv('csv_file_name.csv')


dff = pd.concat([DFF,csv_file_df],axis=1) ## concatenation of the two dataframe

##finally the csv file of the whole json file
dff.to_csv(r'csv_file_name.csv')
################################### END ###########################################


####Another type of file

with open('json_file_name.txt','rb') as f_input:
    json_data = json.load(f_input)

fieldnames = set()

for entry in json_data['dictionary_name']['dictionary_name']:        ###If the main file is under multiple dictionary
    fieldnames.update(get_leaves(entry).keys())
    
    
with open('elastic.csv', 'w', newline='',encoding='utf8') as f_output:
    csv_output = csv.DictWriter(f_output, fieldnames=sorted(fieldnames))
    csv_output.writeheader()
    csv_output.writerows(get_leaves(entry) for entry in json_data['dictionary_name']['dictionary_name'])
    

df = pd.read_csv('csv_file_name.csv',encoding='utf-8')

##### This portion for the column inside where another json data is existed

xy=ast.literal_eval(df_elastic['column_name_where another json file existed'][0])
xy


for i in range(len(df['column_name_where another json file existed'])):
    df['column_name_where another json file existed'][i]=ast.literal_eval(df_elastic['column_name_where another json file existed'][i])

p_time = []
for i in range(len(df_elastic['column_name_where another json file existed'])):
    v = df['column_name_where another json file existed'][i]['the dict name which we needed from the json column']
    p_time.append(v)
 
 
del df['column_name_where another json file existed']
df['the dict name which we needed from the json column'] = p_time

df.to_csv(r'final_csv_file_name.csv')
