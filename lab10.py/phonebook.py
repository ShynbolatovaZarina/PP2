import psycopg2
import csv
import sys

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="phonebook_db",
        user="postgres",
        password="password"   # ← сюда поставь пароль!!!
    )

 
import psycopg2
from config import load_config
import csv
 
 
def create_tables():
    sql = """
    CREATE TABLE IF NOT EXISTS phonebook (
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(50) NOT NULL,
        last_name VARCHAR(50),
        phone VARCHAR(20) NOT NULL
    );
    """
    config = load_config(r"C:\Users\shynb\OneDrive\Документы\GitHub\PP2\lab10.py\database.ini")
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute(sql)
        conn.commit()
 
 
def list_users():
    config = load_config(r"C:\Users\shynb\OneDrive\Документы\GitHub\PP2\lab10.py\database.ini")
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id, first_name, last_name, phone FROM phonebook ORDER BY id")
            rows = cur.fetchall()
            for row in rows:
                print(row)
 
 
def insert_user(first_name, last_name, phone):
    sql = "INSERT INTO phonebook(first_name, last_name, phone) VALUES (%s,%s,%s) RETURNING id"
    config = load_config(r"C:\Users\shynb\OneDrive\Документы\GitHub\PP2\lab10.py\database.ini")
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute(sql, (first_name, last_name, phone))
            user_id = cur.fetchone()[0]
        conn.commit()
        return user_id
 
 
def insert_from_csv(path):
    with open(path, encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader, None)
        for first_name, last_name, phone in reader:
            insert_user(first_name, last_name, phone)
 
 
def delete_by_name(first_name):
    sql = "DELETE FROM phonebook WHERE first_name = %s"
    config = load_config(r"C:\Users\shynb\OneDrive\Документы\GitHub\PP2\lab10.py\database.ini")
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute(sql, (first_name,))
            deleted = cur.rowcount
        conn.commit()
    return deleted
 
 
def run_custom_sql():
    config = load_config(r"C:\Users\shynb\OneDrive\Документы\GitHub\PP2\lab10.py\database.ini")
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            while True:
                q = input("SQL > ").strip()
                if q.lower() == "exit":
                    break
                try:
                    cur.execute(q)
 
                    if cur.description:
                        for r in cur.fetchall():
                            print(r)
                    else:
                        conn.commit()
                        print("ok")
                except Exception as e:
                    print("error:", e)
 
 
def main():
    create_tables()
 
    while True:
        print("""
1 - show all
2 - insert mannually
3 - load csv
4 - delete by name
5 - your sql
0 - exit
""")
        c = input("choice: ")
 
        if c == "1":
            list_users()
        elif c == "2":
            fn = input("name: ")
            ln = input("sur name: ")
            ph = input("phone number: ")
            print("ID:", insert_user(fn, ln, ph))
        elif c == "3":
            path = input("path to csv: ")
            insert_from_csv(path)
        elif c == "4":
            name = input("name: ")
            print("deleted:", delete_by_name(name))
        elif c == "5":
            run_custom_sql()
        elif c == "0":
            break
 
 
if __name__ == "__main__":
    main()
 