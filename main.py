from PIL import Image, ImageTk
from tkinter import Tk, Label, BOTH, Frame, Button, messagebox
 
class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")   
        self.parent = parent
        self.create_menu()
    
    def close(self):
        if messagebox.askyesno('Выход', 'Действительно хотите завершить работу с приложением?'):
            self.parent.destroy()
#  в перспективе надо переделать данную часть
        else:
            messagebox.askyesno('Вы отказались от выхода из программы', 'Продолжаем!')
    
    def create_menu(self):
        self.pack(fill=BOTH, expand=1)
        self.btn_exit = Button(text="Выход", height = 2, width = 10, command = self.close)
        self.btn_exit.place(x = 5, y = 25)

        nordshine = Image.open("NordSh.jpg")
        nordshineing = ImageTk.PhotoImage(nordshine)
        Label1 = Label(self, image=nordshineing)
        Label1.image = nordshineing
        Label1.place(x=50, y = 100)

if __name__ == '__main__':
    root = Tk()
    root.title("Мой графический редактор")
    root.geometry("1250x1050+500+400")
    root.attributes("-alpha", 0.9)
    app = Example(root)
    root.mainloop()