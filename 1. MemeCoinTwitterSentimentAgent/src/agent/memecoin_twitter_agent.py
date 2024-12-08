import os
import logging
import requests

from typing import List, Any

import constants
from .llm import OpenAILLM

logger = logging.getLogger(__name__)


class MemecoinTwitterAgent:
    def __init__(self) -> None:
        self.model = OpenAILLM()
        self.bearer_token = os.getenv("TWITTER_BEARER_TOKEN")
        self.base_twitter_url = os.getenv("BASE_TWITTER_URL")

    def _extract_tweets(self, memecoin: str) -> List[Any]:
        if not memecoin.startswith("$"):
            memecoin = "$"+memecoin
            
        params = {
            "query": memecoin,
            "max_results": constants.MAX_RESULTS,
            "tweet.fields": constants.TWEET_FILEDS,
        }

        headers = {"Authorization": f"{self.bearer_token}"}

        response = requests.get(
            constants.BASE_TWEET_RETRIEVAL_URL, headers=headers, params=params
        )
        if response.status_code == 200:
            return response.json().get("data", [])
        else:
            print(
                f"Faced error while retrieving tweets for memecoin {memecoin}: {response.status_code}, {response.text}!"
            )
            return []

    def _buil_context(self, tweets: List[Any]) -> str:
        context = ""
        logger.info(f"{tweets[0].keys()}")
        for tweet in tweets:
            tweet_url = constants.BASED_TWEET_URL.replace("TWEET_ID", tweet.get("id"))
            context += f"Tweet Content: {tweet.get("text", "")} \nTweet URL: {tweet_url} \n {constants.TWEET_SEPARATOR} \n"
        logger.info(f"Here is the context: \n {context}")
        return context

    def sentiment_analysis(self, memecoin: str) -> str:
        extracted_tweets = self._extract_tweets(memecoin=memecoin)
        if not extracted_tweets:
            return constants.NO_RESULT_MESSAGE

        llm_context = self._buil_context(tweets=extracted_tweets)
        sentiment = self.model.completions(memecoin=memecoin, context=llm_context)

        return sentiment
