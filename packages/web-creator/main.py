from digital_ocean_utils import publish_app
from repo_actions import create_repo, clone_repo, commit_and_push
from llm_services import call_llm

def main(event, context):
    subject = 'food delivery'
    reqeust = (f"Create an html and an embedded css for a website of {subject}. Menubar must be on the left side."
               f" IMPORTANT: Don't explain the code or how to program. Legal HTML and css only!")
    repo_name = call_llm(f'Summarize in two words the request: {subject}', model_name="gpt-3.5-turbo").replace(' ', '').lower()
    print(repo_name)

    res = create_repo(repo_name=repo_name, description='some stupid description')
    clone_repo(repo_name=repo_name, repo_url=res['html_url'])
    chat_completion = remove_redundant(call_llm(prompt=reqeust, model_name="gpt-4o-mini"))

    with open(f'{repo_name}/index.html', 'w+') as f:
        f.write(chat_completion)

    commit_and_push(repo_name)
    live_url = publish_app(name=repo_name.replace('_', ''), repo_url=f'HananKavitz/{repo_name}')
    return live_url


def remove_redundant(html):
    lr_striped = html.lstrip('<!DOCTYPE html>')
    both_striped = lr_striped.rstrip('</html>')
    return both_striped


if __name__ == '__main__':
    print(main(None, None))

