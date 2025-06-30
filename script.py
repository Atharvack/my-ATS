import subprocess
import os
import tika 
from tika import parser
tika.TikaClientOnly = True
import PyPDF2  

def extract_text_tika(pdf_path, f):
    raw = parser.from_file(pdf_path)
    f.write("\n=== [Body Text via Apache Tika] ===\n\n")
    f.write(raw.get('content', 'No content extracted via Tika.'))

def extract_metadata_exiftool(pdf_path, f):
    f.write("\n\n=== [Metadata via ExifTool] ===\n\n")
    output = subprocess.check_output(['exiftool', pdf_path], universal_newlines=True)
    f.write(output)


pdf_file = input("Enter path: ").strip()
if not os.path.isfile(pdf_file):
    print(" File not found. Please check the path and try again.")
    exit(1)

# Output file path
output_file = os.path.join(os.path.dirname(pdf_file), "ats_output.txt")

with open(output_file, "w", encoding="utf-8") as f:
    f.write(f" ATS Extraction for File: {os.path.basename(pdf_file)}\n")
    f.write("=" * 60 + "\n")
    extract_text_tika(pdf_file, f)
    extract_metadata_exiftool(pdf_file, f)
    

print(f"\n All ATS-style output written to: {output_file}")


#/home/atharva/Downloads/Resumes/New York/ML Resume/Atharva_ML_1.3.pdf