import os
from pydoc import describe
from PIL import Image
from PyPDF2 import PdfMerger

def collect_files(base_dir):
    collected = []

    for root, dirs, files in os.walk(base_dir):
        files = sorted(files)
        for file in files:
            if file.lower().endswith(('.pdf', '.jpg', '.jpeg', '.png')):
                full_path = os.path.join(root, file)
                collected.append((root, full_path))

    # Por nome da pasta e depois por nome do arquivo
    collected.sort(key=lambda x: (x[0].lower(), os.path.basename(x[1]).lower()))
    return [file_path for _, file_path in collected]

def convert_images_to_pdf(image_paths):
    temp_pdfs = []

    for image_path in image_paths:
        try:
            image = Image.open(image_path).convert("RGB")
            temp_pdf_path = image_path + ".temp.pdf"
            image.save(temp_pdf_path)
            temp_pdfs.append(temp_pdf_path)
        except Exception as e:
            print(f"Could not convert {image_path}: {e}")
    return temp_pdfs

def main():
    base_dir = os.getcwd()
    print("Scanning...")

    files = collect_files(base_dir)

    if len(files) == 0:
        print("No files found! Exiting...")
        return
    else: print(f"Found {len(files)} file(s) to merge.")

    pdfs = []
    image_paths = []

    for f in files:
        if f.lower().endswith('.pdf'):
            pdfs.append(f)
        else:
            image_paths.append(f)

    image_pdfs = convert_images_to_pdf(image_paths)

    all_pdfs = pdfs + image_pdfs
    print("Merging PDFs...")

    merger = PdfMerger()
    for pdf in all_pdfs:
        try:
            merger.append(pdf)
        except Exception as e:
            print(f"Error adding {pdf}: {e}")

    output_path = os.path.join(base_dir, "merged_output.pdf")
    merger.write(output_path)
    merger.close()

    print(f"Merged PDF created: {output_path}")


    # Limpa os arquivos temps
    for temp_pdf in image_pdfs:
        os.remove(temp_pdf)

    input("Done! Press Enter to exit...")
    os.startfile(output_path)

if __name__ == "__main__":
    main()
