import sqlite3
import json

def get_connection():
    return sqlite3.connect("pivotforge.db")

create_table_sql = """
CREATE TABLE IF NOT EXISTS comps (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    comp_name TEXT NOT NULL UNIQUE,
    playstyle TEXT NOT NULL,
    traits TEXT NOT NULL,
    core_units TEXT NOT NULL,
    flex_units TEXT,
    item_priority TEXT NOT NULL,
    main_carry TEXT NOT NULL
);
"""

def create_schema():
    conn = get_connection()

    try:
        conn.execute(create_table_sql)
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()

def add_comp(
    comp_name,
    playstyle,
    traits,
    core_units,
    flex_units,
    item_priority,
    main_carry,
):
    conn = get_connection()

    try:
        conn.execute(
            """
            INSERT INTO comps (
                comp_name,
                playstyle,
                traits,
                core_units,
                flex_units,
                item_priority,
                main_carry
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                comp_name,
                playstyle,
                json.dumps(traits),
                json.dumps(core_units),
                json.dumps(flex_units),
                json.dumps(item_priority),
                main_carry,
            ),
        )

        conn.commit()

    except Exception:
        conn.rollback()
        raise

    finally:
        conn.close()

def get_comp(comp_name):
    conn = get_connection()

    try:
        cursor = conn.execute(
            """
            SELECT comp_name, playstyle, traits, core_units,
                   flex_units, item_priority, main_carry
            FROM comps
            WHERE comp_name = ?
            """,
            (comp_name,),
        )

        row = cursor.fetchone()

        if row is None:
            return None

        return {
            "comp_name": row[0],
            "playstyle": row[1],
            "traits": json.loads(row[2]),
            "core_units": json.loads(row[3]),
            "flex_units": json.loads(row[4]) if row[4] is not None else [],
            "item_priority": json.loads(row[5]),
            "main_carry": row[6],
        }

    finally:
        conn.close()

def get_all_comps():
    conn = get_connection()

    try:
        cursor = conn.execute(
            """
            SELECT comp_name, playstyle, traits, core_units,
                   flex_units, item_priority, main_carry
            FROM comps
            """
        )

        rows = cursor.fetchall()

        comps = []

        for row in rows:
            comps.append({
                "comp_name": row[0],
                "playstyle": row[1],
                "traits": json.loads(row[2]),
                "core_units": json.loads(row[3]),
                "flex_units": json.loads(row[4]) if row[4] is not None else [],
                "item_priority": json.loads(row[5]),
                "main_carry": row[6],
            })

        return comps

    finally:
        conn.close()

if __name__ == "__main__":
    create_schema()

    comp = get_comp("Test Inferno")
    print("One comp:")
    print(comp)

    comps = get_all_comps()
    print("\nAll comps:")
    print(comps)