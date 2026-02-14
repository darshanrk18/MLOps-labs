# MLOps Labs

A comprehensive repository containing all lab exercises for the MLOps course.

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
└── README.md
```

---

## Shopping Cart Application

A simple shopping cart that tracks items, prices and quantities.

### API

| Method | Description |
|--------|-------------|
| `add_item(name, price, quantity=1)` | Add an item. Duplicates increment quantity. |
| `remove_item(name)` | Remove an item. Returns `True` if found. |
| `update_quantity(name, quantity)` | Update quantity. Set to 0 to remove. |
| `get_subtotal()` | Total price of all items. |
| `get_item_count()` | Total number of items (sum of quantities). |
| `get_items()` | Copy of all items. |
| `clear()` | Remove all items. |

### Example

```python
from src.shopping_cart import ShoppingCart

cart = ShoppingCart()
cart.add_item("Apple", 1.50, 3)
cart.add_item("Bread", 2.50)
print(cart.get_subtotal())   # 7.0
print(cart.get_item_count()) # 4
```

---

## Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

```bash
cd Lab1
pip install -r requirements.txt
```

---

## Running Tests

### Pytest

From the repository root:

```bash
PYTHONPATH=Lab1 pytest Lab1/test/ -v
```

From the `Lab1` directory:

```bash
cd Lab1
pytest test/ -v
```

### Unittest

From the repository root:

```bash
python -m unittest Lab1.test.unittest_test -v
```

Or using the file path:

```bash
python -m unittest Lab1/test/unittest_test.py
```

---

## CI/CD — GitHub Actions

Two workflows run automatically on push to `main`:

| Workflow | Trigger | Description |
|----------|---------|-------------|
| **Pytest** | Push to `main` or `releases/**`; label created; issue opened/labeled | Runs pytest, uploads JUnit XML report as artifact |
| **Unittest** | Push to `main` | Runs Python unittest suite |

Test results appear in the **Actions** tab. The Pytest workflow uploads `pytest-report.xml` as an artifact for downstream tooling.
