#!/usr/bin/python3
# coding=UTF-8

import serial
import matplotlib.pyplot as plt
from drawnow import *
import sys

n = 0
# 生成画布
plt.figure(figsize=(16, 12), dpi=180)
ser = None
# 打开交互模式
plt.ion()

x = []
a1_list = []
a2_list = []

def new_thread():
    global n,x,a1_list,a2_list,ser
    ser = serial.Serial('/dev/ttyUSB1', 9600)
    print(ser)
    if ser.isOpen():
       print("open success")
    else:
        print("open failed")
    while True:
        ser.write(b'x\n')
        count = ser.inWaiting()
        if count > 0:
            data = ser.readline()
            if data != b'':
                print("receive:", data)
                pass
            x.append(n)
            n = n + 1
            try:
                a1_list.append(int(data.split(b',')[0]))
                a2_list.append(int(data.split(b",")[1]))
                drawnow(plot_thread)

                if n > 50:
                    x.pop(0)
                    a1_list.pop(0)
                    a2_list.pop(0)

            except BaseException:
                pass

            

def plot_thread():
    global x,a1_list,a2_list
    plt.ylim(-1050, 1050)
    plt.plot(x, a1_list)
    plt.plot(x, a2_list)


if __name__ == '__main__':
    try:
        new_thread()
        plt.pause(0.0000001)
    except KeyboardInterrupt:
        if ser != None:
            ser.close()
        sys.exit()