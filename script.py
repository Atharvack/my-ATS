import subprocess
import os
from tika import parser  # pip install tika
import PyPDF2  # pip install PyPDF2

def extract_text_tika(pdf_path):
    raw = parser.from_file(pdf_path)
    print("\n=== [Body Text via Apache Tika] ===\n")
    print(raw['content'])

def extract_metadata_exiftool(pdf_path):
    print("\n=== [Metadata via ExifTool] ===\n")
    output = subprocess.check_output(['exiftool', pdf_path], universal_newlines=True)
    print(output)

def extract_text_pypdf(pdf_path):
    print("\n=== [Text via PyPDF2] ===\n")
    with open(pdf_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            print(page.extract_text())


pdf_file = input("Enter path: ").strip()
if not os.path.isfile(pdf_file):
    print("❌ File not found. Please check the path and try again.")
    exit(1)
    
extract_text_tika(pdf_file)
extract_metadata_exiftool(pdf_file)
extract_text_pypdf(pdf_file)
