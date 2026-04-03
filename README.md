# MLOps Labs

Repository for MLOps course labs. Each lab lives in its own folder with a dedicated `README.md`.

## Current Submission

This repository's Lab Assignment 5 submission is in `Lab5/`.

- Lab folder: [`Lab5/`](Lab5/)
- Lab documentation: [`Lab5/README.md`](Lab5/README.md)
- Customizations from the original lab: Wine dataset, Logistic Regression, feature scaling, and saved model metrics

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

## Lab 5: Dockerized ML Workflow

Containerized machine learning workflow that trains and evaluates a classifier inside Docker. This lab covers:

- **Docker packaging** - Build a reproducible ML runtime with a `Dockerfile`
- **Model training** - Train a scikit-learn classifier from a Python entrypoint
- **Artifact generation** - Save evaluation metrics and the trained model to `outputs/`
- **Customization** - Uses the Wine dataset with `LogisticRegression` and `StandardScaler`

See [Lab5/README.md](Lab5/README.md) for setup, run instructions, and submission details.

---

## Project Structure

```
MLOps-labs/
├── .github/
│   └── workflows/
│       ├── github_lab1_pytest_action.yml   # Pytest CI workflow
│       └── github_lab1_unittest_action.yml # Unittest CI workflow
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
├── Lab5/
│   ├── src/
│   │   └── main.py                         # Train and evaluate the ML model
│   ├── outputs/                            # Generated metrics and model artifacts
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── .dockerignore
│   └── README.md                           # Lab 5 documentation
└── README.md
```

---

## Notes

- `Lab3/` is the lab prepared for assignment submission.
- Each lab folder contains its own setup instructions and implementation details.
- For the grader, the most relevant entry points are the root `README.md`, `Lab3/README.md`, and the deployed Cloud Run URL.
