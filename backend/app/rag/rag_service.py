from app.rag.embedding_service import (
    EmbeddingService
)

from app.rag.vector_store import (
    VectorStore
)

from app.ai.gemini_provider import (
    GeminiProvider
)


class RAGService:

    def __init__(self):

        self.embedding_service = (
            EmbeddingService()
        )

        self.vector_store = (
            VectorStore()
        )

        self.llm = GeminiProvider()

    def ask(
        self,
        question: str
    ):

        question_embedding = (
            self.embedding_service
            .generate_embedding(question)
        )

        results = self.vector_store.search(
            embedding=question_embedding,
            n_results=5
        )

        documents = (
            results.get("documents", [[]])[0]
        )

        metadatas = (
            results.get("metadatas", [[]])[0]
        )

        context = "\n\n".join(
            documents
        )

        prompt = f"""
        You are an AI Support Analyst for a ticketing system.

        Use ONLY the context below.

        If the answer is not supported, say:
        "I don't have enough information in the tickets database."

        Context:
        {context}

        Question:
        {question}

        Instructions:
        - Be precise
        - Summarize when needed
        - Prefer operational insights
        - Do not hallucinate

        Answer:
        """

        answer = self.llm.generate(
            prompt
        )

        sources = []

        for metadata in metadatas:

            source = metadata.get(
                "source"
            )

            if source not in sources:
                sources.append(source)

        return {
            "answer": answer,
            "sources": sources
        }