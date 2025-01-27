import os
from tkinter import Tk, Button, filedialog, Label, messagebox
from PIL import Image

def select_and_convert():
    # Open file dialog to select .webp file
    file_path = filedialog.askopenfilename(
        filetypes=[("WEBP files", "*.webp")],
        title="Select a WEBP file"
    )
    
    if not file_path:
        return  # User cancelled
    
    try:
        # Open the image and convert to PNG
        with Image.open(file_path) as img:
            img = img.convert("RGBA")  # Ensure transparency is preserved
            base_name = os.path.splitext(file_path)[0]
            png_path = f"{base_name}.png"
            img.save(png_path, "PNG")
        
        # Show success message
        messagebox.showinfo("Success", f"File converted and saved at:\n{png_path}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred:\n{e}")

# Create the main GUI window
root = Tk()
root.title("WEBP to PNG Converter")
root.geometry("300x150")

# GUI components
Label(root, text="WEBP to PNG Converter", font=("Arial", 14)).pack(pady=10)
Button(root, text="Select WEBP File", command=select_and_convert, width=20).pack(pady=20)

# Run the GUI event loop
root.mainloop()
