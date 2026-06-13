from dotenv import load_dotenv
from crewai import LLM
import os

load_dotenv()

llm = LLM(
    model="openrouter/openrouter/auto",
    api_key=os.getenv("OPENROUTER_API_KEY")
)