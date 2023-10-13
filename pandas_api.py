import pandas as pd
import numpy as np
import openai
import os
from dotenv import load_dotenv
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI


load_dotenv()

openai.api_key = os.getenv('PROJECT_API_KEY')

data_dict = {
    "name": [
        "Maria",
        "Kasia",
        "Ania",
        "Gosia"
    ],
    "date of birth":[
        "20.11.1982",
        "12.06.1995",
        "02.01.2004",
        "02.07.2001"
    ],
    "mail address":[
        "fga@o2.com",
        "wrthj@gmail.com",
        "nhwr@gmail.com",
        "wthjwyj@wp.pl"
    ]
}
df = pd.DataFrame(data_dict)
print(df.head())