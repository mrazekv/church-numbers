#!/usr/bin/env python
# -*- coding: utf-8 -*-

from display import displayApp
from web import webThread

display_thread = displayApp()
web_thread = webThread(display_thread)

#display_thread.start()
web_thread.start()
display_thread.run()

print("Display exits")
web_thread.stop()

