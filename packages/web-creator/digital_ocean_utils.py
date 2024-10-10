import requests
import os
import json
from time import sleep

def publish_app(name, repo_url):
    data = {
        "spec": {
            "name": name,
            "region": "ams",
            "static_sites": [
                {
                    "name": name,
                    "environment_slug": "html",
                    "github": {
                        "branch": "main",
                        "deploy_on_push": True,
                        "repo": repo_url
                    }
                }
            ]
        }
    }

    headers = {
        "Authorization": f"Bearer {os.environ.get('DIGITAL_OCEAN_TOKEN')}",
        "Content-Type": "application/json"
    }

    res = requests.post('https://api.digitalocean.com/v2/apps', json=data, headers=headers)

    if res.status_code != 200:
        print(res.content['message'])
        exit(1)

    print('sleeping')

    sleep(60)
    res2 = requests.get('https://api.digitalocean.com/v2/apps', headers=headers)
    apps = json.loads(res2.content.decode('ascii'))['apps']
    app = next((x for x in apps if x['spec']['name'] == name), None)
    return app['live_url']