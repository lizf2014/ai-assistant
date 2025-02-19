import logging
import os

from dotenv import load_dotenv
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI

from tools.google_search import google_search
from tools.twitter import post_tweet


def run():
    print("Running start")
    load_dotenv()

    chat_llm = get_chat_llm()

    tools = [google_search, post_tweet]

    prompt = get_prompt()
    agent = create_tool_calling_agent(chat_llm, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
    response = agent_executor.invoke({"input": "帮忙搜索下 kobe 的一句名言，并将其发布到 twitter"})

    logging.log(logging.INFO, response)
    print("Running end")


def get_chat_llm():
    chat_llm = ChatOpenAI(
        api_key=os.getenv("API_KEY"),
        base_url=os.getenv("BASE_URL"),
        model=os.getenv("MODEL"),
    )
    return chat_llm


def get_prompt():
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", """
            你是一个搜索和自动发帖的助手。
            当用户要求生成一篇文章时，请调用‘search_and_contents’函数和‘find_similar_and_contents’函数。
            当用户要求搜索什么时，请调用‘google_search’函数。
            当用户需要发布帖文到 twitter 时，请调用‘post_tweet’函数。
            """),
            MessagesPlaceholder("chat_history", optional=True),
            ("user", "{input}"),
            MessagesPlaceholder("agent_scratchpad")
        ]
    )
    return prompt
