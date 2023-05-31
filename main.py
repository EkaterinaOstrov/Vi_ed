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
    
    def brightness_click(self):
        pass
    
    def contrast_click(self):
        pass
    
    def rgb_balans_click(self):
        pass
    
    def choice_big(self):
        pass

    def choice_small(self):
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

    def rnd_green_click(self):
        pass

    def rnd_blue_click(self):
        pass

    def rnd_biruza_click(self):
        pass
    
    def rnd_fiol_click(self):
        pass
    
    def rnd_lilov_click(self):
        pass

    def random_color_click(self):
        pass

    def create_menu(self):
        menu = Menu(self.parent)
        self.file_menu = Menu(menu)
        self.filters_menu = Menu(menu)
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
        self.filters_menu.add_command(label="Негатив", command=self.negative_click,
        state='disabled')
        self.filters_menu.add_command(label="Шум", command=self.rnd_noise_click,
        state='disabled')
        self.filters_menu.add_command(label="Оттенки серого", command=self.gray_click,
        state='disabled')
        self.filters_menu.add_command(label="Сепия", command=self.serpia_click,
        state='disabled')
        self.filters_menu.add_command(label="Черно-белый",
        command=self.black_white_click, state='disabled')
        self.filters_menu.add_command(label="Оттенки красного",
        command=self.rnd_red_click, state='disabled')
        self.filters_menu.add_command(label="Оттенки зеленого",
        command=self.rnd_green_click, state='disabled')
        self.filters_menu.add_command(label="Оттенки синего",
        command=self.rnd_blue_click, state='disabled')
        self.filters_menu.add_command(label="Оттенки бирюзового",
        command=self.rnd_biruza_click, state='disabled')
        self.filters_menu.add_command(label="Оттенки фиолетового",
        command=self.rnd_fiol_click, state='disabled')        
        self.filters_menu.add_command(label="Оттенки лилового",
        command=self.rnd_lilov_click, state='disabled')
        self.filters_menu.add_command(label="Случайные цвета",
        command=self.random_color_click, state='disabled')

#наполнение подменю Параметр
        self.parametr_menu.add_command(label="Яркость", command=self.brightness_click,
        state='disabled')
        self.parametr_menu.add_command(label="Контрастность",
        command=self.contrast_click, state='disabled')
        self.parametr_menu.add_command(label="Цветовой баланс",
        command=self.rgb_balans_click, state='disabled')
        self.parametr_menu.add_command(label="Увеличить", command=self.choice_big,
        state='disabled')
        self.parametr_menu.add_command(label="Уменьшить", command=self.choice_small,
        state='disabled')
        self.parametr_menu.add_command(label="Повернуть", command=self.choice_rotation,
        state='disabled')

        label_fail = Label(root, text="Параметры файла")
        label_fail.place(x=22, y=30)

#кнопка для открытия изображения
        self.btn_open = Button(text="Открыть",  height=3, width=20, command=self.open)
        self.btn_open.place(x=25, y =60)

#кнопка для применения фильтра "Сохранить"
        self.btn_save = Button(text="Сохранить", height=3, width=20, command=self.save, state="disabled")
        self.btn_save.place(x=25, y=120)
#кнопка для применения фильтра "Очистить"
        self.btn_clean = Button(text="Очистить", height=3, width=20, command=self.clean, state="disabled")
        self.btn_clean.place(x=25, y=180)

#кнопка для применения фильтра "Выход"
        self.btn_close = Button(text="Выход", height=3, width=20, command=self.close)
        self.btn_close.place(x=25, y=240)

        label_fail_par = Label(root, text="Параметры изображения")
        label_fail_par.place(x=25, y=300)

        self.btn_yar = Button(text="Яркость", height=3, width=20, command=self.brightness_click, state="disabled")
        self.btn_yar.place(x=25, y=360)

        self.btn_contr = Button(text="Контрастность", height=3, width=20, command=self.contrast_click, state="disabled")
        self.btn_contr.place(x=25, y=420)

        self.btn_cvb = Button(text="RGB баланс", height=3, width=20, command=self.rgb_balans_click, state='disabled')
        self.btn_cvb.place(x = 25, y = 480)

        self.parent.config(menu=menu)

    def contour(self):
        image = Image.open(self.filename)      
        image = image.filter(ImageFilter.CONTOUR)
        
        self.photo = ImageTk.PhotoImage(image)
        self.display.itemconfigure(self.display_img, image=self.photo, anchor="nw")

if __name__ == '__main__':
    root = Tk()
    root.title("VISUAL EDITOR")
    root.geometry("1250x1050+500+400")
    app = Example(root)
    root.mainloop()