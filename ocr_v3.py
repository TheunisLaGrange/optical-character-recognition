from pathlib import Path
import pytesseract
from PIL import Image

# If Tesseract is not in your PATH, specify the full path:
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def ocr_image(image_path):
    # Open the image
    img = Image.open(image_path)
    
    # Extract text
    text = pytesseract.image_to_string(img)
    
    return text
  

file_name = input("Enter the file name (without extension): ").strip()  
text = file_name
if "png" in text:
    print("File Type not to be incuded in file name!")
# Create a Path object
file_path = Path("./images/" + file_name + ".jpg") # Assuming the file is in the "images" directory and has a .png extension

# Check if file exists and is a regular file
if file_path.is_file():
    #print(f"✅ The file '{file_name}' exists.")
    pass
else:
    print(f"❌ The file '{file_name}' does not exist.")
    exit(1) 

extracted_text = ocr_image(file_path)
print("Extracted Text:\n", extracted_text)
output_file="./output/result.txt"
with open(output_file, "a") as f:
                f.write(extracted_text + "\n")
