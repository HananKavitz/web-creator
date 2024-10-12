from digital_ocean_utils import publish_app
from repo_actions import create_repo, clone_repo, commit_and_push
from llm_services import call_llm

def main(event, context):
    subject = 'food delivery'
    reqeust = (f"Create an html and an embedded css for a website of {subject}. Menubar must be on the left side."
               f" IMPORTANT: Don't explain the code or how to program."
               f" Don't give any prefix explanation and no postfix explanation. Legal HTML and css only!")
    repo_name = call_llm(f'Summarize in two words the request: {subject}', model_name="gpt-3.5-turbo")
    repo_name_short = repo_name.replace(' ', '').lower()

    print(repo_name)

    res = create_repo(repo_name=repo_name_short, description=repo_name)
    clone_repo(repo_name=repo_name_short, repo_url=res['html_url'])
    chat_completion = call_llm(prompt=reqeust, model_name="gpt-4o-mini")

    with open(f'{repo_name_short}/index.html', 'w+') as f:
        f.write(chat_completion)

    commit_and_push(repo_name_short)
    live_url = publish_app(name=repo_name_short.replace('_', ''), repo_url=f'HananKavitz/{repo_name_short}')
    return live_url


if __name__ == '__main__':
    print(main(None, None))

