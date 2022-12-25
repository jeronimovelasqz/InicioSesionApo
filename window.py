from tkinter import *


class InicioSesion:


    def __init__(self):
        self.window = Tk()

        self.window.geometry("1477x871")
        self.window.configure(bg = "#ffffff")
        self.canvas = Canvas(
            self.window,
            bg = "#ffffff",
            height = 871,
            width = 1477,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        self.canvas.place(x = 0, y = 0)

        self.background_img = PhotoImage(file = f"background.png")
        self.background = self.canvas.create_image(
            632.0, 397.0,
            image=self.background_img)

        self.entry0_img = PhotoImage(file = f"img_textBox0.png")
        self.entry0_bg = self.canvas.create_image(
            745.0, 275.5,
            image = self.entry0_img)

        self.entry0 = Entry(
            bd = 0,
            bg = "#f2a6a6",
            highlightthickness = 0)

        self.entry0.place(
            x = 612.0, y = 254,
            width = 266.0,
            height = 41)

        self.entry1_img = PhotoImage(file = f"img_textBox1.png")
        self.entry1_bg = self.canvas.create_image(
            745.0, 360.5,
            image = self.entry1_img)

        self.entry1 = Entry(
            bd = 0,
            bg = "#f2a6a6",
            highlightthickness = 0)

        self.entry1.place(
            x = 612.0, y = 339,
            width = 266.0,
            height = 41)

        self.img0 = PhotoImage(file = f"img0.png")
        self.b0 = Button(
            image = self.img0,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.btn_clicked,
            relief = "flat")

        self.b0.place(
            x = 664, y = 397,
            width = 148,
            height = 43)

        self.img1 = PhotoImage(file = f"img1.png")
        self.b1 = Button(
            image = self.img1,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.btn_clicked,
            relief = "flat")

        self.b1.place(
            x = 688, y = 538,
            width = 148,
            height = 21)

        self.img2 = PhotoImage(file = f"img2.png")
        self.b2 = Button(
            image = self.img2,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.btn_clicked,
            relief = "flat")

        self.b2.place(
            x = 595, y = 463,
            width = 301,
            height = 14)

        self.window.resizable(False, False)
        self.window.mainloop()


    def btn_clicked(self):
        print("Button Clicked")

Window = InicioSesion()
