import xbmcplugin
import re
import urllib
import xbmcgui
import sys
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
xml_regex_title = xml_regex = '<title>(.*?)</title>'
xml_regex_url = xml_regex = '<link>(.*?)</link>'
xml_regex_thumbnail = xml_regex = '<thumbnail>(.*?)</thumbnail>'
xml_regex_external = xml_regex = '<externallink>(.*?)</externallink>'
xml_regex_folder = xml_regex = '<title>(.*?)</title>\s*<externallink>(.*?)</externallink>\s*<thumbnail>(.*?)</thumbnail>'
xml_items = '<item>(.*?)</item>'

def addMenuitem(url, li, folder):
    return xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=folder)

def endMenu():
    xbmcplugin.endOfDirectory(addon_handle)
    
def build_url(query):
    return base_url + '?' + urllib.urlencode(query)

def read_xml_file(data):
    data = data.replace('\n','').replace('\t','').replace('  ','')
    matches = re.findall(xml_items,data)
    for match in matches:
        if 'externallink' in match:
            title = re.findall(xml_regex_title,match)[0]
            url = re.findall(xml_regex_external,match)[0]
            thumbnail = re.findall(xml_regex_thumbnail,match)[0]
            if 'http' in url:
                url = build_url({'mode':'read_url_list', 'link': url})
            else:
                url = build_url({'mode':'read_local_list', 'link': url})
            if thumbnail == '' or thumbnail == None:
                thumbnail = default_poster
            li = xbmcgui.ListItem(title, iconImage=thumbnail, thumbnailImage=thumbnail)
            li.setInfo("video", {"Title": title, "FileName": title, "Plot": title})
            li.setProperty('fanart_image', default_fanart)
            addMenuitem(url, li, True)
        elif 'link' in match:
            title = re.findall(xml_regex_title,match)[0]
            url = re.findall(xml_regex_url,match)[0]
            thumbnail = re.findall(xml_regex_thumbnail,match)[0]
            if thumbnail == '' or thumbnail == None:
                thumbnail = default_poster
            li = xbmcgui.ListItem(title, iconImage=thumbnail, thumbnailImage=thumbnail)
            li.setInfo("video", {"Title": title, "FileName": title, "Plot": title})
            li.setProperty('IsPlayable', 'true')
            li.setProperty('fanart_image', default_fanart)
            addMenuitem(url, li, False)
    endMenu()

 