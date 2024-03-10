import tkinter as tk
from PIL import Image, ImageTk
import os

class ImageSlideshow(tk.Frame):
    def __init__(self, master=None, image_folder=None):
        super().__init__(master)
        self.master = master
        self.image_folder = image_folder
        self.images = []
        self.current_image = None
        self.load_images()
        self.create_widgets()
        
    def load_images(self):
        for filename in os.listdir(self.image_folder):
            image_path = os.path.join(self.image_folder, filename)
            with Image.open(image_path) as img:
                img = img.resize((800, 800), Image.ANTIALIAS)
                self.images.append(ImageTk.PhotoImage(img))
                
    def create_widgets(self):
        self.label = tk.Label(self.master, image=self.images[0])
        self.label.pack()
        self.current_image = 0
        self.after(3000, self.show_next_image)
        
    def show_next_image(self):
        self.current_image += 1
        if self.current_image >= len(self.images):
            self.current_image = 0
        self.label.configure(image=self.images[self.current_image])
        self.after(3000, self.show_next_image)

root = tk.Tk()
root.geometry("800x800")
root.title("Image Slideshow")

slideshow = ImageSlideshow(root, image_folder="D://measure_screw_detection//detected_screw_save_pic//")
slideshow.pack()

root.mainloop()
