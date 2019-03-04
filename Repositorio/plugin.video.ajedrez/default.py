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

addonID = 'plugin.video.ajedrez'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')
fanart = local.getAddonInfo('fanart')


YOUTUBE_CHANNEL_ID1 = "ChessFM"
YOUTUBE_CHANNEL_ID2 = "UC2_vIPPZtRtu5I9bfS62GQw"
YOUTUBE_CHANNEL_ID3 = "ClasesAjedrez"
YOUTUBE_CHANNEL_ID4 = "luisfsiles"
YOUTUBE_CHANNEL_ID5 = "mikerahal"
YOUTUBE_CHANNEL_ID6 = "UCKGR-mRvc0U3lS27SC9pemQ"
YOUTUBE_CHANNEL_ID7 = "Reydama"
YOUTUBE_CHANNEL_ID8 = "PLV4hXa725NQJJwowUWm27snEJbnH1ORyk"
YOUTUBE_CHANNEL_ID9 = "PL5916C65F96DE8B29"
YOUTUBE_CHANNEL_ID10 = "PLA07871F115404B1C"
YOUTUBE_CHANNEL_ID11 = "PL172A0CE5BABDF843"
YOUTUBE_CHANNEL_ID12 = "PLFE387E4D02266429"
YOUTUBE_CHANNEL_ID13 = "PLV4hXa725NQLyo012qXx1U7Cpk6_pWiLH"
YOUTUBE_CHANNEL_ID14 = "PLV4hXa725NQLqO6PGpfx_K1FDl_dXAqJg"
YOUTUBE_CHANNEL_ID15 = "PLV4hXa725NQJb1FZ9tm4LbmOrSD0XbEen"
YOUTUBE_CHANNEL_ID16 = "PL0jWOfkzaPFodBr2HbsVpXsatoeVj_mS1"



# Entry point
def run():
    plugintools.log("ajedrez.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        pass
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("ajedrez.main_list "+repr(params))

    plugintools.add_item( 
        #action="", 
        title="[COLOR white]CHESS FM[/COLOR]",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID1+"/",
        thumbnail="https://yt3.ggpht.com/-lNr9e3kFuPg/AAAAAAAAAAI/AAAAAAAAAAA/gDKYDdqxzm8/s288-mo-c-c0xffffffff-rj-k-no/photo.jpg",
        fanart=fanart,
        folder=True )
    
    plugintools.add_item( 
        #action="", 
        title="[COLOR white]CIRCULO DE AJEDREZ CAPABLANCA[/COLOR]",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID2+"/",
        thumbnail="https://yt3.ggpht.com/-DZrXXZri1GY/AAAAAAAAAAI/AAAAAAAAAAA/q7Z2TnYrq2Y/s288-mo-c-c0xffffffff-rj-k-no/photo.jpg",
        fanart=fanart,
        folder=True )
    
    plugintools.add_item( 
        #action="", 
        title="[COLOR white]ICHESS[/COLOR]",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID3+"/",
        thumbnail="https://yt3.ggpht.com/-P9hsqiSlrd0/AAAAAAAAAAI/AAAAAAAAAAA/hGJ8NfYblJY/s288-mo-c-c0xffffffff-rj-k-no/photo.jpg",
        fanart=fanart,
        folder=True )   

    plugintools.add_item( 
        #action="", 
        title="[COLOR white]LUIS FERNANDEZ SILES[/COLOR]",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID4+"/",
        thumbnail="https://yt3.ggpht.com/-mrrspwDMn2k/AAAAAAAAAAI/AAAAAAAAAAA/5nfafuYHf9k/s288-mo-c-c0xffffffff-rj-k-no/photo.jpg",
        fanart=fanart,
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR white]MICHAEL RAHAL[/COLOR]",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID5+"/",
        thumbnail="https://yt3.ggpht.com/-VGjuaQf42q8/AAAAAAAAAAI/AAAAAAAAAAA/XA-bG6dUWVw/s288-mo-c-c0xffffffff-rj-k-no/photo.jpg",
        fanart=fanart,
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR white]PARTIDAS INMORTALES DE AJEDREZ[/COLOR]",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID6+"/",
        thumbnail="https://yt3.ggpht.com/a-/AN66SAwDs6JCu3JZiv2QH2lC-aZpDVeSVZmy7Cmaaw=s288-mo-c-c0xffffffff-rj-k-no",
        fanart=fanart,
        folder=True )
   
    plugintools.add_item( 
        #action="", 
        title="[COLOR white]REYDAMA[/COLOR]",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID7+"/",
        thumbnail="https://yt3.ggpht.com/a-/AN66SAwCO18PcX1CE9J_QGfwonIokfVRsAjzQAMgPQ=s288-mo-c-c0xffffffff-rj-k-no",
        fanart=fanart,
        folder=True )
    
    plugintools.add_item( 
        #action="", 
        title="[COLOR white]LA HISTORIA DEL AJEDREZ[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID8+"/",
        thumbnail="https://i.imgur.com/ZDf4p4a.jpg",
        fanart=fanart,
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR white]PARTIDAS MEMORABLES[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID9+"/",
        thumbnail="https://i.imgur.com/Cx0xj50.jpg",
        fanart=fanart,
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR white]TEORIA DE APERTURAS E INTRODUCCIONES[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID10+"/",
        thumbnail="https://i.imgur.com/p6eXgfn.jpg",
        fanart=fanart,
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR white]COMPOSICIONES Y PROBLEMAS[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID11+"/",
        thumbnail="https://i.imgur.com/y2ltVdO.jpg",
        fanart=fanart,
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR white]TRAMPAS[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID12+"/",
        thumbnail="https://i.imgur.com/xs7dHX6.jpg",
        fanart=fanart,
        folder=True )
    
    plugintools.add_item( 
        #action="", 
        title="[COLOR white]PARTIDAS MAGISTRALES DE AJEDREZ[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID13+"/",
        thumbnail="https://i.imgur.com/cjPdy1s.jpg",
        fanart=fanart,
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR white]LOS 100 PATRONES QUE HAY QUE SABER EN AJEDREZ[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID14+"/",
        thumbnail="https://i.imgur.com/6AQ7x3R.jpg",
        fanart=fanart,
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR white]LOS 7 ERRORES DE CALCULO EN AJEDREZ[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID15+"/",
        thumbnail="https://i.imgur.com/FedOnbH.jpg",
        fanart=fanart,
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR white]AJEDREZ PARA NIÑOS[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID16+"/",
        thumbnail="https://i.imgur.com/xOsnL9r.jpg",
        fanart=fanart,
        folder=True )



run()
