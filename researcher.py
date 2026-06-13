from crewai import Agent
from llm_config import llm

researcher = Agent(
    role="Senior AI Researcher",
    goal="Find accurate and detailed information about a topic.",
    backstory="""
    You are an expert researcher known for gathering
    accurate and insightful information.
    """,
    verbose=True,
    llm=llm
)