import re
from docx import Document
from PyPDF2 import PdfReader

# -------- PDF TEXT --------
def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text() + "\n"
    return text

# -------- DOCX TEXT --------
def extract_text_from_docx(file):
    doc = Document(file)
    return "\n".join([p.text for p in doc.paragraphs])

# -------- CLAUSE SPLIT --------
def split_clauses(text):
    clauses = re.split(r'\n|(?<=\.)\s', text)
    return [c.strip() for c in clauses if len(c.strip()) > 25]
