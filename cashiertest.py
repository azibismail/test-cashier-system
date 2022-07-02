import socket
import sys
import time
import errno
import math
from multiprocessing import Process

ok_message = '\nHTTP/1.0 200 OK\n\n'
nok_message = '\nHTTP/1.0 404 Not Found\n\n'

def process_start(s_sock, self, a=0, recieve=0, change=0, temp=0):

	s_sock.send(str.encode("*****JUDE'S RESTAURANT MENU*****")
	s_sock.send(str.encode("\n1.Adobo---->30", "\n2.Nilaga---->35", "\n3.Pork Chop---->50", "\n4.Letchon Paksiw---->40", "\n5.Cash Out", "\n6.Exit"))
	
	self.a = a
	self.r = r
	self.recieve = recieve
	self.change = change
	self.temp = temp
	
	while True:
		data = s_sock.recv(2048)
		data = data.decode("utf-8")
		
		try:
			
			c = int(input("Choose:\n"))
			
			if (c == 1):
				d = int(input("Enter the quantity:\n"))
				self.r = self.r + 30 * d
				
			elif (c == 2):
				d = int(input("Enter the quantity:\n"))
				self.r = self.r + 35 * d
				
			elif (c == 3):
				d = int(input("Enter the quantity:\n"))
				self.r = self.r + 50 * d
				
			elif (c == 4):
				d = int(input("Enter the quantity:\n"))
				self.r = self.r + 40 * d
				
			elif (c == 5):
				print("total:", self.r)
				if (self.r > 0):
					recieve = int(input("Input Money Receive:\n"))
					print("Change:", recieve - self.r)
					print("******Thank You Come Again!!!******")
					quit()
					
			elif (c == 6):
				quit()
			
			else:
				print("Invalid option")
				
		except:
			print('Invalid input!')
			
		if not data:
			break
			
	s_sock.close()

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("",8888)) #port connnected
    print("waiting for client connection ...")
    s.listen(28)

    try:
        while True:
            try:
                s_sock, s_addr = s.accept()
                p = Process(target=process_start, args=(s_sock,))
                p.start()

            except socket.error:

                print('SOCKET ERROR!')

            except Exception as e:
                print("INTERRUPT!")
                print(e)
                sys.exit(1)
    finally:
           s.close()
