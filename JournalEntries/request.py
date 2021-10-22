import sqlite3
import json
from models import Entry



def get_all_entries():

    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            a.id,
            a.subject,
            a.date,
            a.feeling,
            a.moods_id,
            a.tags_id
            a.time_spent
        """)
        entries = []
        dataset = db_cursor.fetchall()
        for row in dataset:
            entry = entry(row['id'], row['subject'], row['date'], row['feeling'],
                            row['moods_id'], row['tags_id'], row['time_spent'])
            entries.append(entry.__dict__)
    return json.dumps(entries)



def get_single_entry(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            a.id,
            a.subject,
            a.date,
            a.feeling,
            a.moods_id,
            a.tags_id
            a.time_spent
        FROM Entry a
        WHERE a.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()

       
        entry = Entry(data['id'], data['subject'], data['date'],
                            data['feeling'], data['moods_id'],
                            data['tags_id'], row['time_spent'])

        return json.dumps(entry.__dict__)


def create_entry(new_entry):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO entry
            ( subject, feeling, date, tags_id, moods_id )
        VALUES
            ( ?, ?, ?, ?, ?);
        """, (new_entry['subject'], new_entry['feeling'],
              new_entry['date'], new_entry['tags_id'],
              new_entry['moods_id'], new_entry['time_spent'] ))
        id = db_cursor.lastrowid
        new_entry['id'] = id


    return json.dumps(new_entry)


def delete_entry(id):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM entry
        WHERE id = ?
        """, (id, ))



def update_entry(id, new_entry):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Entry
            SET
                subject = ?,
                date = ?,
                feeling = ?,
                moods_id = ?,
                tags_id = ?
                time_spent = ?
        WHERE id = ?
        """, (new_entry['subject'], new_entry['date'],
              new_entry['feeling'], new_entry['moods_id'],
              new_entry['tags_id'], new_entry['time_spent'] (id, ))

        # Were any rows affected?
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True


