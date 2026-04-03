import re
from functools import lru_cache

from flask import jsonify
from sklearn.datasets import load_wine
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


def _slugify_feature_name(name: str) -> str:
    normalized = re.sub(r"[^a-z0-9]+", "_", name.lower())
    return normalized.strip("_")


@lru_cache(maxsize=1)
def _load_model_artifact() -> dict:
    dataset = load_wine()
    features = dataset.data
    target = dataset.target

    feature_names = [_slugify_feature_name(name) for name in dataset.feature_names]

    X_train, X_test, y_train, y_test = train_test_split(
        features,
        target,
        test_size=0.2,
        random_state=42,
        stratify=target,
    )

    model = RandomForestClassifier(
        n_estimators=250,
        max_depth=8,
        random_state=42,
    )
    model.fit(X_train, y_train)

    accuracy = accuracy_score(y_test, model.predict(X_test))
    class_labels = list(dataset.target_names)

    return {
        "dataset_name": "wine",
        "feature_names": feature_names,
        "class_labels": class_labels,
        "model": model,
        "accuracy": round(float(accuracy), 4),
    }


def _build_example_payload(feature_names: list[str]) -> dict:
    example_values = [13.2, 2.1, 2.4, 16.8, 101, 2.7, 2.9, 0.28, 1.95, 5.4, 1.02, 3.1, 1100]
    return {name: value for name, value in zip(feature_names, example_values)}


def _normalize_features(payload: dict, feature_names: list[str]) -> list[float]:
    if "features" in payload:
        raw_features = payload["features"]
        if not isinstance(raw_features, list):
            raise ValueError("'features' must be a list of numeric values.")
        if len(raw_features) != len(feature_names):
            raise ValueError(
                f"'features' must contain exactly {len(feature_names)} values."
            )
        try:
            return [float(value) for value in raw_features]
        except (TypeError, ValueError) as exc:
            raise ValueError("All feature values must be numeric.") from exc

    missing_fields = [name for name in feature_names if name not in payload]
    if missing_fields:
        raise KeyError(
            "Missing required feature fields: " + ", ".join(missing_fields)
        )

    try:
        return [float(payload[name]) for name in feature_names]
    except (TypeError, ValueError) as exc:
        raise ValueError("All feature values must be numeric.") from exc


def wine_quality_predictor(request):
    artifact = _load_model_artifact()
    feature_names = artifact["feature_names"]

    if request.method == "GET":
        return jsonify(
            {
                "message": "Wine classification Cloud Function is running.",
                "dataset": artifact["dataset_name"],
                "model_type": "RandomForestClassifier",
                "accuracy": artifact["accuracy"],
                "class_labels": artifact["class_labels"],
                "expected_features": feature_names,
                "example_payload": _build_example_payload(feature_names),
            }
        )

    if request.method != "POST":
        return jsonify({"error": "Only GET and POST are supported."}), 405

    payload = request.get_json(silent=True)
    if not isinstance(payload, dict):
        return jsonify({"error": "Request body must be valid JSON."}), 400

    try:
        features = _normalize_features(payload, feature_names)
    except KeyError as exc:
        return jsonify({"error": str(exc)}), 400
    except ValueError as exc:
        return jsonify({"error": str(exc)}), 400

    probabilities = artifact["model"].predict_proba([features])[0]
    predicted_index = int(artifact["model"].predict([features])[0])

    return jsonify(
        {
            "prediction": artifact["class_labels"][predicted_index],
            "predicted_index": predicted_index,
            "class_probabilities": {
                label: round(float(probability), 4)
                for label, probability in zip(artifact["class_labels"], probabilities)
            },
        }
    )
