import win32gui
global hwnd
hwnd = 0

def legacy_findWindow_runelite(Name):  # find window name returns PID of the window
    global hwnd
    hwnd = win32gui.FindWindow(None, "RuneLite - " + Name)
    #hwnd = win32gui.GetForegroundWindow()
    print('findWindow:', hwnd)
    win32gui.SetActiveWindow(hwnd)
    #win32gui.ShowWindow(hwnd)
    win32gui.MoveWindow(hwnd, 0, 0, 865, 830, True)

def findWindow_runelite():  # find window name returns PID of the window
    global hwnd
    hwnd = win32gui.FindWindow(None, "RuneLite") # follow the setup guide to remove the username in the title using the runelite settings
    #hwnd = win32gui.GetForegroundWindow() # link is: https://youtu.be/JO2FvkJwppA
    print('findWindow:', hwnd)
    win32gui.SetActiveWindow(hwnd)
    #win32gui.ShowWindow(hwnd)
    win32gui.MoveWindow(hwnd, 0, 0, 865, 830, True)

findWindow_runelite()
