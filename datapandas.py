from ibm_watson import PersonalityInsightsV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import pandas as pd
import matplotlib as mpl
import seaborn as  sns
from os.path import join, dirname
import json
import csv

authenticator = IAMAuthenticator('')
personality_insights = PersonalityInsightsV3(
    version='2017-10-13',
    authenticator=authenticator
)

personality_insights.set_service_url('https://api.eu-gb.personality-insights.watson.cloud.ibm.com')

with open(join(dirname(__file__), './myfile.txt'),encoding="utf-8") as profile_json:
    print(profile_json)
   
    profile = personality_insights.profile(
        profile_json.read(),
        accept='text/csv',
        content_type='text/plain',
        #csv_headers=True,
        consumption_preferences=True,
        raw_scores=True
    ).get_result()
    
profile2 = profile.content
cr = csv.reader(profile2.decode('utf-8').splitlines())
my_list = list(cr)
for row in my_list:
    print(row)
print(type(profile2))

print((profile))
##df=pd.read_csv(profile)
##print(df.head())
##print(json.dumps(profile, indent=2))
##details=json.dumps(profile, indent=2)
##print(type(details))
with open('analysis.csv', 'a') as json_file:
    
    csvwriter = csv.writer(json_file)
    for row in my_list:
        csvwriter.writerow(row)
        
        
   


