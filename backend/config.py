import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    COINMARKETCAP_API_KEY = "YOUR_COINMARKETCAP_API_KEY"
    OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"

    # CoinMarketCap API Endpoints
    CMC_BASE_URL = "https://pro-api.coinmarketcap.com/v1"
    CRYPTO_METRICS_URL = f"{CMC_BASE_URL}/cryptocurrency/quotes/latest"
    CRYPTO_NEWS_URL = f"{CMC_BASE_URL}/content/posts/latest"

    PRICE_API_URL = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
    HISTORICAL_API_URL = "https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/historical"
    # RAG Configuration
    VECTOR_STORE_PATH = r"\backend\rag\vector_store"
    HISTORICAL_DATA_PATH = r"\backend\rag\historical_data.csv"

    #News API KEY
    NEWS_API_KEY= "YOUR_NEWS_API_KEY"
    # Cache Settings
    CACHE_TTL = 300  # 5 minutes
    #Reddit APIs
    REDDIT_CLIENT_ID="YOUR_REDDIT_CLIENT_ID"
    REDDIT_CLIENT_SECRET="YOUR_REDDIT_CLIENT_SECRET"
    REDDIT_USER_AGENT = "YOUR_REDDIT_USER_AGENT_NAME"
