from PIL import Image
from pytesseract import pytesseract

path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
image_path = r'C:\Users\Lorenzo\Desktop\Python\vscode-test\lineup-to-table\sunday-lineup.png'

img = Image.open(image_path)

pytesseract.tesseract_cmd = path_to_tesseract

text = pytesseract.image_to_string(img)

string_to_list = text.split("-")

print(string_to_list)