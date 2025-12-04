import psycopg2
import csv
import sys
import re   

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="phonebook_db",
        user="postgres",
        password="zarina06"   
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
        phone VARCHAR(20) NOT NULL,
        email VARCHAR(100)
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
            cur.execute("SELECT id, first_name, last_name, phone, email FROM phonebook ORDER BY id")
            rows = cur.fetchall()
            for row in rows:
                print(row)
 
 
def insert_user(first_name, last_name, phone, email=None):
    sql = "INSERT INTO phonebook(first_name, last_name, phone, email) VALUES (%s,%s,%s,%s) RETURNING id"
    config = load_config(r"C:\Users\shynb\OneDrive\Документы\GitHub\PP2\lab10.py\database.ini")
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute(sql, (first_name, last_name, phone, email))
            user_id = cur.fetchone()[0]
        conn.commit()
        return user_id
 
 
def insert_from_csv(path):
    with open(path, encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader, None)
        for row in reader:
            if len(row) == 4:
                first_name, last_name, phone, email = row
            elif len(row) == 3:
                first_name, last_name, phone = row
                email = None
            else:
                print("bad row:", row)
                continue
            insert_user(first_name, last_name, phone, email)
 
 
def delete_by_name_or_phone(value):
    sql = """
        DELETE FROM phonebook
        WHERE first_name = %s
           OR last_name = %s
           OR phone = %s
    """
    config = load_config(r"C:\Users\shynb\OneDrive\Документы\GitHub\PP2\lab10.py\database.ini")
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute(sql, (value, value, value))
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



def search_by_pattern(pattern):
    like_pattern = f"%{pattern}%"
    sql = """
        SELECT id, first_name, last_name, phone, email
        FROM phonebook
        WHERE first_name ILIKE %s
           OR last_name ILIKE %s
           OR phone ILIKE %s
           OR email ILIKE %s
        ORDER BY id
    """
    config = load_config(r"C:\Users\shynb\OneDrive\Документы\GitHub\PP2\lab10.py\database.ini")
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute(sql, (like_pattern, like_pattern, like_pattern, like_pattern))
            rows = cur.fetchall()
            return rows



def upsert_user(first_name, last_name, phone, email=None):
    config = load_config(r"C:\Users\shynb\OneDrive\Документы\GitHub\PP2\lab10.py\database.ini")
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT id FROM phonebook WHERE first_name = %s AND last_name = %s",
                (first_name, last_name)
            )
            row = cur.fetchone()
            if row:
                user_id = row[0]
                cur.execute(
                    "UPDATE phonebook SET phone = %s, email = %s WHERE id = %s",
                    (phone, email, user_id)
                )
                action = "updated"
            else:
                cur.execute(
                    "INSERT INTO phonebook(first_name, last_name, phone, email) VALUES (%s, %s, %s, %s) RETURNING id",
                    (first_name, last_name, phone, email)
                )
                user_id = cur.fetchone()[0]
                action = "inserted"
        conn.commit()
    return action, user_id



def is_valid_phone(phone: str) -> bool:
    if len(phone) < 5 or len(phone) > 20:
        return False
    return bool(re.fullmatch(r"\+?\d+", phone))



def insert_many_users(users):
    invalid = []
    for fn, ln, ph in users:
        if not is_valid_phone(ph):
            invalid.append((fn, ln, ph))
            continue
        try:
            insert_user(fn, ln, ph)
        except Exception as e:
            print("DB error for:", fn, ln, ph, "->", e)
            invalid.append((fn, ln, ph))
    return invalid



def list_users_paginated(limit, offset):
    sql = """
        SELECT id, first_name, last_name, phone, email
        FROM phonebook
        ORDER BY id
        LIMIT %s OFFSET %s
    """
    config = load_config(r"C:\Users\shynb\OneDrive\Документы\GitHub\PP2\lab10.py\database.ini")
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute(sql, (limit, offset))
            rows = cur.fetchall()
            return rows


def main():
    create_tables()
 
    while True:
        print("""
1 - show all
2 - insert manually
3 - load csv
4 - delete by name or phone        
5 - your sql
6 - search by pattern              
7 - upsert user (insert / update)  
8 - insert many users (console)    
9 - show with pagination           
0 - exit
""")
        c = input("choice: ")
 
        if c == "1":
            list_users()

        elif c == "2":
            fn = input("name: ")
            ln = input("sur name: ")
            ph = input("phone number: ")
            em = input("email (optional): ")
            if em.strip() == "":
                em = None
            print("ID:", insert_user(fn, ln, ph, em))

        elif c == "3":
            path = input("path to csv: ")
            insert_from_csv(path)

        elif c == "4":
            value = input("name or phone: ")
            deleted = delete_by_name_or_phone(value)
            print("deleted:", deleted)

        elif c == "5":
            run_custom_sql()

        elif c == "6":   
            pattern = input("pattern (part of name / surname / phone / email): ")
            rows = search_by_pattern(pattern)
            if not rows:
                print("no results")
            else:
                for r in rows:
                    print(r)

        elif c == "7":  
            fn = input("name: ")
            ln = input("sur name: ")
            ph = input("phone number: ")
            em = input("email (optional): ")
            if em.strip() == "":
                em = None
            action, uid = upsert_user(fn, ln, ph, em)
            print(f"user {action}, id = {uid}")

        elif c == "8":  
            print("Enter users one per line: first_name,last_name,phone")
            print("Empty line to stop.")
            users = []
            while True:
                line = input("> ").strip()
                if not line:
                    break
                parts = [p.strip() for p in line.split(",")]
                if len(parts) != 3:
                    print("format: first_name,last_name,phone")
                    continue
                users.append(tuple(parts))
            invalid = insert_many_users(users)
            if invalid:
                print("Invalid phones:")
                for item in invalid:
                    print(item)
            else:
                print("All users inserted successfully.")

        elif c == "9":   
            try:
                limit = int(input("limit: "))
                offset = int(input("offset: "))
            except ValueError:
                print("limit/offset must be integers")
                continue
            rows = list_users_paginated(limit, offset)
            for r in rows:
                print(r)

        elif c == "0":
            break
 
 
if __name__ == "__main__":
    main()
