import json
from pathlib import Path

import joblib
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


BASE_DIR = Path(__file__).resolve().parents[1]
MODEL_DIR = BASE_DIR / "model"
MODEL_PATH = MODEL_DIR / "model.pkl"
METRICS_PATH = MODEL_DIR / "metrics.json"


def run_training() -> dict:
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data,
        iris.target,
        test_size=0.2,
        random_state=42,
        stratify=iris.target,
    )

    model = Pipeline(
        [
            ("scaler", StandardScaler()),
            ("classifier", LogisticRegression(max_iter=2000)),
        ]
    )
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    report = classification_report(y_test, predictions, output_dict=True)

    MODEL_DIR.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, MODEL_PATH)

    metrics = {
        "dataset": "iris",
        "model": "LogisticRegression with StandardScaler",
        "accuracy": accuracy,
        "target_names": iris.target_names.tolist(),
        "classification_report": report,
    }
    METRICS_PATH.write_text(json.dumps(metrics, indent=2), encoding="utf-8")

    return metrics


if __name__ == "__main__":
    saved_metrics = run_training()
    print(f"Saved model to: {MODEL_PATH}")
    print(f"Saved metrics to: {METRICS_PATH}")
    print(f"Accuracy: {saved_metrics['accuracy']:.4f}")
