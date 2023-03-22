import sys
import os
import re
try:
    # The insertion index should be 1 because index 0 is this file
    sys.path.insert(1, '{}/help'.format(
        os.getcwd()))  # the type of path is string
    # because the system path already have the absolute path to folder a
    # so it can recognize file_a.py while searching
    from help.banner import colors
    from help.json_me import json_me
    from help.req import request

except (ModuleNotFoundError, ImportError) as e:
    print("{} fileure".format(type(e)))
else:
    print("Import succeeded")


def is_wordpress(target) -> bool:
    """To determine if the site Runing Wordpress or not"""
    if not (target.startswith('https://') or target.startswith('http://')):

        target = 'http://' + target
    req = request(target)
    r = req.get(target, headers={"User-agent": "Firefox and whatever 1.1...."})
    if r.status_code == 200:
        try:
            pattern = re.compile(
                r"<meta name\=\"generator\" content\=\"(WordPress \d+\.\d+\.?(\d+)?)\" \/>"
            )
            if pattern.search(r.text):
                return True
            else:
                return False
        except Exception as e:
            pass
