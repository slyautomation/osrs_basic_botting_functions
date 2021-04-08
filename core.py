import win32gui
global hwnd
hwnd = 0

def findWindow_runelite(Name):  # find window name returns PID of the window
    global hwnd
    hwnd = win32gui.FindWindow(None, "RuneLite - " + Name)
    #hwnd = win32gui.GetForegroundWindow()
    print('findWindow:', hwnd)
    win32gui.SetActiveWindow(hwnd)
    #win32gui.ShowWindow(hwnd)
    win32gui.MoveWindow(hwnd, 0, 0, 865, 830, True)

findWindow_runelite('user name')
