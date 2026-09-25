import json
import os
import sqlite3
from pathlib import Path


APP_DATA_DIR = (
    Path(
        os.getenv(
            "LOCALAPPDATA",
            Path.home()
        )
    )
    / "AlgoBench"
)

APP_DATA_DIR.mkdir(
    parents=True,
    exist_ok=True
)

DATABASE_PATH = (
    APP_DATA_DIR
    / "algobench.db"
)

DATABASE_PATH = (
    Path(__file__).resolve().parent.parent
    / "algobench.db"
)


def get_connection():
    return sqlite3.connect(
        DATABASE_PATH
    )


def initialize_database():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS test_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            test_type TEXT NOT NULL,
            mode TEXT,
            score INTEGER,
            result TEXT,
            details TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """
    )

    connection.commit()
    connection.close()

    initialize_settings()


def initialize_settings():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS app_settings (
            setting_key TEXT PRIMARY KEY,
            setting_value TEXT NOT NULL
        )
        """
    )

    default_settings = {
        "appearance": "Dark",
        "refresh_rate": "1"
    }

    for key, value in default_settings.items():

        cursor.execute(
            """
            INSERT OR IGNORE INTO app_settings (
                setting_key,
                setting_value
            )
            VALUES (?, ?)
            """,
            (
                key,
                value
            )
        )

    connection.commit()
    connection.close()


def save_test_result(
    test_type,
    mode=None,
    score=None,
    result=None,
    details=None
):

    connection = get_connection()
    cursor = connection.cursor()

    details_json = json.dumps(
        details or {}
    )

    cursor.execute(
        """
        INSERT INTO test_history (
            test_type,
            mode,
            score,
            result,
            details
        )
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            test_type,
            mode,
            score,
            result,
            details_json
        )
    )

    connection.commit()
    connection.close()


def get_test_history():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT
            id,
            test_type,
            mode,
            score,
            result,
            created_at
        FROM test_history
        ORDER BY id DESC
        """
    )

    rows = cursor.fetchall()

    connection.close()

    return rows


def clear_test_history():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        DELETE FROM test_history
        """
    )

    connection.commit()
    connection.close()


def save_setting(
    key,
    value
):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO app_settings (
            setting_key,
            setting_value
        )
        VALUES (?, ?)

        ON CONFLICT(setting_key)
        DO UPDATE SET
            setting_value = excluded.setting_value
        """,
        (
            key,
            str(value)
        )
    )

    connection.commit()
    connection.close()


def get_setting(
    key,
    default=None
):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT setting_value
        FROM app_settings
        WHERE setting_key = ?
        """,
        (
            key,
        )
    )

    row = cursor.fetchone()

    connection.close()

    if row:
        return row[0]

    return default