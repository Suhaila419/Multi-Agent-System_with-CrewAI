import os
import streamlit as st
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, LLM

load_dotenv()

st.set_page_config(
    page_title="Agentic AI Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Agentic AI Assistant")
st.caption("An AI assistant powered by CrewAI and Google GenAI")

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    st.error("GOOGLE_API_KEY was not found. Check your .env file.")
    st.stop()

with st.sidebar:
    st.header("Settings")
    st.write("Framework: CrewAI")
    st.write("Provider: Google GenAI")
    st.info("Make sure your configured model is available to your API key.")

topic = st.text_input(
    "What would you like the AI agent to explain?",
    placeholder="e.g. Artificial Intelligence, RAG, Multi-Agent Systems"
)

if st.button("Run AI Agent", type="primary"):
    if not topic.strip():
        st.warning("Please enter a topic first.")
    else:
        try:
            with st.spinner("The AI agent is working..."):
                llm = LLM(
                    model=os.getenv(
                        "CREWAI_MODEL",
                        "gemini/gemma-4-31b-it"
                    ),
                    api_key=api_key,
                    temperature=0.2
                )

                agent = Agent(
                    role="AI Learning Assistant",
                    goal="Explain technical topics clearly and accurately",
                    backstory=(
                        "You are an AI assistant who explains "
                        "technical concepts with practical examples."
                    ),
                    llm=llm,
                    verbose=False,
                    max_retry_limit=1
                )

                task = Task(
                    description=(
                        "Explain the following topic: {topic}. "
                        "Include a definition, key concepts, "
                        "a practical example, and a short conclusion."
                    ),
                    expected_output=(
                        "A clear, structured explanation with "
                        "a practical example."
                    ),
                    agent=agent
                )

                crew = Crew(
                    agents=[agent],
                    tasks=[task],
                    verbose=False
                )

                result = crew.kickoff(inputs={"topic": topic})

            st.subheader("Agent Response")
            st.markdown(str(result))

        except Exception as e:
            st.error("The agent could not complete the request.")
            st.code(f"{type(e).__name__}: {e}")
            st.caption(
                "Check the model name, API availability, "
                "and your CrewAI configuration."
            )
