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
            a.name,
            a.breed,
            a.status,
            a.location_id,
            a.customer_id,
            l.name location_name,
            l.address location_address
        FROM entry a
        JOIN Location l
            ON l.id = a.location_id
        JOIN Customer c
            ON c.id = l.location_id
        """)
        entries = []
        dataset = db_cursor.fetchall()
        for row in dataset:
            entry = entry(row['id'], row['name'], row['breed'], row['status'],
                            row['location_id'], row['customer_id'])
            location = Location(row['location_id'], row['location_name'], row['location_address'])
            customer = Customer(row['customer_id']), row['customer_name'], row['customer_address'], row['customer_email'], row['customer_password']
            entry.location = location.__dict__
            entries.append(entry.__dict__)
    return json.dumps(entries)



def get_single_entry(id):
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
        FROM entry a
        WHERE a.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()

       
        entry = entry(data['id'], data['name'], data['breed'],
                            data['status'], data['location_id'],
                            data['customer_id'])

        return json.dumps(entry.__dict__)


def create_entry(new_entry):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO entry
            ( name, status, breed, customer_id, location_id )
        VALUES
            ( ?, ?, ?, ?, ?);
        """, (new_entry['name'], new_entry['status'],
              new_entry['breed'], new_entry['customer_id'],
              new_entry['location_id'], ))
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
        UPDATE entry
            SET
                name = ?,
                breed = ?,
                status = ?,
                location_id = ?,
                customer_id = ?
        WHERE id = ?
        """, (new_entry['name'], new_entry['breed'],
              new_entry['status'], new_entry['location_id'],
              new_entry['customer_id'], id, ))

        # Were any rows affected?
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True


