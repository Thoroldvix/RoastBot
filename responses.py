import os
import sys

import openai as openai

openai.api_key = os.getenv('OPENAI_API_KEY')


def get_roast_response(user_id):
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt='Напиши креативное оскорбление в стиле шекспира',
            temperature=0.8,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.61
        )
        response_str = response['choices'][0]['text'].replace('"', '')
        return f'{response_str} <:sirO:755463220264960080> <@{user_id}>'
    except Exception as e:
        sys.exit(e)
