# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Thanks to the Authors of the base code
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#
# modified by: XMAS
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.xmas'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "PLRAXyxVrb5CWPQVCrzIs5ghV4OOB2zb-1" 	#EVENTO EN VIVO CANAL 1 (lolo)
YOUTUBE_CHANNEL_ID_2 = "PLxgvkEADrKB35Era-Bvyhp3NnksYnfwnz" 	#EVENTO EN VIVO CANAL 2 (djl)
YOUTUBE_CHANNEL_ID_3 = "PLd1t82HTOKhktfQDjDd7dH95_K-82gLM9" 	#BELENES VIVIENTES
YOUTUBE_CHANNEL_ID_4 = "PLd1t82HTOKhmC4tvHHSKzU_s1Q2E8kuMK" 	#CUENTOS Y TRADICIONES DE NAVIDAD
YOUTUBE_CHANNEL_ID_5 = "PLd1t82HTOKhlR8mjzfnTpziYfBzIyjWOs" 	#EN FORMA
YOUTUBE_CHANNEL_ID_6 = "PLrVO4I6tVbCr4ZBBgr-cQKAtx6IJnem9d" 	#MANUALIDADES DE NAVIDAD
YOUTUBE_CHANNEL_ID_7 = "PL230B7AB7843582D9" 	#MUSICA TRADICIONAL DE TODO DICIEMBRE EN COLOMBIA
YOUTUBE_CHANNEL_ID_8 = "PLI0gV8q-K1GCNJVwAULecpc6FcxVk6wYr" 	#NAVIDAD
YOUTUBE_CHANNEL_ID_9 = "PLd1t82HTOKhmJJeAmJP4srYBQNTY62IMw" 	#PELICULAS NAVIDAD
YOUTUBE_CHANNEL_ID_10 = "PLd1t82HTOKhm2s8dj4SOZfFOlDlAxb3yT" 	#RECETAS NAVIDEÑAS
YOUTUBE_CHANNEL_ID_11= "PLd1t82HTOKhlyHjE5ZYw_PoIe5OyTp7ra" 	#RECUERDOS NAVIDEÑOS
YOUTUBE_CHANNEL_ID_12 = "PLd1t82HTOKhnhOVTxXBmCt8wg-Si5MQ8s" 	#VILLANCICOS
YOUTUBE_CHANNEL_ID_13 = "PL1DB78981EB340421" 	#VILLANCICOS TRADICIONALES


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
        title="[COLOR lime]EVENTO EN VIVO CANAL 1[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="http://www.designbolts.com/wp-content/uploads/2013/12/xmas-logo-design.jpg",
		fanart="http://www.cnbinggui.net/data_images/wallpapers/42/471469-xmas.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR lime]EVENTO EN VIVO CANAL 2[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="http://www.designbolts.com/wp-content/uploads/2013/12/xmas-logo-design.jpg",
		fanart="http://www.cnbinggui.net/data_images/wallpapers/42/471469-xmas.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR lime]BELENES VIVIENTES[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="http://www.designbolts.com/wp-content/uploads/2013/12/xmas-logo-design.jpg",
		fanart="http://www.cnbinggui.net/data_images/wallpapers/42/471469-xmas.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR lime]CUENTOS Y TRADICIONES DE NAVIDAD[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="http://www.designbolts.com/wp-content/uploads/2013/12/xmas-logo-design.jpg",
		fanart="http://www.cnbinggui.net/data_images/wallpapers/42/471469-xmas.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR lime]EN FORMA[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="http://www.designbolts.com/wp-content/uploads/2013/12/xmas-logo-design.jpg",
		fanart="http://www.cnbinggui.net/data_images/wallpapers/42/471469-xmas.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR lime]MANUALIDADES DE NAVIDAD[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="http://www.designbolts.com/wp-content/uploads/2013/12/xmas-logo-design.jpg",
		fanart="http://www.cnbinggui.net/data_images/wallpapers/42/471469-xmas.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR lime]MUSICA TRADICIONAL DE TODO DICIEMBRE EN COLOMBIA[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="http://www.designbolts.com/wp-content/uploads/2013/12/xmas-logo-design.jpg",
		fanart="http://www.cnbinggui.net/data_images/wallpapers/42/471469-xmas.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR lime]NAVIDAD[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="http://www.designbolts.com/wp-content/uploads/2013/12/xmas-logo-design.jpg",
		fanart="http://www.cnbinggui.net/data_images/wallpapers/42/471469-xmas.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR lime]PELICULAS NAVIDAD[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="http://www.designbolts.com/wp-content/uploads/2013/12/xmas-logo-design.jpg",
		fanart="http://www.cnbinggui.net/data_images/wallpapers/42/471469-xmas.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR lime]RECETAS NAVIDEÑAS[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="http://www.designbolts.com/wp-content/uploads/2013/12/xmas-logo-design.jpg",
		fanart="http://www.cnbinggui.net/data_images/wallpapers/42/471469-xmas.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR lime]RECUERDOS NAVIDEÑOS[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_11+"/",
        thumbnail="http://www.designbolts.com/wp-content/uploads/2013/12/xmas-logo-design.jpg",
		fanart="http://www.cnbinggui.net/data_images/wallpapers/42/471469-xmas.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR lime]VILLANCICOS[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_12+"/",
        thumbnail="http://www.designbolts.com/wp-content/uploads/2013/12/xmas-logo-design.jpg",
		fanart="http://www.cnbinggui.net/data_images/wallpapers/42/471469-xmas.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR lime]VILLANCICOS TRADICIONALES[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_13+"/",
        thumbnail="http://www.designbolts.com/wp-content/uploads/2013/12/xmas-logo-design.jpg",
		fanart="http://www.cnbinggui.net/data_images/wallpapers/42/471469-xmas.jpg",
        folder=True )

run()