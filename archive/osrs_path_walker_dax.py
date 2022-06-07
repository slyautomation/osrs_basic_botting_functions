
# use ctrl-f and the find ',0'and replace with ','
# remove last ',' in last row
import json
#import server
from api_dax_walker import post_http_path, API_SECRET, API_KEY
import simplejson

from api_dax_walker import post_http_path, API_KEY, API_SECRET


def get_live_info(category):
    try:
        f = open('live_data.json', )
        data = json.load(f)
        return data[category]
    except:
        pass

def get_location_points(location):
    f = open('location.json', )
    data = json.load(f)
    print(len(data['locations']))
    coords = []
    x = 0
    while x < len(data['locations']):
        if data['locations'][x]['name'] == location:
            print(data['locations'][x]['coords'])
            coords = data['locations'][x]['coords']
        x += 1
    return coords

def save_json_data(data):
    data = simplejson.loads(data)
    with open(f"paths.json", "w") as outfile:
        simplejson.dump(data, outfile)

def get_current_location():
    position_data = get_live_info('worldPoint')
    print(position_data)
    default_z = 0
    live_x, live_y = position_data['x'], position_data['y']
    return (live_x, live_y, default_z)

def list_of_paths():
    pathArray = []
    f = open('paths.json', )
    data = json.load(f)
    print(data['path'])
    for d in data['path']:
        print((d['x'], d['y'], d['z']))
        pathArray.append([d['x'], d['y']])
    return pathArray

start = get_current_location()
end = get_location_points('Lumbridge')

path = post_http_path(start, end, API_KEY, API_SECRET)

save_json_data(path)


path = list_of_paths()
print(path)

TARGET_PATH = path