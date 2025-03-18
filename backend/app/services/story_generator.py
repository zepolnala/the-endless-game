import openai
import os

def generate_story(user_message: str):
    openai_api_key = os.getenv("OPENAI_API_KEY")
    
    if not openai_api_key:
        raise ValueError("La API Key de OpenAI no está configurada correctamente.")

    client = openai.OpenAI(api_key=openai_api_key)
    
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": user_message}]
    )
    
    return {"response": response.choices[0].message.content}
