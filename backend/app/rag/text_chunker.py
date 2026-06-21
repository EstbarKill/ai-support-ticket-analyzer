class TextChunker:

    def chunk(
        self,
        text: str,
        chunk_size: int = 500
    ):

        chunks = []

        for i in range(
            0,
            len(text),
            chunk_size
        ):

            chunks.append(
                chunks = text.split("\n\n")
            )

        return chunks