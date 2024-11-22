# Twitter Params
MAX_RESULTS = 50
BASE_TWEET_RETRIEVAL_URL = "https://api.twitter.com/2/tweets/search/recent"
BASED_TWEET_URL = "https://twitter.com/user/status/TWEET_ID"
TWEET_FILEDS = "id,text,author_id,created_at"
TWEET_SEPARATOR = "------------"

# OpenAI Model
OPENAI_MODEL_NAME = "gpt-4o-mini"
TEMPERATURE = 0

NO_RESULT_MESSAGE = """
Unfortunately, we could not find any tweets from influencers on X (previously ‘Twitter’) that are relevant to your question.
Please try another question.
"""