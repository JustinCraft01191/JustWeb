import requests
import json

APIKEY = 'd105b014a9444de2bb4136870eb5ac05'
url = 'https://newsapi.org/v2/everything'
header = {"X-Api-Key" : APIKEY}

# Palm Articles
palm_data = requests.get(url=url, params={"q": 'Palm Oil Indonesia', "sortBy" : "popularity"}, headers=header)
palm_data.raise_for_status()
with open("static/articles/palm.json", "w") as f_palm:
    f_palm.write(json.dumps(palm_data.json(), indent=4))

# Coconut Articles
coconut_data = requests.get(url=url, params={"q": 'coconut oil exports imports', "sortBy" : "popularity"}, headers=header)
coconut_data.raise_for_status()
with open("static/articles/coconut.json", "w") as f_coconut:
    f_coconut.write(json.dumps(coconut_data.json(), indent=4))



