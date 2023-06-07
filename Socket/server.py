import socket
import threading
import queue
import json  # json.dumps(some)打包   json.loads(some)解包
import time
import os
import os.path
import requests
import sys
from ftplib import FTP

# IP = socket.gethostbyname(socket.getfqdn(socket.gethostname()))
IP = '192.168.156.159'
PORT = 30001
apikey = 'ee19328107fb41e987a42a064a68d0da'
url = 'http://openapi.tuling123.com/openapi/api/v2'
que = queue.Queue()                             # 用于存放客户端发送的信息的队列
users = []                                      # 用于存放在线用户的信息  [conn, user, addr]
lock = threading.Lock()                         # 创建锁, 防止多个线程写入数据的顺序打乱


def call_robot(url, apikey, msg):
    data = {
        "reqType": 0,
        "perception": {
            "inputText": {  # inputText文本信息
                "text": msg
            },
            # 用户输入图片url
            "inputImage": {  # 图片信息，后跟参数信息为url地址，string类型
                "url": "https://cn.bing.com/images/"
            },
            # 用户输入音频地址信息
            "inputMedia": {  # 音频信息，后跟参数信息为url地址，string类型
                "url": "https://www.1ting.com/"
            },
            # 客户端属性信息
            "selfInfo": {  # location 为selfInfo的参数信息，
                "location": {  # 地理位置信息
                    "city": "昆明",  # 所在城市，不允许为空
                    "province": "",  # 所在省份，允许为空
                    "street": ""  # 所在街道，允许为空
                }
            },
        },
        "userInfo": {  # userInfo用户参数，不允许为空
            "apiKey": "ee19328107fb41e987a42a064a68d0da",  # 你注册的apikey,机器人标识,32位
            "userId": "Brandon"  # 随便填，用户的唯一标识，长度小于等于32位
        }
    }
    headers = {'content-type': 'application/json'}  # 必须是json
    r = requests.post(url, headers=headers, data=json.dumps(data))
    return r.json()

#####################################################################################


# 将在线用户存入online列表并返回
def onlines():
    online = []
    for i in range(len(users)):
        online.append(users[i][1])
    return online


class ChatServer(threading.Thread):
    global users, que, lock

    def __init__(self, ip,port):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        # FTP.set_pasv(0)
        # self.setDaemon(True)
        # self.ADDR = ('', port)
        # self.PORT = port
        # os.chdir(sys.path[0])
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        os.chdir(sys.path[0])
        # self.s.bind((ip,port))
        # self.s.listen()
        # self.s.bind((IP,PORT))
        # self.s.listen()
        # self.conn = None
        # self.addr = None

    # 用于接收所有客户端发送信息的函数
    def tcp_connect(self, conn, addr):
        # 连接后将用户信息添加到users列表
        user = conn.recv(1024)                                    # 接收用户名
        user = user.decode()

        for i in range(len(users)):
            if user == users[i][1]:
                print('User already exist')
                user = '' + user + '_2'

        if user == 'no':
            user = addr[0] + ':' + str(addr[1])
        users.append((conn, user, addr))
        print(' New connection:', addr, ':', user, end='')         # 打印用户名
        d = onlines()                                                   # 有新连接则刷新客户端的在线用户显示
        self.recv(d, addr)
        try:
            while True:
                data = conn.recv(1024)
                data = data.decode()
                self.recv(data, addr)                         # 保存信息到队列
            conn.close()
        except:
            print(user + ' Connection lose')
            self.delUsers(conn, addr)                             # 将断开用户移出users
            conn.close()

    # 判断断开用户在users中是第几位并移出列表, 刷新客户端的在线用户显示
    def delUsers(self, conn, addr):
        a = 0
        for i in users:
            if i[0] == conn:
                users.pop(a)
                print(' Remaining online users: ', end='')         # 打印剩余在线用户(conn)
                d = onlines()
                self.recv(d, addr)
                print(d)
                break
            a += 1

    # 将接收到的信息(ip,端口以及发送的信息)存入que队列
    def recv(self, data, addr):
        lock.acquire()
        try:
            que.put((addr, data))
        finally:
            lock.release()

    # 将队列que中的消息发送给所有连接到的用户
    def sendData(self):
        while True:
            if not que.empty():
                data = ''
                reply_text = ''
                message = que.get()                               # 取出队列第一个元素
                if isinstance(message[1], str):                   # 如果data是str则返回Ture
                    for i in range(len(users)):
                        # user[i][1]是用户名, users[i][2]是addr, 将message[0]改为用户名
                        for j in range(len(users)):
                            if message[0] == users[j][2]:
                                print(' this: message is from user[{}]'.format(j))
                                if '@Robot' in message[1] and reply_text == '':
                                    
                                    msg = message[1].split(':;')[0]
                                    reply = call_robot(url, apikey, msg)
                                    reply_text = reply['results'][0]['values']['text']
                                    data = ' ' + users[j][1] + '：' + message[1] + ':;' + 'Robot：' + '@' + \
                                           users[j][1] + ',' + reply_text
                                    break
                                elif '@Robot' in message[1] and (not reply_text == ''):
                                    data = ' ' + users[j][1] + '：' + message[1] + ':;' + 'Robot：' + '@' + \
                                           users[j][1] + ',' + reply_text
                                else:
                                    data = ' ' + users[j][1] + '：' + message[1]
                                    break      
                        users[i][0].send(data.encode())
                # data = data.split(':;')[0]
                if isinstance(message[1], list):  # 同上
                    # 如果是list则打包后直接发送  
                    data = json.dumps(message[1])
                    for i in range(len(users)):
                        try:
                            users[i][0].send(data.encode())
                        except:
                            pass

    def run(self):

        self.s.bind((self.ip,self.port))
        self.s.listen(5)
        print('Chat server starts running...')
        q = threading.Thread(target=self.sendData)
        q.start()
        while True:
            conn, addr = self.s.accept()
            t = threading.Thread(target=self.tcp_connect, args=(conn, addr))
            t.start()
        # self.s.close()



if __name__ == '__main__':
    cserver = ChatServer(IP,PORT)
    cserver.start()


