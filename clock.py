import time
import os, os.path
loop = 100
os.system('cls' if os.name == 'nt' else 'clear')

while True:
 time_naitive = 0.00
 loop = 10000
 print("1 - Time")
 print("2 - stopwatch")
 print("3 - countdown")
 text = input("witch option do you chose: ")
 if text == "1":
     while loop >= 0:
      t2 = time.localtime()
      t = time.asctime(t2)
      print(t)
      loop = loop - 1
      print("do CTRL + C to close program")
      time.sleep(1)
      os.system('cls' if os.name == 'nt' else 'clear')
    
 if text == "2":
     while loop >= 0:
        time_naitive = time_naitive + 0.1
        print(round(time_naitive, 1))
        print("do CTRL + C to stop timer")
        time.sleep(0.1)
        os.system('cls' if os.name == 'nt' else 'clear')
        loop = loop - 1

     
 if text == "3":
     continue
 else:
     print("invalid option")
     os.system('cls' if os.name == 'nt' else 'clear')
