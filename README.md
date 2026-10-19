# ✍️ AI Article Writer — Multi-Agent System with CrewAI

An AI-powered article generation system built with **CrewAI** and **Google GenAI**. The project uses specialized AI agents to plan, write, and edit blog articles based on a user-provided topic.

## ✨ Features

- **Content Planning:** Develops an article outline and identifies key points relevant to the topic.
- **AI Article Writing:** Produces a structured article based on the content plan.
- **Editorial Review:** Reviews the draft for clarity, balanced viewpoints, and journalistic writing standards.
- **Multi-Agent Collaboration:** Organizes the content creation workflow into specialized agent roles.
- **Configurable LLM:** Uses a Google AI model configured through CrewAI.
- **Interactive Notebook:** Supports experimentation and testing through Jupyter Notebook.

## 🧠 AI Agents

### 1. Content Planner
- Plans engaging and informative article content.
- Identifies important ideas and information the audience needs.
- Creates the foundation for the writing process.

### 2. Content Writer
- Transforms the content plan into a complete blog article.
- Organizes ideas into a logical structure.
- Writes content tailored to the intended audience.

### 3. Editor
- Reviews the article draft.
- Improves clarity, readability, and consistency.
- Checks for balanced viewpoints and journalistic writing practices.

## 🔄 Workflow

1. The user provides an article topic.
2. The Content Planner creates a structured plan.
3. The Content Writer develops the article from the plan.
4. The Editor reviews and refines the draft.
5. The final article is returned to the user.

## 🛠️ Tech Stack

- Python
- CrewAI
- Google GenAI
- Large Language Models (LLMs)
- Jupyter Notebook

## 📂 Project Structure

```text
Agentic-AI/
├── crewai.ipynb
├── app.py
├── .gitignore
├── .python-version
└── README.md
```

## ⚙️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Suhaila419/Agentic-AI.git
cd Agentic-AI
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv .venv
```

**Windows:**
```bash
.venv\Scripts\activate
```

**Linux / macOS / Codespaces:**
```bash
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
python -m pip install --upgrade pip
python -m pip install "crewai[google-genai]" streamlit python-dotenv
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_google_api_key
CREWAI_MODEL=your_supported_crewai_model
```

Replace the placeholders with your API key and a model supported by your Google AI API access.

**Security:** Never commit your `.env` file or expose API keys in your notebook or source code.

### 5. Run the Application

If `app.py` contains the Streamlit interface:

```bash
streamlit run app.py
```

Alternatively, open `crewai.ipynb` in Jupyter Notebook and select the appropriate Python environment to run the notebook cells.

## 🚀 Future Improvements

- Add web research and source verification to improve factual reliability.
- Support different article formats and writing styles.
- Allow users to specify article length, tone, and target audience.
- Add article export options such as Markdown and PDF.
- Improve error handling and evaluate the quality of generated articles.

---

*An agentic AI project exploring collaborative content planning, writing, and editing with CrewAI.*
