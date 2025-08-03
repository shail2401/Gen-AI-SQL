# GenAI SQL Assistant

GenAI SQL Assistant is an end-to-end large language model (LLM) project powered by Google PaLM and LangChain. It allows users to interact with structured databases using natural language—no SQL expertise required. By combining the capabilities of generative AI and real-time database querying, the tool translates user prompts into executable SQL, enabling fast and intuitive access to business insights. This solution bridges the gap between non-technical users and data, making advanced analytics accessible through conversational AI.



## Overview

This project allows users to ask questions in plain English and receive database answers by dynamically generating and executing SQL queries using a Retrieval-Augmented Generation (RAG) pipeline.



## Tech Stack

- Python  
- [Google PaLM API](https://developers.generativeai.google)  
- [LangChain](https://www.langchain.com/)  
- SQLite (Chinook DB)  
- Python



## Project Structure
```
Gen-AI-SQL-Assistant/
├── app.py # Main app logic
├── sql_chain.py 
├── chinook.db 
├── .env # Environment variables ( API key)
├── requirements.txt 
├── utils/
│ └── db_loader.py 
├── sql_chain/
│ └── init.py 
└── .gitignore
```


##  Dataset
This project uses the Chinook Database, a sample music store DB featuring customers, invoices, artists, albums, and tracks



## License

This project is licensed under the MIT License.

Includes data from the Chinook Database, which is also provided under the MIT License.
