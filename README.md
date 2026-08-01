# mini-rag-practice

This is a best practice of RAG model for Question answering

## Requirments

- Python 3.8 or later

## Activate conda on WSL 
```bash
$ conda activate mini-rag-app
```

## Installation
### Install the required packages
```bash
$ pip install -r requirments.txt
```
### Setup the environment variables
```bash
$ cp .env.example .env
```

## Running the app on uvicorn 
```bash
$ uvicorn src.main:app --reload
```