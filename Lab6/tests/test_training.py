import json
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from train_model import LOG_PATH, METRICS_PATH, run_training


def test_run_training_creates_metrics_and_logs():
    metrics = run_training()

    assert metrics["dataset"] == "breast_cancer"
    assert metrics["model"] == "RandomForestClassifier"
    assert metrics["accuracy"] >= 0.9
    assert len(metrics["top_features"]) == 5

    assert METRICS_PATH.exists()
    assert LOG_PATH.exists()

    saved_metrics = json.loads(METRICS_PATH.read_text(encoding="utf-8"))
    assert saved_metrics["accuracy"] == metrics["accuracy"]

    log_lines = [
        json.loads(line)
        for line in LOG_PATH.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    event_types = [entry["event_type"] for entry in log_lines]

    assert "training_started" in event_types
    assert "data_split" in event_types
    assert "training_completed" in event_types
    assert event_types.count("feature_importance") == 5
