# AnswerApp

A question-answering application that uses MongoDB Atlas Vector Search and OpenAI to provide intelligent responses based on your documents.


## Features

- **Vector Search**: Find the most similar documents to your query
- **RAG (Retrieval-Augmented Generation)**: Generate AI-powered answers using your documents
- **MongoDB Atlas Integration**: Store and search document embeddings

## Files

- `extract_information.py` - Main Gradio web interface (may have browser issues)
- `load_data.py` - Load documents into MongoDB Atlas
- `key_param.py` - Configuration file with API keys
- `sample_files/` - Directory containing your documents. Ive left some sample files here for testing.

## Quick Start

1. **Setup Configuration**
   ```bash
   # Edit key_param.py with your API keys
   openai_api_key = "your-openai-key"
   MONGO_URI = "your-mongodb-atlas-uri"
   ```

2. **Load Your Documents**
   ```bash
   python load_data.py
   ```

3. **Create Vector Search Index**
   - Go to MongoDB Atlas → Atlas Search
   - Create index on `collection_of_text_blobs`
   - Use this configuration:
   ```json
   {
     "mappings": {
       "dynamic": true,
       "fields": {
         "embedding": {
           "dimensions": 1536,
           "similarity": "cosine",
           "type": "knnVector"
         }
       }
     }
   }
   ```

4. **Run the App**
   ```bash
      python extract_information.py
   ```

## Usage

- Type questions about your loaded documents
- Get both similarity search results and AI-generated answers
- Use `quit` to exit, `help` for options

## Requirements

- Python 3.8+
- MongoDB Atlas account
- OpenAI API key
- Packages

## Installation

```bash
pip install requirements.txt
```

## Troubleshooting

- **Import errors**: Make sure all packages are installed
- **Connection issues**: Check your MongoDB URI and OpenAI API key 
