# Lab 4 Cloud Function Project

## Overview

This submission is based on `GCP_Labs/CloudFunction_Labs/Lab1-CloudFunction_Setup`, but it is customized into a production-style HTTP Cloud Function for wine classification instead of reusing the original Iris example.

The function supports:

- `GET` requests for health and model metadata
- `POST` requests for wine-class prediction from JSON input
- local testing with `pytest`
- deployment to Google Cloud Functions Gen 2

## Changes Made from the Original Lab

- replaced the original Iris model with the scikit-learn Wine dataset
- replaced the basic logistic regression example with a `RandomForestClassifier`
- added a metadata response for `GET` requests
- added stronger request validation for malformed JSON and missing features
- added an example request payload file for quick testing
- added automated tests and a dedicated GitHub Actions workflow

## Project Structure

```text
Lab4/
├── main.py
├── requirements.txt
├── sample_request.json
├── tests/
│   └── test_main.py
└── README.md
```

## Local Setup

From `Lab4/`:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run Locally

Start the function locally with the Functions Framework:

```bash
functions-framework --target wine_quality_predictor --source main.py --debug
```

The local endpoint will be available at `http://127.0.0.1:8080`.

## Test the Function

From `Lab4/`:

```bash
pytest tests/test_main.py -v
```

## Example Requests

Metadata request:

```bash
curl http://127.0.0.1:8080
```

Prediction request:

```bash
curl -X POST http://127.0.0.1:8080 \
  -H "Content-Type: application/json" \
  -d @sample_request.json
```

## Deploy to Google Cloud Functions

After authenticating with `gcloud`, deploy with:

```bash
gcloud functions deploy lab4-wine-predictor \
  --gen2 \
  --runtime python311 \
  --region us-central1 \
  --source . \
  --entry-point wine_quality_predictor \
  --trigger-http \
  --allow-unauthenticated
```

## Live Deployment

The function is deployed at:

- Cloud Function URL: `https://us-central1-civic-access-359510.cloudfunctions.net/lab4-wine-predictor`
- Service URL: `https://lab4-wine-predictor-v3st7gvnza-uc.a.run.app`

Example live checks:

```bash
curl https://us-central1-civic-access-359510.cloudfunctions.net/lab4-wine-predictor
curl -X POST https://us-central1-civic-access-359510.cloudfunctions.net/lab4-wine-predictor \
  -H "Content-Type: application/json" \
  -d @sample_request.json
```

## Submission Notes

This lab satisfies the assignment requirement that the submitted work must not be identical to the source lab. The dataset, model choice, prediction interface, validation logic, tests, and documentation were all changed from the original example.
