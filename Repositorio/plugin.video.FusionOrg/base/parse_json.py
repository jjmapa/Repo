import json
import xbmcplugin
import sys
import xbmcgui
import urllib
import xbmcaddon
import xbmc
import os

addon = xbmcaddon.Addon()
addon_dir = xbmc.translatePath(xbmc.translatePath(addon.getAddonInfo('Path')).decode('utf-8'))
addon_data_dir = xbmc.translatePath(xbmc.translatePath(addon.getAddonInfo('profile')).decode('utf-8'))
base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
xbmcplugin.setContent(addon_handle, 'tvshows')
default_poster = os.path.join(addon_dir, 'resources','media','default_poster_list.jpg')
default_fanart = os.path.join(addon_dir, 'resources','media','default_fan_list.jpg')

def addMenuitem(url, li, folder):
    return xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=folder)

def endMenu():
    xbmcplugin.endOfDirectory(addon_handle)
    
def build_url(query):
    return base_url + '?' + urllib.urlencode(query)

def read_json_file(data):
    items = json.loads(data)
 
    for item in items:
        if item['Folder'] == 'False':
            title = item['Titulo']
            url = item['Enlace']
            if item['Poster'] == '' or item['Poster'] == None:
                item['Poster'] = default_poster
            if item['Fondo'] == '' or item['Fondo'] == None:
                item['Fondo'] = default_fanart
            li = xbmcgui.ListItem(title, iconImage=item['Poster'], thumbnailImage=item['Fondo'])
            li.setInfo("video", {"Title": title, "FileName": title, "Plot": item['Sinopsis']})
            li.setProperty('IsPlayable', 'true')
            li.setProperty('fanart_image', item['Fondo'])
            addMenuitem(url, li, False)
        elif item['Folder'] == 'True':
            title = item['Titulo']
            if item['Poster'] == '' or item['Poster'] == None:
                item['Poster'] = default_poster
            if item['Fondo'] == '' or item['Fondo'] == None:
                item['Fondo'] = default_fanart
            url = build_url({'mode':'readjson', 'direccion': item['Enlace']})
            li = xbmcgui.ListItem(title, iconImage=item['Poster'], thumbnailImage=item['Fondo'])
            li.setInfo("video", {"Title": title, "FileName": title, "Plot": item['Sinopsis']})
            li.setProperty('fanart_image', item['Fondo'])
            addMenuitem(url, li, True)
    endMenu()
