import psycopg2
from config import load_config


def get_conn():
    return psycopg2.connect(**load_config())


def create_snake_tables():
    commands = (
        """
        CREATE TABLE IF NOT EXISTS game_user (
            id SERIAL PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS user_score (
            id SERIAL PRIMARY KEY,
            user_id INTEGER NOT NULL REFERENCES game_user(id) ON DELETE CASCADE,
            score INTEGER NOT NULL,
            level INTEGER NOT NULL,
            created_at TIMESTAMP DEFAULT NOW()
        )
        """
    )
    with get_conn() as conn:
        with conn.cursor() as cur:
            for cmd in commands:
                cur.execute(cmd)
        conn.commit()


def get_or_create_user(username: str) -> int:
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id FROM game_user WHERE username = %s", (username,))
            row = cur.fetchone()
            if row:
                return row[0]

            cur.execute(
                "INSERT INTO game_user(username) VALUES (%s) RETURNING id",
                (username,)
            )
            user_id = cur.fetchone()[0]
        conn.commit()
    return user_id


def get_current_level(user_id: int) -> int:
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT COALESCE(MAX(level), 1) FROM user_score WHERE user_id = %s",
                (user_id,)
            )
            level = cur.fetchone()[0]
    return level


def save_score(user_id: int, level: int, score: int):
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO user_score(user_id, level, score)
                VALUES (%s, %s, %s)
                """,
                (user_id, level, score)
            )
        conn.commit()

