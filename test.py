'''
    Created by Tracy on 2016/3/9
    Mail tracyliubai@gmail.com
'''
url = ['http://7qn8b3.com1.z0.glb.clouddn.com/我的野蛮女友LostMemory엽기적인 그녀私の野蛮な彼女 原声音乐.mp3']
img = ['http://photos.tuchong.com/445896/f/9712423.jpg', 'http://photos.tuchong.com/445896/f/9712283.jpg',
       'http://photos.tuchong.com/445896/f/9712254.jpg', 'http://photos.tuchong.com/445896/f/9712219.jpg',
       'http://photos.tuchong.com/445896/f/9711352.jpg', 'http://photos.tuchong.com/445896/f/9711353.jpg',
       'http://photos.tuchong.com/445896/f/9711291.jpg', 'http://photos.tuchong.com/445896/f/9709668.jpg']
from utils import download

test = download(url_list=url, folder='mp3')
test.start()

test = download(url_list=img, folder='img',path='D:/Document/test',down_type=1)
test.start()
