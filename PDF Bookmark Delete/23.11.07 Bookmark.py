import fitz
import re
import sys
import time
from plyer import notification
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
        toc_new = [a for a in toc if a[0]==1 or (a[0] <= 3 and re.search(r'^((\d+)(\.)){1,2}\d+([^\.\d]|$)',a[1]))]
        doc.set_toc(toc_new)
        doc.saveIncr()

        while True:
            time.sleep(1)
            notification.notify(
                title = "Finished executing "+sys.argv[0],
                message = "Successful",
            )
            #print('Successful')
            #time.sleep(1)
            break

    except Exception as e:
        while True:
            time.sleep(1)
            notification.notify(
                title = "Error in executing "+sys.argv[0],
                message = str(e),
            )
            #print(e)
            #time.sleep(1)
            break
        
