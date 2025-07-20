from langchain_ollama import OllamaEmbeddings

# Initialize the Ollama embedding client once
embeddings = OllamaEmbeddings(model="nomic-embed-text:latest")

def embed_text(text: str) -> list[float]:
    """
    Returns an embedding vector for the given text using Ollama via LangChain,
    or an empty list if something goes wrong.
    """
    try:
        vector = embeddings.embed_query(text)
        return vector
    except Exception as e:
        print("Error embedding text with LangChain OllamaEmbeddings:", e)
        return []
