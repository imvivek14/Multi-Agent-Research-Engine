import streamlit as st
from dotenv import load_dotenv
import os
from datetime import datetime

from crewai import Task, Crew, Process
from tavily import TavilyClient

from researcher import researcher
from analyst import analyst
from fact_checker import fact_checker

from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

load_dotenv()

st.set_page_config(
    page_title="Multi-Agent Research Engine",
    page_icon="🤖",
    layout="wide"
)

st.markdown("""
<style>
.main {
    padding-top: 2rem;
}

.stButton > button {
    width: 100%;
    height: 3em;
    font-size: 18px;
    font-weight: bold;
}

.block-container {
    max-width: 1100px;
}

h1 {
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
# 🤖 Multi-Agent Research Engine
### Research • Verify • Analyze • Export

Generate professional research reports using
AI agents, web search, fact-checking, and automated reporting.
""")

with st.sidebar:
    st.title("⚙️ Project Info")

    st.success("3 AI Agents")

    st.write("""
    **Workflow**

    🔍 Researcher

    ✅ Fact Checker

    📊 Analyst

    📄 PDF & Markdown Export
    """)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Agents", "3")

with col2:
    st.metric("Search Engine", "Tavily")

with col3:
    st.metric("Exports", "PDF + MD")

topic = st.text_input(
    "Enter a topic to research",
    placeholder="Artificial Intelligence, Tesla, Quantum Computing..."
)

if st.button("Generate Report"):

    with st.spinner("Researching... Please wait."):

        tavily = TavilyClient(
            api_key=os.getenv("TAVILY_API_KEY")
        )

        search_results = tavily.search(
            query=topic,
            max_results=5
        )

        with st.expander("🔍 View Research Sources"):
            for result in search_results["results"]:
                st.write(f"**{result['title']}**")
                st.write(result["url"])
                st.write("---")
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
            expected_output="A verified research summary.",
            agent=fact_checker
        )

        report_task = Task(
            description="""
Convert the verified research into a professional report.
Use headings and proper structure.
""",
            expected_output="A professional report.",
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

        os.makedirs("reports", exist_ok=True)
        
        filename = f"reports/report_{timestamp}.md"
        

        with open(filename, "w", encoding="utf-8") as file:
            file.write(str(result))
        pdf_filename = f"reports/report_{timestamp}.pdf"

        doc = SimpleDocTemplate(pdf_filename)

        styles = getSampleStyleSheet()

        content = [Paragraph(str(result).replace("\n", "<br/>"), styles["BodyText"])]

        doc.build(content)

        st.success("Report Generated Successfully!")

        st.subheader("Generated Report")

        report_text = str(result)

        st.markdown(report_text)

        st.download_button(
            label="📥 Download Report",
            data=report_text,
            file_name=f"report_{timestamp}.md",
            mime="text/markdown"
            )
        
    with open(pdf_filename, "rb") as pdf_file:
        st.download_button(
        label="📄 Download PDF Report",
        data=pdf_file,
        file_name=f"report_{timestamp}.pdf",
        mime="application/pdf"
    )

st.markdown("---")

st.caption(
    "Built with CrewAI • OpenRouter • Tavily • Streamlit"
)
        
