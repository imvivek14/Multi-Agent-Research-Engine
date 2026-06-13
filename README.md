# 🤖 Multi-Agent Research Engine

An AI-powered research platform built with **CrewAI**, **OpenRouter**, **Tavily**, and **Streamlit** that performs web research, fact-checking, report generation, and document export through a multi-agent workflow.

## 🚀 Features

* 🔍 Real-time web research using Tavily Search
* 🤖 Multi-agent architecture with CrewAI
* ✅ Fact-checking and validation workflow
* 📊 Professional report generation
* 📄 PDF export
* 📝 Markdown export
* 🌐 Streamlit web interface
* 💾 Automatic report storage

---

## 🏗️ Architecture

```text
User Topic
      ↓
Tavily Search
      ↓
Research Agent
      ↓
Fact Checker Agent
      ↓
Analyst Agent
      ↓
Report Generation
      ↓
PDF / Markdown Export
```

---

## 🧠 Agents

### Research Agent

Responsible for gathering and analyzing information from web search results.

### Fact Checker Agent

Validates findings, identifies unsupported claims, and improves reliability.

### Analyst Agent

Transforms verified research into a structured professional report.

---

## 🛠️ Tech Stack

* Python
* CrewAI
* OpenRouter
* Tavily Search API
* Streamlit
* ReportLab
* Git & GitHub

---

## 📸 Dashboard

![Dashboard](screenshots/Dashboard.png)

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/imvivek14/Multi-Agent-Research-Engine.git
cd Multi-Agent-Research-Engine
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the environment

Windows:

```bash
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root:

```env
OPENROUTER_API_KEY=your_openrouter_api_key
TAVILY_API_KEY=your_tavily_api_key
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 📄 Output

The application generates:

* Research reports in Markdown format
* Research reports in PDF format
* Downloadable reports through the Streamlit interface

---

## 🎯 Future Improvements

* Citation tracking
* Multiple report templates
* Research history dashboard
* Database integration
* Team collaboration features
* Cloud deployment

---

## 👨‍💻 Author

**Vivek Surati**

Built as an AI Engineering project demonstrating:

* Multi-Agent Systems
* AI Workflow Orchestration
* LLM Integration
* Web Research Automation
* Streamlit Application Development
