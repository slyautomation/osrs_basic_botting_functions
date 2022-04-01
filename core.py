import win32gui
import yaml
import platform
global hwnd
hwnd = 0

with open("pybot-config.yaml", "r") as yamlfile:
    data = yaml.load(yamlfile, Loader=yaml.FullLoader)
    
def findWindow_Linux(data):
    import subprocess
    subprocess.call(["xdotool", "search", "--name", data, "windowfocus", "%2"])
    subprocess.call(["xdotool", "getwindowfocus", "windowmove", "0", "0"])
    subprocess.call(["xdotool", "getwindowfocus", "windowsize", "860", "830"])

    
def getWindow_Linux(data):
    import subprocess
    subprocess.call(["xdotool", "search", "--name", data, "windowfocus", "%2"])
    rect = subprocess.call(["xdotool", "getwindowfocus", "getwindowgeometry"])
    # Take care of borders for finding character
    x = rect[0]
    # 30 is the amount of pixels in the client top border
    y = rect[1] + 30
    # 50 is the amount of pixels in the client side border
    w = rect[2] - x - 50
    h = rect[3] - y - 30
    # Find center
    print('window width:', w, 'window height:', h)
    return x, y, w, h
    
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
    
def getWindow(data):  # find window name returns PID of the window
    global hwnd
    hwnd = win32gui.FindWindow(None, data)
    # hwnd = win32gui.GetForegroundWindow()860
    print('findWindow:', hwnd)
    win32gui.SetActiveWindow(hwnd)
    win32gui.SetForegroundWindow(hwnd)
    rect = win32gui.GetWindowRect(hwnd)
    # Take care of borders for finding character
    x = rect[0]
    # 30 is the amount of pixels in the client top border
    y = rect[1] + 30
    # 50 is the amount of pixels in the client side border
    w = rect[2] - x - 50
    h = rect[3] - y - 30
    # Find center
    print('window width:', w, 'window height:', h)
    return x, y, w, h

print('Operating system:', platform.system())
if platform.system() == 'Linux':
    findWindow_Linux(data[0]['Config']['client_title'])
else:
    findWindow(data[0]['Config']['client_title'])
