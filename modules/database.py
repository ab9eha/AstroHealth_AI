import sqlite3
import pandas as pd

from config import DATABASE_PATH


def get_connection():
    return sqlite3.connect(DATABASE_PATH)


def initialize_database():
    with get_connection() as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS alerts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                indicator TEXT,
                value REAL,
                unit TEXT,
                level TEXT,
                message TEXT
            )
        """)


def save_alerts(alerts, timestamp):
    if not alerts:
        return

    with get_connection() as connection:
        for alert in alerts:
            connection.execute("""
                INSERT INTO alerts
                (timestamp, indicator, value, unit, level, message)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                str(timestamp),
                alert["indicator"],
                float(alert["value"]),
                alert["unit"],
                alert["level"],
                alert["message"],
            ))


def get_alert_history(limit=100):
    with get_connection() as connection:
        cursor = connection.execute("""
            SELECT timestamp, indicator, value, unit, level, message
            FROM alerts
            ORDER BY id DESC
            LIMIT ?
        """, (limit,))

        columns = [
            "timestamp",
            "indicator",
            "value",
            "unit",
            "level",
            "message",
        ]

        return pd.DataFrame(
            cursor.fetchall(),
            columns=columns
        )


def clear_alert_history():
    with get_connection() as connection:
        connection.execute("DELETE FROM alerts")