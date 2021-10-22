import sqlite3
import json
from models import Mood


def get_all_moods():

    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            a.id,
            a.type,
        """)
        moods = []
        dataset = db_cursor.fetchall()
        for row in dataset:
            mood = Mood(row['id'], row['type'])
            moods.append(mood.__dict__)
    return json.dumps(moods)



def get_single_mood(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            a.id,
            a.type,
        FROM mood a
        WHERE a.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()

       
        mood = Mood(data['id'], data['type'])

        return json.dumps(mood.__dict__)


def create_mood(new_mood):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO mood
            ( type )
        VALUES
            ( ?, ?, ?, ?, ?);
        """, (new_mood['type'], ))
        id = db_cursor.lastrowid
        new_mood['id'] = id


    return json.dumps(new_mood)


def delete_mood(id):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM mood
        WHERE id = ?
        """, (id, ))



def update_mood(id, new_mood):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Mood
            SET
                type = ?,
                
        WHERE id = ?
        """, (new_mood['type'], id, ))

        # Were any rows affected?
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True


