# -*- coding: utf-8 -*-
import pandas as pd
from pandas import DataFrame
import numpy as np
import os
import sys
import Common_functions.General_functions as gf
import Instruments.CtrlBoard as cb
import time
from PyQt5.QtWidgets import *

class a():
    CtrlB=object
    port='com9'
    drv_up=''
    drv_down=''
    config_path=''
    device_type=''

writ_type='345' #'all'
drv_vdc,tempe=('0x135f',4170)
sn='WRRC290080'
device_type='IDT'
f1=r'R:\金样\WRRC250305\DC\20220929_110306\WRRC250305_DC_20220929_110306.csv'
config_path=r'C:\Test_script\FS400_Final_Test_Desk1\Configuration'
df=object
if device_type=='ALU':
    drv_up = os.path.join(config_path, 'Setup_driverup_Ctrlboard56017837A002_20211203_ALU.txt')
    drv_down = os.path.join(config_path, 'Setup_driverdown_CtrlboardA001_20210820_ALU.txt')
if device_type=='IDT':
    drv_up = os.path.join(config_path, 'Setup_driverup_Ctrlboard56017837A002_20211203.txt')
    drv_down = os.path.join(config_path, 'Setup_driverdown_CtrlboardA001_20210820.txt')
board_up = os.path.join(config_path, 'Setup_brdup_CtrlboardA001_20220113_C80.txt')

mawin=a()
cb.open_board(mawin,mawin.port)
mawin.CtrlB.write(b'slave_on\n\r')
print(mawin.CtrlB.read_until(b'shell'))
print(mawin.CtrlB.read_all())
mawin.CtrlB.write(b'fs400_stop_fs400_performance\n\r')
print(mawin.CtrlB.read_until(b'shell'))
print(mawin.CtrlB.read_all())
mawin.CtrlB.write(b'cpld_spi_wr 0x31 1\n\r')
print(mawin.CtrlB.read_until(b'shell'))
print(mawin.CtrlB.read_all())

page_lis=[0,1,2,3,4,5,7,8,9,11,12,13,14,15,16]
for i in page_lis:
    gf.read_eeprom_information(mawin,i)

if writ_type=='all':
    df1=pd.read_csv(f1)
    print(df1)

    #Drv up
    #Driver power up
    cb.board_set(mawin,board_up)
    cb.board_set(mawin,drv_up)
    gf.write_eeprom_final(mawin,sn,df1,device_type,drv_vdc,tempe)
else:
    page_lis=[3,4,5]
    for i in page_lis:
        gf.write_eeprom_final_pageSeperate(mawin,i,sn,df,device_type)
cb.board_set(mawin,drv_down)
mawin.CtrlB.close()