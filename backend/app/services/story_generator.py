import openai
import os

def generate_story(user_message: str):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": user_message}]
    )
    return {"response": response["choices"][0]["message"]["content"]}