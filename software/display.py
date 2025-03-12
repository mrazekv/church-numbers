#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
import time
import os
from math import ceil
from subprocess import Popen, PIPE

import requests

os.environ["SDL_VIDEODRIVER"] = "kmsdrm"


def rgb(value):
    value = value.lstrip('#')
    if len(value) == 6:
        return tuple(int(value[i:i+2], 16) for i in (0, 2, 4))
    return (0, 0, 0)


class displayApp:
    def __init__(self, is_slave=False):
        self.nmr = 000
        self.part = 0
        self.is_slave = is_slave
        # urls for notification (post) ["http://www.localhost:8080/set_status"]
        if not is_slave:
            #self.uris = ["http://localhost:8000/set_status"]
            self.uris = [] # no slave device
        else:
            self.master = "http://localhost:8080"
            self.uris = []

        self.file = ""
        self.fileset = False
        self.config = {}
        self.zalm = "Žalm"

        self.disoff = None   # cas vypnuti displeje
        self.pwr_is_off = False  # displej je vypnuty
        # limit pro vypnuti displeje v sekundach, doporucuji cca 30 minut kvuli moznemu zobrazeni modre obrazovky
        self.offlimit = 20*60
        self.totlimit = 90*60  # limit necinnosti v sekundach - 1.5 hodiny
        self.last_change = time.time()
        self.last_slave_update = 0

        self.keynmr = 0
        self.keypart = 0

        self.set_scheme(0)

        self.changed = True
        
        pygame.display.init()
        pygame.font.init()
        pygame.mouse.set_visible(False)

        pygame.init()
        displayInfo = pygame.display.Info()
        print(displayInfo)
        
    def get_status(self):
        return {
            "nmr": self.nmr,
            "part": self.part,
            "file": self.file,
            "fileset": self.fileset,
            "zalm": self.zalm,
            "config": self.config,
        }
        
    def set_status(self, status):
        try:
            for n in ["nmr", "part", "file", "fileset", "zalm", "config"]:
                if n not in status:
                    raise Exception(f"Missing key {n}")
                if getattr(self, n) != status[n]:
                    self.changed = True
                    self.last_change = time.time()
                setattr(self, n, status[n])
        except Exception as e:
            print("Error", e)
            
    def slave_update(self):
        print("Slave update")
        try:
            status = requests.get(f"{self.master}/get_status").json()
            self.set_status(status)
        except Exception as e:
            print("Error on update", e)

    def notify(self):
        for uri in self.uris:
            try:
                requests.post(uri, json=self.get_status(), timeout=1)
            except Exception as e:
                print("Error", e)

    def get_zalm(self):
        return self.zalm

    def set_zalm(self, value):
        self.zalm = value
        self.changed = True
        self.last_change = time.time()

    def set_scheme(self, color):
        if 0:
            # zlute pozadi, tmavy text
            self.config = {
                "background": rgb("f0e68c"),  # zluta
                "number": rgb("333333"),
                "part": rgb("666666"),
                "file": rgb("666666"),
            }
        elif color == 0:
            # zlute pozadi, tmavy text + oranzova sloka
            self.config = {
                "background": rgb("f0e68c"),  # zluta
                "number": rgb("333333"),
                "part": rgb("cc3300"),
                "file": rgb("666666"),
            }

        elif color == 1:
            # zlute pozadi, cerveny text, seda sloka
            self.config = {
                "background": rgb("f0e68c"),  # zluta
                "number": rgb("c5000f"),
                "part": rgb("333133"),
                "file": rgb("330000"),
            }

        elif 0:
            # svetle pozadi, zeleny text
            self.config = {
                "background": rgb("#ffffe6"),
                "number": rgb("006600"),
                "part": rgb("cc3300"),
                "file": rgb("666666"),
            }

        elif 0:
            # tmave pozadi, zeleny text
            self.config = {
                "background": rgb("#000000"),
                "number": rgb("ffffff"),
                "part": rgb("cc3300"),
                "file": rgb("666666"),
            }

    def is_zalm(self):
        if self.nmr == 1 and not self.fileset:
            return True
        if self.part == 99:
            return True
        return False

    def get_number(self):
        if self.is_zalm():  # zalm
            return "00000"
        return "%03d%02d" % (self.nmr, self.part)

    def set_number(self, value, change_name=True):
        if len(value) != 5:
            return False

        oldnmr = self.nmr
        oldpart = self.part
        nmr = int(value[:3])
        part = int(value[3:])

        if nmr == 0 and change_name:
            self.file = ""
            self.fileset = False
            # nmr = oldnmr
            # part = oldpart
            self.set_scheme(0)
        if nmr == 999 and change_name:
            self.file = u"Zpěvníček"
            self.fileset = True
            nmr = oldnmr
            part = oldpart
            self.set_scheme(1)
 #       if nmr == 3 and change_name:
 #           self.file = "Hosana"
 #           self.fileset = True
 #           nmr = oldnmr
 #           part = oldpart

        if not self.fileset:
            # logika sloupskeho zpevniku
            if nmr in list(range(150, 152)) + list(range(240, 246)) + list(range(340, 342)) + list(range(440, 441)) + list(range(740, 756)) + list(range(880, 893)) + list(range(943, 946)):
                self.file = u"Sloupský zpěvník"
            # logika ordinaria
            elif nmr in range(500, 510):
                self.file = u"Ordinárium"
            elif nmr == 990:
                self.file = "Poutníci naděje"
            else:
                self.file = ""

        self.nmr = nmr
        self.part = part
        self.changed = True
        self.last_change = time.time()

        self.kmsproc = None

    def conf(self, k):
        """ Vraci barvu podle klice """
        return self.config.get(k, (0, 0, 0))

    def display_long_text(self, text, color):
        """ Zobrazi dlouhy text na stred obrazovky, zacina od nejvetsiho pisma a postupne zmensuje.
        
        Args:
            text (str): text k zobrazeni
            color (tuple): barva textu
        
        """
        font_size = 800

        while 1:
            font_zalm = pygame.font.Font(
                "fonts/DroidSerif/DroidSerif-Regular.ttf", font_size)  # 400
            # text = "Smiluj se, Pane, neboť jsme zhřešili."
            # text = "Smilujse,Pane,neboťjsmezhřešili."

            allowed_width = self.s_width - 100
            x, y = self.s_width // 2, self.s_height // 2
            # first, split the text into words
            words = text.split()
            if len(words) == 0:
                break
            if len(words) == 1:
                words.append("")
                words.append("")
            # now, construct lines out of these words
            lines = []
            while len(words) > 0:
                # get as many words as will fit within allowed_width
                line_words = []
                while len(words) > 0:
                    line_words.append(words.pop(0))
                    fw, fh = font_zalm.size(' '.join(line_words + words[:1]))
                    if fw > allowed_width:
                        break

                # add a line consisting of those words
                line = ' '.join(line_words)
                lines.append(line.strip())

            # get the height of the text
            sizes = [font_zalm.size(line) for line in lines]
            total_height = sum(h for w, h in sizes)
            max_width = max(w for w, h in sizes)
            if total_height < self.s_height - 100 and max_width < self.s_width - 100:
                # vse se vejde
                break
            else:
                # zmensit pismo
                font_size = ceil(font_size * 0.9)
                if font_size < 50:
                    # mensi nez 50, nejde zobrazit
                    break

        y = (self.s_height - total_height) // 2

        # we'll render each line below the last, so we need to keep track of
        # the culmative height of the lines we've rendered so far
        y_offset = 0
        for line in lines:
            fw, fh = font_zalm.size(line)

            # (tx, ty) is the top-left of the font surface
            tx = x - fw / 2
            ty = y + y_offset

            font_surface = font_zalm.render(line, True, color)
            # print("render", line, tx, ty)
            self.screen.blit(font_surface, (tx, ty))

            y_offset += fh

    def handle_key(self, event):         
        #print("event", event)   
        if event.type == pygame.QUIT:
            return True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return True

            for i in range(0, 10):
                if event.key in [getattr(pygame, f'K_{i}'), getattr(pygame, f'K_KP{i}')]:
                    self.keynmr = (self.keynmr * 10 + i) % 1000
                    self.keypart = 0
                    self.set_number("%03d%02d" %
                                    (self.keynmr, self.keypart), True)
                    return False

            if event.key in [pygame.K_PLUS, pygame.K_KP_PLUS]:
                self.keypart = (self.keypart + 1) % 100
                self.set_number("%03d%02d" %
                                (self.keynmr, self.keypart), False)
                return False

            if event.key in [pygame.K_MINUS, pygame.K_KP_MINUS]:
                if self.keypart > 0:
                    self.keypart = (self.keypart - 1)
                self.set_number("%03d%02d" %
                                (self.keynmr, self.keypart), False)
                return False
        return False

    def set_power_state(self, state: bool, force=False):
        if state:
            if self.pwr_is_off or force:
                os.system("vcgencmd display_power 1")
                self.pwr_is_off = False
        else:
            if not self.pwr_is_off or force:
                os.system("vcgencmd display_power 0")
                self.pwr_is_off = True

    def run(self):
        # maximalni rozliseni na vystupu
        modes = pygame.display.list_modes()
        print(modes)
        mode = max(modes)
        mode = (1920, 1080) # DEBUG
        screen = pygame.display.set_mode(mode, pygame.DOUBLEBUF)
        
        #screen = pygame.display.set_mode(mode)
        self.screen = screen
        s_width, s_height = mode
        self.s_width = s_width
        self.s_height = s_height
        clock = pygame.time.Clock()

        # ukonceni klavesou escape
        done = False

        # definice pisem
        font = pygame.font.Font("fonts/DroidSerif/DroidSerif-Bold.ttf", 800)
        font_large = pygame.font.Font(
            "fonts/DroidSerif/DroidSerif-Bold.ttf", 800)  # 1100
        font2_small = pygame.font.Font(
            "fonts/DroidSerif/DroidSerif-Regular.ttf", 450)  # 400
        font2_large = pygame.font.Font(
            "fonts/DroidSerif/DroidSerif-Regular.ttf", 550)  # 500
        font3 = pygame.font.Font("fonts/DroidSerif/DroidSerif-Italic.ttf", 180)

        if self.is_slave:
            print("is slave")
            if self.last_slave_update + 120 < time.time():
                #print("do slave update")
                self.last_slave_update = time.time()
                self.slave_update()
                
        curr_state = False
        while not done:
            clock.tick(10) # 10 FPS
            if self.is_slave:
                if self.last_slave_update + 120 < time.time():
                    self.last_slave_update = time.time()
                    self.slave_update()
            
            for event in pygame.event.get():
                done = done or self.handle_key(event)

            if curr_state != self.get_status() or self.changed:
                #print(" --- redraw", self.changed)
                #start_time = time.time()
                curr_state = self.get_status()
                self.changed = False
                #print("Status time: ", time.time() - start_time , " s")

                if curr_state["nmr"]:  # neni vyply displej
                    self.disoff = None
                    self.set_power_state(True)

                    screen.fill(self.conf("background"))
                    if self.is_zalm():  # zalm

                        self.display_long_text(
                            self.get_zalm(), self.conf("number"))

                    elif not curr_state["file"] and not self.part:  # pouze cislo
                        text = font_large.render(f"{curr_state['nmr']:03d}", True, self.conf("number"))
                        
                        screen.blit(text, ((s_width - text.get_width()) //
                                    2, (s_height + 50 - text.get_height()) // 2))

                    else:  # vsechny informace
                        text = font.render(f"{curr_state['nmr']:03d}", True, self.conf("number"))
                        if curr_state["part"] < 10:
                            font2 = font2_large
                        else:
                            font2 = font2_small

                        text2 = font2.render(f"{curr_state['part']}", True, self.conf("part"))
                        
                        part_corr = font.get_descent() - font2.get_descent()

                        # pokud je zpevnik, posnuout dolu
                        bottom = s_height
                        if not curr_state["file"]:
                            bottom -= 50

                        corr1 = -text2.get_width() // 2
                        corr2 = text.get_width() // 2

                        if not curr_state["part"]:  # pokud eni cislo sloky, neni potreba posun
                            corr1 = 0

                        screen.blit(
                            text, (corr1 + (s_width - text.get_width()) // 2, bottom - text.get_height()))

                        if curr_state["part"]:  # cislo sloky
                            screen.blit(text2, (corr2 + (s_width - text2.get_width()) //
                                        2, bottom - text2.get_height() + part_corr))

                        if curr_state["file"]:  # zpevnik
                            text3 = font3.render(
                                curr_state["file"], True, self.conf("file"))
                            screen.blit(
                                text3, ((s_width - text3.get_width()) // 2, 110 - text3.get_height() // 2))

                else:  # displej je vyply
                    if not self.disoff:
                        self.disoff = time.time()

                    screen.fill(rgb("#000000"))
                #print("Draw time: ", time.time() - start_time , " s")
                pygame.display.update()  # update all
                pygame.event.pump()
                pygame.display.update()  # update all twice because two buffers?
                pygame.event.pump()
                pygame.display.update()  # update all twice because two buffers?
                pygame.event.pump()
               # pygame.display.update()  # update all
                #pygame.display.update()  # update all
                #print("Flip time: ", time.time() - start_time , " s")
                #pygame.time.delay(1000)
                #print("Delay time: ", time.time() - start_time , " s")

                self.notify() # poslat notifikaci o zmene
            if not curr_state["nmr"]:  # vyply displej bez ohledu na zmenu
                if not self.pwr_is_off and time.time() - self.disoff > self.offlimit:
                    self.set_power_state(False)
            if not self.pwr_is_off and time.time() - self.last_change > self.totlimit:
                self.set_power_state(False)

            

        self.set_power_state(True, force=True)

        pygame.quit()
        print("Display EXIT")
