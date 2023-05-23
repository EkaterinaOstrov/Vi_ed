from PIL import ImageTk, Image, ImageFilter
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

#добавляем фильтр для применения размытия к изображению    
    def blur(self):
        image = Image.open(self.filename)

        image = image.filter(ImageFilter.BLUR)

        self.photo = ImageTk.PhotoImage(image)
        self.display.itemconfigure(self.display_img, image = self.photo, anchor="nw")

    def miniatura(self):#использование фильтра для создания миниатюр  
        image = Image.open(self.filename)

        image = image.resize((150, 150), Image.ANTIALIAS)

        self.photo = ImageTk.PhotoImage(image)
        self.display.itemconfigure(self.display_img, image=self.photo, anchor="nw")

    def create_menu(self):
#кнопка для открытия изображения
        self.btn_open = Button(text="Открыть",  height=3, width=20, command=self.open)
        self.btn_open.place(x=25, y =60)

#кнопка для применения фильтра "Размытие"
        self.btn_blur = Button(text="Размытие изображения", height=3, width=20, command=self.blur)
        self.btn_blur.place(x=25, y= 120)
#кнопка для применения фильтра "Создание миниатюры"
        self.btn_miniatura = Button(text="Создать миниатюру", height=3, width=20, command=self.miniatura)
        self.btn_miniatura.place(x=25, y=180)

if __name__ == '__main__':
    root = Tk()
    root.title("VISUAL EDITOR")
    root.geometry("1250x1050+500+400")
    app = Example(root)
    root.mainloop()