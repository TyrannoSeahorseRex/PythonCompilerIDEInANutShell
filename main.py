from tkinter import *
from tkinter.filedialog import asksaveasfilename
from tkinter.filedialog import askopenfilename
import subprocess

compiler = Tk()
compiler.title('IDE IN A NUT-SHELL 🌰')

file_path = ''

def set_file_path(path):
  global file_path
  file_path = path

def run():
  if file_path == '':
    save_prompt = Toplevel()
    text = Label(save_prompt, text='Please save your code before attempting to run it :)')
    text.pack()
    return
  command = f'python {file_path}'
  process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
  output, error = process.communicate()
  code_output.insert(END, output)
  code_output.insert(END, error)
