import random
from tkinter import *
from tkinter import filedialog
from PIL import Image
import numpy as np
from tkinter import messagebox
import colorsys


    # Define the bounding box of the sprite
sprite_x1 = 50
sprite_y1 = 50
sprite_x2 = 200
sprite_y2 = 200
def is_sprite_pixel(x, y):

    # Check if the pixel is within the bounding box
    if x >= sprite_x1 and x <= sprite_x2 and y >= sprite_y1 and y <= sprite_y2:
        return True
    else:
        return False

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(padx=10, pady=10)
        self.create_widgets()

    def create_widgets(self):
        # Set the color scheme
        self.master.config(bg='black')
        fg_color = 'white'
        button_color = 'gray'

        # Create a label for the image file path
        self.file_label = Label(self, text="No file selected", bg='black', fg=fg_color, font=("Helvetica", 16))
        self.file_label.pack(pady=5)

        # Create a button to select the image file
        self.file_button = Button(self, text="Select Image", command=self.select_file, bg=button_color, fg=fg_color)
        self.file_button.pack(pady=5)

        # Create a label for the number of files to output
        self.num_files_label = Label(self, text="Number of Files:")
        self.num_files_label.pack()

        # Create an entry box for the number of files to output
        self.num_files_entry = Entry(self)
        self.num_files_entry.pack()

        # Create a label for the output directory path
        self.dir_label = Label(self)
        self.dir_label.pack()

        # Create a button to select the output directory
        self.dir_button = Button(self, text="Select Directory", command=self.select_dir)
        self.dir_button.pack()

        # Create a button to start the color change process
        self.start_button = Button(self, text="Start", command=self.start)
        self.start_button.pack()

    def select_file(self):
        # Open a file dialog to select an image file
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])

        # Update the file label with the selected file path
        self.file_label.config(text=file_path)

    def select_dir(self):
        # Open a directory dialog to select an output directory
        dir_path = filedialog.askdirectory()

        # Update the directory label with the selected directory path
        self.dir_label.config(text=dir_path)

    
    def start(self):
        # Get the selected image file path and open the image
        img_path = self.file_label.cget("text")
        img = Image.open(img_path)
        img = img.convert('RGB')

        # Set the bounding box to the full image
        self.sprite_x1 = 0
        self.sprite_y1 = 0
        self.sprite_x2, self.sprite_y2 = img.size

        # Get the number of files to output and the selected output directory path
        num_files = int(self.num_files_entry.get())
        dir_path = self.dir_label.cget("text")

        # Loop through each new image and set its color randomly
        for i in range(num_files):
            img_array = np.array(img)

            # Generate a new random color for each image
            new_color = np.array([random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)])

            # Apply the color change to the sprite
            for x in range(self.sprite_x1, self.sprite_x2):
                for y in range(self.sprite_y1, self.sprite_y2):
                    img_array[y, x] = new_color

            # Convert the numpy array back to a PIL image
            new_img = Image.fromarray(img_array)

            # Save each new image with a different name for each color in the selected output directory
            new_img.save(f'{dir_path}/enemy1_{i}.png')

            print(f'enemy1_{i}.png saved successfully!')

        # Ask if they would like to change the color of another image
        if messagebox.askyesno("Change Color", "Would you like to change the color of another image?"):
            # Clear all input fields and labels and start over
            self.file_label.config(text="")
            self.num_files_entry.delete(0, END)
            self.dir_label.config(text="")
            self.master.update()
            return

        # Exit the application if they do not want to change another image
        else:
            exit()


# Create a Tkinter window and start the application
root = Tk()
root.title("Knotz Color Changer")
# Create a label widget with the text "All Rights Reserved, Knotz4Life, LLC."
label = Label(root, text="All Rights Reserved, Knotz4Life, LLC.", borderwidth= 25)

# Pack the label widget into the root window
label.pack()
app = Application(master=root)
app.mainloop()
