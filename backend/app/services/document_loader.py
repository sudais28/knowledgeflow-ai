from pathlib import Path

from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    Docx2txtLoader,
)


def load_document(file_path: str):

    extension = Path(file_path).suffix.lower()


    if extension == ".pdf":
        loader = PyPDFLoader(file_path)

    elif extension == ".txt":
        loader = TextLoader(file_path)

    elif extension == ".docx":
        loader = Docx2txtLoader(file_path)

    else:
        raise ValueError(
            "Unsupported file type"
        )


    documents = loader.load()

    return documents