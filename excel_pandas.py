import pandas as pd
import numpy as np
import openai
import os
from dotenv import load_dotenv
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI


load_dotenv()

openai.api_key = os.getenv('PROJECT_API_KEY')

excel_data_df = pd.read_excel('import_ekonometria.xls.xlsx', sheet_name='Arkusz1')

print(excel_data_df)