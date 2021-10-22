import sqlite3
import json
from models import Tag


def get_all_tags():

    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            a.id,
            a.type
        """)
        tags = []
        dataset = db_cursor.fetchall()
        for row in dataset:
            tag = Tag(row['id'], row['type'])
            tags.append(tag.__dict__)
    return json.dumps(tags)



def get_single_tag(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            a.id,
            a.type
        FROM Tag a
        WHERE a.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()

       
        tag = tag(data['id'], data['type'])

        return json.dumps(tag.__dict__)


def create_tag(new_tag):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Tag
            ( type )
        VALUES
            ( ?, ?, ?, ?, ?);
        """, (new_tag['type'] ))
        id = db_cursor.lastrowid
        new_tag['id'] = id


    return json.dumps(new_tag)


def delete_tag(id):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM tag
        WHERE id = ?
        """, (id, ))



def update_tag(id, new_tag):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Tag
            SET
                type = ?,
                
        WHERE id = ?
        """, (new_tag['type'], id, ))

        # Were any rows affected?
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True


