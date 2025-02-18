import logging

from dotenv import load_dotenv
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from longchain import get_chat_llm
from tools.google_search import google_search
from tools.twitter import post_tweet

load_dotenv()

class Agent:
    def run(self):
        print("Running the agent start")
        chat_llm = get_chat_llm()

        tools = [google_search, post_tweet]

        agent_prompt = get_prompt()
        agent = create_tool_calling_agent(chat_llm, tools, agent_prompt)
        agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
        response = agent_executor.invoke({"input": "帮忙搜索下 kobe 的一句名言，并将其发布到 twitter"})

        logging.log(logging.INFO, response)
        print("Running the agent end")


def get_prompt():
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", """
            你是一个搜索和自动发帖的助手。
            如果用户要求生成一篇文章时，请调用‘search_and_contents’函数和‘find_similar_and_contents’函数。
            如果用户要求搜索什么时，请调用‘google_search’函数。
            如果用户需要发布帖文到 twitter 时，请调用‘post_tweet’函数。
            请以友好的语气回答问题。"""),
            MessagesPlaceholder("chat_history", optional=True),
            ("user", "{input}"),
            MessagesPlaceholder("agent_scratchpad")
        ]
    )
    return prompt
