# -*- coding: utf-8 -*-
import xbmcaddon
import xbmc

from datetime import datetime
import time

from resources.lib.iptvsc import generate_epg

tz_offset = int((time.mktime(datetime.now().timetuple())-time.mktime(datetime.utcnow().timetuple()))/3600)
addon = xbmcaddon.Addon()

time.sleep(60)
if not addon.getSetting('epg_interval'):
    interval = 12*60*60
else:
    interval = int(addon.getSetting('epg_interval'))*60*60
next = time.time() + 10

while not xbmc.Monitor().abortRequested():
    if xbmc.Monitor().waitForAbort(3):
        break
    if(next < time.time()):
        time.sleep(3)
        if addon.getSetting('username') and len(addon.getSetting('username')) > 0 and addon.getSetting('password') and len(addon.getSetting('password')) > 0:
            if addon.getSetting('autogen') == 'true':
                generate_epg(show_progress = False)
        if not addon.getSetting('epg_interval'):
            interval = 12*60*60
        else:
            interval = int(addon.getSetting('epg_interval'))*60*60      
        next = time.time() + float(interval)
    time.sleep(1)
addon = None