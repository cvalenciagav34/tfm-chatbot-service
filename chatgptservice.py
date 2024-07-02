# import the OpenAI Python library for calling the OpenAI API
import openai

def getResponse(text):
    try:
        openai.api_key = "sk-proj-GzqCHxRc36sv1lvs9vGxT3BlbkFJS6X6qaF4WAbOhl6E8m7t"
        completion = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "system", "content": "You are a helpful assistant designed to help me in travel plans."},
                {"role": "user", "content": text}
                ]
        )
        return completion.choices[0].message.content
    except Exception as exception:
        print(exception)
        return "error"