# 🦙 LLaMA3 + DuckDB SQL Analytics Bot

This project is a **natural language SQL analytics chatbot** powered by **LLaMA3 (via Ollama)** and **DuckDB**, built using **LangChain** and **Streamlit**.

Ask questions like:
- "How many records are in the web_analytics table?"
- "What is the average session duration by country?"
- "Which page has the highest bounce rate?"

## 📦 Features

- 🔎 Query a local DuckDB database using plain English
- 🧠 LLaMA3 model locally served via Ollama
- ⚙️ LangChain agent parses and executes SQL intelligently
- 💻 Streamlit frontend to interact with the bot
- ✅ Local and private (no external APIs needed)

---

## 🚀 How to Run

### 1. Clone the Repo
```bash
git clone https://github.com/<your-username>/llama3-duckdb-analytics-bot.git
cd llama3-duckdb-analytics-bot
````

### 2. Install Dependencies

Make sure you have Python 3.10+ and run:

```bash
pip install -r requirements.txt
```

### 3. Start Ollama with LLaMA3

Download and start LLaMA3 using [Ollama](https://ollama.com/):

```bash
ollama run llama3
```

### 4. Launch the Bot

```bash
streamlit run bot.py
```

---

## 📁 File Structure

```
.
├── bot.py                    # Streamlit app
├── web_analytics.csv         # Raw data (optional)
├── web_analytics.duckdb      # DuckDB database file
├── requirements.txt          # Python dependencies
└── README.md
```

---

## 📊 Example Table Schema (`web_analytics`)

| page\_url | country | sessions | bounce\_rate | avg\_duration |
| --------- | ------- | -------- | ------------ | ------------- |
| /home     | US      | 1200     | 40%          | 00:02:10      |
| /pricing  | IN      | 800      | 60%          | 00:01:30      |

---

## 🧠 Technologies Used

* [LangChain](https://python.langchain.com/)
* [DuckDB](https://duckdb.org/)
* [Ollama](https://ollama.com/)
* [Streamlit](https://streamlit.io/)
* [LLaMA3](https://ollama.com/library/llama3)

---

## 🛡️ License

MIT License

---

## 👨‍💻 Author

Built with ❤️ by [Your Name](https://github.com/<your-username>)

```

---

Let me know if you'd like:
- A visual badge (e.g., for Streamlit, Python, DuckDB)
- A demo GIF or screenshot section
- Instructions for deploying on Streamlit Cloud

I can also auto-generate the `requirements.txt` from your current env if needed.
```
