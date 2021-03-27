from core import findWindow_runelite
from functions import Image_count # 'ashes_icon.png'
from functions import image_Rec_clicker # r'copper_ore.png', 'item', 0.9, 'left'
from functions import pick_item # 1935-1280,498
from functions import find_Object # 0 red ,1 green ,2 amber
from functions import random_break # 0.5,5
from functions import Image_color # 0.5,5
from functions import release_drop_item
from functions import drop_item
def get_wood():
    j = 0
    while j < 10:
        invent = Image_count('wood_icon.png')
        print(invent)
        find_Object(2)
        random_break(5,10)
        if invent > 27:
            drop_item()
            image_Rec_clicker('wood_icon.png', 'item', 5,5 ,0.9, 'left')
            release_drop_item()


#Image_color()
get_wood()