from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_text(text: str):
    """
    Split text into overlapping chunks.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        separators=[
            "\n\n",
            "\n",
            ". ",
            " ",
            "",
        ],
    )

    return splitter.split_text(text)