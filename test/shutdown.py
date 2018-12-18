import os
#windows
#os.system('shutdown -s -t 0')
#linux
#os.system('shutdown -h now')

url = 'https://www.python.org/ftp/python/3.7.1/Python-3.7.1.tgz'
version=(url.split('/'))
print(url.split('/')[-1])
print(version[-1])
cmd = 'tar zxvf '+ version[-1]
print(cmd)