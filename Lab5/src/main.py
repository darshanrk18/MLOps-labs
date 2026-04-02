import json
import os

import joblib
from sklearn.datasets import load_wine
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


if __name__ == "__main__":
    os.makedirs("outputs", exist_ok=True)

    wine = load_wine()
    X, y = wine.data, wine.target

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y,
    )

    model = Pipeline(
        [
            ("scaler", StandardScaler()),
            ("classifier", LogisticRegression(max_iter=2000)),
        ]
    )

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred, output_dict=True)

    model_path = "outputs/wine_model.pkl"
    joblib.dump(model, model_path)

    metrics = {
        "dataset": "wine",
        "model": "LogisticRegression with StandardScaler",
        "accuracy": accuracy,
        "classification_report": report,
    }

    metrics_path = "outputs/metrics.json"
    with open(metrics_path, "w") as f:
        json.dump(metrics, f, indent=2)

    print("Model training completed successfully.")
    print(f"Accuracy: {accuracy:.4f}")
    print(f"Saved model to: {model_path}")
    print(f"Saved metrics to: {metrics_path}")