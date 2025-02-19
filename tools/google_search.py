import os

import langchain_core.tools
from dotenv import load_dotenv
from langchain_core.tools import Tool
from langchain_google_community import GoogleSearchAPIWrapper


@langchain_core.tools.tool
def google_search(
    message: str
):
    """
    Search message from google.

    Parameters:
    - message (str): The search query.
    """
    load_dotenv()
    search = GoogleSearchAPIWrapper()

    tool = Tool(
        name="google_search",
        description="Search Google for recent results.",
        func=search.run,
    )
    return tool.run(message)

if __name__ == '__main__':
    print(google_search("What is the capital of France?"))

