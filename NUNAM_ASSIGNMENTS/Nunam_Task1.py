#17MIS0307_PARTHIBAN_S
#importing os
import os
#importing pandas
import pandas as pd
#creating dataframe
nunam_assignment = pd.DataFrame()
#file directory walk in
for file in os.listdir(os.getcwd()):
    #ifcase for searching file ends with .csv
    if file.endswith('.csv'):
        #reading file and appending
        nunam_assignment = nunam_assignment.append(pd.read_csv(file))
#merging into a file
nunam_assignment.to_csv('detail.csv')


#creating dataframe
nunam_assignment = pd.DataFrame()
#file directory walk in
for file in os.listdir(os.getcwd()):
    #ifcase for searching file ends with .csv
    if file.endswith('.csv'):
        #reading file and appending
        nunam_assignment = nunam_assignment.append(pd.read_csv(file))
#merging into a file
nunam_assignment.to_csv('detailVol.csv')


#creating dataframe
nunam_assignment = pd.DataFrame()
#file directory walk in
for file in os.listdir(os.getcwd()):
    #ifcase for searching file ends with .csv
    if file.endswith('.csv'):
        #reading file and appending
        nunam_assignment = nunam_assignment.append(pd.read_csv(file))
#merging into a file
nunam_assignment.to_csv('detailTemp.csv')



