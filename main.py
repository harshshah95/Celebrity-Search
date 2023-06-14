import os
os.environ["OPENAI_API_KEY"] = ""
from langchain.llms import OpenAI
llm = OpenAI(openai_api_key="OPENAI_API_KEY")