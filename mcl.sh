import os
start=input('Launch on startup installation y or n')
print('Installing required packages.')
os.system('pip3 install random')
os.system('pip3 install time')
os.system('pip3 install requests')
os.system('pip3 install sys')
os.system('pip3 install enquiries')
os.system('pip3 install colorama')
if start == 'y':
 os.system('bash mooncord.sh')
