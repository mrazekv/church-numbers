#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
from display import displayThread
from web import webThread
import time

display_thread = displayThread()
web_thread = webThread(display_thread)

#display_thread.start()
web_thread.start()
display_thread.run()

print("Display exits")
web_thread.stop()

