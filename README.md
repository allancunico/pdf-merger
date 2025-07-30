# PDF Merger

This was a personal project, aiming to simplifying merging multiples files into a single PDF file. It is a simple command-line tool that scans all PDF and image files in the current directory and its subfolders, sorts them alphabetically by folder and filename, and merges them into a PDF file.

## How it Works 

- Recursively scans folders starting from the program's location
- Sorts files by folder path and then by filename (alphabetical order)
- Converts images to PDF format before merging
- Merges all PDFs and converted images into one document
- Automatically opens the merged PDF when done (Windows only)
- Cleans up temporary files after merging

## Supported Formats

- .pdf
- .jpg
- .jpeg
- .png

## Build .exe (Optional)

To create a standalone Windows executable:  

### Requirements

- Python 3.7+
- Packages:
  - Pillow
  - PyInstaller
  - PyPDF2

Install dependencies:
```bash
pip install -r requirements.txt
```

Build:
```bash
pyinstaller --onefile --console pdf_merger.py
```
Output will be in the dist/ folder as pdf_merger.exe.
