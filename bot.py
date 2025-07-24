import os
import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, inspect, text
from langchain_community.utilities import SQLDatabase
from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.agents import AgentType
from langchain_community.llms import Ollama

# --- CONFIG ---
db_file_path = "C:/Users/test/Downloads/AB/web_analytics.duckdb"
csv_path = "C:/Users/test/Downloads/AB/web_analytics.csv"
table_name = "web_analytics"

# --- STREAMLIT UI ---
st.set_page_config(page_title="📊 Web Analytics Chatbot", layout="centered")
st.title("📈 Ask Questions About Your Web Analytics Data")

# --- SQLAlchemy Engine ---
engine = create_engine(f"duckdb:///{db_file_path}")
inspector = inspect(engine)

# --- Ensure Table Exists ---
if table_name not in inspector.get_table_names():
    st.info(f"Creating table '{table_name}' from CSV...")

    df = pd.read_csv(csv_path)
    df.to_sql(table_name, con=engine, index=False, if_exists="replace")

    # Re-check
    inspector = inspect(engine)
    if table_name not in inspector.get_table_names():
        st.error(f"❌ Table '{table_name}' not found after creation.")
        st.stop()

st.success(f"✅ Table '{table_name}' is ready.")
st.info(f"Available tables: {inspector.get_table_names()}")

# --- LangChain Setup ---
llm = Ollama(model="llama3")

db = SQLDatabase(engine=engine, include_tables=[table_name])
toolkit = SQLDatabaseToolkit(db=db, llm=llm)

agent = create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# --- User Input ---
user_question = st.text_input("💬 Ask a question about your data:")

if user_question:
    with st.spinner("🔍 Thinking..."):
        try:
            response = agent.run(user_question)
            st.markdown("🧠 **Response:**")
            st.write(response)
        except Exception as e:
            st.error(f"❌ Error: {e}")
