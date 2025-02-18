from dotenv import load_dotenv
import os

from langchain_openai import ChatOpenAI

def get_chat_llm():
    load_dotenv()
    print(os.getenv("API_KEY"))

    chat_llm = ChatOpenAI(
        api_key=os.getenv("API_KEY"),
        base_url=os.getenv("BASE_URL"),
        model=os.getenv("MODEL"),
    )
    return chat_llm