import csv
import os

import requests
import json
import pandas as pd
import webbrowser
import numpy as np
from datetime import datetime
import ctypes  # An included library with Python install.
from win10toast import ToastNotifier

print(os.path.dirname('csv'))
def resourcePath(relativePath):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        basePath = sys._MEIPASS
    except Exception:
        basePath = os.path.abspath(".")

    return os.path.join(basePath, relativePath)

def ensure_dir():
    directory = os.path.dirname('csv')
    print(directory)
    if not os.path.exists('csv'):
        os.makedirs('csv')

ensure_dir()

directory = os.path.dirname('csv')

toaster = ToastNotifier()
toaster.show_toast("Python Script Uploading Data", "Retrieving data from prices.runescape.wiki and saving as csv", icon_path=resourcePath("app_icon_sly.ico"), duration=5)


# datetime object containing current date and time
from pandas.io.json import json_normalize

now = datetime.now()

print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)

new = 2  # open in a new tab, if possible

# python-requests
# prices.runescape.wiki/api/v1/osrs/1h


# Show all columns
pd.set_option('display.max_columns', None)
# Show all lines
pd.set_option('display.max_rows', None)
# value display length is 100, the default is 50
pd.set_option('max_colwidth', 200)



def call_http_prices():
    headers = {
        'User-Agent': 'Flipping Price',
        'From': 'email@gmail.com'  # This is another valid field
    }
    response = requests.get("https://prices.runescape.wiki/api/v1/osrs/1h", headers=headers)
    stats = json.loads(response.text)
    print(stats)
    return stats

# average over 12 hour window get data each hour over a week

jsonData = call_http_prices()

data = pd.DataFrame(jsonData)
data['item_id'] = data.index
data['index_id'] = np.arange(len(data))
#print(data)


test = data['data']
test_pd = pd.DataFrame(json_normalize(test))
test_pd['avgHighPrice'] = test_pd['avgHighPrice'].apply('{:.0f}'.format)
test_pd['avgLowPrice'] = test_pd['avgLowPrice'].apply('{:.0f}'.format)
#temp_data = pd.DataFrame(json_normalize(test))
temp_data = pd.json_normalize(test)
temp_data['index_id'] = np.arange(len(temp_data))
data = pd.merge(data, temp_data, left_on='index_id', right_on='index_id', how='left').drop(['index_id','data'], axis=1)

timeframe = data.iloc[0]['timestamp']
datetime_time = datetime.fromtimestamp(timeframe).strftime('%d-%b-%Y-%H%M')

#print(datetime_time)
#print(data)

format_data = pd.DataFrame(data)

data = format_data.drop(columns='timestamp').fillna(0)

#finalData = toptenvalue(dataFile)

#data = pd.DataFrame(finalData)

#addmargins()
#addtestdate()
data.to_csv(os.path.dirname('csv') + 'csv\\raw_data-' + datetime_time + '.csv', index=False)
print(os.path.dirname('csv') + 'csv\\raw_data-' + datetime_time + '.csv')
html = data.to_html()
text_file = open("index.html", "w")
text_file.write(html)
text_file.close()

url = "index.html"
webbrowser.open(url, new=new)

