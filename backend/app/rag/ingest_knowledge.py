from app.rag.embedding_service import EmbeddingService
from app.rag.knowledge_loader import KnowledgeLoader
from app.rag.text_chunker import TextChunker
from app.rag.vector_store import VectorStore


class KnowledgeIngestionService:

    def __init__(self):

        self.loader = KnowledgeLoader()

        self.chunker = TextChunker()

        self.embedding_service = (
            EmbeddingService()
        )

        self.vector_store = (
            VectorStore()
        )

    def ingest(
        self,
        knowledge_path: str = "knowledge_base"
    ):

        documents = self.loader.load_documents(
            knowledge_path
        )
        if not documents:
            return {
                "answer": "No relevant tickets found.",
                "sources": []
            }
        total_chunks = 0

        for document in documents:

            source = document["source"]

            content = document["content"]

            chunks = self.chunker.chunk(
                content
            )

            for index, chunk in enumerate(chunks):

                embedding = (
                    self.embedding_service
                    .generate_embedding(chunk)
                )

                doc_id = (
                    f"{source}_{index}"
                )

                self.vector_store.add_document(
                    doc_id=doc_id,
                    content=chunk,
                    embedding=embedding,
                    source=source
                )

                total_chunks += 1

        return {
            "documents": len(documents),
            "chunks": total_chunks,
            "status": "completed"
        }


if __name__ == "__main__":

    result = (
        KnowledgeIngestionService()
        .ingest()
    )

    print(result)