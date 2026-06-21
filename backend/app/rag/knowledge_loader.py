from pathlib import Path


class KnowledgeLoader:

    def load_documents(
        self,
        knowledge_path: str
    ):

        documents = []

        base_path = Path(
            knowledge_path
        )

        for file in base_path.glob("*.md"):

            content = file.read_text(
                encoding="utf-8"
            )

            documents.append({
                "source": file.name,
                "content": content
            })

        return documents