import json


def get_live_info():
    '''Returns specific live information from the game client via the Status Socket plugin.'''
    try:
        f = open('live_data.json', )
        data = json.load(f)
        return data
    except:
        pass

def update_inventory():
    """Updates the current inventory."""
    inventory = None
    data = get_live_info()
    if data != None:
        inventory = data['inventory']
    return inventory

def update_positon():
    """Updates the current position of the player."""
    position = None
    data = get_live_info()
    if data != None:
        position = [data['worldPoint']['x'], data['worldPoint']['y']]
    return position
def update_run_energy():
    """Updates the current run energy."""
    run_energy = None
    data = get_live_info()
    if data != None:
        run_energy = data['runEnergy']
    return run_energy

def update_camera_angle():
    """Updates current camera angle."""
    camera_angle = None
    data = get_live_info()
    if data != None:
        camera_angle = data['camera']['yaw']
    return camera_angle