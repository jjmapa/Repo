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

addonID = 'plugin.video.AprendiendoKodi'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "UCI38hnZ-iZelucTB5WRgBdA"
YOUTUBE_CHANNEL_ID_2 = "UCI38hnZ-iZelucTB5WRgBdA"
YOUTUBE_CHANNEL_ID_3 = "UCI38hnZ-iZelucTB5WRgBdA"
YOUTUBE_CHANNEL_ID_4 = "UCI38hnZ-iZelucTB5WRgBdA"
YOUTUBE_CHANNEL_ID_5 = "UCI38hnZ-iZelucTB5WRgBdA"
YOUTUBE_CHANNEL_ID_6 = "UCI38hnZ-iZelucTB5WRgBdA"
YOUTUBE_CHANNEL_ID_7 = "UCI38hnZ-iZelucTB5WRgBdA"

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
        title="                                                [COLOR gold]Bienvenidos a mi Canal.[/COLOR]",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://yt3.ggpht.com/-ThdkX6yZXmo/AAAAAAAAAAI/AAAAAAAAAAA/C9USGa6grqU/s288-mo-c-c0xffffffff-rj-k-no/photo.jpg",
		fanart="https://aprendiendokodi.files.wordpress.com/2017/12/splash-e1514301137957.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="                                  [COLOR gold]Kodi es más sencillo de lo que piensas[/COLOR]",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://yt3.ggpht.com/-ThdkX6yZXmo/AAAAAAAAAAI/AAAAAAAAAAA/C9USGa6grqU/s288-mo-c-c0xffffffff-rj-k-no/photo.jpg",
		fanart="https://aprendiendokodi.files.wordpress.com/2017/12/splash-e1514301137957.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="                                 [COLOR gold]Vamos a aprender a configurarlo desde 0[/COLOR]",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://yt3.ggpht.com/-ThdkX6yZXmo/AAAAAAAAAAI/AAAAAAAAAAA/C9USGa6grqU/s288-mo-c-c0xffffffff-rj-k-no/photo.jpg",
		fanart="https://aprendiendokodi.files.wordpress.com/2017/12/splash-e1514301137957.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="                                                 [COLOR gold]Disfruta de mi mundo.[/COLOR]",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://yt3.ggpht.com/-ThdkX6yZXmo/AAAAAAAAAAI/AAAAAAAAAAA/C9USGa6grqU/s288-mo-c-c0xffffffff-rj-k-no/photo.jpg",
		fanart="https://aprendiendokodi.files.wordpress.com/2017/12/splash-e1514301137957.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="                           [COLOR lime]No olvides suscribirte a mi Canal de You Tube[/COLOR]",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://yt3.ggpht.com/-ThdkX6yZXmo/AAAAAAAAAAI/AAAAAAAAAAA/C9USGa6grqU/s288-mo-c-c0xffffffff-rj-k-no/photo.jpg",
		fanart="https://aprendiendokodi.files.wordpress.com/2017/12/splash-e1514301137957.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="                                                    [COLOR gold]Entra y disfruta [/COLOR]",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="https://yt3.ggpht.com/-ThdkX6yZXmo/AAAAAAAAAAI/AAAAAAAAAAA/C9USGa6grqU/s288-mo-c-c0xffffffff-rj-k-no/photo.jpg",
		fanart="https://aprendiendokodi.files.wordpress.com/2017/12/splash-e1514301137957.png",
        folder=True ) 
		
    plugintools.add_item( 
        #action="", 
        title="                                              [COLOR red]##### ENTRAR #####[/COLOR]",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://yt3.ggpht.com/-ThdkX6yZXmo/AAAAAAAAAAI/AAAAAAAAAAA/C9USGa6grqU/s288-mo-c-c0xffffffff-rj-k-no/photo.jpg",
		fanart="https://aprendiendokodi.files.wordpress.com/2017/12/splash-e1514301137957.png",
        folder=True ) 
		
run()
