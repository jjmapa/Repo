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

addonID = 'plugin.video.Orchestra'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

xbmc.executebuiltin('Container.SetViewMode(500)')

YOUTUBE_CHANNEL_ID_3 = "PLoFFBa2_rK4Raab4obNXsRvrSVb4fnngf"
YOUTUBE_CHANNEL_ID_4 = "PL-0V4YhqTz2CPRP6oztF-eMWYmSVRTPCu"
YOUTUBE_CHANNEL_ID_5 = "PLAwhk8ZgpJdNf_zcwuX__T285d_uhHSnD"
YOUTUBE_CHANNEL_ID_6 = "PLRYhYjaYNiltoudRxjRg--8_NKMdTIqty"
YOUTUBE_CHANNEL_ID_7 = "PL55419FAEED3342BD"
YOUTUBE_CHANNEL_ID_10 = "PLK3sGd6kNVwrbNUzZYrgpAsWHvSjdiQAW"
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
        title="Como tocar la bateria desde cero",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://i.imgur.com/EqVc7FC.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Como tocar la flauta dulce desde cero",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://i.imgur.com/DAUBsx2.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Como tocar la guitarra acustica desde cero",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="https://i.imgur.com/HkE3eDb.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Como tocar la guitarra electrica desde cero",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://i.imgur.com/5wtDYbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Como tocar el piano desde cero",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="https://i.imgur.com/tpgpygr.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Como tocar el violin desde cero",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://i.imgur.com/ctetWWG.jpg",
        folder=True )

run()