import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()
POSTGRES_URL = os.getenv("POSTGRES_URL")


def list_all_titles():
    """Retrieve all unique book titles with their languages."""
    query = "SELECT DISTINCT title, language FROM book_embeddings;"
    with psycopg2.connect(POSTGRES_URL) as conn:
        cur = conn.cursor()
        cur.execute(query)
        results = cur.fetchall()
        print("All Titles:")
        for result in results:
            print(f"Title: {result[0]}, Language: {result[1]}")
        cur.close()


def list_segments_by_title(book_title):
    """Retrieve all segments (id and chunk index) for a specific book by title."""
    query = f"""
    SELECT id, chunk_index, chunk_text
    FROM book_embeddings
    WHERE title = '{book_title}';
    """
    with psycopg2.connect(POSTGRES_URL) as conn:
        cur = conn.cursor()
        cur.execute(query)
        results = cur.fetchall()
        print(f"Segments for '{book_title}':")
        for result in results:
            print(f"ID: {result[0]}, Chunk Index: {result[1]}, Text: {result[2][:50]}...")
        cur.close()


def list_all_segments():
    """Retrieve all segments in the database."""
    query = "SELECT id, title, chunk_index, language FROM book_embeddings;"
    with psycopg2.connect(POSTGRES_URL) as conn:
        cur = conn.cursor()
        cur.execute(query)
        results = cur.fetchall()
        print("All Segments:")
        for result in results:
            print(f"ID: {result[0]}, Title: {result[1]}, Chunk Index: {result[2]}, Language: {result[3]}")
        cur.close()


if __name__ == "__main__":
    print("Listing all book titles:")
    list_all_titles()

