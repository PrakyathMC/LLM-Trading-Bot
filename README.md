🤖 LLM-Powered Financial Trading Bot
An intelligent trading assistant built with RAG (Retrieval-Augmented Generation) that analyzes financial documents and provides expert insights using OpenAI and AstraDB vector storage.


🚀 Features

PDF Analysis: Processes financial documents and SEC filings
Intelligent Q&A: Context-aware responses using RAG architecture
Vector Search: Semantic search powered by AstraDB
Web Interface: Clean Flask-based chat UI
Cloud Ready: Deployed on AWS EC2

🛠️ Tech Stack

LLM Framework: LangChain + OpenAI GPT
Vector Database: DataStax AstraDB
Backend: Flask (Python)
Document Processing: PyPDF + RecursiveCharacterTextSplitter
Deployment: AWS EC2

📋 Prerequisites

Python 3.8+
OpenAI API Key
AstraDB Account
AWS Account (for deployment)



🔧 Installation

Clone the repository

## git clone https://github.com/PrakyathMC/LLM-Trading-Bot.git
## cd LLM-Trading-Bot

Create virtual environment

## python -m venv venv
## source venv/bin/activate  # On Windows: venv\Scripts\activate

Install dependencies

# pip install -r requirements.txt

Set up environment variables

# Create .env file
OPENAI_API_KEY=your_openai_key
ASTRA_DB_API_ENDPOINT=your_endpoint
ASTRA_DB_APPLICATION_TOKEN=your_token
ASTRA_DB_KEYSPACE=default_keyspace
💻 Usage

Run locally

python app.py

Access the application

http://localhost:5000

Ask financial questions


"What is the company's revenue for 2023?"
"Explain the risk factors"
"What are the main products?"

🏗️ Architecture
### PDF Documents → LangChain Loader → Text Chunking → Vector Embeddings → AstraDB ↓
### User Query → Flask API → Retriever → LLM (GPT) → Generated Response ← Context

📁 Project Structure
LLM-Trading-Bot/
├── app.py                 # Flask application
├── tradingbot/
│   ├── data_ingestion.py  # Document processing & vector storage
│   ├── retrieval_generation.py  # RAG chain setup
│   └── helper.py          # PDF loading utilities
├── data/                  # Financial documents
├── templates/             # HTML templates
└── requirements.txt       # Python dependencies
# 🌐 AWS Deployment
# Deployed on AWS EC2 t3.large instance for optimal performance:

# Launch EC2 instance with security group (ports 22, 5000)
# Clone repository and install dependencies
# Configure environment variables
# Run with python app.py

🎯 Key Features Implemented

✅ RAG pipeline with LangChain
✅ Vector similarity search
✅ Conversation context handling
✅ Real-time Q&A interface
✅ Cloud deployment ready

📊 Performance

# Chunk Size: 500 characters with 100 overlap
# Retrieval: Top 3 most relevant chunks
# Response Time: ~2-3 seconds average


👨‍💻 Author
Prakyath MC
AI/ML Engineer 
📄 License
MIT License - feel free to use this project for learning!

## Note: This is a demonstration project for learning LLMOps concepts. Not intended for actual trading decisions.RetryClaude can make mistakes. Please double-check responses.