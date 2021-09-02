#made by SKY#0845 on discord
#this is an OS you can make apps in it py doing file.create the file.edit then rom/exe

#dont exicute image files .gif .jpg only .txt .js .css .py .lua

#https://manytools.org/hacker-tools/convert-images-to-ascii-art/go/
#^^^^^^^^^^^^
#image genorator just add to folder and do file.print then the filename (exa: noob.txt)


import time
import os, os.path
import json

password="1234"
username = "SKY#0845"

JVM = True


def console(JVM):
 print("BootLeg Loader V1.4")
 
 while True:
  print("\033[1;32;40m \033[0;0m")
  
  text = input(username + "~ ")

  #java will be implemented to be able to do java code directly into prompt and it will run
  if text == "load.v1.0":
     print("\033[1;32;40m Java-Loader JVM v1.0  \n")
     JVM = False
     print("compleate")
  
  
  
  
  if JVM == True:

  
   if text == "exit()":
      print("shutting Down")
      print("")
      time.sleep(2)
      break  
 
   elif text == "rom/":
      list = os.listdir()
      print(list)
   elif text == "clear":
      os.system('cls' if os.name == 'nt' else 'clear')
      print("BootLeg Loader V1.4")

   elif text == "file.edit":
     filename = input("What File Would You Like To Edit: ")
     f = open(filename, "w")
     new_data = input("FileEdit~ ")
     f.write(new_data)
     f.close()
   elif text == "file.print":
     filename = input("What File Would You Like To Print: ")
     try:
      f = open(filename, "r")
      print(f.read())
      f.close()
     except:
      print("\033[1;31;40m  ERROR \033[0;0m")

   elif text == "rom/create":
     file = input("FileName~ ")
     f = open(file, "x")
     f.close()
   elif text == "rom/exe":
     filename2 = input("what file: ")
     exec(open(filename2).read())
   elif text == "os.time":
     obj = time.localtime()
     t = time.asctime(obj)
     print(t)

   elif text == "calculator":
     exec(open("compute.py").read())

   else:
      try:
        if text == "main.py":
         awnser = input("are you shure you want to launch another instance, it may break your files. (yes | no ): ")
         if awnser == "yes":
           exec(open(text).read())
         else:
           continue
        else:
          exec(open(text).read())

        
      except:
        print("\033[1;31;40m  ERROR \033[0;0m")
        continue
      
  else:
    print("\033[1;31;40m you turned on JAVA and that is curently not used and none of the commands will work \033[0;0m")

print("logged in as "+ username)
while True:
 code = input("password: ")
 if code == password:
   console(JVM)
 else:
   print("Incorect Password")


