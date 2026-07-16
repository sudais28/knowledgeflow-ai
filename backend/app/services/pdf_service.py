import fitz  # PyMuPDF


def extract_text(pdf_path: str) -> str:
    """
    Extract all text from a PDF file.

    Args:
        pdf_path: Path to the PDF file.

    Returns:
        Extracted text as a single string.
    """

    document = fitz.open(pdf_path)

    text = ""

    for page in document:
        text += page.get_text()

    document.close()

    return text.strip()