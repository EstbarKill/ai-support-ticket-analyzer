from sentence_transformers import SentenceTransformer


class EmbeddingService:

    def __init__(self):

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

    def generate_embedding(
        self,
        text: str
    ):

        return self.model.encode(
            text
        ).tolist()

    def generate_embeddings(
        self,
        texts: list[str]
    ):

        return self.model.encode(
            texts
        ).tolist()

    def add_document(
        self,
        doc_id,
        content,
        embedding,
        source
    ):

        self.collection.add(
            ids=[doc_id],
            documents=[content],
            embeddings=[embedding],
            metadatas=[
                {
                    "source": source
                }
            ]
        )

    def search(
        self,
        embedding,
        n_results=5
    ):

        return self.collection.query(
            query_embeddings=[embedding],
            n_results=n_results
        )        