from ibm_watson import PersonalityInsightsV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from os.path import join, dirname
import json

authenticator = IAMAuthenticator('W0dHJK7UL6B4LDaIM7124Gt50CSssoVOjMkXhrj7dnq1')
personality_insights = PersonalityInsightsV3(
    version='2017-10-13',
    authenticator=authenticator
)

personality_insights.set_service_url('https://api.eu-gb.personality-insights.watson.cloud.ibm.com')

with open(join(dirname(__file__), './myfile.txt'),encoding="utf-8") as profile_json:
    print(profile_json)
   
    profile = personality_insights.profile(
        profile_json.read(),
        'application/json',
        content_type='text/plain',
        consumption_preferences=True,
        raw_scores=True
    ).get_result()
print(json.dumps(profile, indent=2))
