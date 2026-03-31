'''
import cv2
import pytesseract
import re
from PIL import Image
import os

tesseract_path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update this path if necessary
if os.path.exists(tesseract_path):
    pytesseract.pytesseract.tesseract_cmd = tesseract_path
else:
    print("The path to tesseract.exe is still incorrect!")

def extract_receipt_total(image_path):
    # 1. Load and Preprocess the image
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Optional: Apply thresholding to make text pop
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    # 2. Perform OCR
    text = pytesseract.image_to_string(gray)
    print("--- Raw Extracted Text ---")
    print(text)
    print("--------------------------")

    # 3. Use Regex to find the Total
    # This looks for "Total" followed by a currency pattern like 12.99
    amounts = re.findall(r'Total[:\s]+[$]?(\d+\.\d{2})', text, re.IGNORECASE)
    
    if amounts:
        # Return the last occurrence, as "Total" often appears near the bottom
        return amounts[-1]
    return None

# Usage
path = "receipt_1.png" 
total1 = extract_receipt_total(path)
t1=total1

if total1:
    print(f"Success! Detected Total: ${total1}")
else:
    print("Could not find a total amount.")

path = "receipt_2.png" 
total2 = extract_receipt_total(path)
t2=total2

if total2:
    print(f"Success! Detected Total: ${total2}")
else:
    print("Could not find a total amount.")

path = "receipt_3.png" 
total3 = extract_receipt_total(path)
t3=total3

if total3:
    print(f"Success! Detected Total: ${total3}")
else:
    print("Could not find a total amount.")

print("\n--- Summary ---")
print('Total of all the three receipts is: $', float(t1) + float(t2) + float(t3))
'''

import cv2
import pytesseract
import re
import os
from PIL import Image

# 1. SET TESSERACT PATH (Ensure this matches your installation)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_total_from_receipt(image_path):
    """Extracts the numerical total from a single receipt image."""
    # Load the image
    image = cv2.imread(image_path)
    
    if image is None:
        print(f"❌ Error: Could not find image at {image_path}")
        return 0.0

    # Preprocessing: Grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # OCR - Convert image to string
    text = pytesseract.image_to_string(gray)
    
    # Regex to find 'Total' followed by a number (e.g., Total: 45.50 or Total 10.00)
    # This looks for 'total', skips symbols/spaces, and grabs the digits
    match = re.search(r'total[:\s]+[$?]?(\d+\.\d{2})', text, re.IGNORECASE)
    
    if match:
        amount = float(match.group(1))
        print(f"✅ Extracted from {os.path.basename(image_path)}: ${amount:.2f}")
        return amount
    else:
        print(f"⚠️ Warning: Could not find a total in {os.path.basename(image_path)}")
        return 0.0

def main():
    # 2. DEFINE YOUR 3 RECEIPT PATHS
    # Use absolute paths to avoid the "File Not Found" error
    receipt_files = [
        r"C:\Users\KIRTI\OneDrive\Desktop\AI-ML project\receipt_1.png",
        r"C:\Users\KIRTI\OneDrive\Desktop\AI-ML project\receipt_2.png",
        r"C:\Users\KIRTI\OneDrive\Desktop\AI-ML project\receipt_3.png"
    ]

    grand_total = 0.0
    print("--- Starting Receipt Processing ---\n")

    for file_path in receipt_files:
        individual_total = extract_total_from_receipt(file_path)
        grand_total += individual_total

    print("\n" + "="*30)
    print(f"FINAL TOTAL EXPENSE: ${grand_total:.2f}")
    print("="*30)

if __name__ == "__main__":
    main()