# Lab 6 ELK Logging for ML Training

## Overview

This submission is based on `ELK_Labs/Lab2_ELK_Setup_Mac`, but it has been redesigned as a structured logging workflow for machine learning training instead of reusing the original Iris plus Logistic Regression example.

The project trains a breast cancer classifier, writes newline-delimited JSON logs for Logstash ingestion, and saves model metrics for exploration in Elasticsearch and Kibana.

## Changes Made from the Original Lab

- replaced the Iris dataset with the breast cancer dataset
- replaced Logistic Regression with a `RandomForestClassifier`
- changed plain text logging into JSON log events
- added metrics export to `artifacts/metrics.json`
- added top feature importance logging for better Kibana exploration
- added automated pytest coverage for the training pipeline
- added Docker Compose support for running Elasticsearch, Kibana, and Logstash together

## Project Structure

```text
Lab6/
├── artifacts/
│   ├── metrics.json
│   └── training.log
├── docker-compose.yml
├── logstash.conf
├── requirements.txt
├── src/
│   └── train_model.py
├── tests/
│   └── test_training.py
└── README.md
```

## Local Setup

From `Lab6/`:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Generate Training Artifacts

From `Lab6/`:

```bash
python src/train_model.py
```

This generates:

- `artifacts/training.log` with structured training events
- `artifacts/metrics.json` with evaluation metrics and top features

## Run Tests

From `Lab6/`:

```bash
pytest tests/test_training.py -v
```

## Run ELK with Docker Compose

Start the stack from `Lab6/`:

```bash
docker compose up -d
```

Check container status:

```bash
docker compose ps
```

Stop the stack when you are done:

```bash
docker compose down
```

Available services:

- Elasticsearch: `http://localhost:9200`
- Kibana: `http://localhost:5601`
- Logstash API: `http://localhost:9600`

## Logstash Configuration

`logstash.conf` is already configured for the Docker workflow:

- it reads `artifacts/training.log` through a mounted file path
- it sends documents to the Elasticsearch index `lab6-training-logs`
- it adds `lab` and `pipeline` fields to each ingested record

If you regenerate `artifacts/training.log`, restart Logstash to reprocess the file:

```bash
docker compose restart logstash
```

## Example ELK Workflow

1. Run `python src/train_model.py` to create fresh training logs.
2. Start the ELK stack with `docker compose up -d`.
3. Open Kibana at `http://localhost:5601`.
4. Create a data view for `lab6-training-logs`.
5. Explore fields such as `event_type`, `accuracy`, `f1_score`, `precision`, `recall`, `name`, and `importance`.

## Screenshot Checklist

If you want proof for submission or notes, take screenshots of:

- `docker compose ps`
- `http://localhost:9200` showing Elasticsearch is running
- Kibana with the `lab6-training-logs` data view
- Kibana Discover view showing ingested training records

## Submission Notes

This lab satisfies the assignment modification requirement because it is not identical to the source lab. The dataset, model, logging format, metrics, and analysis workflow were all changed.