from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from colorthief import ColorThief
import os


def show_image():
    global filename, img
    filename = filedialog.askopenfilename(initialdir='/',
                                          title='Select Image File',
                                          filetypes=(('PNG file','*.png'),
                                                    ('JPG file','*.jpg'),     
                                                     ('ALL file','*.txt')))
    
    if filename:
        img = Image.open(filename)
        img = img.resize((340, 260))  
        img = ImageTk.PhotoImage(img)
        img_label.configure(image=img)   
        img_label.image = img
    else:
        messagebox.showwarning("Warning", "No image selected!")

def find_colors():
    if 'filename' not in globals() or not filename:
        messagebox.showerror("Error", "Please select an image first!")
        return
    
    try:
        cf = ColorThief(filename)
        palette = cf.get_palette(color_count=12)  

        for i, rgb in enumerate(palette, start=1):
            color = f'#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}'
            if i <= 6:
                colors_left.itemconfig(globals()[f'c{i}'], fill=color)
                globals()[f'hex{i}'].config(text=color)
            else:
                colors_right.itemconfig(globals()[f'c{i}'], fill=color)
                globals()[f'hex{i}'].config(text=color)

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


window = Tk()
window.title("IMAGE COLOR DETECTOR")
window.geometry('900x500+100+100')
window.config(bg="white")
window.resizable(False, False)


black_gap = Label(window, width=140, height=10, bg='blue')
black_gap.grid(column=0, row=1)


frame = Frame(window, width=800, height=400, bg='cyan')
frame.place(x=50, y=50)


logo = PhotoImage(file='Mention your image path') # image path 
Label(frame, image=logo, bg="cyan").place(x=30, y=10)
Label(frame, text='Color Finder', font='arial 25 bold', bg='cyan').place(x=120, y=25)


colors_left = Canvas(frame, bg='blanchedalmond', width=150, height=280, highlightthickness=0)
colors_left.place(x=40, y=110)

c1 = colors_left.create_rectangle((10,10,40,40), fill='black')
hex1 = Label(colors_left, text='#000000', fg='#000', font='arial 11 bold', bg='blanchedalmond')
hex1.place(x=50, y=15)

c2 = colors_left.create_rectangle((10,40,40,80), fill='black')
hex2 = Label(colors_left, text='#000000', fg='#000', font='arial 11 bold', bg='blanchedalmond')
hex2.place(x=50, y=55)

c3 = colors_left.create_rectangle((10,80,40,120), fill='black')
hex3 = Label(colors_left, text='#000000', fg='#000', font='arial 11 bold', bg='blanchedalmond')
hex3.place(x=50, y=95)

c4 = colors_left.create_rectangle((10,120,40,160), fill='black')
hex4 = Label(colors_left, text='#000000', fg='#000', font='arial 11 bold', bg='blanchedalmond')
hex4.place(x=50, y=135)

c5 = colors_left.create_rectangle((10,160,40,200), fill='black')
hex5 = Label(colors_left, text='#000000', fg='#000', font='arial 11 bold', bg='blanchedalmond')
hex5.place(x=50, y=175)

c6 = colors_left.create_rectangle((10,200,40,240), fill='black')
hex6 = Label(colors_left, text='#000000', fg='#000', font='arial 11 bold', bg='blanchedalmond')
hex6.place(x=50, y=215) 


colors_right = Canvas(frame, bg='blanchedalmond', width=150, height=280, highlightthickness=0)
colors_right.place(x=180, y=110)

c7 = colors_right.create_rectangle((10,10,40,40), fill='black')
hex7 = Label(colors_right, text='#000000', fg='#000', font='arial 11 bold', bg='blanchedalmond')
hex7.place(x=50, y=15)

c8 = colors_right.create_rectangle((10,40,40,80), fill='black')
hex8 = Label(colors_right, text='#000000', fg='#000', font='arial 11 bold', bg='blanchedalmond')
hex8.place(x=50, y=55)

c9 = colors_right.create_rectangle((10,80,40,120), fill='black')
hex9 = Label(colors_right, text='#000000', fg='#000', font='arial 11 bold', bg='blanchedalmond')
hex9.place(x=50, y=95)

c10 = colors_right.create_rectangle((10,120,40,160), fill='black')
hex10 = Label(colors_right, text='#000000', fg='#000', font='arial 11 bold', bg='blanchedalmond')
hex10.place(x=50, y=135)

c11 = colors_right.create_rectangle((10,160,40,200), fill='black')
hex11 = Label(colors_right, text='#000000', fg='#000', font='arial 11 bold', bg='blanchedalmond')
hex11.place(x=50, y=175)

c12 = colors_right.create_rectangle((10,200,40,240), fill='black')
hex12 = Label(colors_right, text='#000000', fg='#000', font='arial 11 bold', bg='blanchedalmond')
hex12.place(x=50, y=215)


selection_frame = Frame(frame, width=400, height=350, bg='burlywood')
selection_frame.place(x=370, y=25)


pic_frame = Frame(selection_frame, bd=3, width=370, height=280, bg='black', relief=GROOVE)
pic_frame.place(x=15, y=15)

img_label = Label(pic_frame, bg='black', width=340, height=260) 
img_label.place(x=0, y=0)


selectimage_btn = Button(selection_frame, text='Select Image', width=17, height=1, font='arial 13 bold', bg="beige", command=show_image)
selectimage_btn.place(x=15, y=300)

find_colors_btn = Button(selection_frame, text='Find Colors', width=17, height=1, font='arial 13 bold', bg='beige', command=find_colors)
find_colors_btn.place(x=205, y=300)

window.mainloop()
