#!/usr/bin/env Python
import sys
import ast
import xbmc
import xbmcgui
import xbmcplugin
import xbmcaddon
import urllib2

addon_handle = int(sys.argv[1])

xbmcplugin.setContent(addon_handle, 'movies')
addon = xbmcaddon.Addon()
home = xbmc.translatePath(addon.getAddonInfo('path'))
iconPath = home + '\\' + 'icon.png'

response = urllib2.urlopen('https://lancer.streamup.com/api/channels/gakinotsukai/playlists')
playlist = ast.literal_eval(response.read())

hls = playlist['hls']

li = xbmcgui.ListItem('Gaki no Tsukai', iconImage=iconPath, thumbnailImage=iconPath)

xbmc.Player().play(hls,li)
