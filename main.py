import getpass
import os
import time


#username = getpass.getuser()
#print("Username :" + username + "\n")
#print("Default dropbox folder : ")


#path = r'C:\Users\\' + username +'\\Dropbox'

#print(path + "\n")

#print("content : \n")
#for i in os.listdir(path):
#        print()

i = 0
for path, dirs, files in os.walk(r'C:\Users\ARJ'):
    for f in files:
        i = i+1
        if f.endswith('.dropbox'):
            print(os.path.join(path, f))

print('Scanned ' + str(i) + ' files')
