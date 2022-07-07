# Old School Botting Functions

Full tutorial on creating Functions for automation using Python for osrs botting. 
The example used will be woodcutting, where the script will use colour detection using opencv and use pyautogui to move the mouse, click and use the keyboard to drop items using an image recognition module that will detect the wood icons in the inventory.

Other python files will also use tesseract-OCR to detect text within images using tesseract-OCR image to text recognition functions.

## Setup

installing pycharm
<a href="https://www.jetbrains.com/pycharm/download/#section=windows">pycharm</a> 

<a href="https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=windows&code=PCC">pycharm windows</a>

<a href="https://github.com/slyautomation/osrs_basic_botting_functions/wiki/How-to-Install-Pycharm"> How to Install Pycharm</a>

<a href="https://github.com/slyautomation/osrs_basic_botting_functions/wiki/How-to-add-Project-with-Pycharm"> How to add Project with Pycharm</a>

<a href="https://github.com/slyautomation/osrs_basic_botting_functions/wiki/how-to-ensure-venv-%28virtual-environment%29-is-active"> Editing how to ensure venv (virtual environment) is active</a>

## core.py and function.py
For the full video tutorial click link: https://www.youtube.com/watch?v=C7ZY4KYpFII

This video is more about how it was created at the start core.py is how to make the python script focus on the old school runescape application and adjust the window size so all the scripts run as intended. Then functions.py is where all the different kinds of shortcut functions are placed to reference the mini map, or a piece of code to do color detection or open the inventory.

## Quick module install Steps

in terminal type:

pip install -r requirements.txt

tesseract-ocr = https://sourceforge.net/projects/tesseract-ocr-alt/files/tesseract-ocr-setup-3.02.02.exe/download

Tutorial on installing tesseract-OCR: https://youtube.com/watch?v=X3snnwzJfEw&t=25m15s

## Runelite Setup
Tutorial on runelite setup click link: https://youtube.com/watch?v=JO2FvkJwppA

### pybot-config.yaml (configuration file)

![image](https://user-images.githubusercontent.com/81003470/177748290-e8337717-0f06-4aeb-afc9-19056bbebc23.png)

client_title: Is the title of the application window usually Runelite if you have completed the steps for the Runelite Setup, if not then enter RuneLite - username or OpenOSRS

![image](https://user-images.githubusercontent.com/81003470/177749000-e7b09b9d-26fc-43ab-95cd-2a84ad12fcc3.png)

![image](https://user-images.githubusercontent.com/81003470/177749289-c6b11dfe-1fe0-4d5d-a67f-bf53d62839ce.png)

enable_on_start: if you don't want the config window to pop up each time, enter as false

file_path_to_client: the head folder where the OSRS client is stored usually .runelite or .openosrs

pc_profile: is the user profile of the pc so it can find runelite or openosrs

![image](https://user-images.githubusercontent.com/81003470/177750475-75e97359-907d-4c2a-b36d-0ada31594fd8.png)

tesseract_path: Is the folder address to tesseract-ocr program

![image](https://user-images.githubusercontent.com/81003470/177748476-6b190ed9-d1b2-4677-96c5-2b47859f2ee6.png)

```diff
- Note: copy the format below make sure to include the slashes (\).
```
![image](https://user-images.githubusercontent.com/81003470/177748290-e8337717-0f06-4aeb-afc9-19056bbebc23.png)

## Woodcutting

### features

Cuts woods and makes fire
- Use object marker plugin to highlight trees red, green or yellow.
- Make sure to have an axe equipped and a tinderbox if firemaking.

- Turn on woodcutting plugin
- Turn off Show weight in item stats
Tutorial on firemaking code click link: https://youtu.be/bHZCQUChG_k

![image](https://user-images.githubusercontent.com/81003470/172408565-e7bb7126-ede9-41ff-a143-b9257cee6344.png)

- Pick a object marker color, a wood type and how long in hours to run for

![image](https://user-images.githubusercontent.com/81003470/172408690-510ff90b-0197-4959-a7a8-201e1620b79b.png)

## fishing.py
- Turn on fishing plugin.
- Make sure to have net for prawn fishing or a rod and bait/feathers for fish.
Tutorial on fishing code click link: https://youtube.com/watch?v=5K-nMy9Pdvg


## mining.py
- Turn on mining plugin.
- Mark ore spots using the object marker to green. 
- Make sure to equip a pick axe.

- enter the ore type, the marker color and how long to run in hours (Change Run_Duration_hours) 
![image](https://user-images.githubusercontent.com/81003470/172346408-c72b05cf-6e23-4846-b5db-e189c6501e60.png)

![image](https://user-images.githubusercontent.com/81003470/172290853-3d98d94c-38c4-41b9-8971-da017776956a.png)

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

- Located in jar_files: Add httpplug-1.0.3.jar to C:\Users\  <username> \.openosrs \plugins
- Located in jar_files: Add shortestagility-5.0.2.jar to C:\Users\ <username> \.openosrs \plugins
  
  ![image](https://user-images.githubusercontent.com/81003470/155945546-695d28b8-5cbd-461a-9342-44d38e6c6b37.png)

### Setup
- Create txt file on desktop paths.txt, the modified plugin shortestagility-5.0.2.jar saves the coordinates when a path target is made in osrs. 
- ![image](https://user-images.githubusercontent.com/81003470/140734894-c097bde1-4448-4e2c-898b-a6fc4238ca98.png)
- ![image](https://user-images.githubusercontent.com/81003470/140739938-3f9d4826-8d07-4ddc-bf17-19407ff7beab.png)
- ![image](https://user-images.githubusercontent.com/81003470/140739552-1633d5db-5d0f-4348-8e71-bb0fa2ec0574.png)

- Use main map and right click then select 'set target', run server.py and then run osrs_walker.py.
- ![ezgif com-gif-maker (1)](https://user-images.githubusercontent.com/81003470/140738915-4ba2106a-ec4f-4a89-97e9-46eacca6f792.gif)



## Wiki
[Wiki page on function descriptions and purpose](https://github.com/slyautomation/osrs_basic_botting_functions/wiki/Purpose-and-Definition-of-Functions-including-argument-s-usage)

Consider donating if you found the project fun and learnt more about python.

![image](https://user-images.githubusercontent.com/81003470/112718441-215b1780-8f47-11eb-81a6-4952b9cb5ef4.png)
