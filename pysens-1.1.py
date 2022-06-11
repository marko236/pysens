import os
import time
a=input("Show previous outputs(y/*): ")
t=int(input("Refresh rate(whole seconds): "))
if a=='y' or a=='Y':
	so=True
else:
	so=False
while 1:
	if so==False:
		os.system('clear')
	os.system("sensors")
	time.sleep(t)