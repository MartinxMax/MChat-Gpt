#!/usr/bin/python3
# @Мартин.
import openai
import socket
import sys
import textwrap
import argparse
import threading
from TOKEN import Token
from loguru import logger


version = "@Мартин. ChatGpt_Server V1.0.0"
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
        if args.TOKEN:
            openai.api_key = args.TOKEN
            if args.PORTFORWARDIGN:
                logger.info("Shared Services On")
                self.__provide_server(args.LHOST, args.LPORT)
            else:
                logger.info("Normal mode On")
                while True:
                    query = input("To AI [exit] <:")
                    if query == "exit":
                        logger.warning("Bye~")
                        break
                    else:
                        logger.warning("Chat-GPT reply:{}".format(self.__chat_gpt_ask(query)))
        else:
            logger.error("You must fill in the Chat Gpt API Token (TOKEN.py)")


    def __handle_client(self,client_socket,address):
        try:
            request = client_socket.recv(1024).decode()
        except Exception as e:
            client_socket.send('You must choose the UTF-8 encoding format'.encode('utf-8'))
        else:
            logger.warning("Received:{} [{}:{}]".format(request,*address))
            client_socket.send(self.__chat_gpt_ask(request).encode('utf-8'))
            logger.warning("Chat-GPT reply [{}:{}]".format(*address))
        client_socket.close()


    def __provide_server(self,host,port):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = ('', int(port))
        server_socket.bind(server_address)
        server_socket.listen(5)
        logger.warning(f"Successfully opened the service to the outside world, with address [{host}:{port}]")
        while True:
            client_socket, client_address = server_socket.accept()
            logger.warning("Accepted connection from {}:{}".format(*client_address))
            client_thread = threading.Thread(target=self.__handle_client, args=(client_socket,client_address))
            client_thread.start()


    def __chat_gpt_ask(self,quer):
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user",
                     "content": quer}
                ],
                temperature=0.4,
                max_tokens=2048
            )
            return completion.choices[0].message["content"]


if __name__ == '__main__':
    init_loger()
    print(logo,title)
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        epilog=textwrap.dedent('''
            Example:
                author-Github==>https://github.com/MartinxMax
            Basic usage:
                python3 {cp} -tk xxxx # Chat-Gpt Token (Alternatively, modify the fixed token in TOKEN.py)
                python3 {cp} -pf # Enable sharing mode
                python3 {cp} -lp # Set local shared data listening port
                python3 {cp} -lh # Set local shared data listening IP
                '''.format(cp=sys.argv[0]
                           )))
    parser.add_argument('-tk', '--TOKEN',default=Token, help='TOKEN')
    parser.add_argument('-pf', '--PORTFORWARDIGN',action='store_true', help='Portforwarding')
    parser.add_argument('-lp', '--LPORT', default="10032",help='local port')
    parser.add_argument('-lh', '--LHOST', default=myip(), help='local host')
    args = parser.parse_args()
    MainServer(args)