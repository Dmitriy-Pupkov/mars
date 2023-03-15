import os

import requests
from dotenv import load_dotenv


load_dotenv()
token = os.getenv('TOKEN')
host = 'http://dialogs.yandex.net'
skill = '4cb7aba2-3928-4df1-aa00-a069d4ba3cdc'
url = f'{host}/api/v1/skills/{skill}/images'
headers = {'Authorization': f'OAuth {token}'}
path = 'cities'
res = {}
for filename in os.listdir(path):
    file = {'file': open(os.path.join(path, filename), 'rb')}
    response = requests.post(url, headers=headers, files=file)
    res[filename] = response.json()['image']['id']
print(res)
