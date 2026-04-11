# Lab 6 ELK Logging for ML Training

## Overview

This submission is based on `ELK_Labs/Lab2_ELK_Setup_Mac`, but it is customized into a structured logging workflow for machine learning training instead of reusing the original Iris plus Logistic Regression example.

The project trains a breast cancer classifier, writes JSON log events for ELK ingestion, and stores training metrics for later inspection in Kibana or Elasticsearch.

## Changes Made from the Original Lab

- replaced the Iris dataset with the breast cancer dataset
- replaced Logistic Regression with a `RandomForestClassifier`
- changed plain text logging into newline-delimited JSON logs for easier Logstash ingestion
- added metrics export to `artifacts/metrics.json`
- added top feature importance logging for better Kibana exploration
- added automated pytest coverage for the training pipeline

## Project Structure

```text
Lab6/
├── artifacts/
│   ├── metrics.json
│   └── training.log
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

## Run the Training Pipeline

From `Lab6/`:

```bash
python src/train_model.py
```

This generates:

- `artifacts/training.log` with structured JSON training events
- `artifacts/metrics.json` with evaluation metrics and top features

## Run Tests

From `Lab6/`:

```bash
pytest tests/test_training.py -v
```

## Logstash Configuration

Update the `path` field in `logstash.conf` so it points to your local `Lab6/artifacts/training.log` file.

Then start Logstash with:

```bash
bin/logstash -f /absolute/path/to/Lab6/logstash.conf
```

The configuration sends records to the Elasticsearch index `lab6-training-logs`.

## Example ELK Workflow

1. Start Elasticsearch on `http://localhost:9200`.
2. Start Kibana on `http://localhost:5601`.
3. Run `python src/train_model.py` to create fresh logs.
4. Start Logstash with the provided `logstash.conf`.
5. In Kibana, create a data view for `lab6-training-logs` and explore fields like `event_type`, `accuracy`, `f1_score`, `precision`, `recall`, and `name`.

## Submission Notes

This lab satisfies the assignment modification requirement because it is not identical to the source lab. The dataset, model, logging format, metrics, and analysis workflow were all changed.
