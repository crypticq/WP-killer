import json
import random
import os
from pathlib import Path




cwd = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

pa = (cwd + "/Exploits/")





def generate_random_name():
    return f"{random.randint(1,1000)}.json"


def json_me(target,exploit, data):
    try:
        if not os.path.exists(pa):
            os.makedirs(pa)
        
        na = exploit + "_" + target.split('/')[-1] + "_"  + generate_random_name()
        with open(pa + na, "w") as WRITE:
            json.dump(data, WRITE, indent=4)
    except Exception as e:
        pass

