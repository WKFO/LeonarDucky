#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
[Author] : KeyLo99
[Contact] : twitter.com/KeyLo_99
"""

from compiler import ducky_compiler
from datetime import datetime
import getopt
import sys
import os


def start():
    termPrint("""
 _                                      ______               _
| |                                     |  _  \             | |
| |      ___   ___   _ __    __ _  _ __ | | | | _   _   ___ | | __ _   _
| |     / _ \ / _ \ | '_ \  / _` || '__|| | | || | | | / __|| |/ /| | | |
| |____|  __/| (_) || | | || (_| || |   | |/ / | |_| || (__ |   < | |_| |
\_____/ \___| \___/ |_| |_| \__,_||_|   |___/   \__,_| \___||_|\_\ \__, |
                                                Coded by KeyLo99    __/ |
 DuckyScript to Arduino Converter               Version:1.0        |___/

""" + "\n", "\033[1;32m", "")
    lines = None
    inputfile = os.getcwd() + "/duck.txt"
    delay = 500
    func = False
    output = os.getcwd() + "/ducky.ino"

    try:
        opts, args = getopt.getopt(sys.argv[1:], "i:d:f:o:h", ["input=", "delay=", "function=", "ouput=", "help"])
    except:
        usage()
        sys.exit(0)
    if(len(opts) != 4):
        usage()
        sys.exit(0)

    for opt, args in opts:
        if opt == "-h" or opt == "--help":
            usage()
            sys.exit(0)
        elif opt in ("-i", "--input"):
            inputfile = args
        elif opt in ("-d", "--delay"):
            delay = args
        elif opt in ("-f", "--function"):
            func = args
        elif opt in ("-o", "--output"):
            output = args

    termPrint("[" + str(datetime.now().strftime("%H:%M:%S")) + "][+] Reading " + inputfile + "...", "\033[1;36m", "")
    try:
        with open(inputfile, "r") as f:
            lines = f.readlines()
    except:
        print("[-] Error: Using default settings.")
        with open(os.getcwd() + "/duck.txt", "r") as f:
             lines = f.readlines()
    time1 = datetime.now()
    with open(output, "w+") as f:
        termPrint("[" + str(datetime.now().strftime("%H:%M:%S")) + "][+] Compiling into " + output + "...",
                  "\033[1;36m", "")
        codes = ducky_compiler.Compile(lines, delay, func)
        f.write(codes)
        #print(codes)
    time2 = datetime.now()
    ctime = str((time2 - time1).seconds)+"." + str((time1 - time2).microseconds)[:3]
    if ctime != "0.0":
        termPrint("[" + str(datetime.now().strftime("%H:%M:%S")) + "][>] Compiled successfully in " + ctime + "\n", "\033[0;32m", "")
    else:
        termPrint("[" + str(datetime.now().strftime("%H:%M:%S")) +"][>] Compiled successfully.\n", "\033[0;32m", "")

def usage():
    termPrint("[-] Example Usage: leonarducky -i duck.txt -d 500 -f False -o ducky.ino\n", "\033[1;31m", "")

def termPrint(ttp, col, oncolor):
    try:
        if("nt" in os.name) and (sys.stdout.isatty()):
            from compiler import color_console
            default_colors = color_console.get_text_attr()
            default_bg = default_colors & 0x0070
            color_console.set_text_attr(color_console.which_color(col) |
                                        default_bg | color_console.FOREGROUND_INTENSITY)
            print(ttp)
            color_console.set_text_attr(default_colors)
        else:
            print(col + ttp + oncolor)
    except:
        print(ttp)

if __name__ == '__main__':
    start()

