import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()
POSTGRES_URL = os.getenv("POSTGRES_URL")

def run_query(query):
    """Executes a given SQL query and returns the results."""
    with psycopg2.connect(POSTGRES_URL) as conn:
        cur = conn.cursor()
        cur.execute(query)
        results = cur.fetchall()
        cur.close()
    return results

def list_books():
    """List all unique books in the database."""
    query = "SELECT DISTINCT title, language FROM book_embeddings;"
    results = run_query(query)
    print("Books in the database:")
    for result in results:
        print(f"Title: {result[0]}, Language: {result[1]}")

def list_segment_ids_and_titles():
    """
    List all segment IDs and their corresponding titles from the book_embeddings table.
    """
    query = """
    SELECT id, title
    FROM book_embeddings
    ORDER BY id ASC;
    """
    results = run_query(query)
    print("Segment IDs and Titles:")
    for result in results:
        print(f"Segment ID: {result[0]}, Title: {result[1]}")

def list_chunks_by_book(book_title):
    """List all chunks of a specific book by title."""
    query = f"""
    SELECT id, chunk_index, chunk_text
    FROM book_embeddings
    WHERE title = '{book_title}'
    ORDER BY chunk_index ASC;
    """
    results = run_query(query)
    print(f"Chunks for '{book_title}':")
    for result in results:
        print(f"ID: {result[0]}, Chunk Index: {result[1]}, Text: {result[2][:50]}...")

def most_similar_chunks_with_text(segment_id, limit=5):
    """Find the most similar chunks to a given segment ID and include chunk text."""
    query = f"""
    SELECT 
        title, 
        chunk_index, 
        chunk_text,
        (embedding <-> (
            SELECT embedding 
            FROM book_embeddings 
            WHERE id = {segment_id}
        )) AS similarity
    FROM book_embeddings
    WHERE id != {segment_id}
    ORDER BY similarity ASC
    LIMIT {limit};
    """
    results = run_query(query)
    print(f"Most similar chunks to segment ID {segment_id}:")
    for result in results:
        print(f"Title: {result[0]}, Chunk Index: {result[1]}, Similarity: {result[3]}")
        print(f"Chunk Text: {result[2][:100]}...\n")

def most_dissimilar_chunks_with_text(segment_id, limit=5):
    """Find the most dissimilar chunks to a given segment ID and include chunk text."""
    query = f"""
    SELECT 
        title, 
        chunk_index, 
        chunk_text,
        (embedding <-> (
            SELECT embedding 
            FROM book_embeddings 
            WHERE id = {segment_id}
        )) AS similarity
    FROM book_embeddings
    WHERE id != {segment_id}
    ORDER BY similarity DESC
    LIMIT {limit};
    """
    results = run_query(query)
    print(f"Most dissimilar chunks to segment ID {segment_id}:")
    for result in results:
        print(f"Title: {result[0]}, Chunk Index: {result[1]}, Similarity: {result[3]}")
        print(f"Chunk Text: {result[2][:100]}...\n")


def compare_books(english_title, spanish_title, limit=5, similarity_threshold=0.9):
    """
    Compare an English book to a Spanish book by chunk similarity.
    If no significant comparisons are found, display a message.
    """
    query = f"""
    SELECT 
        e.chunk_index AS english_chunk, 
        s.chunk_index AS spanish_chunk, 
        (e.embedding <-> s.embedding) AS similarity,
        e.chunk_text AS english_text,
        s.chunk_text AS spanish_text
    FROM book_embeddings e, book_embeddings s
    WHERE e.title = '{english_title}' AND s.title = '{spanish_title}'
    ORDER BY similarity ASC
    LIMIT {limit};
    """
    results = run_query(query)

    print(f"Comparison between '{english_title}' and '{spanish_title}':")

    if not results:
        print("No matching data found for the given books.\n")
        return
    

    filtered_results = [result for result in results if result[2] < similarity_threshold]
    
    if not filtered_results:
        print("No significant similarities found. Showing the closest matches:\n")
        filtered_results = results  
    
    for result in filtered_results:
        print(f"English Chunk: {result[0]}, Spanish Chunk: {result[1]}, Similarity: {result[2]}")
        print(f"English Text: {result[3][:100]}...")
        print(f"Spanish Text: {result[4][:100]}...\n")

def average_embedding_by_book():
    """Compute the average embedding for each book."""
    query = """
    SELECT 
        title, 
        AVG(embedding) AS avg_embedding
    FROM book_embeddings
    GROUP BY title;
    """
    results = run_query(query)
    print("Average embeddings by book:")
    for result in results:
        print(f"Title: {result[0]}, Average Embedding: {result[1]}")

if __name__ == "__main__":

    print("\nListing all segment IDs and titles:")
    list_segment_ids_and_titles()

    print("\nFinding most similar chunks to segment ID 478:")
    most_similar_chunks_with_text(segment_id=478)

    print("\nFinding most dissimilar chunks to segment ID 478:")
    most_dissimilar_chunks_with_text(segment_id=478)

    print("\nComparing 'A Room With A View' with 'Vida De Lazarillo De Tormes Y De Sus Fortunas Y Adversidades':")
    compare_books("A Room With A View", "Vida De Lazarillo De Tormes Y De Sus Fortunas Y Adversidades")
