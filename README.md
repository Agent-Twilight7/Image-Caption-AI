# Image-Caption-AI
A cutting-edge application that leverages AI to generate creative captions for images while offering customizable filters, making visual storytelling interactive and fun.
# Enhanced Image Caption Generator with Streamlit, Hugging Face, and PyTorch

This repository features an **enhanced image captioning application** that integrates advanced AI with a sleek and intuitive user interface. Built using **Streamlit**, **Hugging Face's transformers**, and **PyTorch**, the app generates descriptive captions for uploaded images, providing a smooth and engaging user experience.

## Overview

The **Enhanced Image Caption Generator** showcases the powerful integration of **AI** and **web development**. It uses the **Salesforce/blip-image-captioning-large** model, a cutting-edge transformer model from Hugging Face, combined with an improved user interface for better accessibility and interaction.

### New Enhancements Include:

- **Custom Theming**: A visually appealing dark-themed interface, powered by Streamlit's theming options.
- **Image Gallery**: A feature allowing users to view a gallery of all uploaded images alongside their captions.
- **Image Enhancements**: Added functionality to apply filters like grayscale or sepia using OpenCV before generating captions.

These upgrades make the app not only functional but also more engaging and user-friendly.

## Key Features

- **Modern UI/UX**: Improved design and theming for a polished user experience.
- **AI-Powered Captions**: Uses Hugging Face's `Salesforce/blip-image-captioning-large` model to produce accurate and context-aware image captions.
- **Filter Options**: Allows users to enhance their images by applying filters before caption generation.
- **Image Gallery**: Displays all uploaded images along with their captions in a gallery format for easy browsing.

---

## How to Run

### Prerequisites

Ensure you have the following installed on your system:

- **Python** (3.8 or higher)
- Required Python libraries (listed in `requirements.txt`)

### Steps

1. Clone this repository:
   ```bash
   git clone <your-repo-url>
   ```
2. Navigate to the project directory:

```cd image-caption-generator ```
3. Install the dependencies:
```pip install -r requirements.txt ```
4. Run the Streamlit app:
```streamlit run main.py ```
5. Access the application in your browser at http://localhost:8501.

## Usage

### Uploading and Captioning Images
1. **Upload an image**: Use the **sidebar** to upload an image file (supported formats: JPG, JPEG, PNG).
2. **Apply filters**: Select from the available filters such as **grayscale** or **sepia** to enhance your image before generating a caption.
3. **Generate caption**: Click the **"Generate Caption"** button to process the image and display the caption alongside the processed version of the image.

### Exploring the Gallery
- The application maintains a gallery of all **previously uploaded images**.
- Each image in the gallery is displayed with its corresponding caption, allowing for better exploration and comparison.

These features make it easy to manage and interact with multiple images in one session!
````

