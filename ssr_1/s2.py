# codin:utf-8

import os
import time


in1 = input('是否安装前置(y/*)').strip().lower()
if in1 == 'y':
    from ssr_1 import s1
    s1.run()
    os.system('pip3 install https://github.com/shadowsocks/shadowsocks/archive/master.zip')
    print('前置安装完毕')
    print('\n\nssr安装完成\n\n')
    time.sleep(2)


'''
安装ssr
'''
def install_ssr():
    ''' 前置要求(安装了anaconda或pip3) '''
    # os.system('pip3 install ./pkgs/shadowsocks-master.zip')

    # os.system('sudo cp ./pkgs/shadowsocks.json /etc/shadowsocks.json')

    os.system('sudo chmod -R 777 /var/log/')    # 解决下个命令没有权限的问题

    os.system('ssserver -c ./pkgs/shadowsocks.json -d start')
    # os.system('ssserver -c shadowsocks.json -d start)

    print('如果显示的是started 那就代表使用成功了')

    # 用这个命令可能会出现一些问题 权限的问题()
    # 解决方法如下（https://www.dazhuanlan.com/2020/06/12/5ee25fd284f44/）
    # sudo chown hugo:hugo /var/run/shadowsocks.pid
    # sudo chown hugo:hugo /var/log/shadowsocks.log


if __name__ == "__main__":
    install_ssr()


