#!/usr/bin/python3
# coding:utf-8

# 参考:https://www.codetd.com/article/2454266

import os


def install_ssr():
    
    os.system("sudo apt install libcanberra-gtk-module libcanberra-gtk3-module gconf2 gconf-service libappindicator1")    
    in1 = input("是否要去换源？(y/*)").strip().lower()
    if in1 == 'y':
        from gongneng import func_1
        func_1.huanyuan()

    
    os.system("sudo dpkg -i ./pkgs/electron-ssr-0.2.6.deb")




