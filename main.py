from openai import OpenAI
import os

def main(event, context):
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
    # print(chat_completion.choices[0].message.content)
    index = chat_completion.choices[0].message.content
    with open('index.html', 'w+') as f:
        f.write(index)

    return index


if __name__ == '__main__':
    print(main(None, None))
