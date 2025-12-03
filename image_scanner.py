from PIL import Image, ImageEnhance, ImageFilter # type: ignore # suppresses VS code warning
import pytesseract # type: ignore # suppressess VS code warning
from tkinter import Tk, filedialog
import string
import re # being used for better text extraction

def atbash_cipher(text):
    # defines standard and reverse alphabets (case sensitive)
    standard_upper = string.ascii_uppercase
    reversed_upper = standard_upper[::-1]
    standard_lower = string.ascii_lowercase
    reversed_lower = standard_lower[::-1]

    # translation table creation
    translation_table = str.maketrans(
        standard_upper + standard_lower,
        reversed_upper + reversed_lower
    )

    return text.translate(translation_table)

SEARCH_PHRASE = atbash_cipher("password:")
PASSWORD_WORD_ATBASH = atbash_cipher("password")

pytesseract.pytesseract.tesseract_cmd = "/opt/homebrew/bin/tesseract" # WILL HAVE TO CHANGE TO YOUR PYTESSERACT EXECUTABLE

def scan_for_password():
    Tk().withdraw()
    file_path = filedialog.askopenfilename(
        title="Select an image file",
        filetypes=[("All files", "*.*")]
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
        print(f"Decrypted Password: {decrypted_password}")
        return decrypted_password
    else:
        print("No password found.")
        return None


Tk().withdraw()
file_path = filedialog.askopenfilename(title="Select an image file", filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.JFIF")])

# load image and process
if file_path:
    img = Image.open(file_path)

    # preprocess image for better OCR results
    img = img.convert('L') # grayscale
    img = ImageEnhance.Contrast(img).enhance(2) # contrast increase
    img = img.filter(ImageFilter.SHARPEN) # sharpen image

    text = pytesseract.image_to_string(img)

    print(text) # for debugging fr

    # use pre-calculated search phrase 'kzhhdliw:'
    encoded_password = None

    for line in text.splitlines():
        # check if the ATBASH version of "password:" is in line
        if SEARCH_PHRASE in line:
            parts = line.split(PASSWORD_WORD_ATBASH)

            # part after keyword is likely the encoded password
            if len(parts) > 1:
                raw_extracted = parts[-1].strip()

                # check for and remove leading colon (if present)
                if raw_extracted.startswith(':'):
                    raw_extracted = raw_extracted[1:].strip()

                    encoded_password = raw_extracted
                    break # found password. exit loop
    
    if encoded_password:
        print (f"Atbash Encoded Password Found: {encoded_password}")

        # to decrypt password
        decrypted_password = atbash_cipher(encoded_password)

        print (f"Decrypted Password: {decrypted_password}")

    else:
        print (f"No password found.")
else:
    print ("No image file selected.")
