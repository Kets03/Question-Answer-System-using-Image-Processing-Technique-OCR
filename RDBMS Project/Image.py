import tkinter as tk
from tkinter import filedialog
from PIL import Image

# Create a function to open a file dialog and get the image path
def get_image_path():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp *.gif")])
    return file_path

# Main function
def main():
    image_path = get_image_path()

    if image_path:
        print(f"Selected image path: {image_path}")
        # You can perform further operations on the selected image here
    else:
        print("No image selected.")

if __name__ == "__main__":
    main()
