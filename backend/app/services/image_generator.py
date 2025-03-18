import openai
import os

def generate_image(user_message: str):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    image_response = openai.Image.create(
        prompt=f"Illustration of {user_message}",
        n=1,
        size="1024x1024"
    )
    return {"image_url": image_response["data"][0]["url"]}