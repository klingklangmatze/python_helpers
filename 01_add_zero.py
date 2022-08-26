import os
from tkinter import Tk, filedialog

root = Tk() # Pointing root to Tk() to use it as Tk() in program.
root.withdraw() # Hides small tkinter window.
root.attributes('-topmost', True) # Opened windows will be active. above all windows despite of selection.
open_file = filedialog.askdirectory() # Returns opened path as str
file_extension = ".opd" # Extension of the files to be changed

count = 0
for i in range(1, 10): #Basically the program changes all files from 1.x to 01.x, 2.x to 02.x ,..., 9.x to 09.x
    while os.path.exists(open_file + "/" + str(i).zfill(0) + file_extension) == True:
        os.rename(open_file + "/" + str(i).zfill(0) + file_extension, open_file + "/" + str(i).zfill(2) + file_extension)
        count += 1
    else:
        pass

print("\n----------------")
print("Renamed " + str(count) + " files.")
print("----------------")
