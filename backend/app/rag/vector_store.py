import chromadb


import chromadb


class VectorStore:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path="./chroma_db"
        )

        self.collection = (
            self.client.get_or_create_collection(
                name="knowledge_base"
            )
        )

    def add_document(
        self,
        doc_id: str,
        content: str,
        embedding: list,
        source: str
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
        embedding: list,
        n_results: int = 5
    ):

        return self.collection.query(
            query_embeddings=[embedding],
            n_results=n_results
        )

    def count(self):

        return self.collection.count()