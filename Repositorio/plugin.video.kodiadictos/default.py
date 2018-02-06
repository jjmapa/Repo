# -*- coding: utf-8 -*-
#------------------------------------------------------------
#Catoal Kodi Addon
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.kodiadictos'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "UCtl25ZDcy1u9BD7F_6GpVNA"
YOUTUBE_CHANNEL_ID_2 = "UCtl25ZDcy1u9BD7F_6GpVNA"
YOUTUBE_CHANNEL_ID_3 = "UCtl25ZDcy1u9BD7F_6GpVNA"
YOUTUBE_CHANNEL_ID_4 = "UCtl25ZDcy1u9BD7F_6GpVNA"
YOUTUBE_CHANNEL_ID_5 = "UCtl25ZDcy1u9BD7F_6GpVNA"
YOUTUBE_CHANNEL_ID_6 = "UCtl25ZDcy1u9BD7F_6GpVNA"
YOUTUBE_CHANNEL_ID_7 = "UCtl25ZDcy1u9BD7F_6GpVNA"

# Entry point
def run():
    plugintools.log("docu.run")
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("docu.main_list "+repr(params))

    plugintools.add_item( 
        #action="", 
        title="                                           [B]Bienvenidos a mi Addon.[/B]",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://yt3.ggpht.com/-HogW-BE-XOs/AAAAAAAAAAI/AAAAAAAAAAA/V9zLyItNyCA/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
		fanart="https://i.ytimg.com/vi/CKsN2VoBPy4/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="                                  [B]Entra en el mundo de los Tuturiales[/B]",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://yt3.ggpht.com/-HogW-BE-XOs/AAAAAAAAAAI/AAAAAAAAAAA/V9zLyItNyCA/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
		fanart="https://i.ytimg.com/vi/CKsN2VoBPy4/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="                                [B]Disfruta de mis Tutoriales. Buscamos[/B]",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://yt3.ggpht.com/-HogW-BE-XOs/AAAAAAAAAAI/AAAAAAAAAAA/V9zLyItNyCA/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
		fanart="https://i.ytimg.com/vi/CKsN2VoBPy4/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="                                [B]lo nuevo de Kodi y lo traemos al canal.[/B]",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://yt3.ggpht.com/-HogW-BE-XOs/AAAAAAAAAAI/AAAAAAAAAAA/V9zLyItNyCA/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
		fanart="https://i.ytimg.com/vi/CKsN2VoBPy4/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="                           [COLOR red]No olvides suscribirte a mi Canal de You Tube[/COLOR]",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://yt3.ggpht.com/-HogW-BE-XOs/AAAAAAAAAAI/AAAAAAAAAAA/V9zLyItNyCA/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
		fanart="https://i.ytimg.com/vi/CKsN2VoBPy4/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="                                            [B]Preparate para disfrutar[/B]",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="https://yt3.ggpht.com/-HogW-BE-XOs/AAAAAAAAAAI/AAAAAAAAAAA/V9zLyItNyCA/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
		fanart="https://i.ytimg.com/vi/CKsN2VoBPy4/hqdefault.jpg",
        folder=True ) 
		
    plugintools.add_item( 
        #action="", 
        title="                                               [COLOR lime]***** PINCHA AQUI *****[/COLOR]",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://yt3.ggpht.com/-HogW-BE-XOs/AAAAAAAAAAI/AAAAAAAAAAA/V9zLyItNyCA/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
		fanart="https://i.ytimg.com/vi/CKsN2VoBPy4/hqdefault.jpg",
        folder=True ) 
		
run()
