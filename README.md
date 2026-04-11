# MLOps Labs

Repository for MLOps course labs. Each lab lives in its own folder with a dedicated `README.md`.

## Current Submission

This repository's Lab Assignment 6 submission is in `Lab6/`.

- Lab folder: [`Lab6/`](Lab6/)
- Lab documentation: [`Lab6/README.md`](Lab6/README.md)
- Customizations from the original lab: Breast cancer dataset, Random Forest model, JSON training logs, feature importance tracking, and ELK-ready Logstash configuration

---

## Lab 1: Github_Labs/Lab1

Introduction to MLOps fundamentals through guided GitHub Labs exercises. This lab covers:

- **GitHub Actions CI/CD** — Automated testing on push
- **Testing frameworks** — Pytest and unittest
- **Project structure** — Modular Python application with tests

---

## Lab 2: Terraform Beginner Lab

Deploy AWS infrastructure (VPC, subnet, EC2) using Terraform. This lab covers:

- **Infrastructure as Code** — Define AWS resources in `.tf` files
- **Terraform workflow** — init, plan, apply, destroy
- **Variables & outputs** — Maintainable, reusable configurations
- **Networking** — VPC, subnet, Internet Gateway, security group

See [Lab2/README.md](Lab2/README.md) for prerequisites, step-by-step instructions, and how to re-run the lab.

---

## Lab 3: Flask GCP API

Customized Flask API lab prepared from `API_Labs/FLASK_GCP_LAB`. This lab covers:

- **Flask API development** - Build prediction endpoints for model inference
- **Model packaging** - Train and persist a scikit-learn pipeline for serving
- **Testing** - Verify endpoints with Flask test client and pytest
- **Cloud deployment** - Package the service for Docker and Cloud Run

See [Lab3/README.md](Lab3/README.md) for setup, API usage, tests, and deployment steps.

---

## Lab 4: GCP Cloud Function

Customized Cloud Function lab prepared from `GCP_Labs/CloudFunction_Labs/Lab1-CloudFunction_Setup`. This lab covers:

- **Serverless inference** - Deploy an HTTP-triggered Google Cloud Function
- **Model customization** - Train a `RandomForestClassifier` on the Wine dataset
- **Request validation** - Support metadata `GET` requests and validated prediction `POST` requests
- **Testing** - Verify the function locally with pytest

See [Lab4/README.md](Lab4/README.md) for setup, local execution, testing, and deployment instructions.

Live function URL: `https://us-central1-civic-access-359510.cloudfunctions.net/lab4-wine-predictor`

---

## Lab 5: Dockerized ML Workflow

Containerized machine learning workflow that trains and evaluates a classifier inside Docker. This lab covers:

- **Docker packaging** - Build a reproducible ML runtime with a `Dockerfile`
- **Model training** - Train a scikit-learn classifier from a Python entrypoint
- **Artifact generation** - Save evaluation metrics and the trained model to `outputs/`
- **Customization** - Uses the Wine dataset with `LogisticRegression` and `StandardScaler`

See [Lab5/README.md](Lab5/README.md) for setup, run instructions, and submission details.

---

## Lab 6: ELK Logging for ML Training

Customized ELK lab prepared from `ELK_Labs/Lab2_ELK_Setup_Mac`. This lab covers:

- **Structured logging** - Emit newline-delimited JSON logs for ELK ingestion
- **Model customization** - Train a `RandomForestClassifier` on the breast cancer dataset
- **Metrics tracking** - Save metrics and top feature importances for later analysis
- **Testing** - Verify the training pipeline and generated artifacts with pytest

See [Lab6/README.md](Lab6/README.md) for setup, training, Logstash configuration, and ELK workflow steps.

---

## Project Structure

```
MLOps-labs/
├── .github/
│   └── workflows/
│       ├── github_lab1_pytest_action.yml   # Pytest CI workflow
│       ├── github_lab1_unittest_action.yml # Unittest CI workflow
│       ├── github_lab3_pytest_action.yml   # Lab 3 CI workflow
│       ├── github_lab4_pytest_action.yml   # Lab 4 CI workflow
│       └── github_lab6_pytest_action.yml   # Lab 6 CI workflow
├── Lab1/
│   ├── requirements.txt
│   ├── src/
│   │   ├── __init__.py
│   │   └── shopping_cart.py                # Shopping Cart application
│   └── test/
│       ├── pytest_test.py                  # Pytest tests
│       └── unittest_test.py                # Unittest tests
├── Lab2/
│   ├── main.tf                             # VPC, subnet, EC2, security group
│   ├── variables.tf
│   ├── outputs.tf
│   ├── terraform.tfvars.example
│   └── README.md                           # Lab 2 documentation
├── Lab3/
│   ├── src/
│   │   ├── main.py                         # Flask inference API
│   │   ├── predict.py                      # Prediction helpers
│   │   ├── test_api.py                     # API tests
│   │   └── train.py                        # Model training script
│   ├── model/                              # Saved model and metrics artifacts
│   ├── streamlit_app.py                    # Simple frontend for testing
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── .dockerignore
│   └── README.md                           # Lab 3 documentation
├── Lab4/
│   ├── main.py                             # HTTP Cloud Function handler
│   ├── requirements.txt
│   ├── sample_request.json                 # Example prediction payload
│   ├── tests/
│   │   └── test_main.py                    # Cloud Function tests
│   └── README.md                           # Lab 4 documentation
├── Lab5/
│   ├── src/
│   │   └── main.py                         # Train and evaluate the ML model
│   ├── outputs/                            # Generated metrics and model artifacts
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── .dockerignore
│   └── README.md                           # Lab 5 documentation
├── Lab6/
│   ├── artifacts/                          # Generated log and metrics artifacts
│   ├── logstash.conf                       # ELK ingestion configuration
│   ├── requirements.txt
│   ├── src/
│   │   └── train_model.py                  # ML training with JSON logging
│   ├── tests/
│   │   └── test_training.py                # Training pipeline tests
│   └── README.md                           # Lab 6 documentation
└── README.md
```

---