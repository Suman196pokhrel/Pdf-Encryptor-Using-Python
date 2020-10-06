from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog as fd
from pdf_encryptor_logic import encryptor_logic
import threading
import time
import os


class GUI(Tk):
    def __init__(self, width=500, height=250, xoffset=500, yoffset=200):
        super().__init__()
        self.width = width
        self.height = height
        self.xoffset = xoffset
        self.yoffset = yoffset
        self.wm_geometry('%dx%d%+d%+d' % (self.width, self.height, self.xoffset, self.yoffset))
        self.title('PDF Encryption')
        self.img_load = Image.open(
            'C:\Imp softwares\Pycharm\Pycharm projects\pdf_encryptor\image_assets\window_icon.png')
        self.image = ImageTk.PhotoImage(self.img_load)
        self.iconphoto(False, self.image)
        self.pdf_save_path = None

        # Menu Bar

        # mainmenu = Menu(self)
        # file_menu = Menu(mainmenu,tearoff=False)
        # file_menu.add_command(label = '')

        # Entry Widget
        self.entry_1 = ttk.Entry(self, width=65)
        self.entry_1.place(x=1, y=20)

        # Btn
        self.btn_1 = ttk.Button(self, width=15, text='SELECT PDF', command=self.select_pdf_fun)
        self.btn_1.place(x=400, y=18)

        # Password Entry
        self.entry_2 = ttk.Entry(self, width=40, show='#')
        self.entry_2.place(x=1, y=50)

        self.label_1 = ttk.Label(self, text='Enter the password you wanna keep')
        self.label_1.place(x=250, y=50)

        # encrypt Button
        self.btn_2 = ttk.Button(self, text='START--ENCRYPTION', command=self.threading_main)
        self.btn_2.place(x=200, y=170)

        # label_new file loaction
        self.label_2 = ttk.Label(self, text='Name for the Encrypted file', )
        self.label_2.place(x=250, y=80)

        self.entry_4 = ttk.Entry(self, width=40)
        self.entry_4.place(x=1, y=80)

        # progress bar
        self.myprogress = ttk.Progressbar(self, orient=HORIZONTAL, length=300, mode='determinate')
        self.myprogress.place(x=100, y=120)

        # self.test_btn = ttk.Button(self,text='TEST Progress',command = self.step)
        # self.test_btn.place(x=150,y=150)

    def select_pdf_fun(self):
        self.pdf_path = fd.askopenfilename()
        self.entry_1.insert(0, self.pdf_path)
        print(self.pdf_path)

    def browse(self):
        self.pdf_save_path = fd.asksaveasfile(mode='w', filetypes=(('All Files', '*.*'), ('PDF files', '*.py')),
                                              defaultextension=".pdf")

        # self.entry_4.insert(0, self.pdf_save_path)
        # print(self.pdf_save_path)

    def start_encryption_fun(self):
        a = self.pdf_path
        b = self.entry_2.get()
        c = self.entry_4.get()
        logic = encryptor_logic.Logic(a)
        logic.encrypt_pdf(b, c)

    def threading_main(self):
        self.threading_1()
        self.threading_2()

    def threading_1(self):
        self.t1 = threading.Thread(target=self.start_encryption_fun, daemon=True)
        self.t1.start()

    def threading_2(self):
        self.t2 = threading.Thread(target=self.step, daemon=True)
        self.t2.start()

    def step(self):
        while self.myprogress['value'] < 100:
            self.myprogress['value'] = self.myprogress['value'] + 1
            time.sleep(0.2)
            self.changing_label = ttk.Label(self, text=f'Encrypition {self.myprogress["value"]} % completed', )
            self.changing_label.place(x=170, y=150)

        self.btn_3 = ttk.Button(self, text='OPEN ENCRYPTED PDF', command=self.open_1)
        self.btn_3.place(x=1, y=190)
        # for i in range(5):
        #     self.myprogress['value'] +=20
        #     # self.update_idletasks()
        #     time.sleep(0.5)

    def open_1(self):
        name = self.entry_4.get()
        my_program = fd.askopenfilename(filetypes=((('PDF FIles',"*.pdf"),("All files","*.*"))))
        os.system("%s"%my_program)


if __name__ == '__main__':
    mainwin = GUI()
    mainwin.mainloop()
