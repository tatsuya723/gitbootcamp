# -*- coding: utf-8 -*-

import binascii
import nfc
import csv
import datetime
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
LEDPin = 26
BuzzerPin = 13
GPIO.setup(LEDPin, GPIO.OUT)
GPIO.setup(BuzzerPin, GPIO.OUT)


class MyCardReader(object):

    p1 = '012e4cd44ad9c56b'
    p2 = '012e4cd44ad9412f'
    p3 = '012e4cd44ad9315c'
    p4 = '012e4cd44ad9924c'
    d1 = 0
    d2 = 0
    d3 = 0

    def on_connect(self, tag):
        print "touched"
        self.idm = binascii.hexlify(tag.idm)
        return True

    def read_id(self):
        clf = nfc.ContactlessFrontend('usb')
        try:
            clf.connect(rdwr={'on-connect': self.on_connect})
        finally:
            clf.close()

    def _notice(self):
        GPIO.output(LEDPin, True)
        for i in range(0, 2):
            GPIO.output(BuzzerPin, True)
            time.sleep(0.1)
            GPIO.output(BuzzerPin, False)
            time.sleep(0.1)
        GPIO.output(LEDPin, False)

    def _error(self):
        GPIO.output(LEDPin, True)
        GPIO.output(BuzzerPin, True)
        time.sleep(1)
        GPIO.output(BuzzerPin, False)
        GPIO.output(LEDPin, False)

    def card_search(self):
        if MyCardReader.p1 == cr.idm:
            cr._notice()
            if MyCardReader.d1 == 0:
                dt_now = datetime.datetime.now()
                MyCardReader.d1 = datetime.datetime(
                    year=dt_now.year, month=dt_now.month, day=dt_now.day, hour=dt_now.hour, minute=dt_now.minute, second=dt_now.second)
                print(MyCardReader.d1)
            else:
                dt_now = datetime.datetime.now()
                now = datetime.datetime(
                    year=dt_now.year, month=dt_now.month, day=dt_now.day, hour=dt_now.hour, minute=dt_now.minute, second=dt_now.second)
                print(now)
                td = abs(now - MyCardReader.d1)
                print(td.total_seconds())
                MyCardReader.d1 = 0
        elif MyCardReader.p2 == cr.idm:
            cr._notice()
            if MyCardReader.d2 == 0:
                dt_now = datetime.datetime.now()
                MyCardReader.d2 = datetime.datetime(
                    year=dt_now.year, month=dt_now.month, day=dt_now.day, hour=dt_now.hour, minute=dt_now.minute, second=dt_now.second)
                print(MyCardReader.d2)
            else:
                dt_now = datetime.datetime.now()
                now = datetime.datetime(
                    year=dt_now.year, month=dt_now.month, day=dt_now.day, hour=dt_now.hour, minute=dt_now.minute, second=dt_now.second)
                print(now)
                td = abs(now - MyCardReader.d2)
                print(td.total_seconds())
                MyCardReader.d2 = 0
        elif MyCardReader.p3 == cr.idm:
            cr._notice()
            if MyCardReader.d3 == 0:
                dt_now = datetime.datetime.now()
                MyCardReader.d3 = datetime.datetime(
                    year=dt_now.year, month=dt_now.month, day=dt_now.day, hour=dt_now.hour, minute=dt_now.minute, second=dt_now.second)
                print(MyCardReader.d3)
            else:
                dt_now = datetime.datetime.now()
                now = datetime.datetime(
                    year=dt_now.year, month=dt_now.month, day=dt_now.day, hour=dt_now.hour, minute=dt_now.minute, second=dt_now.second)
                print(now)
                td = abs(now - MyCardReader.d3)
                print(td.total_seconds())
                MyCardReader.d3 = 0
        else:
            cr._error()


if __name__ == '__main__':
    cr = MyCardReader()
    while True:
        print "touch card:"
        cr.read_id()
        cr.card_search()
        print "released"
        print cr.idm
        with open('log.csv', 'a') as f:
            writer = csv.writer(f)
            dt_now = datetime.datetime.now()
            writer.writerow([1, dt_now, cr.idm])
        f.close()
        print('done. see log.csv')
