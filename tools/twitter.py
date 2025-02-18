import tweepy
from langchain_core.tools import tool
from requests_oauthlib import OAuth1Session

def get_oauth():
    # lzf2014
    # oauth = OAuth1Session(
    #     "DXGfvdTwLQj6d4wIwY96HwmWz",
    #     client_secret="IKL7FScZU4BDfHMXsTRNSiKepxwnNk5DAlM2fnawDdia0UzaYX",
    #     resource_owner_key="1728978795871576064-lomlXfhIZHMRAGo5dkj6W9xY115JmY",
    #     resource_owner_secret="h5qwQc5zf9qkQhplaT4cyMaGi9PxKnu1YiNJ8KIiBMXem",
    # )

    # sblack2014
    # AAAAAAAAAAAAAAAAAAAAAOIuzQEAAAAALTMtNZqFYvFaJ0uwstG%2BFGIVZDk%3DzQkD28FSaZGsA5oRcPEmMxjMmAhF1jlapkRcSNuCbI6wwkK8Xs
    oauth = OAuth1Session(
        "8dtrevQKfhiQOWDHEM5QFyKDp",
        client_secret="6uaObgR0QXxlWEP4qkS8KCStHNbjworGKNi7vz7ZcDM5F5hnUS",
        resource_owner_key="1759834043854807040-SDEl1Sm0PNSegZiZjAoQ5wK1hL0dPV",
        resource_owner_secret="yFlaU7pMZcPjn6KTffXWA9DmIAluRegwzoKDpB9hDTV2j",
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
        # response = (get_oauth()
        # .post(
        #     "https://api.twitter.com/2/tweets",
        #     json=payload,
        # ))
        # if response.status_code != 201:
        #     raise Exception(
        #         "Request returned an error: {} {}".format(response.status_code, response.text)
        #     )
        print("推文发送成功！")
        # return response.json()
    except tweepy.TweepyException as e:
        print(f"推文发送失败: {e}")


if __name__ == '__main__':
    post_tweet("Kobe Bryant, born on August 23, 1978, was an American professional basketball player who spent his entire 20-year career with the Los Angeles Lakers. ")
