# store.py
import chromadb
from embeder import embed_text

# Initialize ChromaDB client (modern approach)
try:
   # Use the new PersistentClient
   client = chromadb.PersistentClient(path="./chroma_data")
   collection = client.get_or_create_collection("websites")
   print("ChromaDB initialized successfully")
except Exception as e:
   print("Error setting up ChromaDB:", e)
   client = None
   collection = None

def add_document(url, chunks):
   """
   Adds each text chunk + its embedding to ChromaDB.
   """
   if collection is None:
       print("ChromaDB not available")
       return
   
   for i, chunk in enumerate(chunks):
       try:
           emb = embed_text(chunk)
           collection.add(
               documents=[chunk],
               embeddings=[emb],
               metadatas=[{"source_url": url, "chunk_index": i}],
               ids=[f"{url}__{i}"]
           )
           print(f"Added chunk {i} for {url}")
       except Exception as e:
           print(f"Error storing chunk {i}:", e)