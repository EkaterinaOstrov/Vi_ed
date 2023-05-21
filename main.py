from PIL import Image, ImageTk
from tkinter import Frame, Canvas, Button, Tk, filedialog, Scrollbar

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)   
        self.parent = parent
        self.create_menu()

        self.image = None
        self.photo = None

#создание области куда будет осуществляться загрузка изображений"
        self.display = Canvas(self.parent, width=800, height=800, bg="gray")
        self.display_img = self.display.create_image(0, 0)
        self.display.pack()

    def open(self):
        self.filename = filedialog.askopenfilename()# создание области для загрузки изображений
#диалоговое окно для выбора изображения
        self.image = Image.open(self.filename)
        self.photo = ImageTk.PhotoImage(self.image)
        self.display.itemconfigure(self.display_img, image=self.photo, anchor = "nw")

#установка скролбаров вертикаль и горизонталь по координатамб для возможности полного просмотра изобращения
        self.scr1 = Scrollbar(root, command=self.display.yview, orient='vertical')
        self.scr1.place(x=150, y=30)

        self.scr2 = Scrollbar(root, command=self.display.xview, orient='horizontal')
        self.scr2.place(x=200,y=550)

#создание кнопки открытия

    def create_menu(self):
        self.btn_open = Button(text="Открыть",  height=3, width=12, command=self.open)
        self.btn_open.place(x=25, y =60)

if __name__ == '__main__':
    root = Tk()
    root.title("VISUAL EDITOR")
    root.geometry("1250x1050+500+400")
    app = Example(root)
    root.mainloop()