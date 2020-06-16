from tkinter import *
import tkinter.ttk as ttk
from tkinter import colorchooser
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageGrab, ImageTk
import PIL
from tkinter import messagebox

root = Tk()
root.title('Painting App')
root.geometry("800x800")

b_color = 'black'

def paint(e):
    # Brush Parameters
    b_width = '%0.0f' % float(my_slide.get())
    # b_color = 'green'
    # Brush types BUTT, ROUND, PROJECTING
    b_type = brush_type.get()
    # Starting position
    x1 = e.x - 1
    y1 = e.y - 1

    # Ending position
    x2 = e.x + 1
    y2 = e.y + 1

    # Draw on the Canvas
    my_canvas.create_line(x1, y1, x2, y2, fill=b_color, width=b_width, capstyle=b_type, smooth=True)


# Change the size of the brush
def change_brush_size(thing):
    slider_lable.config(text='%0.0f' % float(my_slide.get()))

# Change brush color
def change_brush_color():
    global b_color
    b_color = 'black'
    b_color = colorchooser.askcolor(color=b_color)[1]
    # color = Label(root, text=brush_color)
    # color.pack(pady=20)

# Change canvas color
def change_canvas_color():
    global bg_color
    bg_color = 'black'
    bg_color = colorchooser.askcolor(color=bg_color)[1]
    my_canvas.config(bg=bg_color)

# Clesr screen
def clear_screen():
    my_canvas.delete(ALL)
    my_canvas.config(bg='white')

# Save image
def save_as_png():
    result = filedialog.asksaveasfilename(initialdir='E:/python by pc/', filetypes=(("png files", "*.png"), ("all files", "*.*")))

    if result.endswith('.png'):
        pass
    else:
        result = result + '.png'

    if result:
        x=root.winfo_rootx()+my_canvas.winfo_x()
        y=root.winfo_rooty()+my_canvas.winfo_y()
        x1=x+my_canvas.winfo_width()
        y1=y+my_canvas.winfo_width()
        ImageGrab.grab().crop((x,y,x1,y1)).save(result)
        #Pop th message box
        messagebox.showinfo("Image saved", "Your Image has been saved")


# Create our canvas
w = 600
h = 400

my_canvas = Canvas(root, width=w, height=h, bg="white")
my_canvas.pack(pady=20)

# my_canvas.create_line(0, 100, 300, 100, fill="red")
# my_canvas.create_line(150, 0, 150, 200, fill="red")

my_canvas.bind('<B1-Motion>', paint)

# Create a brush options frame
brush_options = Frame(root)
brush_options.pack(pady=20)

# Brush Size
brush_size_frame = LabelFrame(brush_options, text='Brush size')
brush_size_frame.grid(row=0, column=0, padx=50)
# Brush slider
my_slide = ttk.Scale(brush_size_frame, from_=50, to=1, command=change_brush_size, orient=VERTICAL, value=10)
my_slide = ttk.Scale(brush_size_frame, from_=50, to=1, command=change_brush_size, orient=VERTICAL, value=10)
my_slide.pack(pady=10, padx=10)
# Brush slider lable
slider_lable = Label(brush_size_frame, text=my_slide.get())
slider_lable.pack(pady=5)

# Bursh type
brush_type_frame = LabelFrame(brush_options, text='Brush Type', height=400)
brush_type_frame.grid(row=0, column=1, padx=50)

brush_type = StringVar()
brush_type.set('round')

# Create radio buttons for brush type
brush_type_radio1 = Radiobutton(brush_type_frame, text='Round', variable=brush_type, value='round')
brush_type_radio2 = Radiobutton(brush_type_frame, text='Slash', variable=brush_type, value='butt')
brush_type_radio3 = Radiobutton(brush_type_frame, text='Diamond', variable=brush_type, value='projecting')

brush_type_radio1.pack(anchor=W)
brush_type_radio2.pack(anchor=W)
brush_type_radio3.pack(anchor=W)

# change colors
change_colors_frame = LabelFrame(brush_options, text='Change colors')
change_colors_frame.grid(row=0, column=2)

# Change brush color
brush_color_button = Button(change_colors_frame, text="Brush color", command=change_brush_color)
brush_color_button.pack(pady=10, padx=10)

# Change canvas background
canvas_color_button = Button(change_colors_frame, text="Canvas color", command=change_canvas_color)
canvas_color_button.pack(pady=10, padx=10)

# Program options frame
options_frame = LabelFrame(brush_options, text='Program options')
options_frame.grid(row=0, column=3, padx=50)

# Clear screen button
clear_button = Button(options_frame, text="Clear screen", command=clear_screen)
clear_button.pack(padx=10, pady=10)

# Save image
save_button = Button(options_frame, text="Save to PNG", command=save_as_png)
save_button.pack(padx=10, pady=10)

root.mainloop()