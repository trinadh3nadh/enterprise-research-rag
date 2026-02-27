from PyPDF2 import PdfReader
from utils.chunker import chunk_text

def load_documents(files):
    docs = []

    for file in files:
        reader = PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""

        chunks = chunk_text(text)

        for idx, chunk in enumerate(chunks):
            docs.append({
                "content": chunk,
                "source": file.name,
                "chunk_id": idx
            })

    return docs