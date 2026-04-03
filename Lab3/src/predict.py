import json
from pathlib import Path

import joblib
import numpy as np

from src.train import METRICS_PATH, MODEL_PATH, run_training


LABELS = ["setosa", "versicolor", "virginica"]
_model = None


def _load_model():
    global _model
    if _model is None:
        if not MODEL_PATH.exists():
            run_training()
        _model = joblib.load(MODEL_PATH)
    return _model


def predict_iris(features: list[float]) -> dict:
    model = _load_model()
    input_data = np.array([features], dtype=float)

    predicted_index = int(model.predict(input_data)[0])
    probabilities = model.predict_proba(input_data)[0]

    return {
        "prediction": LABELS[predicted_index],
        "predicted_index": predicted_index,
        "confidence": round(float(np.max(probabilities)), 4),
        "probabilities": {
            label: round(float(probabilities[index]), 4)
            for index, label in enumerate(LABELS)
        },
    }


def get_metadata() -> dict:
    if not METRICS_PATH.exists():
        run_training()
    return json.loads(METRICS_PATH.read_text(encoding="utf-8"))
