#made by SKY#0845 on discord
#this is an OS you can make apps in it py doing file.create the file.edit then rom/exe

#dont execute image files .gif .jpg only .txt .js .css .py .lua

#https://manytools.org/hacker-tools/convert-images-to-ascii-art/go/
#^^^^^^^^^^^^
#image genorator just add to folder and do file.print then the filename (exa: noob.txt)


import time
import os, os.path
import json
import random
while True:
  # some JSON:
  x =  '{ "password":"1234", "username":"SKY", "password2":"1234", "username2":"guest"}'
  # parse x:
  y = json.loads(x)
  
  # the result is a Python dictionary:
  thing = input("username: ")
  
  if thing == y["username"]:
    username = thing
    break
  elif thing == y["username2"]:
    username = thing
    break
    
      
  
  else:
    print("username not found go into main.py and add the username + password. For now yor username is Guest and password is 1234")
    username = ""
  








JVM = True


def console(JVM):
 print("BootLeg Loader V1.4")
 
 while True:
  print("\033[1;32;40m \033[0;0m")
  
  text = input('\033[1;34;40m' + username + "~ \033[0m ")

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
   if text == "random":
     print("rolled a\033[1;35;40m", str(random.randint(1,100)), "\033[0m")
 
   elif text == "rom/":
      list = os.listdir()
      print("\033[1;32;40m ", list, "   \033")
   elif text == "clear":
      os.system('cls' if os.name == 'nt' else 'clear')
      print("BootLeg Loader V1.4")

   elif text == "file.edit":
     filename = input("\033[1;36;40m What File Would You Like To Edit: \033")
     f = open(filename, "w")
     new_data = input("FileEdit~ ")
     f.write(new_data)
     f.close()
   elif text == "file.print":
     filename = input("\033[1;36;40m What File Would You Like To Print: \033")
     try:
      f = open(filename, "r")
      print(f.read())
      f.close()
     except:
      print("\033[1;31;40m  ERROR \033[0;0m")

   elif text == "rom/create":
     file = input("\033[1;36;40m FileName~ \033")
     f = open(file, "x")
     f.close()
   elif text == "rom/exe":
     filename2 = input("\033[1;36;40m what file: \033")
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
         awnser = input("\033[1;36;40m are you shure you want to launch another instance, it may break your files. (yes | no ): \033")
         if awnser == "yes":
           exec(open(text).read())
         else:
           continue
        else:
          if text.endswith('.txt'):
            f = open(text, "r")
            print(f.read())
            f.close()
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
  if username == y["username"]:
   if code == y["password"]:
    os.system('cls' if os.name == 'nt' else 'clear')
    console(JVM)
   else:
    print("Incorect Password")

  elif username == y["username2"]:
   if code == y["password2"]:
    os.system('cls' if os.name == 'nt' else 'clear')
    console(JVM)
   else:
    print("Incorect Password")

  else:
    print("Incorect username/password")

   


