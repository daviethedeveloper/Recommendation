import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

POSTGRES_URL = os.getenv("POSTGRES_URL")

conn = psycopg2.connect(POSTGRES_URL)
cur = conn.cursor()

def create_tables():
    cur.execute("CREATE EXTENSION IF NOT EXISTS vector;")

    cur.execute("""
        CREATE TABLE IF NOT EXISTS book_embeddings (
            id SERIAL PRIMARY KEY,
            title TEXT,
            chunk_index INT,
            language TEXT,
            chunk_text TEXT,
            embedding VECTOR(1536)
        );
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS book_comparisons (
            id SERIAL PRIMARY KEY,
            english_title TEXT,
            spanish_title TEXT,
            english_chunk_index INT,
            spanish_chunk_index INT,
            similarity FLOAT
        );
    """)

    conn.commit()

if __name__ == "__main__":
    create_tables()
    print("Tables created successfully.")
    cur.close()
    conn.close()
