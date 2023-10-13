import argparse
import typing
import openai
import os
import requests
from PIL import Image
from io import BytesIO
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv('PROJECT_API_KEY')

def generate(description : str) -> dict:
    res = openai.Image.create(
        prompt = description,

        n=1,

        size='1024x1024',
    )
    return res['data'][0]['url']

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="This program is creating images biased by your command"
    )
    parser.add_argument("-d", "--description", help="desctiption of image which is going to be created")
    args = parser.parse_args()
    description = args.description 
    url1 = generate(description) 
    
    response = requests.get(url1, stream=True)

    Image.open(response.raw).save('created_image.png')

