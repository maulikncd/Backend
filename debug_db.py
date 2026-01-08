import sqlite3
from pathlib import Path

def check_db():
    db_path = r"d:\A.I\Ai Team\Main Code\Website_builder\backend\auth.db"
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    print("--- TABLES ---")
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    for row in cursor.fetchall():
        print(row)
        
    print("\n--- CONVERSATIONS COUNT ---")
    try:
        cursor.execute("SELECT COUNT(*) FROM conversations")
        print(cursor.fetchone()[0])
    except Exception as e:
        print(f"Error: {e}")

    print("\n--- MESSAGES COUNT ---")
    try:
        cursor.execute("SELECT COUNT(*) FROM messages")
        print(cursor.fetchone()[0])
    except Exception as e:
        print(f"Error: {e}")
        
    conn.close()

if __name__ == "__main__":
    check_db()
