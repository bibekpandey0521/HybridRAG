HybridRAG

A FastAPI-based PDF processing application that converts PDF documents into Markdown and extracts images using PyMuPDF4LLM.

Features

Upload PDF files

Convert PDF to Markdown

Extract images from PDFs

Save Markdown and images locally

FastAPI REST API

Swagger API documentation

Tech Stack

Python

FastAPI

Uvicorn

PyMuPDF4LLM

PyMuPDF

Project Structure
HybridRAG/
│
├── main.py
├── ingestion.py
├── pipeline.py
├── config.py
├── retrivers/
├── requirements.txt
├── .gitignore
└── README.md

Setup
1. Clone the project
git clone https://github.com/bibekpandey0521/HybridRAG.git
cd HybridRAG

2. Create virtual environment
python -m venv env

3. Activate environment

For Git Bash:

source env/Scripts/activate

4. Install dependencies
pip install -r requirements.txt

Run the Server
python -m uvicorn main:app --reload


Server:

http://127.0.0.1:8000


Swagger documentation:

http://127.0.0.1:8000/docs

API
Upload PDF
POST /upload-pdf


Uploads a PDF file.

Convert PDF to Markdown
POST /pdf-to-markdown


Converts the uploaded PDF into Markdown and extracts images.

Workflow
PDF
 ↓
Upload
 ↓
PyMuPDF4LLM
 ↓
Markdown + Images
 ↓
Future RAG Pipeline

Git

The virtual environment should not be pushed to GitHub.

.gitignore:

env/
venv/
.venv/
__pycache__/
*.pyc
.env
uploads/

Future Plans

Text chunking

Embeddings

Vector database

Semantic search

LLM integration

Complete RAG pipeline

GitHub

https://github.com/bibekpandey0521/HybridRAG