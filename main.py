import lzma
import tkinter as tk
from tkinter import filedialog

def compress_file():
    # prompt the user to select a file
    input_file = filedialog.askopenfilename()

    # specify the output file path
    output_file = input_file + '.lzma'

    # open the input file in read mode
    with open(input_file, 'rb') as f:
        # read the contents of the input file
        data = f.read()

        # compress the data using the LZMA algorithm
        compressed_data = lzma.compress(data)

        # open the output file in write mode
        with open(output_file, 'wb') as f:
            # write the compressed data to the output file
            f.write(compressed_data)

# create the main window
root = tk.Tk()

# create a button to compress a file
compress_button = tk.Button(root, text='Compress File', command=compress_file)
compress_button.pack()

# run the main loop
root.mainloop()