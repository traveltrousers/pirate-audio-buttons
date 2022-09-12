#!/usr/bin/python
import gpiozero
import time
import os

class cmdbutton(object):

    def __init__(self, pin, short_duration, long_duration, short_action=None, long_action=None):
        self.__pin = pin
        self.short_duration = short_duration
        self.long_duration = long_duration
        self.short_action = short_action
        self.long_action = long_action
        self.__button = gpiozero.Button(self.__pin, pull_up=True,
                                        hold_time=self.long_duration)
        self.__press_time = None
        self.__button.when_held = self.__on_hold
        self.__button.when_pressed = self.__on_press
        self.__button.when_released = self.__on_release

    def __on_press(self):
        # button pressed
        self.__press_time = time.time()

    def __on_release(self):
        release_time = time.time()
        pressed_for = release_time - self.__press_time
        if pressed_for <= self.short_duration:
            # do short press stuff here
            try:
                self.short_action()
            except KeyboardInterrupt:
                raise
            except:
                pass

    def __on_hold(self):
            try:
                self.long_action()
            except KeyboardInterrupt:
                raise
            except:
                pass

if __name__ == '__main__':
	def do_short():
		os.system ('mpc next')

	def do_long():
		os.system ('mpc clear')
		os.system ('mpc load "Indie Radio"')
		os.system ('mpc play')
		os.system ('mpc repeat on')

pin = 16
short_duration = 0.7
long_duration = 1.5

btn = cmdbutton(pin=pin,
                    short_duration=short_duration,
                    long_duration=long_duration,
                    short_action = do_short,
                    long_action=do_long)

while True:
	time.sleep(1)

