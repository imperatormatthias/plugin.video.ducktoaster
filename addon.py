#!/usr/bin/env Python
import sys
import xbmc
import xbmcgui
import xbmcplugin
import xbmcaddon

addon_handle = int(sys.argv[1])

xbmcplugin.setContent(addon_handle, 'movies')
addon = xbmcaddon.Addon()
home = xbmc.translatePath(addon.getAddonInfo('path'))
iconPath = home + '\\' + 'icon.png'

url = 'https://video-cdn.streamup.com/app/gakinotsukai/chunklist.m3u8'
li = xbmcgui.ListItem('Gaki no Tsukai', iconImage=iconPath, thumbnailImage=iconPath)
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

xbmcplugin.endOfDirectory(addon_handle)
