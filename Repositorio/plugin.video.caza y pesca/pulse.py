# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Sourced From Online Templates And Guides
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#
# Thanks To: Google Search For This Template
# Modified: Pulse
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.caza y pesca'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

xbmc.executebuiltin('Container.SetViewMode(500)')

YOUTUBE_CHANNEL_ID_4 = "FLXOsDlyt9OZ-_16s4-B_Kqw"
YOUTUBE_CHANNEL_ID_5 = "PLD0FAFCDAD290F64A"
YOUTUBE_CHANNEL_ID_6 = "PLYrb5O7QbgD2F4cm_S7FhSFxnUAkWuk9y"
YOUTUBE_CHANNEL_ID_7 = "PLR0UFwDJjIpWSP9gA5ViG6pcG-cE5qMVI"
YOUTUBE_CHANNEL_ID_10 = "PLSYOVm2dLb6U666CVhsL_Lc02wi4pPcXS"
YOUTUBE_CHANNEL_ID_11 = "PLTJa_1DEgo8kMGEvIJGil1q1Ex7QbTvSf"
YOUTUBE_CHANNEL_ID_130 = "RDQMUx0d98dosI8"
YOUTUBE_CHANNEL_ID_133 = "LL3VnU-n_kDqhYNUi3ARahuw"
YOUTUBE_CHANNEL_ID_138 = "PLLtogDdWbh1fP1f2JiKprNUgfve3ac-B9"
YOUTUBE_CHANNEL_ID_139 = "PLLtogDdWbh1cLugSpGZTLaeCF17QFNXNC"
YOUTUBE_CHANNEL_ID_140 = "PL57hixRkd6kx2ra3yRD8pJosHlMrq3tnL"
YOUTUBE_CHANNEL_ID_141 = "LLWJ8ZjK7MPGKH9rBVjflGUw"
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
        title="Caza y Pesca Navarra",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_141+"/",
        thumbnail="https://i.imgur.com/NgAbRMJ.jpg",
        folder=True )
	
    plugintools.add_item( 
        #action="", 
        title="Lo mejor de la caza",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_140+"/",
        thumbnail="https://i.imgur.com/l0dfxAF.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Pesca Jara y Sedal",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_139+"/",
        thumbnail="https://i.imgur.com/ySFXZox.jpg",
        folder=True )
		
	
    plugintools.add_item( 
        #action="", 
        title="Caza Jara y Sedal",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_138+"/",
        thumbnail="https://i.imgur.com/ySFXZox.jpg",
        folder=True )
	

    plugintools.add_item( 
        #action="", 
        title="Producciones Villar",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_133+"/",
        thumbnail="https://i.imgur.com/cMuIhUj.jpg",
        folder=True )
	
    plugintools.add_item( 
        #action="", 
        title="Pesca Radical",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_130+"/",
        thumbnail="https://i.imgur.com/A4Qx7oZ.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="La Hora Cazavision",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://i.imgur.com/i5NJOYc.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Aimpoint",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://i.imgur.com/gulCPRC.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Hunters Video",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="https://i.imgur.com/UVKoCY4.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Pesca HD Black Bass",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_11+"/",
        thumbnail="https://i.imgur.com/otTNPHR.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Sedientos de Pesca",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://i.imgur.com/fundpkc.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Caza Natura",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="https://i.imgur.com/Qnttpbg.jpg",
        folder=True )
		
run()