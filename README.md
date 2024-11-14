# Book Recommendation System

## Summary of the Project
This project leverages text embeddings to compare and recommend books based on semantic similarity between chunks of text. The system is designed to query book embeddings in English and Spanish, allowing for cross-lingual book recommendations.

---

## Features

1. **Interface with External Data**
   - The project processes text embeddings generated from external APIs (e.g., OpenAI GPT models) and loads them into a database for analysis.

2. **Caching and Database Integration**
   - Uses **PostgreSQL** as the persistent database for storing embeddings and metadata.
   - Placeholder: Integration with a caching layer (e.g., Redis) for optimizing query performance can be added.

3. **Performance Support**
   - System is scalable for handling high read and write requests, depending on the infrastructure setup (e.g., horizontally scalable databases).

4. **Failover Support**
   - Placeholder: Adding failover strategy for zero-downtime data recovery.

5. **Real-World Use Case**
   - Designed to provide cross-lingual book recommendations to researchers, linguists, and readers, making the world a better place by bridging language gaps in literature.

6. **Concurrency and Security**
   - Handles concurrent access by using SQL queries optimized for simultaneous read/write operations.
   - Customer data is safeguarded by excluding sensitive keys from public repositories and ensuring secure access via `.env` configurations.

---

## Current Book Dataset

### English Books:
- **PRIDE, and PREJUDICE**
- **Middlemarch**
- **A Room With A View**
- **Cranford**
- **History of Tom Jones**

### Spanish Books:
- **Vida De Lazarillo De Tormes Y De Sus Fortunas Y Adversidades**
- **Los cuatro jinetes del apocalipsis**
- **Amor y Pedagogía**
- **EL SOMBRERO DE TRES PICOS**
- **La prueba**

---


## System Design

### Architecture Diagram
Placeholder for the system architecture diagram showing:
- Data ingestion (text embeddings from OpenAI GPT models).
- Storage in PostgreSQL.
- Query flow for finding similar and dissimilar book chunks.

### Scaling Bottlenecks
- Bottleneck: Database performance under high read/write loads.
- Solution: Horizontal scaling or caching layer (e.g., Redis).

### Anticipated Limits
- PostgreSQL can handle a limited number of simultaneous connections.
- Embedding vector size (1536) can lead to storage bloat if not compressed or optimized.

---

## Key Learnings

1. **Cross-Lingual Recommendations:**
   - Leveraging embeddings to bridge language gaps in literature is feasible and impactful.

2. **Embedding Storage:**
   - Handling large embedding vectors requires careful database design and indexing.

3. **Scalability Considerations:**
   - A caching layer (e.g., Redis) is crucial for supporting high-performance demands.

---

## Failover Strategy
- **Placeholder:** Implement failover with a managed database (e.g., AWS RDS Multi-AZ) or a replica-based approach.

---

## Performance Characteristics
- **Read Latency:** Currently dependent on PostgreSQL query performance.
- **Write Latency:** Scalable with appropriate database indexing.

---

## Recorded Video Placeholder
[Link to Recorded Video](https://example.com)

---

## Images of Books
1. PRIDE, and PREJUDICE: ![PRIDE, and PREJUDICE](images/pride_prejudice.png)
2. Middlemarch: ![Middlemarch](images/Middlemarch.png)
3. A Room With A View: ![A Room With A View](images/a_room_with_a_view.png)
4. Vida De Lazarillo De Tormes Y De Sus Fortunas Y Adversidades: ![Vida De Lazarillo De Tormes](images/vida_de_lazarillo_de_tormes_y_de_sus_fortunas_y_adversidades.png)
5. Los cuatro jinetes del apocalipsis: ![Los cuatro jinetes del apocalipsis](images/los_cuatro_jinetes_del_apocalipsis.png)
6. Cranford: ![Cranford](images/cranford.png)
7. History of Tom Jones: ![History of Tom Jones](images/history_of_tom_jones.png)


---

## How to Run the Project

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/daviethedeveloper/Recommendation.git
   cd Recommendation
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up the Environment:**
   - Create a `.env` file and add your sensitive keys:
     ```
     OPENAI_API_KEY=<your_openai_api_key>
     POSTGRES_URL=<your_postgres_url>
     ```

4. **Run Database Setup:**
   ```bash
   python db_build.py
   python db_insert.py
   ```

5. **Explore the System:**
   ```bash
   python explore_database.py
   ```

6. **Run Analysis:**
   ```bash
   python book_embedding_analysis.py
   ```

---

## Feedback and Questions
Feel free to open an issue or ask questions in the GitHub repository or the Discord channel. Feedback is highly encouraged!

---
