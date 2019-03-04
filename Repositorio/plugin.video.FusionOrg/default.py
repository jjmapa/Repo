# coding=utf-8
import xbmcaddon
import sys
import urlparse
import xbmcplugin
import xbmcgui
from base.tools import *
from base import *

addon = xbmcaddon.Addon('plugin.video.FusionOrg')
addonname = addon.getAddonInfo('name')
language = addon.getSetting('language')
filenamejson = addon.getSetting('filename')
filejson = addon.getSetting('file')

filenamejsonshared = addon.getSetting('filenameshared')
filejsonshared = addon.getSetting('filejson')

args = urlparse.parse_qs(sys.argv[2][1:])
xbmcplugin.setContent(addon_handle, 'movies')
mode = args.get('mode', None)

#===============================================================================
# if language == 'Latino':
#     from languages.spanish import *
# elif language == 'Español':
#     from languages.spanish import *
# elif language == 'English':
#     from languages.english import *
# elif language == 'Portuges':
#     from languages.portuguese import *
# else:
#     from languages.spanish import *
#===============================================================================

from languages.spanish import *

#Imprime el Menu Principal de la Aplicacion
if mode is None:
    Directorios()
    menuppal(categoriasprincipales(),infosprincipales(),fanartsprincipales(),modesprincipales(),postersprincipales())
#Imprime Submenu de la Categoria Television
elif mode[0] == 'mode01':
    menuppal(subcategoriastv(),subinfostv(),subfanartstv(),submodestv(),subposterstv())

#Imprime el SubMenu de la Categoria de Peliculas
elif mode[0] == 'mode02':
    menucategoriasmovies(subcategoriasmovies(),subinfosmovies(),subfanartsmovies(),submodesmovies(),subpostersmovies(),archivosmovies())
    
elif mode[0] == 'for_year':
    web = args['direccion'][0]
    movieslistyear(web, 'movies', 'Por Año')    
#Imprime las Peliculas Dentro de las Categorias
elif mode[0] == 'movies':
    web = args['direccion'][0]
    categoria = args['categoria'][0]
    movieslist(web, 'servidores', categoria)
    
#Imprime el SubMenu de los TV Shows
elif mode[0] == 'mode03':    
    menucategoriastvshows(subcategoriastvshows(),subinfostvshows(),subfanartstvshows(),submodestvshows(),subposterstvshows(),subtagstvshows())
    
#imprime las colecciones activas
elif mode[0] == 'collections':
    collections_list(subcategoriascollections(), suburlcollections(), subposterscollections(), subfanartscollections(), subinfoscollections(), submodescollections())

elif mode[0] == 'collection':
    web = args['direccion'][0]
    categoria = args['categoria'][0]
    collection_list(web,categoria)
    
#Imprime la Lista de Series
elif mode[0] == 'tvshows':
    web = args['direccion'][0]
    categoria = args['categoria'][0]
    tvshowslist(web, 'seasons', categoria)
    
#Imprime la Lista de Temporadas de Series
elif mode[0] == 'seasons':
    fanart = args['fanart'][0]
    sinopsis = args['info'][0]
    web = args['direccion'][0]
    tmdbid = args['tmdbid'][0]
    serie = args['serie'][0]
    seasonlist(web,fanart,sinopsis,'episodes', tmdbid, serie)
    
#Imprime la Lista de Episodios de la Temporada
elif mode[0] == 'episodes':
    web = args['direccion'][0]
    tmdbid = args['tmdbid'][0]
    serie = args['serie'][0]
    episodeslist(web,'servidores2', tmdbid, serie)
    
elif mode[0] == 'mode04':
    search()
    
#Imprime  El Menu de la Lista de Servidores para Peliculas
elif mode[0] == 'servidores':
    titulo = args['foldername'][0]
    thumbnail = args['thumbnail'][0]
    fanart = args['fanart'][0]
    try:
        sinopsis = args['info'][0]
    except:
        sinopsis = 'Sin info'
    url = args['direccion'][0]
    servidores(titulo,thumbnail,fanart,sinopsis,url)
    
#Imprime El Menu de la Lista de Servidores para Series
elif mode[0] == 'servidores2':
    web = args['direccion'][0]
    tmdbid = args['tmdbid'][0]
    season = args['season'][0]
    episode = args['episode'][0]
    serie = args['serie'][0]
    servidores2(web,tmdbid,season,episode, serie)

elif mode[0] == 'mode05':
    menuppal(subtools(),subtoolsinfos(),subtoolsposters(),subtoolsmodes(),subtoolsfanarts())
    
#Metodo de Reproduccion de Video
elif mode[0] == 'play':
    url = args['playlink'][0]
    tmdbid = args['tmdbid'][0]
    reproductor(url,tmdbid)

elif mode[0] == 'conversion':
    conversion_json()

elif mode[0] == 'playstb':
    tiempo, url = uptobox(args)
    if not tiempo:
        reproductor(url)
    else:         
        mensaje("Debe esperar: " + url)
        pass
    
elif mode[0] == 'add_my_list':
    add_my_list()

elif mode[0] == 'remove_my_list':
    name = ''
    url = args['link'][0]
    name = args['name'][0]
    remove_my_list(url,name)
    
elif mode[0] == 'add_share_list':
    add_shared_list()

elif mode[0] == 'remove_shared_list':
    iddb = args['iddb'][0]
    namedb = args['namedb'][0]
    remove_shared_list(iddb,namedb)

elif mode[0] == 'read_my_lists':
    read_my_lists()
    
elif mode[0] == 'get_shared_lists':
    get_shared_lists()

elif mode[0] == 'get_my_shared_lists':
    get_my_shared_lists()

elif mode[0] == 'read_local_list':
    file = args['link'][0]
    read_local_list(file)

elif mode[0] == 'read_url_list':
    url = args['link'][0]
    read_url_list(url)
    
elif mode[0] == 'vote_list':
    iddb = args['iddb'][0]
    namedb = args['namedb'][0]
    vote_list(iddb, namedb)
    
elif mode[0] == 'get_token_uptobox':
    get_token_uptobox()
    
elif mode[0] == 'wait':
    pass

elif mode[0] == 'open_settings':
    addon.openSettings()
    
    
