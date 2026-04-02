# Lab 5 Docker ML Project

## Overview
This project demonstrates how to containerize a machine learning workflow using Docker. The application trains a classification model inside a container, evaluates it, and writes both the trained model and evaluation metrics to the `outputs/` directory.

## Changes Made from Original Lab
This lab was modified from the original Docker lab in the following ways:

- Uses the Wine dataset instead of the Iris dataset
- Uses Logistic Regression instead of Random Forest
- Adds feature scaling with `StandardScaler`
- Saves the trained model to `outputs/wine_model.pkl`
- Saves evaluation metrics to `outputs/metrics.json`

These changes make the project different from the original lab while keeping the same Docker-based ML workflow, which satisfies the assignment requirement to submit a modified version of one of the provided labs.

## Project Structure
```text
.
├── src/
│   └── main.py
├── outputs/
├── requirements.txt
├── Dockerfile
├── .dockerignore
└── README.md
```

## Requirements
Make sure Docker is installed on your system. You do not need a local Python environment to run the lab through Docker.

## How to Run

From the `Lab5/` directory:

## Build the Docker Image
```bash
docker build -t lab5-wine:v1 .
```

## Run the Container
Run the container and mount the local `outputs/` folder so generated files are written to your machine:

```bash
docker run --rm -v "$(pwd)/outputs:/app/outputs" lab5-wine:v1
```

## What the Program Does

When the container starts, it:

1. Loads the Wine dataset from scikit-learn
2. Splits the data into train and test sets
3. Applies `StandardScaler`
4. Trains a `LogisticRegression` classifier
5. Evaluates model performance on the test set
6. Saves the trained model and metrics into `outputs/`

## Expected Output
When the container runs successfully, you should see output similar to:

```text
Model training completed successfully.
Accuracy: 0.9722
Saved model to: outputs/wine_model.pkl
Saved metrics to: outputs/metrics.json
```

## Output Files
After running the container, the following files will be created in the `outputs/` folder:

- `wine_model.pkl`: the trained machine learning model
- `metrics.json`: the evaluation metrics for the trained model

Sample metrics from a successful run are included in `outputs/metrics.json`.

## Submission
For Lab Assignment 5, submit the GitHub repository link containing this project. The key files for grading are:

- `Lab5/src/main.py`
- `Lab5/Dockerfile`
- `Lab5/requirements.txt`
- `Lab5/README.md`

## Summary
This project shows how Docker can be used to package and run a machine learning workflow in a consistent environment. It also demonstrates a customized version of the original lab by using a different dataset, model, and output artifacts.
