from crewai import Agent
from llm_config import llm

analyst = Agent(
    role="Research Analyst",
    goal="Convert research findings into a professional report.",
    backstory="""
    You are an experienced analyst who transforms
    raw research into structured reports.
    """,
    verbose=True,
    llm=llm
)