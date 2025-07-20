def chunk_text(text):
    """
    Splits text into fixed-size overlapping chunks.
    Returns a list of strings, or empty list on error.
    """
    try:
        max_tokens = 500
        overlap = 50
        words = text.split()
        chunks = []
        start = 0
        while start < len(words):
            end = min(start + max_tokens, len(words))
            chunks.append(" ".join(words[start:end]))
            start += max_tokens - overlap
        return chunks
    except Exception as e:
        print('Error chunking text:', e)
        return []
