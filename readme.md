HybridRAG

A FastAPI-based PDF processing application that allows users to upload PDF files, convert PDF content into Markdown using PyMuPDF4LLM, and extract embedded images using PyMuPDF.

Features

Upload PDF files through a REST API

Validate PDF file uploads

Save uploaded PDFs locally

Convert PDF documents to Markdown

Extract embedded images from PDFs

Save extracted images separately

FastAPI Swagger documentation

Easy local development setup

Tech Stack

Python

FastAPI

Uvicorn

PyMuPDF4LLM

PyMuPDF

REST API

Project Structure
HybridRAG/
│
├── env/
│
├── uploads/
│   ├── example.pdf
│   ├── example.md
│   └── example_images/
│       ├── page_1_image_1.png
│       └── page_2_image_1.jpg
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md


The env/ directory should not be pushed to GitHub. Generated files inside uploads/ should also normally be excluded from Git.

Installation
1. Clone the repository
git clone <your-github-repository-url>
cd HybridRAG

2. Create a virtual environment
python -m venv env

3. Activate the virtual environment

For Windows Git Bash:

source env/Scripts/activate


You should see:

(env)

4. Install dependencies
pip install -r requirements.txt


If you do not have requirements.txt, install the dependencies manually:

pip install "fastapi[standard]"
pip install pymupdf4llm
pip install pymupdf
pip install uvicorn


Then generate the requirements file:

pip freeze > requirements.txt

Running the Application

Start the FastAPI server:

python -m uvicorn main:app --reload


The application will run at:

http://127.0.0.1:8000

Swagger API Documentation

FastAPI provides interactive API documentation through Swagger UI.

Open:

http://127.0.0.1:8000/docs


You can test the API directly from the Swagger interface.

API Endpoints
Upload PDF
POST /upload-pdf


Uploads a PDF file and saves it inside the uploads directory.

Example response:

{
    "message": "PDF uploaded successfully",
    "filename": "sample.pdf",
    "saved_path": "uploads/sample.pdf"
}

Convert PDF to Markdown
POST /pdf-to-markdown


This endpoint:

Finds the latest uploaded PDF.

Converts the PDF into Markdown.

Saves the Markdown file.

Extracts embedded images.

Saves the extracted images into a separate folder.

Example output:

uploads/
├── sample.pdf
├── sample.md
└── sample_images/
    ├── page_1_image_1.png
    ├── page_1_image_2.jpg
    └── page_2_image_1.png


Example response:

{
    "message": "PDF converted successfully",
    "pdf_file": "uploads/sample.pdf",
    "markdown_file": "uploads/sample.md",
    "image_folder": "uploads/sample_images",
    "image_count": 3,
    "images": [
        "uploads/sample_images/page_1_image_1.png",
        "uploads/sample_images/page_1_image_2.jpg",
        "uploads/sample_images/page_2_image_1.png"
    ]
}

Application Workflow
        PDF File
           │
           ▼
    ┌──────────────┐
    │ Upload PDF   │
    └──────┬───────┘
           │
           ▼
    ┌──────────────┐
    │ Save PDF     │
    └──────┬───────┘
           │
           ▼
    ┌──────────────────┐
    │ PyMuPDF4LLM      │
    │ PDF → Markdown   │
    └────────┬─────────┘
             │
       ┌─────┴──────┐
       ▼            ▼
   Markdown      Images
       │            │
       ▼            ▼
   .md file    Image folder

Example Usage

Start the server:

python -m uvicorn main:app --reload


Open Swagger:

http://127.0.0.1:8000/docs


Then:

1. Open POST /upload-pdf
2. Click "Try it out"
3. Select a PDF
4. Click "Execute"
5. Open POST /pdf-to-markdown
6. Click "Try it out"
7. Click "Execute"


The converted Markdown and extracted images will be stored in the uploads directory.

requirements.txt

Example:

fastapi
uvicorn
pymupdf
pymupdf4llm
python-multipart


python-multipart is required by FastAPI for handling file uploads.

.gitignore

Create a .gitignore file in the project root:

# Virtual environment
env/
venv/
.venv/

# Python cache
__pycache__/
*.py[cod]

# Environment variables
.env

# Generated PDF files
uploads/*.pdf

# Generated Markdown files
uploads/*.md

# Extracted images
uploads/*_images/

# IDE
.vscode/
.idea/

# OS files
.DS_Store
Thumbs.db

Git Commands

Check the files that will be committed:

git status


Add files:

git add .


Commit:

git commit -m "Add PDF processing API"


Push to GitHub:

git push origin main

Future Improvements

Planned improvements may include:

PDF text chunking

Embedding generation

Vector database integration

Semantic search

RAG pipeline

LLM integration

Multiple document support

Document metadata extraction

Persistent document storage

Authentication

Background PDF processing

License

This project is for learning and development purposes.