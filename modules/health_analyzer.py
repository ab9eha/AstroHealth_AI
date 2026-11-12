from config import REFERENCE_RANGES


def analyze_reading(row):
    alerts = []

    checks = {
        "heart_rate": ("Heart rate", "bpm"),
        "spo2": ("Blood oxygen", "%"),
        "temperature": ("Body temperature", "°C"),
        "respiration": ("Respiration rate", "breaths/min"),
        "systolic": ("Systolic pressure", "mmHg"),
        "diastolic": ("Diastolic pressure", "mmHg"),
    }

    for key, (label, unit) in checks.items():
        value = float(row[key])
        low, high = REFERENCE_RANGES[key]

        if value < low:
            alerts.append({
                "indicator": label,
                "value": value,
                "unit": unit,
                "message": f"{label} is below the configured reference range.",
                "level": "Warning",
            })

        elif value > high:
            alerts.append({
                "indicator": label,
                "value": value,
                "unit": unit,
                "message": f"{label} is above the configured reference range.",
                "level": "Warning",
            })

    return alerts


def get_health_status(row, ai_anomaly=False):
    alerts = analyze_reading(row)

    if alerts:
        return "ATTENTION REQUIRED", "warning", alerts

    if ai_anomaly:
        return (
            "AI ANOMALY DETECTED",
            "info",
            [{
                "indicator": "AI pattern analysis",
                "value": 1,
                "unit": "flag",
                "message": "The machine-learning model identified an unusual pattern.",
                "level": "Info",
            }]
        )

    return "WITHIN REFERENCE", "success", []