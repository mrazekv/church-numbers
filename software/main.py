#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
from display import displayThread
from web import webThread
#from uart import uartThread
import time

display_thread = displayThread()
# UART neni v zakladni verzi vyuzivan
# uart_thread = uartThread(display_thread)
web_thread = webThread(display_thread)

#display_thread.start()
web_thread.start()
display_thread.run()

print("Display exits")
web_thread.stop()



# Wait until one thread exits, then exit the second
while display_thread.is_alive() and web_thread.is_alive():
    time.sleep(1)

if not display_thread.is_alive():
    print("Display thread exited, stopping web thread")
    web_thread.stop()
else:
    print("Web thread exited, stopping display thread")
    display_thread.stop()
    
    
    
    
import sys
sys.exit()

# uart_thread.start()
if 1:
    print("Exiting")
    while display_thread.is_alive():
        time.sleep(1)

    print("Web threadstopping")
    web_thread.stop()
 #   uart_thread.stop()



