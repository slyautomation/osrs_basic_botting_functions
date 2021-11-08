import random
import time

import win32gui
import pyautogui
from time import sleep
import math
import json

from osrs_return_data_status import update_run_energy
from read_path import get_current_path, get_current_path_random



class Walking():
    degreesPerYaw: float = 360 / 2048

    def __init__(
            self,
            client_top_border: int,
            client_side_border: int,
            tiles_pixels: int,
            offset_minimap_x: float,
            offset_minimap_y: float,
            offset_minimap_x_resize: float,
            offset_minimap_y_resize: float,
            offset_run_button_x: float,
            offset_run_button_y: float,
            offset_logout_x: float,
            offset_logout_y: float
    ):

        self.client_top_border = client_top_border
        self.client_side_border = client_side_border
        self.tiles_pixels = tiles_pixels
        self.offset_minimap_x = offset_minimap_x
        self.offset_minimap_y = offset_minimap_y
        self.offset_minimap_x_resize = offset_minimap_x_resize
        self.offset_minimap_y_resize = offset_minimap_y_resize
        self.offset_run_button_x = offset_run_button_x
        self.offset_run_button_y = offset_run_button_y
        self.offset_logout_x = offset_logout_x
        self.offset_logout_y = offset_logout_y
        self.run_bool = False


    def get_run_button(self, window_features: list) -> list:
        x, y, w, h = window_features
        run_x = x + (w - self.offset_run_button_x)
        run_y = y + self.offset_run_button_y
        return [run_x, run_y]

    def get_logout_cross(self, window_features: list) -> list:
        x, y, w, h = window_features
        run_x = x + (w - self.offset_logout_x)
        run_y = y + self.offset_logout_y
        return [run_x, run_y]

    def get_window(self, windowname: str) -> list:
        '''Returns the position of the window and the size of the window excluding the borders.'''
        # Get window handle.
        hwnd = win32gui.FindWindow(None, windowname)
        # Set window to foreground.
        win32gui.SetForegroundWindow(hwnd)
        # Get the window size.
        rect = win32gui.GetWindowRect(hwnd)
        # Adjust size for borders
        x = rect[0]
        y = rect[1] + self.client_top_border
        w = rect[2] - x - self.client_side_border
        h = rect[3] - y - self.client_top_border
        return [x, y, w, h]

    def find_center_minimap_resizable(self, window_features: list) -> list:
        '''Returns the center of the window, excluding the borders.'''
        x, y, w, h = window_features
        map_center_x = x + (w - self.offset_minimap_x_resize)
        map_center_y = y + self.offset_minimap_y_resize
        return [map_center_x, map_center_y]

    def find_center_window(self, window_features: list) -> list:
        '''Returns the center of the window, excluding the borders.'''
        x, y, w, h = window_features
        center_x = round(x + w / 2)
        center_y = round(y + h / 2)
        return [center_x, center_y]

    def get_live_info(self, category: str) -> dict:
        '''Returns specific live information from the game client via the Status Socket plugin.'''
        try:
            f = open('live_data.json', )
            data = json.load(f)
            return data[category]
        except:
            pass


    def get_center_minimap(self, coordinates: list) -> list:
        '''Returns the coordinates of the center of the minimap.'''
        map_center_x = coordinates[0] + self.offset_minimap_x
        map_center_y = coordinates[1] - self.offset_minimap_y
        return [map_center_x, map_center_y]

    def compute_tiles(self, live_x: int, live_y: int, new_x: int, n_y: int) -> list:
        '''Returns the range to click from the minimap center in amount of tiles.'''
        # Get live camera data.
        camera_data = self.get_live_info('camera')
        if camera_data != None:
            # Get camera angle.
            yaw = camera_data['yaw']
            # Account for anticlockwise OSRS minimap.
            degrees = 360 - self.degreesPerYaw * yaw
            # Turn degrees into pi-radians.
            theta = math.radians(degrees)
            # Turn position difference into pixels difference.
            x_reg = (new_x - live_x) * self.tiles_pixels
            y_reg = (live_y - n_y) * self.tiles_pixels
            # Formulas to compute norm of a vector in a rotated coordinate system.
            tiles_x = x_reg * math.cos(theta) + y_reg * math.sin(theta)
            tiles_y = -x_reg * math.sin(theta) + y_reg * math.cos(theta)
            return [round(tiles_x, 1), round(tiles_y, 1)]
        return [live_x, live_y]

    def change_position(self, center_mini: list, live_pos: list, new_pos: list):
        '''Clicks the minimap to change position'''
        tiles = self.compute_tiles(live_pos[0], live_pos[1], new_pos[0], new_pos[1])
        pyautogui.click(center_mini[0] + tiles[0], center_mini[1] + tiles[1])
        #self.walking_wait(new_pos[0], new_pos[1])
        self.walking_wait_forgive(new_pos[0], new_pos[1])

    def walking_wait(self, new_x: int, new_y: int):
        '''Wait until finished walking.'''
        position_data = self.get_live_info('worldPoint')
        live_x, live_y = position_data['x'], position_data['y']
        while live_x != new_x or live_y != new_y:
            print(f"hasn't reach next point...current position ({live_x},{live_y}) next target ({new_x},{live_y})" )
            position_data = self.get_live_info('worldPoint')
            if position_data == None:
                live_x, live_y = live_x, live_y
            else:
                live_x, live_y = position_data['x'], position_data['y']
            continue

    def walking_wait_forgive(self, new_x: int, new_y: int):
        '''Wait until finished walking.'''
        t_end = time.time() + random.randrange(10, 15)
        position_data = self.get_live_info('worldPoint')
        live_x, live_y = position_data['x'], position_data['y']
        while abs(new_x - live_x) > 2 or abs(new_y - live_y) > 2:
            if time.time() > t_end:
                print(time.time(),"| ", t_end)
                break
            print(f"hasn't reach next point...current position ({live_x},{live_y}) next target ({new_x},{live_y})" )
            position_data = self.get_live_info('worldPoint')
            if position_data == None:
                live_x, live_y = live_x, live_y
            else:
                live_x, live_y = position_data['x'], position_data['y']
            continue


    def turn_run_on(self) -> None:
        """Turns on run energy."""
        window = self.get_window('OpenOSRS')
        run_on = self.get_run_button(window)
        x = run_on[0] + random.randrange(-3, 3)
        y = run_on[1] + random.randrange(-3, 3)
        pyautogui.moveTo(x,y, duration = 0.2)
        pyautogui.click()


    def handle_running(self) -> None:
        """Turns on run if run energy is higher than 60."""
        # If run is off and run energy is larger than 60, turn on run.
        run_energy = update_run_energy()
        print(run_energy)
        if run_energy < 5 or run_energy == 100:
            self.run_bool = False
        if run_energy > 60 and self.run_bool == False:
            self.turn_run_on()
            self.run_bool = True

    def walk(self, path):
        '''Walks a path by clicking on the minimap'''
        window = self.get_window('OpenOSRS')
        center_minimap = self.find_center_minimap_resizable(window)
        # center_window = self.find_center_window(window)
        # center_minimap = self.get_center_minimap(center_window)
        path = path
        position_data = self.get_live_info('worldPoint')
        live_pos = [position_data['x'], position_data['y']]
        new_pos = path[0]

        # Walk while path has coordinates.
        while path:
            new_pos = path[0]
            print(f'target: ({new_pos[0]},{new_pos[1]})')

            # Turn on running if needed
            self.handle_running()

            self.change_position(center_minimap, live_pos, new_pos)
            # Wait for the map to catch up with live position.
            sleep(2)
            # Update position data.
            position_data = self.get_live_info('worldPoint')
            while position_data == None:
                sleep(0.1)
            live_pos = position_data['x'], position_data['y']
            print(f'current: ({live_pos[0]},{live_pos[1]})')
            # Remove first coordinate.
            path.pop(0)


#Paths = get_current_path()
Paths = get_current_path_random()
print(Paths)
client_top_border = 30
client_side_border = 50
tiles_pixels = 4
offset_minimap_x = 377.0
offset_minimap_y = 195.0
offset_minimap_x_resize = 72
offset_minimap_y_resize = 81
offset_run_button_x = 150
offset_run_button_y = 130
offset_logout_x = 10
offset_logout_y = 10
walker = Walking(client_top_border,
                 client_side_border,
                 tiles_pixels,
                 offset_minimap_x,
                 offset_minimap_y,
                 offset_minimap_x_resize,
                 offset_minimap_y_resize,
                 offset_run_button_x,
                 offset_run_button_y,
                 offset_logout_x,
                 offset_logout_y
)

walker.walk(Paths)
