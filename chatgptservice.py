# import the OpenAI Python library for calling the OpenAI API
import openai
from dotenv import load_dotenv
import os
import json

def getResponse(text):
    try:
        with open('config.json', 'r') as config_file:
            config = json.load(config_file)
        api_key_json = config.get('api_key_chatgpt')
        load_dotenv()
        api_key = os.getenv('api_key_chatgpt',api_key_json)
        openai.api_key = api_key
        completion = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "system", "content": "You are a helpful assistant designed to help me in travel plans in Medellín."},
                {"role": "user", "content": text}
                ]
        )
        return completion.choices[0].message.content
    except Exception as exception:
        print(exception)
        return "error"