from PIL import ImageTk, Image, ImageFilter
from tkinter import Frame, Canvas, Button, Tk, filedialog, Scrollbar, Label, messagebox, Menu

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

    def save(self):
        pass
    
    def clean(self):
        pass
    
    def close(self):
        pass
    
    def brightness_clik(self):
        pass
    
    def contrast_click(self):
        pass
    
    def rgb_balance(self):
        pass
    
    def choice_big(self):
        pass
    
    def choice_rotation(self):
        pass
    
    def negative_click(self):
        pass
    
    def rnd_noise_click(self):
        pass
    
    def gray_click(self):
        pass
    
    def serpia_click(self):
        pass
    
    def black_white_click(self):
        pass
    
    def rnd_red_click(self):
        pass
   
'''    
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
        image = Image.open(self.filename)
        
        image = image.resize((150, 150), Image.ANTIALIAS)
        
        self.photo = ImageTk.PhotoImage(image)
        self.display.itemconfigure(self.display_img, image=self.photo, anchor="nw")

    def contour(self): #использование фильтра контрурирования
        image = Image.open(self.filename)

        image = image.filter(ImageFilter.CONTOUR)

        self.photo = ImageTk.PhotoImage(image)
        self.display.itemconfigure(self.display_img, image=self.photo, anchor="nw")

    def emboss(self):
        image = Image.open(self.filename)

        image = image.filter(ImageFilter.EMBOSS)
        
        self.photo = ImageTk.PhotoImage(image)
        self.display.itemconfigure(self.display_img, image=self.photo, anchor="nw")'''
    
    def create_menu(self):
        menu = Menu(self.parent)
        self.file_menu = Menu(menu)
        self.filter_menu = Menu(menu)
        self.parametr_menu = Menu(menu)

#формирование подменю
        menu.add_cascade(label="Файл",menu=self.file_menu)
        menu.add_cascade(label="Фильтры", menu=self.filters_menu)
        menu.add_cascade(label="Параметры", menu=self.parametr_menu)

#наполнение подменю Файл
        self.file_menu.add_command(label="Открыть", command=self.open)
        self.file_menu.add_command(label="Сохранить", command=self.save, state="disabled")
        self.file_menu.add_command(label="Очистить", command=self.clean, state="disabled")
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Выход", command=self.close)

#наполнение подменю Фильтр
        self.filters_menu.add_command(label="Негатив", command=self.negativ_click, state="disabled")

#наполнение подменю Параметр
        self.parametr_menu.add_command(label="Яркость", command=self.brightness_clik, state="disabled")
        self.parametr_menu.add_command(label="Контрастность", command=self.contrast_click, state="disabled")

        label_fail = Label(root, text="Параметры файла")
        label_fail.place(x=22, y=30)

#кнопка для открытия изображения
        self.btn_open = Button(text="Открыть",  height=3, width=20, command=self.open)
        self.btn_open.place(x=25, y =60)

'''
 #кнопка для применения фильтра "Размытие"
        self.btn_blur = Button(text="Размытие изображения", height=3, width=20, command=self.blur)
        self.btn_blur.place(x=25, y= 120)
#кнопка для применения фильтра "Создание миниатюры"
        self.btn_miniatura = Button(text="Создать миниатюру", height=3, width=20, command=self.miniatura)
        self.btn_miniatura.place(x=25, y=180)
#кнопка для применения фильтра "Создание миниатюры"
        self.btn_contour = Button(text="Контур", height=3, width=20, command=self.contour)
        self.btn_contour.place(x=25, y=240)

#кнопка для применения фильтра "Тиснение"
        self.btn_emboss = Button(text="Тиснение", height=3, width=20, command=self.emboss)
        self.btn_emboss.place(x=25, y=300)
'''

#кнопка для применения фильтра "Сохранить"
        self.btn_save = Button(text="Сохранить", height=3, width=20, command=self.save, state="disabled")
        self.btn_save.place(x=25, y=60)
#кнопка для применения фильтра "Очистить"
        self.btn_clean = Button(text="Очистить", height=3, width=20, command=self.clean, state="disabled")
        self.btn_clean.place(x=25, y=105)

#кнопка для применения фильтра "Выход"
        self.btn_close = Button(text="Выход", height=3, width=20, command=self.close)
        self.btn_close.place(x=25, y=195)

        self.parent.config(menu=menu)

if __name__ == '__main__':
    root = Tk()
    root.title("VISUAL EDITOR")
    root.geometry("1250x1050+500+400")
    app = Example(root)
    root.mainloop()