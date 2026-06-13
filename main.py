from dotenv import load_dotenv
import os
from tavily import TavilyClient
from crewai import Agent, Task, Crew, Process, LLM
from datetime import datetime
from researcher import researcher
from analyst import analyst
from fact_checker import fact_checker

load_dotenv()

tavily = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)


topic = input("Enter a topic to research: ")

search_results = tavily.search(
    query=topic,
    max_results=5
)

web_context = ""

for result in search_results["results"]:
    web_context += f"""
Title: {result['title']}
URL: {result['url']}
Content: {result['content']}
"""

research_task = Task(
    description=f"""
Research the following topic:

{topic}

Use the following web research:

{web_context}

Create a comprehensive research summary including:

- Overview
- Current trends
- Major developments
- Benefits
- Challenges
- Future outlook

Use the provided web information heavily.
""",
    expected_output="A detailed research summary.",
    agent=researcher
)

fact_check_task = Task(
    description="""
    Review the research findings.

    Verify:
    - Accuracy
    - Consistency
    - Unsupported claims
    - Potential misinformation

    Improve reliability while preserving useful information.
    """,
    expected_output="A verified and corrected research summary.",
    agent=fact_checker
)

report_task = Task(
    description="""
    Convert the research findings into a professional report.
    Use clear headings and sections.
    """,
    expected_output="A complete professional report.",
    agent=analyst
)

crew = Crew(
    agents=[researcher, fact_checker, analyst],
    tasks=[research_task, fact_check_task, report_task],
    process=Process.sequential,
    verbose=True
)

result = crew.kickoff()

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

filename = f"reports/report_{timestamp}.md"

with open(filename, "w", encoding="utf-8") as file:
    file.write(str(result))

print(f"\nReport saved to: {filename}")

print("\n")
print("=" * 80)
print("FINAL REPORT")
print("=" * 80)
print(result)