import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest

FEATURES = [
    "heart_rate",
    "spo2",
    "temperature",
    "respiration",
    "systolic",
    "diastolic",
    "activity",
]


def detect_anomalies(df):
    result = df.copy()

    if len(result) < 10:
        result["ai_anomaly"] = 0
        result["anomaly_score"] = 0.0
        return result

    model = IsolationForest(
        n_estimators=150,
        contamination=0.04,
        random_state=42
    )

    model.fit(result[FEATURES])

    predictions = model.predict(result[FEATURES])

    result["ai_anomaly"] = np.where(
        predictions == -1, 1, 0
    )

    result["anomaly_score"] = -model.decision_function(
        result[FEATURES]
    )

    return result


def get_anomaly_summary(df):
    total = len(df)
    anomalies = int(df["ai_anomaly"].sum())

    return {
        "total_readings": total,
        "anomalies": anomalies,
        "normal": total - anomalies,
        "anomaly_rate": (
            anomalies / total * 100 if total else 0
        ),
    }