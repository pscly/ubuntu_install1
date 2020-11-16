#!/usr/bin/python3
# coding:utf-8

import os




def install_ssr():
    
    os.system("sudo apt install libcanberra-gtk-module libcanberra-gtk3-module gconf2 gconf-service libappindicator1")    
    in1 = input("是否要去换源？(y/*)").strip().lower()
    if in1 == 'y':
        from ssr_1 import s2
        






