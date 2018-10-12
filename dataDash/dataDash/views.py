import pandas as pd
import os

#finding all excel files and sheets inside each files

def file_reader(file_name,sheet):
    file_path = os.getcwd()+'/static/data/'+str(file_name)
    print(file_path)

    #loading data into pandas
    data = pd.read_excel(file_path,header=None,sheet_name=sheet)
    for key in data:
     print(data[key][0])
    # print(data)

