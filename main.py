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

def save_as():
  if file_path == '':
    path = asksaveasfilename(filetypes=[('Python Files', '*.py')])
  else:
    path = file_path
  with open(path, 'w') as file:
    code = editor.get('1.0', END)
    file.write(code)
    set_file_path(path)

def open_file():
  path = askopenfilename(filetypes=[('Python Files', '*.py')])
  with open(path, 'r') as file:
    code = file.read()
    editor.delete('1.0', END)
    editor.insert('1.0', code)
    set_file_path(path)

menu_bar = Menu(compiler)
