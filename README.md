# GenAI SQL Assistant

Natural language SQL querying powered by **Google PaLM**, **LangChain**, and the **Chinook** sample database.

---

## Overview

This project allows users to ask questions in plain English and receive database answers by dynamically generating and executing SQL queries using a Retrieval-Augmented Generation (RAG) pipeline.

---

## Tech Stack

- Python  
- [Google PaLM API](https://developers.generativeai.google)  
- [LangChain](https://www.langchain.com/)  
- SQLite (Chinook DB)  
- Python

---

## Project Structure
```
Gen-AI-SQL-Assistant/
├── app.py # Main app logic
├── sql_chain.py # LangChain SQL chain setup
├── chinook.db # Sample SQLite database
├── .env # Environment variables ( API key)
├── requirements.txt # Project dependencies
├── utils/
│ └── db_loader.py # DB connection helper
├── sql_chain/
│ └── init.py # SQL agent logic
└── .gitignore
```
