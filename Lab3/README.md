# Lab 3 Flask GCP API Project

## Overview
This lab is based on the `API_Labs/FLASK_GCP_LAB`.

The project provides a Flask API for Iris flower prediction, packages the service for Docker and Cloud Run, and includes a small Streamlit frontend for interactive testing.

## Changes Made from the Original Lab

- Created a dedicated top-level `Lab3/` folder for submission consistency
- Replaced the original `RandomForestClassifier` with a `LogisticRegression` pipeline plus `StandardScaler`
- Added automatic metric export to `model/metrics.json`
- Added `GET /health` and `GET /metadata` endpoints
- Improved `POST /predict` to validate request payloads and return confidence scores and class probabilities
- Reworked the frontend to use a configurable `API_URL` instead of a hardcoded deployed endpoint
- Added API tests using Flask's test client
- Cleaned up Docker configuration for Cloud Run deployment with `gunicorn`

## Project Structure

```text
Lab3/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── predict.py
│   ├── test_api.py
│   └── train.py
├── model/
│   └── .gitkeep
├── streamlit_app.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
└── README.md
```

## API Endpoints

- `GET /` returns a simple service summary
- `GET /health` returns a basic health check
- `GET /metadata` returns model and dataset metadata
- `POST /predict` predicts the Iris class from flower measurements

### Example Prediction Request

```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

### Example Prediction Response

```json
{
  "prediction": "setosa",
  "predicted_index": 0,
  "confidence": 0.9784,
  "probabilities": {
    "setosa": 0.9784,
    "versicolor": 0.0215,
    "virginica": 0.0001
  }
}
```

## Local Setup

From `Lab3/`:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m src.train
python -m src.main
```

The API runs locally on `http://127.0.0.1:8080`.

## Run Tests

From `Lab3/`:

```bash
pytest src/test_api.py -v
```

## Run the Streamlit Frontend

If the API is running locally:

```bash
streamlit run streamlit_app.py
```

If you deploy the API to Cloud Run, set the API URL first:

```bash
export API_URL="https://your-cloud-run-service-url"
streamlit run streamlit_app.py
```

## Build and Run with Docker

Build the image:

```bash
docker build -t lab3-iris-api .
```

Run the container locally:

```bash
docker run --rm -p 8080:8080 lab3-iris-api
```

## Cloud Run Deployment

After authenticating with `gcloud`, you can build and deploy:

```bash
gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/lab3-iris-api
gcloud run deploy lab3-iris-api \
  --image gcr.io/YOUR_PROJECT_ID/lab3-iris-api \
  --platform managed \
  --region us-east1 \
  --allow-unauthenticated
```

## Live Deployment

The API is deployed on Google Cloud Run at:

- Service URL: `https://lab3-iris-api-797881056927.us-east1.run.app`
- Health check: `https://lab3-iris-api-797881056927.us-east1.run.app/health`
- Metadata endpoint: `https://lab3-iris-api-797881056927.us-east1.run.app/metadata`

To run the Streamlit frontend against the deployed service:

```bash
export API_URL="https://lab3-iris-api-797881056927.us-east1.run.app"
streamlit run streamlit_app.py
```

## Submission Links

- GitHub repository: `https://github.com/darshanrk18/MLOps-labs`
- Lab 3 folder: `https://github.com/darshanrk18/MLOps-labs/tree/main/Lab3`
- Cloud Run service: `https://lab3-iris-api-797881056927.us-east1.run.app`

## Submission Notes

This version satisfies the assignment's modification requirement because it is not a direct copy of the original source lab. The model, API behavior, frontend configuration, testing approach, and deployment setup were all updated.
