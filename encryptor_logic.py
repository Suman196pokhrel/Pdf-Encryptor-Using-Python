import PyPDF2
from  tkinter import filedialog as fd
import time


# pdf_writer = PyPDF2.PdfFileWriter()
#
# pdf = PyPDF2.PdfFileReader(r'C:\Imp softwares\Pycharm\Pycharm projects\pdf_encryptor\pdf_assets\arp_assignment_1.pdf')
#
# for page_num in range(pdf.numPages):
#     pdf_writer.addPage(pdf.getPage(page_num))
#     print(page_num)
#
# password_1 = '0000'
# pdf_writer.encrypt(password_1)
#
#
# with open('test_encryption.pdf','wb') as f:
#     pdf_writer.write(f)
#     f.close()

class Logic:
    def __init__(self, file_path):
        self.file_path = file_path
        self.reader = PyPDF2.PdfFileReader(file_path)
        self.writer = PyPDF2.PdfFileWriter()

        # replicating number of pages in old pdf to new
        for page in range(self.reader.numPages):
            self.writer.addPage(self.reader.getPage(page))

    def encrypt_pdf(self, password,new_file_name):
        self.writer.encrypt(password)
        time.sleep(0.001)
        with open(new_file_name,'wb') as f:
            self.writer.write(f)



if __name__ == '__main__':
    aa = r'C:\Imp softwares\Pycharm\Pycharm projects\pdf_encryptor\pdf_assets\arp_assignment_1.pdf'
    password_1 = '0000'
    new_file_name_1 = 'logic_test.pdf'
    test = Logic(aa)
    test.encrypt_pdf(password_1,new_file_name_1)
