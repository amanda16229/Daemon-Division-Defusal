# image_scanner.py

from PIL import Image, ImageEnhance, ImageFilter
import pytesseract
from tkinter import filedialog
import string

def atbash_cipher(text):
    standard_upper = string.ascii_uppercase
    reversed_upper = standard_upper[::-1]
    standard_lower = string.ascii_lowercase
    reversed_lower = standard_lower[::-1]

    translation_table = str.maketrans(
        standard_upper + standard_lower,
        reversed_upper + reversed_lower
    )
    return text.translate(translation_table)

SEARCH_PHRASE = atbash_cipher("password:")
PASSWORD_WORD_ATBASH = atbash_cipher("password")

# Update this path to your Tesseract installation
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def scan_for_password():
    file_path = filedialog.askopenfilename(
        title="Select an image file",
        filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.jfif"), ("All files", "*.*")]
    )

    if not file_path:
        print("No image file selected.")
        return None

    img = Image.open(file_path)
    img = img.convert('L')
    img = ImageEnhance.Contrast(img).enhance(2)
    img = img.filter(ImageFilter.SHARPEN)

    text = pytesseract.image_to_string(img)
    print(text)  # debug

    encoded_password = None
    for line in text.splitlines():
        if SEARCH_PHRASE in line:
            parts = line.split(PASSWORD_WORD_ATBASH)
            if len(parts) > 1:
                raw_extracted = parts[-1].strip()
                if raw_extracted.startswith(':'):
                    raw_extracted = raw_extracted[1:].strip()
                encoded_password = raw_extracted
                break

    if encoded_password:
        decrypted_password = atbash_cipher(encoded_password)
        print(f"Encoded Password: {encoded_password}")
        print(f"Decrypted Password: {decrypted_password}")
        return encoded_password, decrypted_password
    else:
        print("No password found.")
        return None

if __name__ == "__main__":
    result = scan_for_password()
    if result:
        encoded, decrypted = result
        print(f"Standalone run -> Encoded: {encoded}, Decrypted: {decrypted}")
