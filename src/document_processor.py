from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_path):
    """
    Extracts text from a PDF file, splitting it into pages.
    """
    text_content = []

    try:
        reader = PdfReader(pdf_path)
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text_content.append(page.extract_text())
        print(f"Extracted text from {len(text_content)} pages")
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
    return text_content


if __name__ == "__main__":
    pdf_path = "documents/sample.pdf"
    pages = extract_text_from_pdf(pdf_path)
    for i, page_text in enumerate(pages):
        print(f"\n--- Page {i+1} ---")
        print(page_text[:200])



