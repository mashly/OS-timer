#!/usr/binn/python3


import os
import time
import ctypes


while True:
	print("1. Shutdown Computer")
	print("2. Restart Computer")
	print("3. Lock")
	choice = int(input("Enter your choice: "))
	if(choice >= 1 and choice <= 4):
		if choice == 1:
			os.system("shutdown /s /t 600")
		elif choice ==2 :
			os.system("shutdown /r /t 600")
		elif choice == 3:
			ctypes.windll.user32.LockWorkStation()
		elif choice == 4:
			quit()
	else:
		break
input("")