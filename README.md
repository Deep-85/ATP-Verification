# ATP Verification

A modular computer vision pipeline developed during my internship for ATP (Acceptance Test Procedure) image verification. The project focuses on extracting and analyzing information from telecom equipment images using OCR and computer vision techniques.

---

## Project Overview

This project automates the verification of ATP images by performing multiple image analysis tasks through a modular pipeline.

The system includes:

- OCR (Optical Character Recognition)
- Image Enhancement
- Blur Detection
- Color Detection
- Object Detection

The design allows each module to work independently while also supporting an integrated analysis pipeline.

---

## Features

- Image preprocessing and enhancement
- OCR-based text extraction
- Blur detection using Laplacian variance
- Dominant color detection
- Object detection using YOLOv8
- Batch image processing support
- Visualization of OCR results

---

## Project Structure

```
ATP-Verification/
│
├── analyze_image.py
├── app.py
├── batch_ocr.py
├── preprocessing.py
├── image_enhancer.py
├── blur_detector.py
├── color_detector.py
├── object_detector.py
├── text_detector.py
├── utils.py
│
├── sample_images/
├── outputs/
│
├── test_ocr.py
├── test_blur.py
├── test_color.py
├── test_object.py
├── test_enhancer.py
│
├── requirements.txt
└── README.md
```

---

## Processing Pipeline

```
Input Image
      │
      ▼
Image Enhancement
      │
      ▼
OCR Text Extraction
      │
      ▼
Blur Detection
      │
      ▼
Color Detection
      │
      ▼
Object Detection
      │
      ▼
Analysis Report
```

---

## Technologies Used

- Python
- OpenCV
- NumPy
- Tesseract OCR
- Ultralytics YOLOv8

### OCR Technologies Evaluated During Development

During development, multiple OCR engines were explored and compared:

- Tesseract OCR
- EasyOCR
- TrOCR
- PaddleOCR (evaluation attempted)
- Surya OCR (evaluation attempted)

The submitted implementation uses the OCR pipeline available in this repository.

---

## Installation

Clone the repository

```bash
git clone https://github.com/Deep-85/ATP-Verification.git
cd ATP-Verification
```

Create virtual environment

```bash
python -m venv venv
```

Activate environment

Linux

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

Run OCR

```bash
python test_ocr.py
```

Analyze an image

```bash
python analyze_image.py
```

Run object detection

```bash
python test_object.py
```

Run blur detection

```bash
python test_blur.py
```

Run color detection

```bash
python test_color.py
```

---

## Challenges Faced

- OCR performance on complex telecom images
- Image quality variations
- Handling blurred images
- Evaluation of multiple OCR engines
- Corporate proxy restrictions while evaluating PaddleOCR and Surya OCR

---

## Future Improvements

- Handwritten text recognition
- Improved OCR accuracy
- FastAPI-based REST API
- Custom-trained object detection model
- ATP report generation
- Better image preprocessing techniques

---

## Author

**Deep Patil**

Internship Project
