import tkinter as tk
from time import strftime
from PIL import ImageTk,Image

root = tk.Tk()
root.title("Welcome Screen")
root.geometry("840x480")
# root.attributes('-fullscreen', True)  # This will open the window in fullscreen by default
# root.resizable(True, False)  # Resize in x and y directions
# root.attributes('-alpha', 0.6)  # Change the opacity of the window - by default it is 1.0

# Read the Image
image = Image.open("E:\\Python\\HelloWorld\\pictures\\DSCN9395.jpg")

# Resize the image using resize() method
resize_image = image.resize((600, 400))


# photo = ImageTk.PhotoImage(Image.open("E:\\Python\\HelloWorld\\pictures\\IMG_20200310_180317.jpg").rotate(180), size="200x200")
photo = ImageTk.PhotoImage(resize_image)
# root.iconphoto(False, photo)
# resized_image = photo.Resiresizze

greetings = tk.Label(root, text = "Welcome to Tkinter App", foreground = "black", background = "green", font = ("Times New Roman", 25))

#Alternate way of setting the text property of a Tkinter label
about_tkinter = tk.Label()
about_tkinter = tk.Label(foreground = "blue", background = "yellow", bd = 10, font = ("Arial", 25))
about_tkinter["text"] = "Standard Python interface to the Tk GUI Toolkit"

# Another way of doing Tkinter config
about_tkinter.config(text="Standard Python interface to the Tk GUI Toolkit")

time_label = tk.Label(root, font = ("calibri", 50, "bold"))
def time_clock():
    string = strftime('Date : %d-%m-%Y  Time : %H:%M:%S %p')
    time_label.config(text = string)
    time_label.after(500, time_clock)

# compound = "top" indicates that both image and picture is displayed in the label and image is on the top
image_label  = tk.Label(root, image=photo, text = "We", font = ("Arial", 24, "bold"), compound="center")



# pack() needs to be done once for each label
greetings.pack()
about_tkinter.pack()
time_label.pack(anchor = "n")
image_label.pack()
time_clock()
# This will keep running till we click on close
root.mainloop()