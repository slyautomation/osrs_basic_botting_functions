import yaml

def resourcePath(relativePath):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        basePath = sys._MEIPASS
    except Exception:
        basePath = os.path.abspath(".")

    return os.path.join(basePath, relativePath)

import os

def ensure_dir():
    directory = os.path.dirname('config')
    print(directory)
    if not os.path.exists('config'):
        os.makedirs('config')

bool_config = os.path.isfile('pybot-config.yaml')

if bool_config:
    print('config already exists!')
    with open("pybot-config.yaml", "r") as yamlfile:
        data = yaml.load(yamlfile, Loader=yaml.FullLoader)
        print("Read successful")
    print(data)

    config_list = [['client title', data[0]['Config']['client_title']], ['pc_profile', data[0]['Config']['pc_profile']],
                   ['file_path_to_client', data[0]['Config']['file_path_to_client']],
                   ['tesseract_path', data[0]['Config']['tesseract_path']]]
else:
    config_list = [['client title','OpenOSRS'], ['pc_profile','C:\\Users\\i7 8700'],
               ['file_path_to_client', '\\.openosrs\\'], ['tesseract_path','C:\\Program Files (x86)\\Tesseract-OCR\\tesseract']]

ensure_dir()

import tkinter
from tkinter import *
from PIL import Image, ImageTk
test = []
root = Tk()

root.title('Sly OSRS PyBot_Config')
root.geometry('680x420')
root.configure(background='#40362C')
Font_tuple = ('Unispace', 15)
Font_tuple_entry = ('Unispace', 10)
filename = resourcePath('osrs_title_2.png')
image1 = Image.open(filename)
image1 = image1.convert('RGBA')
h = (400, 400)
image1.thumbnail(h, Image.NORMAL)
test1 = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test1, background='#40362C', anchor=CENTER, justify=CENTER)
label1.image = test1
label1.grid(column=0, columnspan=2)
x = 1
while x < len(config_list) + 1:
    lbl = Label(root, text=(config_list[(x - 1)][0]), background='#40362C', fg='yellow', padx=20)
    lbl.configure(font=Font_tuple)
    lbl.grid(column=0, row=x)
    x += 1

x = 1
while x < len(config_list) + 1:
    txt = Entry(root,width=50, background='#40362C', fg='yellow')
    txt.insert(-1, (config_list[(x - 1)][1]) )
    txt.configure(font=Font_tuple_entry)
    test.append(txt)
    txt.grid(column=1, row=x)
    x += 1

def clicked():
    c_title = test[0].get()
    p_profile = test[1].get()
    f_path = test[2].get()
    t_path = test[3].get()
    article_info = [
        {
            'Config': {
                'client_title': c_title,
                'pc_profile': p_profile,
                'file_path_to_client': f_path,
                'tesseract_path': t_path
            }
        }
    ]

    with open("pybot-config.yaml", 'w') as yamlfile:
        data = yaml.dump(article_info, yamlfile)
        print("Write successful")
    print('config file generated!!!')
    with open("pybot-config.yaml", "r") as yamlfile:
        data = yaml.load(yamlfile, Loader=yaml.FullLoader)
        print("Read successful")
    print(data)


btn = Button(root, text='Generate Config File', fg='yellow',
  command=clicked,
  background='#40362C',
  pady=0)
btn.grid(column=0, row=6, columnspan=2, pady=20)
btn.configure(font=Font_tuple)
root.mainloop()