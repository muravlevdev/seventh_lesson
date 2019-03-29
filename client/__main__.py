import json
import socket
import argparse
from client_log_config import setup_log_config
import logging
import select


def sys_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-addr', default='localhost')
    parser.add_argument('-port', default=7777)
    parser.add_argument('-m', '--mode', type=str, default='w')

    return parser


def send_message(req_json):
    sock.send(req_json.encode('utf-8'))


def make_presence():
    action = input('Enter action: ')
    data = input('Data: ')

    request_json = json.dumps(
        {
            'action': action,
            'data': data
        }
    )

    return request_json


def unbox_recvd_message(resp_data):
    dict_data = json.loads(
        resp_data.decode('utf-8')
    )
    return dict_data


if __name__ == "__main__":
    parser = sys_arg_parser()
    args = parser.parse_args()
    setup_log_config()
    logging.info(f'Starting client')

    try:
        sock = socket.socket()
        sock.connect((args.addr, int(args.port)))
        print('Connected to ', args.addr, args.port)
        logging.info(f'Connected to ", {args.addr}, {args.port}')
    except Exception as err:
        logging.error(f'Unnable to connect to server {args.addr}, port {args.port}')
        sock.close()    
    
    if args.mode == 'w':
        while True:
            
            try:
                message = make_presence()
                send_message(message)
                logging.info(f'Message sent: {message}')

            except Exception as err:
                logging.error(f'Unnable to send message {message}!')
                sock.close()
            
    else:
        while True:
            rlist, wlist, xlist = select.select([], [sock], [], 0)
            response = sock.recv(1024)

            if response:
                recieved_message = unbox_recvd_message(response)
                print(recieved_message)
                logging.info(f'Recieved message: {recieved_message}')
                break

    



