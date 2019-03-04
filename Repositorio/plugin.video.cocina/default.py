# -*- coding: utf-8 -*-
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.cocina'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')
fanart = local.getAddonInfo('fanart')


YOUTUBE_CHANNEL_ID1 = "UCXMrqL3QHKQP6Q-iObZjrXA"
YOUTUBE_CHANNEL_ID2 = "CanalCocina"
YOUTUBE_CHANNEL_ID3 = "UCjKISfZVA-BPQtT45gk-c2w"
YOUTUBE_CHANNEL_ID4 = "UCQtVEU1LEtZDj8aLi6Lkw2A"
YOUTUBE_CHANNEL_ID5 = "UCuXVuYLaRma-GfiEVzEmrOw"
YOUTUBE_CHANNEL_ID6 = "UCpMXMR99Qd11oF7_XhbeM1w"
YOUTUBE_CHANNEL_ID7 = "UCb4_NZsY18tESzn-JcLUFWw"
YOUTUBE_CHANNEL_ID8 = "CocinaSabor"
YOUTUBE_CHANNEL_ID9 = "elcocinerofiel"
YOUTUBE_CHANNEL_ID10 = "Recetasparatucocina"
YOUTUBE_CHANNEL_ID11 = "UCkO-_6f9MWRBm7BaNSmtOcA"
YOUTUBE_CHANNEL_ID12 = "UCVf-uzV0XR-3DLtRs1sg6Og"
YOUTUBE_CHANNEL_ID14 = "lasrecetasdemj"
YOUTUBE_CHANNEL_ID15 = "RecetaFacil"
YOUTUBE_CHANNEL_ID16 = "LasRecetasDePepa"


# Entry point
def run():
    plugintools.log("cocina.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        pass
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("cocina.main_list "+repr(params))

    plugintools.add_item( 
        #action="", 
        title="[COLOR white]ALBERTO CHICOTE[/COLOR]",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID6+"/",
        thumbnail="https://yt3.ggpht.com/-ttx61-5ZHTY/AAAAAAAAAAI/AAAAAAAAAAA/GKjzWrkiFsA/s288-mo-c-c0xffffffff-rj-k-no/photo.jpg",
        fanart=fanart,
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR white]ANNA RECETAS FACILES[/COLOR]",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID12+"/",
        thumbnail="https://yt3.ggpht.com/-eRU6yx5yIL8/AAAAAAAAAAI/AAAAAAAAAAA/cJ_171k5skw/s288-mo-c-c0xffffffff-rj-k-no/photo.jpg",
        fanart=fanart,
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR white]CANAL COCINA[/COLOR]",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID2+"/",
        thumbnail="https://yt3.ggpht.com/-V-00YQE5U4k/AAAAAAAAAAI/AAAAAAAAAAA/RWMkolRg0Y0/s288-mo-c-c0xffffffff-rj-k-no/photo.jpg",
        fanart=fanart,
        folder=True )   

    plugintools.add_item( 
        #action="", 
        title="[COLOR white]COCINA FAMILIAR[/COLOR]",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID1+"/",
        thumbnail="https://yt3.ggpht.com/-d1Wu4NEKLSM/AAAAAAAAAAI/AAAAAAAAAAA/syFK4wvJZVo/s288-mo-c-c0xffffffff-rj-k-no/photo.jpg",
        fanart=fanart,
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR white]COCINA SABOR[/COLOR]",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID8+"/",
        thumbnail="https://yt3.ggpht.com/-rjENtaNAQoo/AAAAAAAAAAI/AAAAAAAAAAA/8xEGqJlxwoQ/s288-mo-c-c0xffffffff-rj-k-no/photo.jpg",
        fanart=fanart,
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR white]COCINAR PARA LOS AMIGOS[/COLOR]",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID11+"/",
        thumbnail="https://yt3.ggpht.com/-SG5UVvY7c88/AAAAAAAAAAI/AAAAAAAAAAA/hyYBphSOKZM/s288-mo-c-c0xffffffff-rj-k-no/photo.jpg",
        fanart=fanart,
        folder=True )
	
    plugintools.add_item( 
        #action="", 
        title="[COLOR white]EL COCINERO FIEL[/COLOR]",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID9+"/",
        thumbnail="https://yt3.ggpht.com/-w8PCIk2-V1k/AAAAAAAAAAI/AAAAAAAAAAA/5NC-K8MUq64/s288-mo-c-c0xffffffff-rj-k-no/photo.jpg",
        fanart=fanart,
        folder=True )
       
    plugintools.add_item( 
        #action="", 
        title="[COLOR white]HOGAR MANIA[/COLOR]",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID7+"/",
        thumbnail="https://yt3.ggpht.com/-D11koLRL1CU/AAAAAAAAAAI/AAAAAAAAAAA/VoMXNimtDCQ/s288-mo-c-c0xffffffff-rj-k-no/photo.jpg",
        fanart=fanart,
        folder=True )
    
    plugintools.add_item( 
        #action="", 
        title="[COLOR white]KWAN HOMSAI[/COLOR]",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID5+"/",
        thumbnail="https://yt3.ggpht.com/-MtXf6Qmca2c/AAAAAAAAAAI/AAAAAAAAAAA/0wcdqtia8Zg/s288-mo-c-c0xffffffff-rj-k-no/photo.jpg",
        fanart=fanart,
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR white]LAS RECETAS DE MJ[/COLOR]",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID14+"/",
        thumbnail="https://yt3.ggpht.com/-z-9i3NZZgDo/AAAAAAAAAAI/AAAAAAAAAAA/v_7VvPqXt20/s288-mo-c-c0xffffffff-rj-k-no/photo.jpg",
        fanart=fanart,
        folder=True )


    plugintools.add_item( 
        #action="", 
        title="[COLOR white]LAS RECETAS DE PEPA[/COLOR]",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID16+"/",
        thumbnail="https://yt3.ggpht.com/-LqzyCHkJD0E/AAAAAAAAAAI/AAAAAAAAAAA/gMnkMCht2aY/s288-mo-c-c0xffffffff-rj-k-no/photo.jpg",
        fanart=fanart,
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR white]ROBIN FOOD[/COLOR]",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID3+"/",
        thumbnail="https://yt3.ggpht.com/-Pe1b5jLFJjc/AAAAAAAAAAI/AAAAAAAAAAA/6ROzojFangA/s288-mo-c-c0xffffffff-rj-k-no/photo.jpg",
        fanart=fanart,
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR white]QUE VIVA LA COCINA[/COLOR]",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID10+"/",
        thumbnail="https://yt3.ggpht.com/-2zRl5PPXeR8/AAAAAAAAAAI/AAAAAAAAAAA/cRFLrP5K-Kc/s288-mo-c-c0xffffffff-rj-k-no/photo.jpg",
        fanart=fanart,
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR white]RTVE COCINA[/COLOR]",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID4+"/",
        thumbnail="https://yt3.ggpht.com/-VW2gsVnGE0w/AAAAAAAAAAI/AAAAAAAAAAA/g7zFgkj3d9g/s288-mo-c-c0xffffffff-rj-k-no/photo.jpg",
        fanart=fanart,
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR white]VICKY RECETA FACIL[/COLOR]",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID15+"/",
        thumbnail="https://yt3.ggpht.com/-WhefNnuwJw8/AAAAAAAAAAI/AAAAAAAAAAA/159e_4Z5Gwk/s288-mo-c-c0xffffffff-rj-k-no/photo.jpg",
        fanart=fanart,
        folder=True )     

   

run()
