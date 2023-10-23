# sql-interpreter

SQL interpreter based on Auto-GPT to autonomously generate and run postgressql code based on natural language input.

![sample output](https://github.com/SamsLogic/sql-interpreter/assets/41964069/e840c96e-46f5-43d5-aeac-5ebaafe3fc11)

## Functionalities
- [x] Automatic PostgresSQL code generation and execution in postgresSQL server
- [x] Automatic database understanding before initiating SQL development
- [x] Automatic Exit condition handled by chatgpt
- [ ] Add logging
- [ ] Handling repeated answers
- [ ] Adding function calling support
- [ ] Better Exit condition
- [ ] Using simpler LLMs
- [ ] UI for better engagement
- [ ] Many more bug fixes

## Requriements

1. python 3.8.10
2. pip

## Setup

1. Setup Virtual Environment
   
   i. Ubuntu
    ```console
    pip3 install virtualenv
    python3 -m virtualenv venv
    source venv/bin/activate
    ```
   ii.Windows
    ```console
    pip install virtualenv
    python -m virtualenv venv
    .\venv\Scripts\activate
    ```
3. Install required libraries
```console
pip install -r requirements.txt
```
3. Maintain .env as per your configurations
   
    i. Ubuntu
    ```console
    cp config/.env.example config/.env
    # Maintain PostgresSQL DB credentials and OpenAI API credentials in the .env file.    
    ```
    ii. Windows
    ```console
    copy config\.env.example config\.env
    # Maintain PostgresSQL DB credentials and OpenAI API credentials in the .env file.
    ```

4. Run the code and have fun
```console
python main.py
```

## Disclaimer

This repository is a basic version of an SQL Interpreter for PostgresSQL databases. This can generate SQL queries and uses LLMs to do so. Currently it only supports ChatGPT and OpenAI API calls. Would love to see the LLM community to build more on this public repo to make it more robust and useful.
