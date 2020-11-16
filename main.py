#!/usr/bin/python3
# codin:utf-8

import os

os.system('sudo timedatectl set-timezone Asia/Shanghai')
os.system("echo '时间设置完成'")



def f1():
    ''' 
    将apt-get 进行更新， 并且安装git
    '''
    os.system("sudo apt-get update")
    os.system("echo '\n\n\n\n\n\n\napt更新完成\n\n\n\n\n\n\n'")
    os.system("sudo apt install git")
    os.system("echo '\n\n\n\n\n\n\ngit安装完成\n\n\n\n\n\n\n'")

def f2():
    '''
    安装离线包 chrome 和 code
    '''

    os.system("sudo dpkg -i ./pkgs/code_1.51.1-1605051630_amd64.deb")
    os.system("sudo dpkg -i ./pkgs/google-chrome-stable_current_amd64.deb ")
    os.system("echo '离线包安装完成'")

def update_apt():
    """
    将apt进行换个源
    """
    from ssr_1 import s2
    # s1.run()
    s2.install_ssr()
    

def install_lantern():
    ''' 安装蓝灯 '''
    os.system('sudo dpkg -i ./pkgs/lantern-installer-64-bit.deb')

funcs = {
    '1': [f1,f1.__doc__.strip()],
    '2': [f2,f2.__doc__.strip()],
    '3': [update_apt,update_apt.__doc__.strip()],
    '4': [install_lantern,install_lantern.__doc__.strip()],
}


def daying():
    print('''
    ! 千万注意， 如果要使用ssr那就得先安装ssr
    否则后面在用的时候，apt就会出现谜一样的问题
    (也可以去使用lantern)

    ''')
    print('默认会将时间地区改变')
    print('=====================================================')
    print('退出请输入q')
    for i in funcs:
        print(f'{i}\t{funcs[i][1]}')




while 1:
    print('\n')
    daying()
    in1 = input("输入模式>>:").strip().lower()
    if in1 == 'q':
        break
    if in1 not in funcs:
        print('你输入有误')
        continue
    
    funcs[in1][0]()
    



print('==OVER==')

