import os

from flask import Flask, jsonify, request

from src.predict import get_metadata, predict_iris


app = Flask(__name__)
EXPECTED_FIELDS = ["sepal_length", "sepal_width", "petal_length", "petal_width"]


@app.get("/")
def index():
    return jsonify(
        {
            "message": "Iris prediction API is running.",
            "endpoints": ["/health", "/metadata", "/predict"],
        }
    )


@app.get("/health")
def health():
    return jsonify({"status": "ok"})


@app.get("/metadata")
def metadata():
    model_metadata = get_metadata()
    return jsonify(
        {
            "dataset": model_metadata["dataset"],
            "model": model_metadata["model"],
            "accuracy": model_metadata["accuracy"],
            "target_names": model_metadata["target_names"],
        }
    )


@app.post("/predict")
def predict():
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return jsonify({"error": "Request body must be valid JSON."}), 400

    missing_fields = [field for field in EXPECTED_FIELDS if field not in data]
    if missing_fields:
        return (
            jsonify(
                {
                    "error": "Missing required fields.",
                    "missing_fields": missing_fields,
                }
            ),
            400,
        )

    try:
        features = [float(data[field]) for field in EXPECTED_FIELDS]
    except (TypeError, ValueError):
        return jsonify({"error": "All feature values must be numeric."}), 400

    result = predict_iris(features)
    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
