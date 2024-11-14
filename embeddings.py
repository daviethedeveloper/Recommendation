import psycopg2
import json
import openai
import os
import numpy
from dotenv import load_dotenv
from pathlib import Path
import time

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def preprocess_book(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    title = None
    content_lines = []
    for line in lines:
        if line.strip():
            if not title:
                title = line.strip()
            else:
                content_lines.append(line.strip())
    content = "\n".join(content_lines)
    chunks = content.split("\n\n")

    max_chunk_length = 12000  # Approx. 3000 words
    final_chunks = []
    for chunk in chunks:
        while len(chunk) > max_chunk_length:
            split_point = chunk[:max_chunk_length].rfind(" ")
            final_chunks.append(chunk[:split_point].strip())
            chunk = chunk[split_point:].strip()
        final_chunks.append(chunk.strip())
    return title, final_chunks

def embed_text(text):
    response = openai.Embedding.create(
        model="text-embedding-ada-002",
        input=text
    )
    return response['data'][0]['embedding']

def process_and_embed_books(folder_path, language):
    output_dir = "embeddings"
    os.makedirs(output_dir, exist_ok=True)
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.txt'):
            file_path = os.path.join(folder_path, file_name)
            title, chunks = preprocess_book(file_path)
            embeddings = []
            for i, chunk in enumerate(chunks):
                embedding = embed_text(chunk)
                embeddings.append({
                    "title": title,
                    "chunk_index": i,
                    "language": language,
                    "chunk_text": chunk,
                    "embedding": embedding
                })
                time.sleep(1)
            output_file = os.path.join(output_dir, f"{Path(file_name).stem}_{language}_embeddings.json")
            with open(output_file, 'w', encoding='utf-8') as out:
                json.dump(embeddings, out, ensure_ascii=False, indent=2)

process_and_embed_books("books/english", "English")
process_and_embed_books("books/spanish", "Spanish")
