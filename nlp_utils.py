import re
from docx import Document
from PyPDF2 import PdfReader

def extract_text_from_pdf(file):
    text = ""
    reader = PdfReader(file)

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    return text


def extract_text_from_docx(file):
    doc = Document(file)
    return "\n".join([p.text for p in doc.paragraphs])

def split_clauses(text):
    """
    Split contract into readable clauses.
    Removes very small useless lines.
    """
    raw_clauses = re.split(r'\n|(?<=\.)\s', text)
    clean_clauses = []

    for clause in raw_clauses:
        clause = clause.strip()

        # ignore very short garbage text
        if len(clause) > 40:
            clean_clauses.append(clause)

    return clean_clauses
