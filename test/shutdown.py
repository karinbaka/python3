import os
#windows
#os.system('shutdown -s -t 0')
#linux
#os.system('shutdown -h now')

url = 'https://www.python.org/ftp/python/3.7.1/Python-3.7.1.tgz'
#version=(url.split('/'))
version = url.split('/')[-1]
#print(version[-1])

cmd = 'tar zxvf '+ version[0:len(version)-4]
print(cmd)

print(os.path.exists("Python-3.7.1.tgz"))