#!/usr/bin/python3
# @Мартин.
import socket
import sys
import textwrap
import argparse
from loguru import logger

version = "@Мартин. ChatGpt_Client V1.0.0"
title = '''
************************************************************************************
<免责声明>:本工具仅供学习实验使用,请勿用于非法用途,否则自行承担相应的法律责任
<Disclaimer>:This tool is onl y for learning and experiment. Do not use it for illegal purposes,
 or you will bear corresponding legal responsibilities
************************************************************************************'''
logo = f'''                                                                    
  ______  __    __       ___   .___________.        _______ .______   .___________.
 /      ||  |  |  |     /   \  |           |       /  _____||   _  \  |           |
|  ,----'|  |__|  |    /  ^  \ `---|  |----`______|  |  __  |  |_)  | `---|  |----`
|  |     |   __   |   /  /_\  \    |  |    |______|  | |_ | |   ___/      |  |     
|  `----.|  |  |  |  /  _____  \   |  |           |  |__| | |  |          |  |     
 \______||__|  |__| /__/     \__\  |__|            \______| | _|          |__|     
                                            Github==>https://github.com/MartinxMax
                                            {version}'''


def init_loger():
    logger.remove()
    logger.add(
        sink=sys.stdout,
        format="<green>[{time:HH:mm:ss}]</green><level>[{level}]</level> -> <level>{message}</level>",
        level="INFO"
    )

def myip():
    return socket.getaddrinfo(socket.gethostname(), None, socket.AF_INET)[0][4][0]

class MainServer():
    def __init__(self,args):
        try:
            host,port = args.RHOST.split(':')
        except Exception as e:
            logger.error("parameter is incorrect (-rh 192.168.101.1:10032)")
        else:

            logger.info("My IP address [{}]",myip())
            while True:
                message = input("To AI [exit] <:")
                if message == "exit":
                    logger.warning("Bye~")
                    break
                self.__connct_server(host,port,message)

    def __connct_server(self,host,port,message):
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((host, int(port)))
            client_socket.send(message.encode('utf-8'))
            response = client_socket.recv(2048).decode('utf-8')
            logger.warning("Chat-GPT reply:"+response)
        except Exception as e:
                print(e)
        finally:
            client_socket.close()
def myip():
    return socket.getaddrinfo(socket.gethostname(), None, socket.AF_INET)[0][4][0]


if __name__ == '__main__':
    init_loger()
    print(logo,title)
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        epilog=textwrap.dedent('''
            Example:
                author-Github==>https://github.com/MartinxMax
            Basic usage:
                python3 {cp} -rh 192.168.101.1:10032 # Connect to remote server
                '''.format(cp=sys.argv[0]
                           )))
    parser.add_argument('-rh', '--RHOST',default="", help='Remote Host')
    args = parser.parse_args()
    MainServer(args)