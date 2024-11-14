import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()
POSTGRES_URL = os.getenv("POSTGRES_URL")

conn = psycopg2.connect(POSTGRES_URL)
cur = conn.cursor()

def drop_tables():
    cur.execute("DROP TABLE IF EXISTS book_embeddings;")
    cur.execute("DROP TABLE IF EXISTS book_comparisons;")
    conn.commit()

if __name__ == "__main__":
    drop_tables()
    print("Tables dropped successfully.")
    cur.close()
    conn.close()
