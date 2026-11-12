APP_NAME = "ASTROHEALTH AI"
APP_VERSION = "1.0.0"

MISSION_NAME = "ORBITAL HEALTH MONITORING"
MISSION_ID = "AH-2026-01"

ASTRONAUT = {
    "name": "Commander Alex Morgan",
    "id": "AST-001",
    "role": "Mission Specialist",
    "mission_day": 127,
    "destination": "Low Earth Orbit",
}

DATABASE_PATH = "astrohealth.db"

# Educational demonstration ranges, not medical diagnostic thresholds.
REFERENCE_RANGES = {
    "heart_rate": (50, 100),
    "spo2": (95, 100),
    "temperature": (36.0, 37.5),
    "respiration": (12, 20),
    "systolic": (90, 120),
    "diastolic": (60, 80),
}

COLORS = {
    "background": "#07111F",
    "panel": "#101D30",
    "panel_light": "#172840",
    "cyan": "#39D5F6",
    "blue": "#648BFF",
    "purple": "#A78BFA",
    "green": "#35D39A",
    "yellow": "#F5C66A",
    "red": "#FF657A",
    "text": "#E8F0FC",
    "muted": "#91A3BA",
}