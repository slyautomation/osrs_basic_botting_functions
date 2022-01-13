# osrs_basic_botting_functions

Full tutorial on creating Basic Functions for automation using Python for osrs botting. 
The example used will be woodcutting, where the script will use colour detection using opencv and use pyautogui to move the mouse, click and use the keyboard to drop items using an image recognition module that will detect the wood icons in the inventory.

Other python files will also use tesseract-OCR to detect text within images using tesseract-OCR image to text recognition functions.

## core.py and function.py
For the full video tutorial click link: https://www.youtube.com/watch?v=C7ZY4KYpFII

## Woodcutting

### features

Cuts woods and makes fire
- Use object marker plugin to highlight trees yellow.
- Make sure to have an axe equipped and a tinderbox if firemaking.
Tutorial on firemaking code click link: https://youtu.be/bHZCQUChG_k
## Quick module install Steps

in terminal type: 

pip install pytesseract==0.3.3

pip install opencv-python

pip install pyautogui

pip install pypiwin32

### Super Quick Setup and install in pycharm:



in terminal type:

pip install -r requirements


tesseract-ocr = https://sourceforge.net/projects/tesseract-ocr-alt/files/tesseract-ocr-setup-3.02.02.exe/download


Tutorial on installing tesseract-OCR: https://youtube.com/watch?v=X3snnwzJfEw&t=25m15s

## Runelite Setup
Tutorial on runelite setup click link: https://youtube.com/watch?v=JO2FvkJwppA
## fishing.py
- Turn on fishing plugin.
- Make sure to have net for prawn fishing or a rod and bait/feathers for fish.
Tutorial on fishing code click link: https://youtube.com/watch?v=5K-nMy9Pdvg


## mining.py
- Turn on mining plugin.
- Mark ore spots using the object marker to green. 
- Make sure to equip a pick axe.
Tutorial on mining code click link: https://youtube.com/watch?v=dkD5gXcgQYI


## combat.py
Tutorial on combat code click link: https://youtube.com/watch?v=llGbhVfU1Bc

## smithing.py

Tutorial on smithing code click link: https://youtube.com/watch?v=YezEeVjoP6o

## magic.py

### features

High alching

Superheat item

Tutorial on magic code click link: https://youtube.com/watch?v=Vyhy2CpfK7I

## osrs_walker.py

Tutorial: TBA

### Setup
- Create txt file on desktop paths.txt, the modified plugin shortest_path-5.0.0.jar saves the coordinates when a path target is made in osrs. 
- ![image](https://user-images.githubusercontent.com/81003470/140734894-c097bde1-4448-4e2c-898b-a6fc4238ca98.png)
- ![image](https://user-images.githubusercontent.com/81003470/140739938-3f9d4826-8d07-4ddc-bf17-19407ff7beab.png)

- Add 'shortestpath-5.0.0.jar' plugin to plugins folder in OpenOSRS or RuneLite.
- ![image](https://user-images.githubusercontent.com/81003470/140739552-1633d5db-5d0f-4348-8e71-bb0fa2ec0574.png)

- Use main map and right click then select 'set target', run server.py and then run osrs_walker.py.
- ![ezgif com-gif-maker (1)](https://user-images.githubusercontent.com/81003470/140738915-4ba2106a-ec4f-4a89-97e9-46eacca6f792.gif)



## Wiki
[Wiki page on function descriptions and purpose](https://github.com/slyautomation/osrs_basic_botting_functions/wiki/Purpose-and-Definition-of-Functions-including-argument-s-usage)

Consider donating if you found the project fun and learnt more about python.

![image](https://user-images.githubusercontent.com/81003470/112718441-215b1780-8f47-11eb-81a6-4952b9cb5ef4.png)
