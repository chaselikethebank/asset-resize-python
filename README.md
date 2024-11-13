# File Cutter


Image too large for load? 
Make it smaller! 

**File Cutter** is a Python application for resizing and optimizing images in bulk. This tool is especially useful for reducing the file size of large images while maintaining quality, making them more suitable for web use, storage, or further processing.

## Project Structure

```plaintext
asset-resize-python
├── README.md
├── file-cutter.py
└── images-print-here
```

- README.md: Documentation for the application.
- file-cutter.py: The main script for resizing and optimizing images.
- images-print-here: A directory where you place images to be resized.

### Features 

- Resize: Reduces the dimensions of each image to 25% of its original size by default.
- Optimize: Uses lossless compression for PNG images and minimal quality reduction for JPEGs, resulting in efficient file sizes with little to no visible quality loss.

### Dependencies 


Python 3.x
```bash
brew install python
```

Receipt
```bash
python3 --version
```

Pillow library for image handling and manipulation.
To install Pillow, use:
```bash
pip install pillow
```

### Usage
1. Place all images you want to resize in the put-images-here folder.
2. Update the input_dir path in file-cutter.py to point to put-images-here.
3. Run the application:

```bash
python file-cutter.py
```

4. Optimized images will be saved in a subdirectory called optimized_images within images-print-here.

### Config
Resize Factor: By default, images are resized to 25% of their original size. Adjust this by changing the resize_factor variable in the script.
Image Quality: JPEGs are saved with a quality setting of 95 for near-lossless compression.

### Notes
- Currently supports .png, .jpg, and .jpeg files.
- The application will display the original and new dimensions of each processed image, along with the location of saved files.

### License
This project is open-source and available for further customization to suit your needs.