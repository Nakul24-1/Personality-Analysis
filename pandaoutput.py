import pandas as pd
import matplotlib as mpl
import seaborn as  sns
from os.path import join, dirname
import json
from pandas.io.json import json_normalize

df = pd.read_csv("analysis.csv") 

print(df[['facet_anger','facet_anxiety','facet_depression', 'facet_immoderation','facet_self_consciousness','facet_vulnerability'
]])
print(df.T)

##with open('analysis.csv','r') as data2:
##    
##    data=json.load(data2)
##    #print(json_normalize(data))
##    df = pd.DataFrame.from_dict(pd.json_normalize(data), orient='columns')
##    
##    print(df)

