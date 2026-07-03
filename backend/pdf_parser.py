import PyPDF2

def parse_pdf(file_path):
    text = ""

    with open(file_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text() or ""

    return text


def extract_transactions(text):
    lines = text.split("\n")
    return [l for l in lines if any(c.isdigit() for c in l)]