#!/usr/bin/python3

import socketserver
import random

class GibbetHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).decode()
        print('Клиент {} сообщает {}'.format(self.client_address[0], self.data))
        if self.data == 'START':
            x = random.randint(1, 100)
            try_count = 10
            self.request.sendall(bytes('GUESS;1;100', 'utf-8'))
            while True:
                self.data = self.request.recv(1024).decode()
                resp = self.data.split(';') # responce = ['GUESS', '1', '100']
                if resp[0] == 'TRY':
                    if int(resp[1]) == x:
                        self.request.sendall(bytes('TRUE', 'utf-8'))
                        print('Клиент {} выиграл'.format(self.client_address[0]))
                        break
                    else:
                        try_count -= 1
                        if try_count == 0:
                            self.request.sendall(bytes('FAIL', 'utf-8'))
                            print('Клиент {} проиграл'.format(self.client_address[0]))
                            break
                        else:
                            if x < int(resp[1]):
                                self.request.sendall(bytes('FALSE;{};<'.format(try_count), 'utf-8'))
                            else:
                                self.request.sendall(bytes('FALSE;{};>'.format(try_count), 'utf-8'))
                            print('Клиент {}. Осталось попыток {}'.format(self.client_address[0], try_count))
                elif resp[0] == 'GOODBYE':
                    print('Клиент {} ушел'.format(self.client_address[0]))
                    self.request.sendall(bytes('GOODBYE', 'utf-8'))
                    break


HOST = 'localhost'
PORT = 9999

server = socketserver.TCPServer((HOST, PORT), GibbetHandler)
print('Сервер игры "Виселица" запущен')
server.serve_forever()
