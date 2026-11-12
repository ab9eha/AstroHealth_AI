import numpy as np
import pandas as pd


FEATURES = [
    "heart_rate",
    "spo2",
    "temperature",
    "respiration",
    "systolic",
    "diastolic",
    "activity",
]


def generate_health_data(rows=300, seed=42):
    """Generate synthetic astronaut health-monitoring data."""

    rng = np.random.default_rng(seed)

    timestamps = pd.date_range(
        end=pd.Timestamp.now().floor("min"),
        periods=rows,
        freq="5min"
    )

    heart_rate = rng.normal(72, 5, rows)
    spo2 = rng.normal(98, 0.7, rows)
    temperature = rng.normal(36.8, 0.2, rows)
    respiration = rng.normal(16, 1.8, rows)
    systolic = rng.normal(115, 7, rows)
    diastolic = rng.normal(75, 5, rows)
    activity = rng.uniform(0, 100, rows)

    # Introduce controlled unusual readings for AI demonstration.
    if rows > 40:
        anomaly_indices = rng.choice(
            np.arange(20, rows - 20),
            size=max(5, rows // 30),
            replace=False
        )

        for index in anomaly_indices:
            anomaly_type = rng.choice(
                ["high_hr", "low_spo2", "high_temp"]
            )

            if anomaly_type == "high_hr":
                heart_rate[index] = rng.uniform(115, 145)

            elif anomaly_type == "low_spo2":
                spo2[index] = rng.uniform(87, 92)

            else:
                temperature[index] = rng.uniform(38.0, 39.0)

    return pd.DataFrame({
        "timestamp": timestamps,
        "heart_rate": np.clip(heart_rate, 35, 180),
        "spo2": np.clip(spo2, 80, 100),
        "temperature": np.clip(temperature, 34, 41),
        "respiration": np.clip(respiration, 5, 40),
        "systolic": np.clip(systolic, 70, 190),
        "diastolic": np.clip(diastolic, 40, 120),
        "activity": np.clip(activity, 0, 100),
    })


def validate_uploaded_data(df):
    """Validate and clean an uploaded health-monitoring CSV."""

    required_columns = [
        "timestamp",
        "heart_rate",
        "spo2",
        "temperature",
        "respiration",
        "systolic",
        "diastolic",
        "activity",
    ]

    missing = [
        column for column in required_columns
        if column not in df.columns
    ]

    if missing:
        raise ValueError(
            "Missing required columns: " + ", ".join(missing)
        )

    cleaned = df[required_columns].copy()

    cleaned["timestamp"] = pd.to_datetime(
        cleaned["timestamp"],
        errors="coerce"
    )

    numeric_columns = required_columns[1:]

    for column in numeric_columns:
        cleaned[column] = pd.to_numeric(
            cleaned[column],
            errors="coerce"
        )

    cleaned = cleaned.dropna().sort_values("timestamp")

    if cleaned.empty:
        raise ValueError(
            "The uploaded dataset contains no valid readings."
        )

    return cleaned.reset_index(drop=True)