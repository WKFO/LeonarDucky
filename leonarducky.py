#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#


"""
Author : KeyLo99
Contact : twitter.com/KeyLo_99
"""

import os, sys
import argparse, time

from src import ducky_compiler

class LeonarDucky(object):
    def __init__(self, input_f='duck.txt', output='ducky.ino', delay=500, function=False):
        self.input = input_f
        self.output = output
        self.delay = delay
        self.function = function

    def log(self, msg, log_type='info '):
        sys.stdout.write('[%s] - %s - %s\n' % (time.ctime(), log_type.capitalize(), msg))
        sys.stdout.flush()

        if log_type == 'fatal':
            sys.exit()

    def compile(self):
        self.log('Program started')

        try:
            start_time = time.time()
            ducky_code = open(self.input, 'r').read().strip().split('\n')
            ino_code = ducky_compiler.Compile(ducky_code, self.delay, self.function)
            finish_time = time.time() - start_time

            self.log('Ducky code converted successfully to Arduino code in %fs' % finish_time)
        except Exception as why:
            self.log(why.strerror, 'fatal')

        try:
            with open(self.output, 'w') as ino_file:
                ino_file.write(ino_code)
                self.log('Arduino code written into %s' % self.output)
        except Exception as why:
            self.log(why.strerror, 'fatal')

def main():
    parser = argparse.ArgumentParser(description='DuckyScript to Arduino Converter')

    parser.add_argument('-i', '--input', dest='input', help='Input file', type=str)
    parser.add_argument('-o', '--output', dest='output', help='Output file', type=str)
    parser.add_argument('-d', '--delay', dest='delay', help='Set delay, default: 500', default=500, type=int)
    parser.add_argument('-f', '--function', dest='function', help='Create function, default: False', action='store_true')

    args = parser.parse_args()

    if all([args.input, args.output]) != True:
        parser.print_help()
        sys.exit()

    compiler = LeonarDucky(args.input, args.output, args.delay, args.function)
    compiler.compile()

if __name__ == '__main__':
    print(open(os.path.join('src', 'banner'), 'r').read() + '\n')
    #init()
    main()