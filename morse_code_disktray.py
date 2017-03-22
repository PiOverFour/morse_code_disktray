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

DBG = True
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

class Morse():
    def __init__(self):
        pass

    def set_time_unit(self, time_unit):
        self.time_unit = time_unit

    def get_short_time(self):
        return self.time_unit
    def get_long_time(self):
        return self.time_unit * 3
    def get_word_gap(self):
        return self.time_unit * 7

    def test_duration(self):
        if DBG:
            self.set_time_unit(0.2)
            return
        try:
            start_time = time.time()
            self.tray_open()
            open_duration = time.time() - start_time
        except:
            self.set_time_unit(0.5)
        try:
            start_time = time.time()
            self.tray_close()
            close_duration = time.time() - start_time
        except:
            pass
        self.set_time_unit(max(open_duration, close_duration) * 1.05)

    def tray_open(self):
        if not DBG:
            sp = subprocess.Popen('eject')
            sp.wait()
        if DBG:
            print('OPEN')

    def tray_close(self):
        if not DBG:
            sp = subprocess.Popen(['eject', '-t'])
            sp.wait()
        if DBG:
            print('CLOSE')

    def sleep(self, t):
        time.sleep(t)
        if DBG:
            print(t)

    def intra_character(self):
        self.sleep(self.get_short_time())

    def inter_letters(self):
        self.sleep(self.get_long_time())

    def inter_words(self):
        self.sleep(self.get_word_gap())

    def dit(self):
        self.tray_open()
        self.sleep(self.get_short_time())
        self.tray_close()

    def dah(self):
        self.tray_open()
        self.sleep(self.get_long_time())
        self.tray_close()

    def echo_char(self, c):
        morse_rep = MORSE_ALPHABET[c]
        for i, dd in enumerate(morse_rep):
            if dd == '.':
                self.dit()
            elif dd == '-':
                self.dah()
            elif dd == '/':
                self.inter_words()
            if i < len(morse_rep)-1:
                self.intra_character()

    def echo_msg(self, msg):
        for i, c in enumerate(msg):
            print(c)
            self.echo_char(c)
            if i < len(msg)-1 and msg[i+1] != '/':
                self.inter_letters()


if __name__ == "__main__":
    args = sys.argv[1:]
    msg = ''
    if args:
        msg = ' '.join(args)
    if not msg:
        msg = raw_input('Input message:')
    msg = msg.upper()

    morse = Morse()
    morse.test_duration()
    morse.echo_msg(msg)
