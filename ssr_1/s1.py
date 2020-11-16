#!/usr/bin/python3
# codin:utf-8
import os

# TODO http://www.techbulo.com/2608.html

# in1 = input('你是否要切换源(默认是清华的源)(Y/n)？').strip().lower()
# if in1 == 'n':



def run():
    os.system('sudo cp ./lists/sources.list /etc/apt/sources.list')
    # os.system('cp  /etc/apt/sources.list.bak  ./.1.list')

    os.system('sudo apt-get update')
    # os.system('sudo apt-get upgrade')     # 更新所有的软件(例如firefox)


    os.system('sudo apt install python3-pip')
    

    
    # 这里之所以要把sudo删除是因为如果不删除的话就会出现问题，pip3的报错(因为dpkg安装部分东西会把apt给修改什么的)
    os.system('pip3 install --upgrade pip pip3 install setuptools')  
    # os.system('sudo pip3 install --upgrade pip pip3 install setuptools')
    
    os.system('pip3 install shadowsocks')
    # os.system('sudo pip3 install shadowsocks')
    os.system('sudo apt-get -y install python-m2crypto')


if __name__ == "__main__":
    # os.system("cat ./lists/sources.list")
    run()
    
