import os
from PIL import Image

input_dir = '/Users/<path to your directory here>'  # Absolute path to your image directory
output_dir = os.path.join(input_dir, 'optimized_images')

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Set resize factor (skip quality for lossless)
resize_factor = 0.25  

# Loop through each file in the input directory
for filename in os.listdir(input_dir):
    # Check if the file is an image based on its extension
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        file_path = os.path.join(input_dir, filename)
        print("Conditional met")
        
        # Open the image and apply transformations
        with Image.open(file_path) as img:
            # Calculate new dimensions based on resize factor
            new_width = int(img.width * resize_factor)
            new_height = int(img.height * resize_factor)
            img = img.resize((new_width, new_height), Image.LANCZOS)
            print("Transformation step complete")
            
            # Save with settings based on file type
            output_path = os.path.join(output_dir, filename)
            
            if filename.lower().endswith('.png'):
                # Lossless compression for PNG
                img.save(output_path, format="PNG", optimize=True)
            else:
                # Save JPEG with minimum quality reduction
                img.save(output_path, format="JPEG", quality=95, optimize=True)
            
            print(f"Original size: {img.size}, New size: {new_width}x{new_height}")
            print(f"Saved to {output_path}")

print(f"All images have been saved: '{output_dir}'")
