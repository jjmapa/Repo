# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Contenido para los verdaderos Salseros de YouTube by cpradof
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#
# Author: cpradof
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.salsaconcache'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

xbmc.executebuiltin('Container.SetViewMode(500)')

YOUTUBE_CHANNEL_ID_1 = "PLvleRX0duEG3pvmkRByTWLwTGDBd9XSP5"
YOUTUBE_CHANNEL_ID_2 = "PLvleRX0duEG2rnSHI48X9PoSE-AfdeKtk"
YOUTUBE_CHANNEL_ID_3 = "PLvleRX0duEG0mWfUbZAGWQQvQmBa4Vb0C"
YOUTUBE_CHANNEL_ID_4 = "PLvleRX0duEG2jWQzD7EZYG29ynlNZSzDo"
YOUTUBE_CHANNEL_ID_5 = "PLvleRX0duEG1aAYDXdHueu5xgI5XdMivc"
YOUTUBE_CHANNEL_ID_6 = "PLvleRX0duEG2HNWSTYUa6Zga6iF7laGyj"
YOUTUBE_CHANNEL_ID_7 = "PLvleRX0duEG3aRRKlVzz18yhTL4JrtL1R"
YOUTUBE_CHANNEL_ID_8 = "PLvleRX0duEG3hEgnU3Vc9AQN80ySCSYyo"
YOUTUBE_CHANNEL_ID_9 = "PLvleRX0duEG1vo6WQ8VBSkAnNSw0I8A9P"
YOUTUBE_CHANNEL_ID_10 = "PLvleRX0duEG3YvGjeah90V9rfOHBY0eNe"
YOUTUBE_CHANNEL_ID_11 = "PLvleRX0duEG1QfwBlOJlT12iixvr2tGvM"
YOUTUBE_CHANNEL_ID_12 = "PLvleRX0duEG3h2vpKM0Rq0POB4ClcMyDP"
YOUTUBE_CHANNEL_ID_13 = "PLvleRX0duEG2oKnIMI-9qudVTL5yZ7mnv" 
YOUTUBE_CHANNEL_ID_14 = "PLvleRX0duEG3ni1w7YofiVoglOzJFUOok" 
YOUTUBE_CHANNEL_ID_15 = "PLvleRX0duEG2GbRQJJcl4EXzJK9GP0_yy" 
YOUTUBE_CHANNEL_ID_16 = "PLvleRX0duEG2x85p-4oWxGZfJoMhcbHs-" 
YOUTUBE_CHANNEL_ID_17 = "PLvleRX0duEG1Jre3V70PqdEFw7eehVvGK"
YOUTUBE_CHANNEL_ID_18 = "PLvleRX0duEG3pmwN_GE4XJDT8qXsh0tpR"
YOUTUBE_CHANNEL_ID_19 = "PLvleRX0duEG1taHGxXU4KUyLrue9jIkS_"
YOUTUBE_CHANNEL_ID_20 = "PLvleRX0duEG1WSxeamEO_QLkpSjTZ0Jmt"
YOUTUBE_CHANNEL_ID_21 = "PLvleRX0duEG20LVDdNz16UyufHtgMdarD"
YOUTUBE_CHANNEL_ID_22 = "PLvleRX0duEG0-Izb430jXrDDO4STRKPV0"
YOUTUBE_CHANNEL_ID_23 = "PLvleRX0duEG26WcOvfNnAlP6qr-KyqbnQ"
YOUTUBE_CHANNEL_ID_24 = "PLvleRX0duEG3hyo79tYYATyNKYr-2n4Z7"
YOUTUBE_CHANNEL_ID_25 = "PLvleRX0duEG1syu16-XcQbYWbCO8vg81s"
YOUTUBE_CHANNEL_ID_26 = "PLvleRX0duEG3_i6Xv6QsY_JmSLcX4CKAj"
YOUTUBE_CHANNEL_ID_27 = "PLvleRX0duEG0KF-lYJf_I8zkKmW4Ciett"
YOUTUBE_CHANNEL_ID_28 = "PLvleRX0duEG0pcnghz5qqXuPhNI3XwKin"
YOUTUBE_CHANNEL_ID_29 = "PLvleRX0duEG27QcgxtNIFiLIxLf1yJ6iq"
YOUTUBE_CHANNEL_ID_30 = "PLvleRX0duEG2vyspDbgM3U5Z-pqIMSKR2"
YOUTUBE_CHANNEL_ID_31 = "PLvleRX0duEG1Q5O5AvGRxu3fL9MtiL-_n"
YOUTUBE_CHANNEL_ID_32 = "PLvleRX0duEG3EEbzeH3Sb_skc8Jhnl0x3"
YOUTUBE_CHANNEL_ID_33 = "PLvleRX0duEG24rqBVMuXbTEX_apeC5auz"
YOUTUBE_CHANNEL_ID_34 = "PLvleRX0duEG3fh5UbBGFiOiBFIUDZvdBn"
YOUTUBE_CHANNEL_ID_35 = "PLvleRX0duEG3yjHdDvqszyd08stLe-rqM"
YOUTUBE_CHANNEL_ID_36 = "PLvleRX0duEG3ks1czJcMMBf0h3TxP09RQ"
YOUTUBE_CHANNEL_ID_37 = "PLvleRX0duEG1jMu5NyuwafpFKCjFiXoA2"
YOUTUBE_CHANNEL_ID_38 = "PLvleRX0duEG3jhAAipNnb3YRt366tso8o"
YOUTUBE_CHANNEL_ID_39 = "PLvleRX0duEG1vocPu2WypVUadVUplXBGb"
YOUTUBE_CHANNEL_ID_40 = "PLvleRX0duEG2r90YP_NmXAAXLRm5LrIEu" 
YOUTUBE_CHANNEL_ID_41 = "PLvleRX0duEG3Z-8jzL3nd0YUOGY5lA0vD"
YOUTUBE_CHANNEL_ID_42 = "PLvleRX0duEG2xiCxAbg6991ipm12u9_h5"
YOUTUBE_CHANNEL_ID_43 = "PLvleRX0duEG0jF58d9NavMbVvv3GvAbN1"
YOUTUBE_CHANNEL_ID_44 = "PLvleRX0duEG0OKMaRpR7MRLFo8r3RI5WI"
YOUTUBE_CHANNEL_ID_45 = "PLvleRX0duEG0CDG7HrSE6XQM6GBeWQgVZ"
YOUTUBE_CHANNEL_ID_46 = "PLvleRX0duEG1UXmBDEfOg8L-PTdENygpO"
YOUTUBE_CHANNEL_ID_47 = "PLvleRX0duEG03W29iqooFBSa1aFqmjFPS"
YOUTUBE_CHANNEL_ID_48 = "PLvleRX0duEG23HtHnFjxjW95WlS-bhpDc"
YOUTUBE_CHANNEL_ID_49 = "PLvleRX0duEG2mN6PDWe0nee8mRcJD55cQ"
YOUTUBE_CHANNEL_ID_50 = "PLvleRX0duEG0GKSTH6uiGnZjesHYs8olJ"
YOUTUBE_CHANNEL_ID_51 = "PLvleRX0duEG3KoSv1kh_ugr8Q-vclNVcT"
YOUTUBE_CHANNEL_ID_52 = "PLvleRX0duEG1WBKVoEiuf6F78h5jZ1cup"
YOUTUBE_CHANNEL_ID_53 = "PLvleRX0duEG37jBvhnqYcLZLdaZmWT-eD"
YOUTUBE_CHANNEL_ID_54 = "PLvleRX0duEG1r59SPS9fjmFlsNiFUBEsL"
YOUTUBE_CHANNEL_ID_55 = "PLvleRX0duEG0YbXGuMuelK475mzRjGeoo"
YOUTUBE_CHANNEL_ID_56 = "PLvleRX0duEG3MjSUSVFeyon274H2g-neG"
YOUTUBE_CHANNEL_ID_57 = "PLvleRX0duEG28fZgk-pfhG1p6nSPr1QVO"
YOUTUBE_CHANNEL_ID_58 = "PLvleRX0duEG0egAHNjj39q6ER5Hy0mRp-"
YOUTUBE_CHANNEL_ID_59 = "PLvleRX0duEG0zXf1TdraPx8pyQlpPqUXF"
YOUTUBE_CHANNEL_ID_60 = "PLvleRX0duEG27LSOo3KcAy4dovUZS3thw"
YOUTUBE_CHANNEL_ID_61 = "PLvleRX0duEG2COIHCUjBExzJjdIeUmLAG"
YOUTUBE_CHANNEL_ID_62 = "PLvleRX0duEG2-yA3b0F7XcCSJicx14c0v"
YOUTUBE_CHANNEL_ID_63 = "PLvleRX0duEG1i-ZE9kk79DS4F5XwgzGxn"
YOUTUBE_CHANNEL_ID_64 = "PLvleRX0duEG3JXA7vA_GwMI-WiZmWovOK"
YOUTUBE_CHANNEL_ID_65 = "PLvleRX0duEG27z9Yai8npVEx1Y6FbVGh4"
YOUTUBE_CHANNEL_ID_66 = "PLvleRX0duEG0pjEIkn-l8j2LTdUAa36Sn"
YOUTUBE_CHANNEL_ID_67 = "PLvleRX0duEG2sxLs5PL4tNnz2NjwfnOqO"
YOUTUBE_CHANNEL_ID_68 = "PLvleRX0duEG2z8O-PlurqpXMVt06piFUq"
YOUTUBE_CHANNEL_ID_69 = "PLvleRX0duEG19hJp_jHrzdLS3ruDAnA69"
YOUTUBE_CHANNEL_ID_70 = "PLvleRX0duEG1ECzNgXDzjupZI0Dif2k-Y"
YOUTUBE_CHANNEL_ID_71 = "PLvleRX0duEG11-YtDsLYo88X-kSLbCi5e"
YOUTUBE_CHANNEL_ID_72 = "PLvleRX0duEG1Gkm35pqB7B8CWm4FTvOy7"
YOUTUBE_CHANNEL_ID_73 = "PLvleRX0duEG3AumDpcrYmyBEL-gg1FQ00"
YOUTUBE_CHANNEL_ID_74 = "PLvleRX0duEG3BorBUku1tyR_5TQEygXee"

  

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
        title="[COLOR lime]Conciertos[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="http://cpradof.darkwebrepo.gq/salsaconcache/Conciertos.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR lime]Salsa Gorda[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="http://cpradof.darkwebrepo.gq/salsaconcache/SalsaGorda.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR lime]Bolero[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="http://cpradof.darkwebrepo.gq/salsaconcache/Boleros.png",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="[COLOR lime]Albumes[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="http://cpradof.darkwebrepo.gq/salsaconcache/Albumes.png",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="[COLOR lime]Sacra[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="http://cpradof.darkwebrepo.gq/salsaconcache/Sacra.png",
        folder=True )	

    plugintools.add_item( 
        #action="", 
        title="[COLOR lime]La vida de…[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="http://cpradof.darkwebrepo.gq/salsaconcache/Historia.png",
        folder=True )	

    plugintools.add_item( 
        #action="", 
        title="[COLOR lime]Navidad[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="http://cpradof.darkwebrepo.gq/salsaconcache/Navidad.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Adalberto Santiago",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="http://cpradof.darkwebrepo.gq/salsaconcache/adalberto.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Alex de Castro  ",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="http://cpradof.darkwebrepo.gq/salsaconcache/AlexdeCastro.png",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Andy Montañez",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="http://cpradof.darkwebrepo.gq/salsaconcache/AndyMontanez.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Angel Canales",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_11+"/",
        thumbnail="http://cpradof.darkwebrepo.gq/salsaconcache/AngelCnles.PNG",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Anthony Cruz",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_12+"/",
        thumbnail="http://cpradof.darkwebrepo.gq/salsaconcache/Anthonycruz.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Bobby Valentin",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_13+"/",
        thumbnail="http://cpradof.darkwebrepo.gq/salsaconcache/BobbyValentin.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Cano Estremera",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_14+"/",
        thumbnail="http://cpradof.darkwebrepo.gq/salsaconcache/canoestremera.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Celia Cruz",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_15+"/",
        thumbnail="http://cpradof.darkwebrepo.gq/salsaconcache/celiacruz.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Chamaco Ramirez",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_16+"/",
        thumbnail="http://cpradof.darkwebrepo.gq/salsaconcache/chamacoramirez.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Cheo Feliciano",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_17+"/",
        thumbnail="http://cpradof.darkwebrepo.gq/salsaconcache/cheo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Chivirico Davila",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_18+"/",
        thumbnail="http://cpradof.darkwebrepo.gq/salsaconcache/chivirico.png",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Conjunto Chaney",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_19+"/",
        thumbnail="http://cpradof.darkwebrepo.gq/salsaconcache/chaney.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="David Pabon",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_20+"/",
        thumbnail="http://cpradof.darkwebrepo.gq/salsaconcache/davidpabon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Dimension Latina",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_21+"/",
        thumbnail="http://cpradof.darkwebrepo.gq/salsaconcache/dimlatina.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Domingo Quiñones",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_22+"/",
        thumbnail="http://cpradof.darkwebrepo.gq/salsaconcache/Domingo-Quin%cc%83ones.png",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="Eddie Santiago",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_23+"/",
        thumbnail="http://cpradof.darkwebrepo.gq/salsaconcache/eddie.png",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="El Gran Combo de Puerto Rico",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_24+"/",
        thumbnail="http://cpradof.darkwebrepo.gq/salsaconcache/elgrancombo.png",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="Fania All Star",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_25+"/",
        thumbnail="http://cpradof.darkwebrepo.gq/salsaconcache/fania.png",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="Frankie Ruiz",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_26+"/",
        thumbnail="http://cpradof.darkwebrepo.gq/salsaconcache/frankie.png",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="Gilberto Santa Rosa",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_27+"/",
        thumbnail="http://cpradof.darkwebrepo.gq/salsaconcache/gilbertito.png",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="Hector Lavoe",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_28+"/",
        thumbnail="http://cpradof.darkwebrepo.gq/salsaconcache/hlavoe.png",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="Hector Tricoche",
        url="plugin://plugin.video.youtube/playlist?list/"+YOUTUBE_CHANNEL_ID_29+"/",
        thumbnail="http://cpradof.darkwebrepo.gq/salsaconcache/htricoche.png",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="Ismael Miranda",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_30+"/",
        thumbnail="http://cpradof.darkwebrepo.gq/salsaconcache/imiranda.png",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="Ismael Quintana",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_31+"/",
        thumbnail="http://cpradof.darkwebrepo.gq/salsaconcache/iquintana.png",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="Ismael Rivera",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_32+"/",
        thumbnail="http://cpradof.darkwebrepo.gq/salsaconcache/irivera.png",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="Jerry Rivera",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_33+"/",
        thumbnail="http://cpradof.darkwebrepo.gq/salsaconcache/jerryrivera.png",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="Johnny Rivera",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_34+"/",
        thumbnail="http://cpradof.darkwebrepo.gq/salsaconcache/johnnyrivera.png",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="Jose Alberto El Canario",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_35+"/",
        thumbnail="http://cpradof.darkwebrepo.gq/salsaconcache/josealberto.png",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="Junior Gonzalez",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_36+"/",
        thumbnail="http://cpradof.darkwebrepo.gq/salsaconcache/juniorgonzalez.png",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="La Lupe",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_37+"/",
        thumbnail="http://cpradof.darkwebrepo.gq/salsaconcache/lalupe.png",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="La Solucion",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_38+"/",
        thumbnail="http://cpradof.darkwebrepo.gq/salsaconcache/lasolucion.png",
        folder=True )
    plugintools.add_item( 
        #action="Lalo Rodriguez", 
        title="Lalo Rodriguez",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_39+"/",
        thumbnail="http://cpradof.darkwebrepo.gq/salsaconcache/lalo.png",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="Lebron Brothers",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_40+"/",
        thumbnail="http://cpradof.darkwebrepo.gq/salsaconcache/lebronbrothers.png",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="Luigi Texidor",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_41+"/",
        thumbnail="http://cpradof.darkwebrepo.gq/salsaconcache/luigie.png",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="Luis Enrique",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_42+"/",
        thumbnail="http://cpradof.darkwebrepo.gq/salsaconcache/luisenrique.png",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="Maelo Ruiz",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_43+"/",
        thumbnail="http://cpradof.darkwebrepo.gq/salsaconcache/maeloruiz.png",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="Marc Anthony",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_44+"/",
        thumbnail="http://cpradof.darkwebrepo.gq/salsaconcache/marc.png",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="Marvin Santiago",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_45+"/",
        thumbnail="http://cpradof.darkwebrepo.gq/salsaconcache/marvin.png",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="Michael Stuart",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_46+"/",
        thumbnail="http://cpradof.darkwebrepo.gq/salsaconcache/mstuart.png",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="Mulenze",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_47+"/",
        thumbnail="http://cpradof.darkwebrepo.gq/salsaconcache/mulenze.png",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="Orquesta Harlow",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_48+"/",
        thumbnail="http://cpradof.darkwebrepo.gq/salsaconcache/orquestaharlow.png",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="Oscar de Leon",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_49+"/",
        thumbnail="http://cpradof.darkwebrepo.gq/salsaconcache/oscardeleon.png",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="Paquito Guzman",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_50+"/",
        thumbnail="http://cpradof.darkwebrepo.gq/salsaconcache/paquitoguzman.png",
        folder=True )		
    plugintools.add_item( 
        #action="", 
        title="Pedro Arroyo",		
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_51+"/",
        thumbnail="http://cpradof.darkwebrepo.gq/salsaconcache/pedroarroyo.png",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="Pete El Conde Rodriguez",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_52+"/",
        thumbnail="http://cpradof.darkwebrepo.gq/salsaconcache/peteconde.png",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="Puerto Rican Power",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_53+"/",
        thumbnail="http://cpradof.darkwebrepo.gq/salsaconcache/prpower.png",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="Pupy Santiago",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_54+"/",
        thumbnail="http://cpradof.darkwebrepo.gq/salsaconcache/pupy.png",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="Rafael de Jesus",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_55+"/",
        thumbnail="http://cpradof.darkwebrepo.gq/salsaconcache/rafaeldejesus.png",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="Raphy Leavitt",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_56+"/",
        thumbnail="http://cpradof.darkwebrepo.gq/salsaconcache/raphyleavitt.png",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="Ray de la Paz",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_57+"/",
        thumbnail="http://cpradof.darkwebrepo.gq/salsaconcache/raydelapaz.png",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="Rey Ruiz",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_58+"/",
        thumbnail="http://cpradof.darkwebrepo.gq/salsaconcache/rayruiz.png",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="Richie Ray y Bobby Cruz",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_59+"/",
        thumbnail="http://cpradof.darkwebrepo.gq/salsaconcache/richybobby.png",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="Roberto Lugo",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_60+"/",
        thumbnail="http://cpradof.darkwebrepo.gq/salsaconcache/robertolugo.png",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="Roberto Roena",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_61+"/",
        thumbnail="http://cpradof.darkwebrepo.gq/salsaconcache/robertoroena.png",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="Ruben Blades",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_62+"/",
        thumbnail="http://cpradof.darkwebrepo.gq/salsaconcache/rubenblades.png",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="Salsa Fever",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_63+"/",
        thumbnail="http://cpradof.darkwebrepo.gq/salsaconcache/salsafever.png",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="Sonora Ponceña",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_64+"/",
        thumbnail="http://cpradof.darkwebrepo.gq/salsaconcache/sonora.png",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="Tipica 73",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_65+"/",
        thumbnail="http://cpradof.darkwebrepo.gq/salsaconcache/tipica73.png",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="Tito Gomez",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_66+"/",
        thumbnail="http://cpradof.darkwebrepo.gq/salsaconcache/titogomez.png",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="Tito Nieves",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_67+"/",
        thumbnail="http://cpradof.darkwebrepo.gq/salsaconcache/titonieves.png",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="Tito Rojas",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_68+"/",
        thumbnail="http://cpradof.darkwebrepo.gq/salsaconcache/titorojas.png",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="Tommy Olivencia",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_69+"/",
        thumbnail="http://cpradof.darkwebrepo.gq/salsaconcache/tommyolivencia.png",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="Tony Vega",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_70+"/",
        thumbnail="http://cpradof.darkwebrepo.gq/salsaconcache/tonyvega.png",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="Victor Manuelle",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_71+"/",
        thumbnail="http://cpradof.darkwebrepo.gq/salsaconcache/victormanuelle.png",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="Willie Colon",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_72+"/",
        thumbnail="http://cpradof.darkwebrepo.gq/salsaconcache/williecolon.png",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="Willie Gonzalez",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_73+"/",
        thumbnail="http://cpradof.darkwebrepo.gq/salsaconcache/williegonzalez.png",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="Willie Rosario",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_74+"/",
        thumbnail="http://cpradof.darkwebrepo.gq/salsaconcache/willierosario.png",
        folder=True )
    
run()
