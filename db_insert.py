import psycopg2
from dotenv import load_dotenv
import os
import json

load_dotenv()
POSTGRES_URL = os.getenv("POSTGRES_URL")

conn = psycopg2.connect(POSTGRES_URL)
cur = conn.cursor()

def insert_embeddings(embeddings_folder):
    for file_name in os.listdir(embeddings_folder):
        if file_name.endswith('.json'):
            with open(os.path.join(embeddings_folder, file_name), 'r', encoding='utf-8') as f:
                embeddings = json.load(f)
                for record in embeddings:
                    cur.execute("""
                        INSERT INTO book_embeddings (title, chunk_index, language, chunk_text, embedding)
                        VALUES (%s, %s, %s, %s, %s)
                    """, (
                        record['title'],
                        record['chunk_index'],
                        record['language'],
                        record['chunk_text'],
                        record['embedding']
                    ))
    conn.commit()

if __name__ == "__main__":
    insert_embeddings("embeddings")
    print("Embeddings inserted successfully.")
    cur.close()
    conn.close()
