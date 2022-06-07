import json
import simplejson
import requests


def run():
    c = s.get("http://localhost:8080/events", stream=True)
    data = simplejson.loads(c.text)
    print(data)
    with open(f"live_data.json", "w+") as outfile:
        json.dump(data, outfile)
    outfile.close()

if __name__ == "__main__":
    s = requests.session()
    while True:
        run()
