import win32gui
import yaml

global hwnd
hwnd = 0

with open("pybot-config.yaml", "r") as yamlfile:
    data = yaml.load(yamlfile, Loader=yaml.FullLoader)

def findWindow_runelite():  # find window name returns PID of the window
    global hwnd
    hwnd = win32gui.FindWindow(None, "RuneLite")
    # hwnd = win32gui.GetForegroundWindow()860
    print('findWindow:', hwnd)
    win32gui.SetActiveWindow(hwnd)
    # win32gui.ShowWindow(hwnd)
    win32gui.MoveWindow(hwnd, 0, 0, 865, 830, True)

def findWindow_openosrs():  # find window name returns PID of the window
    global hwnd
    hwnd = win32gui.FindWindow(None, "OpenOSRS")
    # hwnd = win32gui.GetForegroundWindow()860
    print('findWindow:', hwnd)
    win32gui.SetActiveWindow(hwnd)
    # win32gui.ShowWindow(hwnd)
    win32gui.MoveWindow(hwnd, 0, 0, 865, 830, True)

def findWindow(data):  # find window name returns PID of the window
    global hwnd
    hwnd = win32gui.FindWindow(None, data)
    # hwnd = win32gui.GetForegroundWindow()860
    print('findWindow:', hwnd)
    win32gui.SetActiveWindow(hwnd)
    # win32gui.ShowWindow(hwnd)
    win32gui.MoveWindow(hwnd, 0, 0, 865, 830, True)

findWindow(data[0]['Config']['client_title'])
