
import os.path
import time
from PIL import Image
import PyPDF2
from PIL.ExifTags import TAGS
import argparse

CREDITS = 'Scorpion v0.1.0 by jledesma@student.42malaga.com'
LOGO = """
\t                          _             
\t                         (_)            
\t ___  ___ ___  _ __ _ __  _  ___  _ __  
\t/ __|/ __/ _ \| '__| '_ \| |/ _ \| '_ \ 
\t\__ \ (_| (_) | |  | |_) | | (_) | | | |
\t|___/\___\___/|_|  | .__/|_|\___/|_| |_|
\t                   | |                  
\t                   |_|         
"""    

def get_image_metadata(image_path):
    """Obtiene los metadatos de una imagen.

    Args:
        image_path (str): Ruta a la imagen.

    Returns:
        dict: Diccionario con los metadatos de la imagen.
    """
    try:
        with Image.open(image_path) as img:
            metadata = {}
            exifdata = img.getexif()
            for tag_id, value in exifdata.items():
                tag = TAGS.get(tag_id, tag_id)
                metadata[tag] = value
            return metadata
    except Exception as e:
        print(f"Error al obtener metadatos de la imagen {image_path}: {e}")
        return {}

def get_pdf_metadata(pdf_path):
    """Obtiene los metadatos de un archivo PDF.

    Args:
        pdf_path (str): Ruta al archivo PDF.

    Returns:
        dict: Diccionario con los metadatos del archivo PDF.
    """
    try:
        with open(pdf_path, 'rb') as f:
            pdf_reader = PyPDF2.PdfFileReader(f)
            metadata = pdf_reader.documentInfo
            return metadata
    except Exception as e:
        print(f"Error al obtener metadatos del archivo PDF {pdf_path}: {e}")
        return {}

parser = argparse.ArgumentParser(description='Extract metadata from image and PDF files')
parser.add_argument('files', metavar='file', type=str, nargs='+',
                    help='path to image or PDF file(s)')
args = parser.parse_args()
print(f"\n\tInitiating scorpion...")
print(LOGO)
print(f"Getting metadatas on files: {args.files}.")
for file_path in args.files:
    if file_path.endswith('.jpg') or file_path.endswith('.jpeg') or file_path.endswith('.png') or file_path.endswith('.gif') or file_path.endswith('.bmp') or file_path.endswith('.pdf'):
        print(f"\nCreation date: {time.ctime(os.path.getctime(file_path))}")
        print(f"Modification date: {time.ctime(os.path.getmtime(file_path))}")
        print(f"Size file: {(os.path.getsize(file_path))}")
        metadata = get_image_metadata(file_path)

    elif file_path.endswith('.pdf'):
        metadata = get_pdf_metadata(file_path)
        print(f"\nCreation date: {time.ctime(os.path.getctime(file_path))}")
        print(f"Modification date: {time.ctime(os.path.getmtime(file_path))}")
        print(f"Size file: {(os.path.getsize(file_path))}")
    else:
        print(f'Error: unsupported file format for file {file_path}')
        continue
    print(f'Metadata for file: {file_path}')
    for key, value in metadata.items():
        print(f'{key}: {value}')
print(f"\t{CREDITS}")


# usage python scorpion.py image1.jpg image2.jpg doc.pdf

#instal pip install PyPDF2 pillow or conda install pillow PyPDF2

# **************************************************************************** #
# python scorpio.py image1.jpg image2.jpg doc.pdf
#                 use path of the file to get metadata
