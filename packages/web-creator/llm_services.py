import os

from openai import OpenAI


def call_llm(prompt, model_name):
    client = OpenAI(
        # This is the default and can be omitted
        # api_key=os.environ.get("OPENAI_API_KEY"),
        api_key=os.environ.get('OPENAI_TOKEN')
    )
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model=model_name,
    )

    return chat_completion.choices[0].message.content