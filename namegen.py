import json
import random
def load_array(path):
    f = open(path, encoding="utf8")
    data = json.loads(f.read())
    return data
italianNames = load_array("names.json")
def randomName(number):
    if number is None:
        return random.choice(italianNames)[:5]
    else:
        return [random.choice(italianNames)[:5] for i in range(number)]
