import sqlite3
import json
from models import Tag
from models import Location
from models import Customer


def get_all_tags():

    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.location_id,
            a.customer_id,
            l.name location_name,
            l.address location_address
        FROM Tag a
        JOIN Location l
            ON l.id = a.location_id
        JOIN Customer c
            ON c.id = l.location_id
        """)
        tags = []
        dataset = db_cursor.fetchall()
        for row in dataset:
            tag = Tag(row['id'], row['name'], row['breed'], row['status'],
                            row['location_id'], row['customer_id'])
            location = Location(row['location_id'], row['location_name'], row['location_address'])
            customer = Customer(row['customer_id']), row['customer_name'], row['customer_address'], row['customer_email'], row['customer_password']
            tag.location = location.__dict__
            tags.append(tag.__dict__)
    return json.dumps(tags)



def get_single_tag(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.location_id,
            a.customer_id
        FROM Tag a
        WHERE a.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()

       
        tag = tag(data['id'], data['name'], data['breed'],
                            data['status'], data['location_id'],
                            data['customer_id'])

        return json.dumps(tag.__dict__)


def create_tag(new_tag):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Tag
            ( name, status, breed, customer_id, location_id )
        VALUES
            ( ?, ?, ?, ?, ?);
        """, (new_tag['name'], new_tag['status'],
              new_tag['breed'], new_tag['customer_id'],
              new_tag['location_id'], ))
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
                name = ?,
                breed = ?,
                status = ?,
                location_id = ?,
                customer_id = ?
        WHERE id = ?
        """, (new_tag['name'], new_tag['breed'],
              new_tag['status'], new_tag['location_id'],
              new_tag['customer_id'], id, ))

        # Were any rows affected?
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True


