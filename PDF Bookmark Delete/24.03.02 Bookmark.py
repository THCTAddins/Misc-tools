import fitz
import re
import sys
import time
from win10toast import ToastNotifier
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()
print(file_path)  # input document filename

if __name__ == "__main__":
    try:

        doc = fitz.open(file_path)
        toc = doc.get_toc(simple=False)
        if "/GOM" in file_path:
            toc_new = [a for a in toc if a[0]==1 or re.search(r'^((\d+)(\.)){1,2}\d*([^\.\d]| $)',a[1]) or re.search(r'^APPENDI|^GRH F|^BAV F',str(a[1]).upper())]
        else:
            toc_new = [a for a in toc if a[0]==1 or re.search(r'^((\d+)(\.)){1,2}\d+([^\.\d]| $)',a[1])]
        doc.set_toc(toc_new)
        doc.saveIncr()

        while True:
            time.sleep(1)
            ToastNotifier.show_toast("Finished executing "+sys.argv[0],"Successful",icon_path='',duration=10)
            #print('Successful')
            #time.sleep(1)
            break

    except Exception as e:
        while True:
            time.sleep(1)
            ToastNotifier.show_toast("Error in executing "+sys.argv[0],str(e),icon_path='',duration=10)
            #print(e)
            #time.sleep(1)
            break