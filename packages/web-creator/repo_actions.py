import os
import requests


def create_repo(repo_name, description):
    data = {"name": repo_name,
            "description": description,
            "private": "false",
            "visibility": "public"}
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {os.environ.get('GITHUB_TOKEN')}",
        "X-GitHub-Api-Version": "2022-11-28"
    }

    res = requests.post('https://api.github.com/user/repos', json=data, headers=headers)

    if res.status_code != 201:
        print(res)
        exit(0)

    ret = res.json()
    print(ret)

    return ret


def clone_repo(repo_name, repo_url):
    os.system(f'mkdir {repo_name}')
    os.system(f'cd {repo_name}')
    os.system(f'git clone {repo_url}')


def commit_and_push(repo_name):
    os.system(f'cd {repo_name} && dir && git add . && git commit -m "first commit" &&  git push -u origin main')