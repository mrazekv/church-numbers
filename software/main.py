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

display_thread.start()
web_thread.start()
# uart_thread.start()
if 1:
    print("Exiting")
    while display_thread.is_alive():
        time.sleep(1)

    print("Web threadstopping")
    web_thread.stop()
 #   uart_thread.stop()



