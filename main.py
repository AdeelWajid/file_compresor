import lzma
import tkinter as tk
from tkinter import filedialog

def compress_file():
    # prompt the user to select a file
    input_file = filedialog.askopenfilename()

    # specify the output file path
    output_file = input_file + '.lzma'

    # update the progress label
    progress_label.config(text='Compressing...')

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

    # update the progress label
    progress_label.config(text='Done!')

def decompress_file():
    # prompt the user to select a file
    input_file = filedialog.askopenfilename()

    # specify the output file path
    output_file = input_file + '.decompressed'

    # update the progress label
    progress_label.config(text='Decompressing...')

    # open the input file in read mode
    with open(input_file, 'rb') as f:
        # read the contents of the input file
        data = f.read()

        # decompress the data using the LZMA algorithm
        decompressed_data = lzma.decompress(data)

        # open the output file in write mode
        with open(output_file, 'wb') as f:
            # write the decompressed data to the output file
            f.write(decompressed_data)

    # update the progress label
    progress_label.config(text='Done!')

# create the main window and set its size to 400x200 pixels
root = tk.Tk()
root.geometry('400x200')

# create a button to compress a file
compress_button = tk.Button(root, text='Compress File', command=compress_file)
compress_button.pack()

# create a button to decompress a file
decompress_button = tk.Button(root, text='Decompress File', command=decompress_file)
decompress_button.pack()

# create a label to display the progress
progress_label = tk.Label(root, text='')
progress_label.pack()

# run the main loop
root.mainloop()
