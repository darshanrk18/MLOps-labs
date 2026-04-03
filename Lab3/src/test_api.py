from src.main import app


def test_health_endpoint():
    client = app.test_client()
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_metadata_endpoint():
    client = app.test_client()
    response = client.get("/metadata")
    payload = response.get_json()

    assert response.status_code == 200
    assert payload["dataset"] == "iris"
    assert "accuracy" in payload
    assert payload["model"] == "LogisticRegression with StandardScaler"


def test_predict_endpoint_returns_prediction_and_confidence():
    client = app.test_client()
    response = client.post(
        "/predict",
        json={
            "sepal_length": 5.1,
            "sepal_width": 3.5,
            "petal_length": 1.4,
            "petal_width": 0.2,
        },
    )
    payload = response.get_json()

    assert response.status_code == 200
    assert payload["prediction"] in {"setosa", "versicolor", "virginica"}
    assert 0 <= payload["confidence"] <= 1
    assert set(payload["probabilities"].keys()) == {
        "setosa",
        "versicolor",
        "virginica",
    }


def test_predict_endpoint_validates_missing_fields():
    client = app.test_client()
    response = client.post(
        "/predict",
        json={
            "sepal_length": 5.1,
            "sepal_width": 3.5,
        },
    )

    assert response.status_code == 400
    assert "missing_fields" in response.get_json()
