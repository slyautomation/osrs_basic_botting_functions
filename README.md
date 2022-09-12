# Old School Botting Functions

Full tutorial on creating Functions for automation using Python for osrs botting. 
The example used will be woodcutting, where the script will use colour detection using opencv and use pyautogui to move the mouse, click and use the keyboard to drop items using an image recognition module that will detect the wood icons in the inventory.

Other python files will also use tesseract-OCR to detect text within images using tesseract-OCR image to text recognition functions.

## Setup

```diff
Note: PC Monitor settings - change resolution to 1920x1080 panel and text of apps was set to 100%.
```
Right click and select Display Settings

![image](https://user-images.githubusercontent.com/81003470/180430422-181e478b-43ed-4d1e-89ba-93c942af7313.png)

In the Scale And Layout section - Change size of text to 100% and Set Display Resolution to 1920 x 1080 for best results.

![image](https://user-images.githubusercontent.com/81003470/180430706-dba89331-09b0-4626-9d42-1a07a0885c41.png)


### Installing Pycharm
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

In Runescape setting,  set the following:

- Ideally under display, enable hide roofs, camera zoom, screen brightness matching below.

![image](https://user-images.githubusercontent.com/81003470/188833251-0e285e58-541c-4ba2-bf33-065581e9d38e.png)

- Under controls, enable shift click to drop items, and set inventory shortcut to ESC keystroke.

![image](https://user-images.githubusercontent.com/81003470/188833473-7de48c91-dd03-44fd-a7a6-081e18ca0fa5.png)

- Under Interfaces ensure Game Client layout is Resizable - Modern Layout
- Show data orbs enabled

![image](https://user-images.githubusercontent.com/81003470/188834061-becf3678-9ec3-4115-845a-b11102b3b384.png)

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

![image](https://user-images.githubusercontent.com/81003470/177980804-669ebd1d-0f9c-4102-8b86-efef42a7d1de.png)

- Make sure to equip a pick axe.

- enter the ore type, the marker color and how long to run in hours (Change Run_Duration_hours) 
![image](https://user-images.githubusercontent.com/81003470/172346408-c72b05cf-6e23-4846-b5db-e189c6501e60.png)

![image](https://user-images.githubusercontent.com/81003470/172290853-3d98d94c-38c4-41b9-8971-da017776956a.png)

Tutorial on mining code click link: https://youtube.com/watch?v=dkD5gXcgQYI


## combat.py
- Turn on NPC Indicators plugin and Opponent Information plugin
- Change Highlight colour to #ff00ffff

![image](https://user-images.githubusercontent.com/81003470/177981614-830a435a-81f5-4d95-bd07-10cca3008a04.png)

- Hold Shift and Right Click on NPC/Mob and select Tag-All

![image](https://user-images.githubusercontent.com/81003470/177981922-1f356fe0-7aa9-4ac9-9b61-7180025b115e.png)

- In the Combat script change the first value to the NPC/Mob name
- Change Run_duraction_hours to the number of hours to run script for

![image](https://user-images.githubusercontent.com/81003470/177982195-47de25fa-f300-4362-bea7-0aa1b2cff258.png)

- To add or use a NPC/Mob not on the list add it to the monster_array as ['each iteration captured by the combat_text'] and add to monster_list the name

![image](https://user-images.githubusercontent.com/81003470/177983040-28802f6f-bb57-4120-837b-830464215ee5.png)

Tutorial on combat code click link: https://youtube.com/watch?v=llGbhVfU1Bc

## thieving.py

### steal_man() Works with Knights, Goblins and Thieves etc.

- Turn on NPC Indicators plugin
- Change Highlight colour to #ff00ffff
- Hold Shift and Right Click on NPC/Mob and select Tag <Man><Knigt> etc.

![image](https://user-images.githubusercontent.com/81003470/179393733-d8a16835-c051-4399-9614-528f8748afde.png)
 
- Make sure pickpocket will be actioned on left click (some npcs even on always right click have 'talk to' as left click option)
  
![image](https://user-images.githubusercontent.com/81003470/179394074-85e3e1b1-e942-437b-8d01-0d024a5817ee.png)
 
- To stop script hold down the capslock key
 
### Improvements to add
 - Stop or eat when health is low (warning this does not stop when health is low)

### steal_tea() 
 
 - Hold shift and mark object Tea Stall (Make sure the color is red)
 
 ![image](https://user-images.githubusercontent.com/81003470/179394490-dede3956-f7c5-48b4-9d1d-fc501d25d9a3.png)
 
 ![image](https://user-images.githubusercontent.com/81003470/179394511-cad0e25a-a314-45f4-a957-44952eee55ba.png)

## Clay Money Maker
This only works at the Rimmington mine and banks at Port Sarim deposit box.
- Turn on mining plugin.
- Make sure to equip a pick axe.
- The Start location when running the clay_beginner_money_maker.py is at the Rimmington Mine start next to the clay deposits
 
![image](https://user-images.githubusercontent.com/81003470/188813727-27fb9e27-ad1b-421c-8c0e-7c6c9f87be6e.png)
```diff
- IMPORTANT! Set compass directly north, click the on the compass to reset straight. 
 Otherwise the walker from deposit box to rimmington mine won't work.
```
![image](https://user-images.githubusercontent.com/81003470/188813195-22c0aabc-b7d8-4d08-87db-4045b33486d3.png)

- Mark clay spots next to the east fence line using the object marker to green (optional are red or amber). 
 
![image](https://user-images.githubusercontent.com/81003470/177980804-669ebd1d-0f9c-4102-8b86-efef42a7d1de.png)

![image](https://user-images.githubusercontent.com/81003470/188812536-c27bec72-e463-43e2-82af-322004526e28.png)

- Mark the deposit box at Port Sarim using the object marker to red.

![image](https://user-images.githubusercontent.com/81003470/188812816-541fd87c-e1b0-4fd9-8509-b3b83df67ef3.png)

This is the path that is takes:

![image](https://user-images.githubusercontent.com/81003470/188812094-800e6793-2827-449b-a090-5bb6d14ebec4.png)
 
Make sure to select the color that you highlighted the clay ores and set the Run Duration to the number of hours:
 
![image](https://user-images.githubusercontent.com/81003470/188814212-8131f6fb-b0f4-4a04-af18-0e740462d39d.png)


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

## Troubleshooting 

python venv/Scripts/pywin32_postinstall.py -install

## Wiki
[Wiki page on function descriptions and purpose](https://github.com/slyautomation/osrs_basic_botting_functions/wiki/Purpose-and-Definition-of-Functions-including-argument-s-usage)

Consider donating if you found the project fun and learnt more about python.

https://www.buymeacoffee.com/slyautomatG
