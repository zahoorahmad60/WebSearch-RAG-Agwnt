# query.py

from langchain_ollama import ChatOllama
from embeder import embed_text
from store import collection

llm = ChatOllama(model="deepseek-r1:1.5b")

def retrieve_and_answer(query, k=3):
    """
    Retrieves top-k chunks from ChromaDB and uses Ollama LLM to answer.
    Returns the answer string, or an empty string on failure.
    """
    try:
        q_emb = embed_text(query)
        if not q_emb:
            return ""

        results = collection.query(
            query_embeddings=[q_emb],
            n_results=k
        )
        docs = results["documents"][0]
        context = "\n---\n".join(docs)

        prompt = (
            "You are an expert assistant. Use the following context to  answer the question.\n\n"
            f"Context:\n{context}\n\n"
            f"Question: {query}\n"
            "Answer:"
        )
        answer = llm.invoke(prompt)
        return answer.content
    except Exception as e:
        print("Error retrieving or answering query:", e)
        return ""
