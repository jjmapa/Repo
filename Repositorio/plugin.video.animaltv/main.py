'''
    Animal TV Add-on

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

from resources.lib import Addon, animaltv
import sys, os, urllib, urllib2
import json
import xbmc, xbmcgui, xbmcplugin, xbmcaddon

import re,urllib
from modules import client

def resolve(url):
    try:
        id = url.split("?v=")[-1].split("/")[-1].split("?")[0].split("&")[0]
        result = client.request('http://www.youtube.com/watch?v=%s' % id)

        message = client.parseDOM(result, 'div', attrs = {'id': 'unavailable-submessage'})
        message = ''.join(message)

        alert = client.parseDOM(result, 'div', attrs = {'id': 'watch7-notification-area'})

        if re.search('LIVE_WATCHING_NOW', result):
            url = live(result, id)
            if not url == None: return url

        if len(alert) > 0: raise Exception()
        if re.search('[a-zA-Z]', message): raise Exception()

        url = 'plugin://plugin.video.youtube/play/?video_id=%s' % id
        return url
    except:
        return


def live(result, id):
    try:
        hls = re.compile('"hls" *: *"(.+?)"').findall(result)
        if len(hls) == 0:
            url = 'https://www.youtube.com/watch?v=%s' % id
            url = 'http://translate.googleusercontent.com/translate_c?anno=2&hl=en&sl=mt&tl=en&u=%s' % url
            hls = client.request(url)
            hls = re.compile('"hls" *: *"(.+?)"').findall(hls)

        url = urllib.unquote(hls[0]).replace('\\/', '/')

        result = client.request(url)
        result = result.replace('\n','')
        url = re.compile('RESOLUTION *= *(\d*)x\d{1}.+?(http.+?\.m3u8)').findall(result)
        url = [(int(i[0]), i[1]) for i in url]
        url.sort()
        url = url[-1][1]
        return url
    except:
        return

addon = xbmcaddon.Addon()
addonname = addon.getAddonInfo('name')
addonid = addon.getAddonInfo('id')
plugin_path = xbmcaddon.Addon(id=addonid).getAddonInfo('path')

Addon.plugin_url = sys.argv[0]
Addon.plugin_handle = int(sys.argv[1])
Addon.plugin_queries = Addon.parse_query(sys.argv[2][1:])

dlg = xbmcgui.Dialog()

Addon.log('plugin url: ' + Addon.plugin_url)
Addon.log('plugin queries: ' + str(Addon.plugin_queries))
Addon.log('plugin handle: ' + str(Addon.plugin_handle)) 

addon_logo = xbmc.translatePath(os.path.join(plugin_path,'tvaddons_logo.png'))

mode = Addon.plugin_queries['mode']

if mode == 'main':
    try:
        channels = animaltv.AnimalTV().get_channels()
        if channels:
            for c in channels:
                channel = c['channel'];
                id = c['id'];
                img = c['img']
                rURL = "plugin://plugin.video.animaltv/?id=" + id + "&channel=" + channel + "&mode=play&rand=" + Addon.random_generator()
                cm_refresh = (Addon.get_string(6000), 'XBMC.RunPlugin(%s/?mode=refresh)' % (Addon.plugin_url))
                cm_menu = [cm_refresh]
           
                Addon.add_video_item(rURL,{'title': channel}, img=img, playable=True, cm=cm_menu, cm_replace=True)
        if len(Addon.get_setting('notify')) > 0:
            Addon.set_setting('notify', str(int(Addon.get_setting('notify')) + 1))  
        else:
            Addon.set_setting('notify', "1")        
        if int(Addon.get_setting('notify')) == 1:
            xbmcgui.Dialog().notification(addonname + ' is provided by:','www.tvaddons.ag',addon_logo,5000,False)
        elif int(Addon.get_setting('notify')) == 9:
            Addon.set_setting('notify', "0")
    except:
        dlg.ok(Addon.get_string(5000), Addon.get_string(8000))
        exit()

elif mode == 'refresh':
    xbmc.executebuiltin('Container.Refresh')

elif mode == 'play':
    id = Addon.plugin_queries['id']
    channel = Addon.plugin_queries['channel']
    stream_status = animaltv.AnimalTV()._get_json('/status_json.php', {'id': id})['status']
    if stream_status == 'live':
        url = "https://www.youtube.com/watch?v=" + id
        stream_url = resolve(url)
        item = xbmcgui.ListItem(path=stream_url)
        xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)
    else:
        dlg.ok(Addon.get_string(5000), channel + " " + Addon.get_string(7000))
        exit()

Addon.end_of_directory()
