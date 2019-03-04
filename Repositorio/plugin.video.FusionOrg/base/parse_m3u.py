import json
import xbmcplugin
import sys
import xbmcgui
import re
import urllib
import xbmcaddon
import xbmc
import os

base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
xbmcplugin.setContent(addon_handle, 'tvshows')
addon = xbmcaddon.Addon()
addon_dir = xbmc.translatePath(xbmc.translatePath(addon.getAddonInfo('Path')).decode('utf-8'))
addon_data_dir = xbmc.translatePath(xbmc.translatePath(addon.getAddonInfo('profile')).decode('utf-8'))
default_poster = os.path.join(addon_dir, 'resources','media','default_poster_list.jpg')
default_fanart = os.path.join(addon_dir, 'resources','media','default_fan_list.jpg')

def addMenuitem(url, li, folder):
    return xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=folder)

def endMenu():
    xbmcplugin.endOfDirectory(addon_handle)
    
def build_url(query):
    return base_url + '?' + urllib.urlencode(query)

def read_m3u_file(data):
    content = data.rstrip()
    match = re.compile(r'#EXTINF:(.+?),(.*?)[\n\r]+([^\r\n]+)').findall(content)
    total = len(match)

    for other,title,url in match:
        if  'group-title' in other:
            m = re.search('group-title=[\'"](.*?)[\'"]', other)
            if m != None:
                matchgt = m.group(1)
            else:
                matchgt = ''
            sinopsis = matchgt
        else:
            sinopsis = ''
            
        if 'tvg-logo' in other:
            m = re.search('tvg-logo=[\'"](.*?)[\'"]', other)
            if m != None:
                matchtl = m.group(1)
            else:
                matchtl = default_poster
            thumbnail = matchtl            

            if thumbnail:
                thumbnail = thumbnail
                
                    
        else:
            thumbnail = default_poster
        
        li = xbmcgui.ListItem(title, iconImage=thumbnail, thumbnailImage=thumbnail)
        li.setInfo("video", {"Title": title, "FileName": title, "Plot": sinopsis})
        li.setProperty('fanart_image', default_fanart)
        if ('youtube.com/user/' in url) or ('youtube.com/channel/' in url) or ('youtube/user/' in url) or ('youtube/channel/' in url):
            url = 'plugin://plugin.video.youtube/%s/%s/' % (url.split( '/' )[-2], url.split( '/' )[-1])
            li.setProperty('IsPlayable', 'false')
            addMenuitem(url, li, True)
        else:
            li.setProperty('IsPlayable', 'true')
            addMenuitem(url, li, False)
    endMenu()
