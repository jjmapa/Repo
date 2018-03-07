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

addonID = 'plugin.video.FamilyCooking'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

xbmc.executebuiltin('Container.SetViewMode(500)')

YOUTUBE_CHANNEL_ID_1 = "PLKii0u4OeI1xbhCIjOekM1B31o2rqbeTg"
YOUTUBE_CHANNEL_ID_2 = "PLKii0u4OeI1zW_mQTHM41zLX75S6VBt_w"
YOUTUBE_CHANNEL_ID_3 = "PLKii0u4OeI1x2gKayHhnsTb1llk-Ew7A5"
YOUTUBE_CHANNEL_ID_4 = "PLKii0u4OeI1wNZBrCi0oHe6zP4M7t25bO"
YOUTUBE_CHANNEL_ID_5 = "PLKii0u4OeI1wv2eNCr0XGQoiZHKSEzxcl"
YOUTUBE_CHANNEL_ID_6 = "PLKii0u4OeI1xnYfbLAS2WomEfhNQ9eOdK"
YOUTUBE_CHANNEL_ID_7 = "PLKii0u4OeI1xzKS946G8CfOiL8X8NCVMY"
YOUTUBE_CHANNEL_ID_8 = "PLKii0u4OeI1yIXrqiJuRNoYqJ6YeDvkIP"
YOUTUBE_CHANNEL_ID_9 = "PLKii0u4OeI1yJGwF0hF0mhiR0IpsYXMRh"
YOUTUBE_CHANNEL_ID_10 = "PLKii0u4OeI1xUZn7kOplo0CI_Y4fPRMRy"
YOUTUBE_CHANNEL_ID_11 = "PLKii0u4OeI1zDK3jlPdL4dUH6uY79EmIy"
YOUTUBE_CHANNEL_ID_12 = "PLKii0u4OeI1w2iRXlI5dYPVLP_EtAkocS"
YOUTUBE_CHANNEL_ID_13 = "PLKii0u4OeI1wgX-D-7u9ZbJV-F5w1T9op" 
YOUTUBE_CHANNEL_ID_14 = "PLKii0u4OeI1xbI8ZlWmYsi_lg-kINf0P0" 
YOUTUBE_CHANNEL_ID_15 = "PLKii0u4OeI1z__rY4UIKbvxVylRTUV9A-"
YOUTUBE_CHANNEL_ID_16 = "PLKii0u4OeI1w9TkI7NrnTuFFu9tP475WQ"
YOUTUBE_CHANNEL_ID_17 = "PLKii0u4OeI1wyFvzDvvqpdM1L-Xb5LaKa" 
YOUTUBE_CHANNEL_ID_18 = "PLKii0u4OeI1xnD2khqiX5CIiTxVwr22RK"
YOUTUBE_CHANNEL_ID_19 = "PLKii0u4OeI1xVlrjUsBUK820gMfXRpkIK"
YOUTUBE_CHANNEL_ID_20 = "PLKii0u4OeI1ydw2w_D1oWsuxgNZJTPQJ-" 
YOUTUBE_CHANNEL_ID_21 = "PLKii0u4OeI1xVILS9D_20VMDH96VtGqnu"
YOUTUBE_CHANNEL_ID_22 = "PLKii0u4OeI1xxeUlt7aiNKvSfcgPUTV3u"
YOUTUBE_CHANNEL_ID_23 = "PLKii0u4OeI1zapzf081QH5Tp1lGlDNRiv" 
YOUTUBE_CHANNEL_ID_24 = "PLKii0u4OeI1zW980L0OpWufmW6-azpOat"
YOUTUBE_CHANNEL_ID_25 = "PLKii0u4OeI1wBqLlqj62imclmpJU5ovcm"
YOUTUBE_CHANNEL_ID_26 = "PLKii0u4OeI1zus2SFxdLVosVLKn38KbqJ"
YOUTUBE_CHANNEL_ID_27 = "PLKii0u4OeI1xoMBSaBD2r5SlOSMl_8sTc" 
YOUTUBE_CHANNEL_ID_28 = "PLKii0u4OeI1z3MCz6F9cqdT_xure8QDnw"
YOUTUBE_CHANNEL_ID_29 = "PLKii0u4OeI1yO0bD0QmSFquzF1oULcK0i"
YOUTUBE_CHANNEL_ID_30 = "LLiQmHWjVLBAZ_k26DGQ2Zgg"
YOUTUBE_CHANNEL_ID_130 = "PLKii0u4OeI1zHagAKyc84cm-JDGn6Wuov"
YOUTUBE_CHANNEL_ID_133 = "PLKii0u4OeI1z4VaJ9ajH3YyruxwcOMjm3"
YOUTUBE_CHANNEL_ID_138 = "PLKii0u4OeI1xUzqGPYbC1q2PY-g-Swc2-"
YOUTUBE_CHANNEL_ID_139 = "PLKii0u4OeI1wm4WevcDPWuR7ALrUGhPk1"
YOUTUBE_CHANNEL_ID_140 = "PLKii0u4OeI1zEL9ePV8hSyNW5KOA7Q93s"
YOUTUBE_CHANNEL_ID_141 = "PLKii0u4OeI1zfSaNKnFpIxiRczwL1sxRA"
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
        title="recetas fit",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_141+"/",
        thumbnail="https://i.imgur.com/S1iwTas.jpg",
        folder=True )
	
    plugintools.add_item( 
        #action="", 
        title="dieta entulinea",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_140+"/",
        thumbnail="https://i.imgur.com/S1iwTas.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="empresas colaboradoras",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_139+"/",
        thumbnail="https://i.imgur.com/S1iwTas.jpg",
        folder=True )
		
	
    plugintools.add_item( 
        #action="", 
        title="panificadora",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_138+"/",
        thumbnail="https://i.imgur.com/S1iwTas.jpg",
        folder=True )
	

    plugintools.add_item( 
        #action="", 
        title="compras aldi",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_133+"/",
        thumbnail="https://i.imgur.com/S1iwTas.jpg",
        folder=True )
	
    plugintools.add_item( 
        #action="", 
        title="compras lidl",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_130+"/",
        thumbnail="https://i.imgur.com/S1iwTas.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Proyectos Bopki",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://i.imgur.com/S1iwTas.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="presentación de productos",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://i.imgur.com/S1iwTas.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="guarrindongadas",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="https://i.imgur.com/S1iwTas.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="mincidelice/dieta proteica",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_11+"/",
        thumbnail="https://i.imgur.com/S1iwTas.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="mycook",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://i.imgur.com/S1iwTas.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="compras dia",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="https://i.imgur.com/S1iwTas.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="compras aliexpres",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://i.imgur.com/S1iwTas.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="bomann",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_15+"/",
        thumbnail="https://i.imgur.com/S1iwTas.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="pan",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_12+"/",
        thumbnail="https://i.imgur.com/S1iwTas.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="postres sin azúcar",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://i.imgur.com/S1iwTas.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="cecofry",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://i.imgur.com/S1iwTas.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="postres fáciles",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_14+"/",
        thumbnail="https://i.imgur.com/S1iwTas.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="compras primor",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="https://i.imgur.com/S1iwTas.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="compras puntuadas",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_13+"/",
        thumbnail="https://i.imgur.com/S1iwTas.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="compras mercadona",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="https://i.imgur.com/S1iwTas.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="recetas navipeich",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_16+"/",
        thumbnail="https://i.imgur.com/S1iwTas.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="gm e",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_17+"/",
        thumbnail="https://i.imgur.com/S1iwTas.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="xavier barriga",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_18+"/",
        thumbnail="https://i.imgur.com/S1iwTas.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="recetas tradicionales catalanas",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_19+"/",
        thumbnail="https://i.imgur.com/S1iwTas.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="sorteo",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_20+"/",
        thumbnail="https://i.imgur.com/S1iwTas.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="compras spar",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_21+"/",
        thumbnail="https://i.imgur.com/S1iwTas.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="recetas de mi madre",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_22+"/",
        thumbnail="https://i.imgur.com/S1iwTas.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="tefal multidelice",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_23+"/",
        thumbnail="https://i.imgur.com/S1iwTas.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="tiendas con descuentos",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_24+"/",
        thumbnail="https://i.imgur.com/S1iwTas.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="haul",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_25+"/",
        thumbnail="https://i.imgur.com/S1iwTas.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="sin gluten",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_26+"/",
        thumbnail="https://i.imgur.com/S1iwTas.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="newcook",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_27+"/",
        thumbnail="https://i.imgur.com/S1iwTas.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="bebidas",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_28+"/",
        thumbnail="https://i.imgur.com/S1iwTas.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="ensaladas",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_29+"/",
        thumbnail="https://i.imgur.com/S1iwTas.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="videos favoritos",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_30+"/",
        thumbnail="https://i.imgur.com/S1iwTas.jpg",
        folder=True )
		
    

run()