# Wikipedia RAG System

A Streamlit-based Retrieval-Augmented Generation (RAG) system that answers questions using Wikipedia articles as its knowledge base.

## Features

- Answers questions using information from selected Wikipedia pages
- Uses OpenAI's GPT-4 and text embeddings for question answering
- Persistent vector index storage for faster subsequent runs
- Displays both answers and source context
- Simple and intuitive web interface

## Prerequisites

- Python 3.8+
- OpenAI API key
- UV package manager (optional but recommended)
- Poetry (for dependency management)

## Installation

### Using UV (recommended)

1. Install UV if you haven't already:
   ```bash
   pip install uv
   ```
2. Clone this repository:

```bash
git clone <your-repository-url>
cd wikipedia-rag-system
```
3. Create and activate a virtual environment:

```bash
uv venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```
4. Install dependencies:

```bash
uv pip install -r requirements.txt
```
### Using traditional pip
Follow steps 2-3 above, then:

```bash
pip install -r requirements.txt
```
## Configuration
Create a .env file in the project root with your OpenAI API key:

```bash
OPENAI_API_KEY=your-api-key-here
```
#### (Optional) Modify the PAGES list in app.py to change which Wikipedia articles are indexed.

### Usage
Running the Application
```bash
streamlit run app.py
```
The application will:

First run: Download and index the specified Wikipedia pages (may take several minutes)

Subsequent runs: Load the pre-built index for faster startup

Once running, open your browser to http://localhost:8501 to access the web interface.

### How to Use
Enter your question in the text box

### Click "Search"

View the answer and supporting context from Wikipedia

## Deployment
Option 1: Streamlit Sharing (easiest)
Create a free account on Streamlit Sharing

Connect your GitHub repository

Set OPENAI_API_KEY as a secret in the deployment settings

Deploy!

Option 2: Docker Deployment
Build the Docker image:

```bash
docker build -t wiki-rag .
```
Run the container:

```bash
docker run -p 8501:8501 -e OPENAI_API_KEY=your-key wiki-rag
```
Access at http://localhost:8501

Option 3: Traditional Server Deployment
Install dependencies on your server as shown in the Installation section

Run with:

```bash
nohup streamlit run app.py --server.port=8501 &
```
Set up a reverse proxy (Nginx/Apache) if needed

Customization
To change which Wikipedia pages are indexed, modify the PAGES list in app.py

To use a different OpenAI model, change the model parameter in both the OpenAI and OpenAIEmbedding initializations

Adjust similarity_top_k in get_query_engine() to change how many context chunks are retrieved

Troubleshooting
Problem: Slow first run

Solution: This is normal as it downloads and indexes Wikipedia content. Subsequent runs will be faster.

Problem: API key not found

Solution: Ensure your .env file exists in the project root and contains OPENAI_API_KEY=your-key

Problem: Index not persisting

Solution: Ensure the application has write permissions in the project directory
