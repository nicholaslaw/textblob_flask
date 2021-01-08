# Sentiment Extraction Using TextBlob, Flask, ElasticSearch and Kibana

A Flask app involving a model by TextBlob to perform sentiment extraction on documents and subsequently ingesting data with results into
ElasticSearch. Kibana can then be used to perform meaningful visualizations on the data.

# Installation Instructions

```
docker-compose up
```

# Getting Started

Send a POST requst to http://localhost:5000 with

{
	"author": "jack",
	"timestamp": "1st January 2020",
	"text": "I love apple"
}

This will return

{
  "created": "created",
  "sentiment": 0.5,
  "subjectivity": 0.6
}

where "created" indicates whether the ingestion of data into ElasticSearch has succeeded, "sentiment" refers to the polarity extracted from TextBlob
and "subjectivity" is defined as the confidence of the extracted sentiment score.

# Things to Note

Elasticsearch index has been fixed to be "sentiment" and ingested data would have fields:

1. author

2. timestamp

3. text

4. polarity

5. subjectivity