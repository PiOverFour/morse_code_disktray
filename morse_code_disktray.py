#!/usr/bin/python


# morse code disktray, morse code communication through disk trays 
# Copyright (C) 2017  Damien Picard dam.pic AT free.fr
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
import subprocess
import time

TIME_UNIT = 0.2
SHORT = TIME_UNIT * 1
LONG = TIME_UNIT * 3
# SHORT_GAP = TIME_UNIT * 3
MEDIUM_GAP = TIME_UNIT * 7

MORSE_ALPHABET = {
    "A" : ".-",
    "B" : "-...",
    "C" : "-.-.",
    "D" : "-..",
    "E" : ".",
    "F" : "..-.",
    "G" : "--.",
    "H" : "....",
    "I" : "..",
    "J" : ".---",
    "K" : "-.-",
    "L" : ".-..",
    "M" : "--",
    "N" : "-.",
    "O" : "---",
    "P" : ".--.",
    "Q" : "--.-",
    "R" : ".-.",
    "S" : "...",
    "T" : "-",
    "U" : "..-",
    "V" : "...-",
    "W" : ".--",
    "X" : "-..-",
    "Y" : "-.--",
    "Z" : "--..",
    " " : "/",

    "1" : ".----",
    "2" : "..---",
    "3" : "...--",
    "4" : "....-",
    "5" : ".....",
    "6" : "-....",
    "7" : "--...",
    "8" : "---..",
    "9" : "----.",
    "0" : "-----",

    "." : ".-.-.-",
    "," : "--..--",
    ":" : "---...",
    "?" : "..--..",
    "'" : ".----.",
    "-" : "-....-",
    "/" : "-..-.",
    "@" : ".--.-.",
    "=" : "-...-",
    }

def tray_open():
    # subprocess.Popen('eject')
    print('OPEN')

def tray_close():
    # subprocess.Popen(['eject', '-t'])
    print('CLOSE')

def sleep(t, dbg=False):
    time.sleep(t)
    if dbg:
        print(t)

DBG = True

def intra_character():
    sleep(SHORT, dbg=DBG)

def inter_letters():
    sleep(LONG, dbg=DBG)

def inter_words():
    sleep(MEDIUM_GAP, dbg=DBG)

def dit():
    tray_open()
    sleep(SHORT, dbg=DBG)
    tray_close()

def dah():
    tray_open()
    sleep(LONG, dbg=DBG)
    tray_close()

def echo_char(c):
    morse_rep = MORSE_ALPHABET[c]
    for i, dd in enumerate(morse_rep):
        if dd == '.':
            dit()
        elif dd == '-':
            dah()
        elif dd == '/':
            inter_words()
        if i < len(morse_rep)-1:
            intra_character()

def echo_msg(msg):
    for i, c in enumerate(msg):
        print(c)
        echo_char(c)
        if i < len(msg)-1 and msg[i+1] != '/':
            inter_letters()


if __name__ == "__main__":
    args = sys.argv[1:]
    if args:
        msg = ' '.join(args)
    else:
        msg = raw_input('Input message:')
    msg = msg.upper()
    echo_msg(msg)
