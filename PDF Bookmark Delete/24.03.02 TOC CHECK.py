import fitz
import re
import tkinter as tk
from tkinter import filedialog, scrolledtext

root = tk.Tk()
root.title('Bookmark List')
root.update_idletasks()

file_path = filedialog.askopenfilename()
print(file_path)  # input document filename

doc = fitz.open(file_path)
toc = doc.get_toc(simple=True)
if "/GOM" in file_path:
    toc_new = [a for a in toc if a[0]==1 or re.search(r'^((\d+)(\.)){1,2}\d*([^\.\d]| $)',a[1]) or re.search(r'^APPENDI|^GRH F|^BAV F',str(a[1]).upper())]
else:
    toc_new = [a for a in toc if a[0]==1 or re.search(r'^((\d+)(\.)){1,2}\d+([^\.\d]| $)',a[1])]

text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width = 200, height = 50)
text_area.grid(column = 0, pady = 10, padx = 10)

# Placing cursor in the text area
text_area.insert(tk.INSERT,list(enumerate([(a + ["\n"]) for a in toc_new])))
text_area.focus()

root.mainloop()