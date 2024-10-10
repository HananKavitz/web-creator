from openai import OpenAI
import os
from digital_ocean_utils import publish_app
from repo_actions import create_repo, clone_repo, commit_and_push


def main(event, context):
    repo_name = 'hanan_repo'
    res = create_repo(repo_name=repo_name, description='some stupid description')
    clone_repo(repo_name=repo_name, repo_url=res['html_url'])
    client = OpenAI(
        # This is the default and can be omitted
        # api_key=os.environ.get("OPENAI_API_KEY"),
        api_key=os.environ.get('OPENAI_TOKEN')
    )
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "create an html for a  website of cat lovers",
            }
        ],
        model="gpt-3.5-turbo",
    )

    index = chat_completion.choices[0].message.content
    with open(f'{repo_name}/index.html', 'w+') as f:
        f.write(index)

    commit_and_push(repo_name)
    live_url = publish_app(name=repo_name.replace('_', ''), repo_url=f'HananKavitz/{repo_name}')
    return live_url


if __name__ == '__main__':
    print(main(None, None))
