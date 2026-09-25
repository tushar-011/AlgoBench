import json
import sqlite3
from pathlib import Path


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