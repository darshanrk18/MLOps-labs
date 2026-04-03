from pathlib import Path
import sys

from flask import Flask, request

sys.path.append(str(Path(__file__).resolve().parents[1]))

from main import _load_model_artifact, wine_quality_predictor


app = Flask(__name__)


def invoke_function(method: str, json_payload=None):
    with app.test_request_context("/", method=method, json=json_payload):
        result = wine_quality_predictor(request)
        if isinstance(result, tuple):
            response, status_code = result
            return response, status_code
        return result, result.status_code


def test_get_returns_metadata():
    response, status_code = invoke_function("GET")

    assert status_code == 200
    payload = response.get_json()

    assert payload["dataset"] == "wine"
    assert payload["model_type"] == "RandomForestClassifier"
    assert len(payload["expected_features"]) == 13


def test_post_predicts_from_named_feature_payload():
    artifact = _load_model_artifact()
    payload = {name: 1.0 for name in artifact["feature_names"]}

    response, status_code = invoke_function("POST", json_payload=payload)

    assert status_code == 200
    prediction = response.get_json()

    assert prediction["prediction"] in artifact["class_labels"]
    assert set(prediction["class_probabilities"]) == set(artifact["class_labels"])


def test_post_rejects_missing_fields():
    response, status_code = invoke_function("POST", json_payload={"alcohol": 13.5})

    assert status_code == 400
    assert "Missing required feature fields" in response.get_json()["error"]


def test_post_rejects_non_json_requests():
    with app.test_request_context("/", method="POST", data="not json"):
        result = wine_quality_predictor(request)
        if isinstance(result, tuple):
            response, status_code = result
        else:
            response = result
            status_code = result.status_code

    assert status_code == 400
    assert response.get_json()["error"] == "Request body must be valid JSON."
