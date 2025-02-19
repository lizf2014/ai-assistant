import os

import tweepy
from dotenv import load_dotenv
from langchain_core.tools import tool
from requests_oauthlib import OAuth1Session


def get_oauth():
    load_dotenv()
    oauth = OAuth1Session(
        client_key=os.getenv("TWITTER_CLIENT_KEY"),
        client_secret=os.getenv("TWITTER_CLIENT_SECRET"),
        resource_owner_key=os.getenv("TWITTER_RESOURCE_OWNER_KEY"),
        resource_owner_secret=os.getenv("TWITTER_RESOURCE_OWNER_SECRET"),
    )
    return oauth


@tool("post_tweet")
def post_tweet(message):
    """
    发送推特帖子
    """
    try:
        payload = {"text": message}
        print(payload)
        response = (get_oauth()
        .post(
            "https://api.twitter.com/2/tweets",
            json=payload,
        ))
        if response.status_code != 201:
            raise Exception(
                "Request returned an error: {} {}".format(response.status_code, response.text)
            )
        print("推文发送成功！")
        return response.json()
    except tweepy.TweepyException as e:
        print(f"推文发送失败: {e}")


if __name__ == '__main__':
    post_tweet(
        "Kobe Bryant, born on August 23, 1978, was an American professional basketball player who spent his entire 20-year career with the Los Angeles Lakers. ")
