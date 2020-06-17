# Serving Textblob using FLask

Just a tivial Flask app using Textblob to generate sentiment score for document.

# Setup

- With Docker

```
docker-compose up -d
```

- Without Docker
```
pip install -r requirements.txt && python app.py
```

# Getting Started

Send a POST requst to http://localhost:5000 with

{
    "text": "I love apple"
}