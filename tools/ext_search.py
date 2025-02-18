import os

from dotenv import load_dotenv
from exa_py import Exa
from langchain_core.tools import tool


@tool
def search_and_contents(
        query: str,
        include_domains: list[str] = None,
        exclude_domains: list[str] = None,
        start_published_date: str = None,
        end_published_date: str = None,
        include_text: list[str] = None,
        exclude_text: list[str] = None,
):
    """
    Search for webpages based on the query and retrieve their contents.

    Parameters:
    - query (str): The search query.
    - include_domains (list[str], optional): Restrict the search to these domains.
    - exclude_domains (list[str], optional): Exclude these domains from the search.
    - start_published_date (str, optional): Restrict to documents published after this date (YYYY-MM-DD).
    - end_published_date (str, optional): Restrict to documents published before this date (YYYY-MM-DD).
    - include_text (list[str], optional): Only include results containing these phrases.
    - exclude_text (list[str], optional): Exclude results containing these phrases.
    """

    load_dotenv()
    exa = Exa(api_key=os.getenv("EXA_API_KEY"))
    return exa.search_and_contents(
        query,
        use_autoprompt=True,
        num_results=5,
        include_domains=include_domains,
        exclude_domains=exclude_domains,
        start_published_date=start_published_date,
        end_published_date=end_published_date,
        include_text=include_text,
        exclude_text=exclude_text,
        text=True,
        highlights=True,
    )


@tool
def find_similar_and_contents(
        url: str,
        exclude_source_domain: bool = False,
        start_published_date: str = None,
        end_published_date: str = None,
):
    """
    Search for webpages similar to a given URL and retrieve their contents.
    The url passed in should be a URL returned from `search_and_contents`.

    Parameters:
    - url (str): The URL to find similar pages for.
    - exclude_source_domain (bool, optional): If True, exclude pages from the same domain as the source URL.
    - start_published_date (str, optional): Restrict to documents published after this date (YYYY-MM-DD).
    - end_published_date (str, optional): Restrict to documents published before this date (YYYY-MM-DD).
    """
    load_dotenv()
    exa = Exa(api_key=os.getenv("EXA_API_KEY"))
    return exa.find_similar_and_contents(
        url,
        num_results=5,
        exclude_source_domain=exclude_source_domain,
        start_published_date=start_published_date,
        end_published_date=end_published_date,
        text=True,
        highlights={"num_sentences": 1, "highlights_per_url": 1},
    )


tools = [search_and_contents, find_similar_and_contents]
