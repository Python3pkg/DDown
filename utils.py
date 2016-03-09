'''
    Created by Tracy on 2016/3/9
    Mail tracyliubai@gmail.com

'''
from urllib.parse import quote
import threading
import urllib.request
import socket, os

socket.setdefaulttimeout(15.0)
'''
url_list    list type
folder      storage  path
path        absolute path like:
            win     D:/Document/test
            unix    /root/document
down_type
            0: urllib.request.urlretrieve
            1: urllib.request.urlopen
'''


class download():
    def __init__(self, url_list, folder='', path='', down_type=0):
        self.url_list = url_list
        self.down_type = down_type
        self.store_folder = ''
        self.flag = False
        if path:
            self.store_folder = path
            self.mkdir()
            if folder:
                self.store_folder += '/' + folder
                self.mkdir()
            else:
                self.flag = True
        else:
            if folder:
                self.store_folder = folder
                self.mkdir()

    def mkdir(self):
        if (os.path.exists(self.store_folder)):
            print('Folder exists')
        else:
            os.makedirs(self.store_folder)
            print('Mkdir folder')

    def start(self):
        fun = self.url_retrieve
        if self.down_type == 1:
            fun = self.url_open
        threads_task = []
        for file in self.url_list:
            t = threading.Thread(target=fun, args=[file])
            threads_task.append(t)
        for task in threads_task:
            task.start()
        for task in threads_task:
            task.join()

    def url_open(self, url):
        try:
            conn = urllib.request.urlopen(url, timeout=60)
            file_name = url.split('/')[-1]
            f = open(self.store_folder + '/' + file_name, 'wb')
            f.write(conn.read())
            f.close()
        except Exception as e:
            print(e)

    def url_retrieve(self, url):
        f = url.split('/')[-1]
        url = quote(url).replace('%3A', ':')

        if self.store_folder == '':
            self.store_folder = f.split('.')[-1]
            self.mkdir()
        if self.flag:
            self.store_folder += '/' + f.split('.')[-1]
            self.mkdir()

        file_name = self.store_folder + '/' + f
        try:
            urllib.request.urlretrieve(url, file_name)
        except Exception as e:
            print(e)
