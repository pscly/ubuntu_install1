import os
def huanyuan():

    os.system('sudo cp /etc/apt/sources.list /etc/apt/sources.bak.list')
    os.system('sudo cp ./lists/sources.list /etc/apt/sources.list')
    
    # os.system('sudo apt-get update')

    # os.system('sudo apt install python3-pip')
