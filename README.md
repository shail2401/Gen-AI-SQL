# GenAI SQL Assistant

Natural language SQL querying powered by **Google PaLM**, **LangChain**, and the **Chinook** sample database.



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
