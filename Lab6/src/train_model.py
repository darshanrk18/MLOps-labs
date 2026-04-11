import json
from pathlib import Path

from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from sklearn.model_selection import train_test_split


ARTIFACTS_DIR = Path(__file__).resolve().parents[1] / "artifacts"
LOG_PATH = ARTIFACTS_DIR / "training.log"
METRICS_PATH = ARTIFACTS_DIR / "metrics.json"


def _write_log(log_file, event_type: str, **payload) -> None:
    record = {"event_type": event_type, **payload}
    log_file.write(json.dumps(record) + "\n")


def run_training() -> dict:
    ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)

    dataset = load_breast_cancer()
    X_train, X_test, y_train, y_test = train_test_split(
        dataset.data,
        dataset.target,
        test_size=0.2,
        random_state=42,
        stratify=dataset.target,
    )

    model = RandomForestClassifier(
        n_estimators=300,
        max_depth=10,
        random_state=42,
    )

    with LOG_PATH.open("w", encoding="utf-8") as log_file:
        _write_log(
            log_file,
            "training_started",
            dataset="breast_cancer",
            model="RandomForestClassifier",
            feature_count=int(dataset.data.shape[1]),
        )
        _write_log(log_file, "data_split", train_samples=len(X_train), test_samples=len(X_test))

        model.fit(X_train, y_train)
        predictions = model.predict(X_test)

        metrics = {
            "dataset": "breast_cancer",
            "model": "RandomForestClassifier",
            "accuracy": round(float(accuracy_score(y_test, predictions)), 4),
            "f1_score": round(float(f1_score(y_test, predictions)), 4),
            "precision": round(float(precision_score(y_test, predictions)), 4),
            "recall": round(float(recall_score(y_test, predictions)), 4),
            "train_samples": int(len(X_train)),
            "test_samples": int(len(X_test)),
            "top_features": [
                {
                    "name": dataset.feature_names[index],
                    "importance": round(float(importance), 4),
                }
                for index, importance in sorted(
                    enumerate(model.feature_importances_),
                    key=lambda item: item[1],
                    reverse=True,
                )[:5]
            ],
        }

        _write_log(log_file, "training_completed", **metrics)
        for feature in metrics["top_features"]:
            _write_log(log_file, "feature_importance", **feature)

    METRICS_PATH.write_text(json.dumps(metrics, indent=2), encoding="utf-8")
    return metrics


if __name__ == "__main__":
    summary = run_training()
    print(json.dumps(summary, indent=2))
