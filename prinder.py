import os
import sys
os.system("title Prinder 0.01")
os.system("prompt prinder@%USERNAME%$$ ")
while True:
    command = input("prinder@mcremote$ ")
    if command=="info":
        print("Prinder version [0.01.000]\n(d) by Traops78\n")
    if command=="quit":
        sys.exit()
    if command=="reload":
        os.system("prinder.py")
    else:
        os.system(command)
        