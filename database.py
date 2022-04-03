import sqlite3
from sqlite3 import Error, Connection
import os


def connect() -> Connection | None:
    """Get connection to DB"""

    conn = existOrCreateDB()
    if not conn:
        try:
            conn = sqlite3.connect('test_task.db')
        except Error as e:
            print(e)

    return conn


def existOrCreateDB() -> Connection | None:
    """Check of existence of DB file"""

    if os.path.exists('test_task.db'):
        return None
    else:
        try:
            conn = sqlite3.connect('test_task.db')
        except Error as e:
            print(e)
            return None

        cursor = conn.cursor()

        with open('script.sql', 'r', encoding="utf-8") as file:
            script = file.read()
            if script != '':
                cursor.executescript(script)
                conn.commit()

        return conn


def insertUser(data: list, conn: Connection):
    """Insert data about user into DB"""

    cursor = conn.cursor()
    cursor.execute(f"""
        INSERT INTO users (
            second_name,
            first_name,
            patronymic,
            region_id,
            city_id,
            phone,
            email
        ) VALUES (
            '{data[0]}',
            '{data[1]}',
            '{data[2]}',
            (SELECT id FROM regions WHERE region_name='{data[3]}'),
            (SELECT id FROM cities WHERE city_name='{data[4]}'),
            '{data[5]}',
            '{data[6]}'
        )
    """)


def getUsers(conn: Connection) -> list:
    """Get data about users from DB"""

    cursor = conn.cursor()

    return cursor.execute("""
        SELECT
            second_name,
            first_name,
            patronymic,
            (SELECT region_name FROM regions WHERE regions.id=users.region_id),
            (SELECT city_name FROM cities WHERE cities.id=users.city_id),
            phone,
            email
        FROM users
    """).fetchall()
