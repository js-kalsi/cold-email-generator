import os
from dotenv import load_dotenv

load_dotenv()

RESOURCE_PATH =  os.environ.get("RESOURCE_PATH") or './resources/dummy_portfolio.csv'

LLM_MODEL_NAME = os.environ.get("LLM_MODEL_NAME") or "llama-3.3-70b-versatile"
LLM_MODEL_TEMP = int(os.environ.get("LLM_MODEL_TEMP") or 0)

GROQ_API_KEY = os.getenv("GROQ_API_KEY")