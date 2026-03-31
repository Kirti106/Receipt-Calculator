# Receipt-Calculator
# 🧾 Receipt Total Extractor

A Python-based project that uses **Tesseract OCR** and **OpenCV** to extract total amounts from receipt images and compute the overall expense automatically.

---

## 📌 Overview

This project processes multiple receipt images, extracts text using Optical Character Recognition (OCR), identifies the **total amount** using pattern matching, and calculates a **final combined total**.

It is useful for:

* Expense tracking
* Automating bill processing
* AI/ML academic projects

---

## 🚀 Features

* Extracts text from receipt images
* Identifies total amount automatically
* Supports multiple receipts
* Displays individual and final totals
* Handles missing or invalid files safely

---

## 🛠️ Tech Stack

* **Python**
* **OpenCV (cv2)** – Image processing
* **pytesseract** – OCR engine interface
* **Tesseract OCR** – Text recognition
* **Regex (re)** – Pattern matching
* **PIL (Pillow)** – Image handling

---

## 📂 Project Structure

```
Receipt-Extractor/
│
├── main.py
├── receipt_1.png
├── receipt_2.png
├── receipt_3.png
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Install Required Python Libraries

```bash
pip install opencv-python pytesseract pillow
```

---

### 2. Install Tesseract OCR

1. Download Tesseract from:
   https://github.com/tesseract-ocr/tesseract

2. Install it (default path recommended)

3. Set the path in your Python code:

```python
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

---

## ▶️ Usage

1. Add your receipt images to the project folder
2. Update file paths in the script:

```python
receipt_files = [
    r"path_to_receipt_1.png",
    r"path_to_receipt_2.png",
    r"path_to_receipt_3.png"
]
```

3. Run the script:

```bash
python main.py
```

---

## 🧠 Working Principle

### Step 1: Image Loading

* Reads the receipt image using OpenCV

### Step 2: Preprocessing

* Converts the image to grayscale for better OCR performance

### Step 3: Text Extraction

* Uses Tesseract OCR to extract text from the image

### Step 4: Pattern Matching

* Applies regex to find the total amount:

```
total[:\s]+[$]?(\d+\.\d{2})
```

### Step 5: Aggregation

* Adds all extracted totals to compute the final expense

---

## 📊 Sample Output

```
--- Starting Receipt Processing ---

✅ Extracted from receipt_1.png: $120.50
✅ Extracted from receipt_2.png: $89.99
⚠️ Warning: Could not find a total in receipt_3.png

==============================
FINAL TOTAL EXPENSE: $210.49
==============================
```

---

## ⚠️ Limitations

* OCR accuracy depends on image quality
* Works best with:

  * Clear, high-resolution images
  * Standard receipt formats
* May fail if:

  * "Total" keyword is missing
  * Font is unclear or distorted

---

## 💡 Future Improvements

* Support for multiple currencies (₹, €, etc.)
* Better regex handling for different formats
* Advanced preprocessing (thresholding, noise removal)
* GUI or web-based interface
* Export results to CSV/Excel
* Use AI models for smarter detection

---
