🚀 HybridRAG

HybridRAG is a Python-based Retrieval-Augmented Generation (RAG) project designed to process PDF documents and prepare their content for intelligent retrieval and question answering.

The project currently provides a FastAPI-based PDF processing pipeline that allows users to upload PDF files, convert them into Markdown using PyMuPDF4LLM, and extract embedded images using PyMuPDF.

✨ Features

📄 PDF document upload

✅ PDF file validation

💾 Local PDF storage

📝 PDF → Markdown conversion

🖼️ Embedded image extraction

📁 Separate image storage

⚡ FastAPI REST API

📚 Interactive Swagger API documentation

🧩 Modular project structure

🔍 Foundation for a future RAG pipeline

🛠️ Tech Stack
Technology	Purpose
🐍 Python	Core programming language
⚡ FastAPI	REST API framework
🚀 Uvicorn	ASGI server
📄 PyMuPDF4LLM	PDF to Markdown conversion
🔧 PyMuPDF	PDF processing and image extraction
🔗 REST API	Client-server communication
📂 Project Structure
HybridRAG/
│
├── retrivers/
│
├── config.py
├── ingestion.py
├── main.py
├── pipeline.py
├── requirements.txt
├── .gitignore
└── README.md

Main Components
File / Directory	Description
main.py	FastAPI application and API endpoints
ingestion.py	Document ingestion and processing logic
pipeline.py	RAG processing pipeline
config.py	Application configuration
retrivers/	Retrieval-related components
requirements.txt	Python dependencies
.gitignore	Files excluded from Git
README.md	Project documentation
⚙️ Installation
1. Clone the Repository
git clone https://github.com/bibekpandey0521/HybridRAG.git
cd HybridRAG

2. Create a Virtual Environment
python -m venv env

3. Activate the Virtual Environment
Windows — Git Bash
source env/Scripts/activate


After activation, your terminal should show:

(env)

Windows — Command Prompt
env\Scripts\activate

Windows — PowerShell
env\Scripts\Activate.ps1

4. Install Dependencies

Install the project dependencies:

pip install -r requirements.txt


If you are setting up the project for the first time and requirements.txt is not available, install the main dependencies manually:

pip install "fastapi[standard]"
pip install uvicorn
pip install pymupdf
pip install pymupdf4llm
pip install python-multipart


Then generate the requirements file:

pip freeze > requirements.txt

▶️ Running the Application

Make sure the virtual environment is activated:

source env/Scripts/activate


Start the FastAPI development server:

python -m uvicorn main:app --reload


The server should start at:

http://127.0.0.1:8000

📚 Swagger API Documentation

FastAPI provides an interactive Swagger UI for testing the API.

Open:

http://127.0.0.1:8000/docs


You can use Swagger to:

Upload PDF files

Test API endpoints

View request parameters

View API responses

Test the PDF processing workflow

🔌 API Endpoints
📤 Upload PDF
POST /upload-pdf


Uploads a PDF document to the application.

Workflow
PDF File
   │
   ▼
Validate File
   │
   ▼
Save PDF
   │
   ▼
Store File Path

Example Response
{
    "message": "PDF uploaded successfully",
    "filename": "sample.pdf",
    "saved_path": "uploads/sample.pdf"
}

📝 Convert PDF to Markdown
POST /pdf-to-markdown


Processes the latest uploaded PDF.

Processing Steps
Uploaded PDF
     │
     ▼
PyMuPDF4LLM
     │
     ▼
Markdown Content
     │
     ├───────────────┐
     ▼               ▼
 .md file       Extract Images
                     │
                     ▼
                Image Folder


The endpoint:

Finds the latest uploaded PDF.

Converts PDF content into Markdown.

Saves the generated Markdown file.

Opens the PDF using PyMuPDF.

Extracts embedded images.

Saves the images separately.

Example Output
uploads/
│
├── sample.pdf
├── sample.md
│
└── sample_images/
    ├── page_1_image_1.png
    ├── page_1_image_2.jpg
    └── page_2_image_1.png

Example Response
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

🔄 Current Processing Pipeline
                 ┌──────────────┐
                 │   PDF File   │
                 └──────┬───────┘
                        │
                        ▼
              ┌──────────────────┐
              │   FastAPI Upload │
              └────────┬─────────┘
                       │
                       ▼
              ┌──────────────────┐
              │   Save PDF       │
              └────────┬─────────┘
                       │
                       ▼
              ┌──────────────────┐
              │   PyMuPDF4LLM    │
              │  PDF → Markdown  │
              └────────┬─────────┘
                       │
                 ┌─────┴─────┐
                 │           │
                 ▼           ▼
           ┌──────────┐ ┌───────────┐
           │ Markdown │ │   Images  │
           │   .md    │ │ Extracted │
           └──────────┘ └───────────┘

🧪 Example Usage
Step 1 — Start the Server
python -m uvicorn main:app --reload

Step 2 — Open Swagger
http://127.0.0.1:8000/docs

Step 3 — Upload a PDF

In Swagger:

Open POST /upload-pdf

Click Try it out

Select a PDF file

Click Execute

Step 4 — Convert the PDF

Then:

Open POST /pdf-to-markdown

Click Try it out

Click Execute

The application will process the uploaded PDF and generate the Markdown and extracted images.

📦 Dependencies

The main dependencies include:

fastapi
uvicorn
pymupdf
pymupdf4llm
python-multipart


Install all dependencies using:

pip install -r requirements.txt

🚫 Git Ignore

The local virtual environment should not be pushed to GitHub.

Recommended .gitignore:

# Virtual environments
env/
venv/
.venv/

# Python cache
__pycache__/
*.py[cod]

# Environment variables
.env
.env.*

# Generated files
uploads/

# IDE
.vscode/
.idea/

# OS files
.DS_Store
Thumbs.db

🌱 Git Workflow

Check the current repository status:

git status


Add changes:

git add .


Commit:

git commit -m "Improve PDF processing pipeline"


Push to GitHub:

git push origin main

🔮 Future Improvements

The project is intended to evolve into a complete RAG system.

Planned improvements include:

🧩 PDF text chunking

🧠 Embedding generation

🗄️ Vector database integration

🔎 Semantic search

🤖 LLM integration

📚 Complete RAG pipeline

📄 Multiple document support

🏷️ Document metadata extraction

💾 Persistent document storage

🔐 Authentication and authorization

⚡ Background document processing

📊 Document processing status

💬 Question answering over uploaded documents

🎯 Project Vision

The long-term goal of HybridRAG is to build a complete document intelligence pipeline:

PDF Documents
      │
      ▼
Document Ingestion
      │
      ▼
PDF Processing
      │
      ├───────────────┐
      ▼               ▼
   Markdown         Images
      │
      ▼
Text Chunking
      │
      ▼
Embeddings
      │
      ▼
Vector Database
      │
      ▼
Retrieval
      │
      ▼
LLM
      │
      ▼
Answer

📌 Repository

GitHub:
https://github.com/bibekpandey0521/HybridRAG

📜 License

This project is currently intended for learning and development purposes.