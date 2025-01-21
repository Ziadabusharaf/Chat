import openpyxl
import os
from PyPDF2 import PdfReader
# from PIL import Image
# import pytesseract  # if you want OCR, you'll need Tesseract installed

class DataManager:
    def __init__(self, data_folder="data_files"):
        self.data_folder = data_folder
        os.makedirs(self.data_folder, exist_ok=True)

    def save_conversation_to_excel(self, conversation_history, excel_file="conversations.xlsx"):
        """Save conversation history to Excel."""
        file_path = os.path.join(self.data_folder, excel_file)
        if os.path.exists(file_path):
            wb = openpyxl.load_workbook(file_path)
        else:
            wb = openpyxl.Workbook()

        sheet = wb.active
        for entry in conversation_history:  # each entry is e.g. ("User", "Hello")
            sheet.append(entry)
        wb.save(file_path)

    def read_pdf(self, pdf_path):
        """Extract text from a PDF file."""
        reader = PdfReader(pdf_path)
        text_content = []
        for page in reader.pages:
            text_content.append(page.extract_text())
        return "\n".join(text_content)

    # Example image processing function
    # def process_image(self, image_path):
    #     with Image.open(image_path) as img:
    #         width, height = img.size
    #         text = pytesseract.image_to_string(img)
    #         return width, height, text
