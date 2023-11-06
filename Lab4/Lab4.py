import os
import random
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from ann import create_annotation_file, load_data_from_csv, get_next_instance

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Dataset Annotation App")
        self.geometry("800x600")
        self.dataset_folder = "D:/Test/dataset322223"
        self.class_label = ""
        self.instance_label = tk.Label(self, text="")
        self.instance_label.pack(pady=20)
        self.load_button = tk.Button(self, text="Load Dataset", command=self.load_dataset)
        self.load_button.pack(pady=20)
        self.next_zebra_button = tk.Button(self, text="Next Zebra", command=self.get_next_zebra)
        self.next_zebra_button.pack(pady=10)
        self.next_horse_button = tk.Button(self, text="Next Horse", command=self.get_next_horse)
        self.next_horse_button.pack(pady=10)
        self.image_label = tk.Label(self)
        self.image_label.pack(pady=20)

    def load_dataset(self):
        self.class_label = random.choice(['zebra', 'bay_horse'])
        csv_file_path = os.path.join(self.dataset_folder, f'annotations_{self.class_label}.csv')
        load_data_from_csv(csv_file_path)
        self.update_instance_label()

    def update_instance_label(self):
        next_instance = get_next_instance(self.class_label)
        if next_instance:
            self.instance_label.config(text=f'Next instance of {self.class_label}: {next_instance}')
            image_path = os.path.join(self.dataset_folder, next_instance)
            img = Image.open(image_path)
            img = img.resize((400, 300), Image.BICUBIC)
            img = ImageTk.PhotoImage(img)
            self.image_label.config(image=img)
            self.image_label.image = img
        else:
            self.instance_label.config(text=f'No available instances for {self.class_label}')
            self.image_label.config(image=None)

    def get_next_zebra(self):
        self.class_label = 'zebra'
        self.update_instance_label()

    def get_next_horse(self):
        self.class_label = 'bay_horse'
        self.update_instance_label()

if __name__ == "__main__":
    app = Application()
    app.mainloop()
