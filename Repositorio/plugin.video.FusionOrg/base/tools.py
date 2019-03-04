# coding=utf-8
import xbmcaddon
import urllib2
import urllib
import sys
import urlparse
import xbmcplugin
import xbmcgui
import xbmc
import sys
import base64
import re
import os
import os.path
import urlresolver
import cookielib
import json
from urllib2 import Request, urlopen, URLError, HTTPError
from servers import *

base_url = sys.argv[0]
addon_handle = int(sys.argv[1])

addon = xbmcaddon.Addon()
addon_dir = xbmc.translatePath(xbmc.translatePath(addon.getAddonInfo('Path')).decode('utf-8'))
addon_data_dir = xbmc.translatePath(xbmc.translatePath(addon.getAddonInfo('profile')).decode('utf-8'))

addonname   = addon.getAddonInfo('name')

username = addon.getSetting('username')
password = addon.getSetting('password')
#===============================================================================
# language = addon.getSetting('language')
#===============================================================================

language = 'Latino'

args = urlparse.parse_qs(sys.argv[2][1:])
mode = args.get('mode', None)

def mensaje(mensaje):
    xbmcgui.Dialog().ok(addonname, mensaje)

def build_url(query):
    return base_url + '?' + urllib.urlencode(query)

def addMenuitem(url, li, folder, sort=''):
    if sort == 'year':
        xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_YEAR)
    elif sort == 'titulo':
        xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_UNSORTED)
    else:
        xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_UNSORTED)
    return xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=folder)

def endMenu():
    xbmcplugin.endOfDirectory(addon_handle)

def read(url):
    opener = urllib2.build_opener()
    opener.addheaders = [('User-Agent', 'FusionOrgByTeamFusion/1.0')]
    response = opener.open(url)
    data = response.read()
    return data

def read2(url):
    opener = urllib2.build_opener()
    opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.71 Safari/537.36')]
    response = opener.open(url)
    data = response.read()
    return data

def Directorios():
    addon_data = xbmc.translatePath("special://userdata/addon_data/plugin.video.FusionOrg")
    try:
        os.stat(addon_data)
    except:
        os.mkdir(addon_data)

    dir_downloads = addon_data+'/descargas'
    try:
        os.stat(dir_downloads)
    except:
        os.mkdir(dir_downloads)
    masterlistLocal = open(addon_data+'/masterlist.json','a')
    masterlistLocal.close()

def listasupload(file, nombre_archivo):
    s = requests.Session()
    data = {'email':username,'password':password}
    url = "http://fusionorg.net/checklogin.php"
    r = s.post(url, data=data)
    texto = str(s.cookies)
    cookie = re.findall('.*?(PHPSESSID=.*?) .*',texto,re.MULTILINE)[0]
    headers = {'User-Agent':'FusionOrgByTeamFusion/1.0', 'Connection':'keep-alive', 'Cookie': cookie,'Host':'fusionorg.net','Referer':'http://fusionorg.net/index.php'}
    url2 = "http://fusionorg.net/upload.php"

    nombre = nombre_archivo+'.json'
    archivo = open(file)
    d= requests.post(url2, headers= headers, files={'titulo': (None, nombre), 'archivo': (archivo, archivo.read(),'application/octet-stream')})
    return mensaje(d.text)

def add_listas_locales():
    dialog = xbmcgui.Dialog()
    nombre = dialog.input('Escribe un Nombre para la Lista', type=xbmcgui.INPUT_ALPHANUM)
    if nombre == '':
        mensaje('El Nombre no puede estar vacio')
    else:
        Pregunta = dialog.select('Tu Lista es Local o de Internet?', ['Es Lista Local', 'Es una Lista Alojada en Internet'])
        if Pregunta == 0:
            Archivo = dialog.browseSingle(1, 'Selecciona tu Lista en Formato JSON', 'files', '.json', False, False, 'special://masterprofile/script_data/Kodi Lyrics')
            if Archivo == '':
                mensaje('No Seleccionaste Ningun Archivo')
            else:
                ret = dialog.yesno('FusionOrg', 'Quieres Agregar un logo a tu Lista?')
                if ret == True:
                    Poster = dialog.browseSingle(1, 'Selecciona una Imagen para tu Logo', 'files', '.jpeg|.jpg|.png', True, True, 'special://masterprofile/script_data/Kodi Lyrics')
                else:
                    Poster = ''
                ret2 = dialog.yesno('FusionOrg', 'Quieres Agregar una Imagen de Fondo Personalizada a tu Lista?')
                if ret2 == True:
                    Fanart = dialog.browseSingle(1, 'Selecciona una Imagen para tu Logo', 'files', '.jpeg|.jpg|.png', True, True, 'special://masterprofile/script_data/Kodi Lyrics')
                else:
                    Fanart = ''
                ret3 = dialog.yesno('FusionOrg', 'Quieres Agregar una Descripcion a tu Lista?')
                if ret3 == True:
                    Sinopsis = dialog.input('Escribe una Breve Descripcion de tu Lista', type=xbmcgui.INPUT_ALPHANUM)
                else:
                    Sinopsis = ''
                addon_data = xbmc.translatePath("special://userdata/addon_data/plugin.video.FusionOrg")
                masterlistLocal = open(addon_data+'/masterlist.json','a')
                masterlistLocal.write('[{"nombre":"'+nombre+'","thumbnail":"'+Poster+'","fanart":"'+Fanart+'","direccion":"'+Archivo+'","Sinopsis":"'+Sinopsis+'"}]\n')
                masterlistLocal.close()
                mensaje('La Lista se Agrego Correctamente')
        else:
            Archivo = dialog.input('Escribe la Direccion URL de la Lista', type=xbmcgui.INPUT_ALPHANUM)
            if Archivo == '':
                mensaje('No Puedes Continuar si no escribes la URL del Archivo')
            else:
                ret = dialog.yesno('FusionOrg', 'Quieres Agregar un logo a tu Lista?')
                if ret == True:
                    Poster = dialog.input('Escribe la Direccion URL de la Imagen de Tu Logo', type=xbmcgui.INPUT_ALPHANUM)
                else:
                    Poster = ''
                ret2 = dialog.yesno('FusionOrg', 'Quieres Agregar una Imagen de Fondo Personalizada a tu Lista?')
                if ret2 == True:
                    Fanart = dialog.input('Escribe la Direccion URL de la Imagen de Fondo', type=xbmcgui.INPUT_ALPHANUM)
                else:
                    Fanart = ''
                ret3 = dialog.yesno('FusionOrg', 'Quieres Agregar una Descripcion a tu Lista?')
                if ret3 == True:
                    Sinopsis = dialog.input('Escribe una Breve Descripcion de tu Lista', type=xbmcgui.INPUT_ALPHANUM)
                else:
                    Sinopsis = ''
                addon_data = xbmc.translatePath("special://userdata/addon_data/plugin.video.FusionOrg")
                masterlistLocal = open(addon_data+'/masterlist.json','a')
                masterlistLocal.write('[{"nombre":"'+nombre+'","thumbnail":"'+Poster+'","fanart":"'+Fanart+'","direccion":"'+Archivo+'","Sinopsis":"'+Sinopsis+'"}]\n')
                masterlistLocal.close()
                mensaje('La Lista se Agrego Correctamente')

def jsonread(file):
    
    with open(file , 'r') as f:
        items = json.load(f)

    for item in items:
        if item['Folder'] == 'False':
            title = item['Titulo']
            url = item['Enlace']
            li = xbmcgui.ListItem(title, iconImage=item['Poster'], thumbnailImage=item['Poster'])
            li.setInfo("video", {"Title": title, "FileName": title, "Plot": item['Sinopsis']})
            li.setProperty('IsPlayable', 'true')
            li.setProperty('fanart_image', item['Fondo'])
            addMenuitem(url, li, False)
        elif item['Folder'] == 'True':
            title = item['Titulo']
            url = build_url({'mode':'readjson', 'direccion': item['Enlace']})
            li = xbmcgui.ListItem(title, iconImage=item['Poster'], thumbnailImage=item['Poster'])
            li.setInfo("video", {"Title": title, "FileName": title, "Plot": item['Sinopsis']})
            li.setProperty('fanart_image', item['Fondo'])
            addMenuitem(url, li, True)

    endMenu()


def jsonreadweb(url):
    req = urllib2.Request(url)
    opener = urllib2.build_opener()
    f = opener.open(req)
    items = json.loads(f.read())
    for item in items:
        if item['Folder'] == 'False':
            title = item['Titulo']
            url = item['Enlace']
            li = xbmcgui.ListItem(title, iconImage=item['Poster'], thumbnailImage=item['Poster'])
            li.setInfo("video", {"Title": title, "FileName": title, "Plot": item['Sinopsis']})
            li.setProperty('IsPlayable', 'true')
            li.setProperty('fanart_image', item['Fondo'])
            addMenuitem(url, li, False)
        elif item['Folder'] == 'True':
            title = item['Titulo']
            url = build_url({'mode':'readjson', 'direccion': item['Enlace']})
            li = xbmcgui.ListItem(title, iconImage=item['Poster'], thumbnailImage=item['Poster'])
            li.setInfo("video", {"Title": title, "FileName": title, "Plot": item['Sinopsis']})
            li.setProperty('fanart_image', item['Fondo'])
            addMenuitem(url, li, True)

    endMenu()

def conversion_json():
    dialog = xbmcgui.Dialog()
    filem3u = dialog.browseSingle(1, 'Selecciona una Lista en Formato M3U', '', '.m3u', False, False, '')
    if (filem3u != ''):
        file = open(filem3u)
        data = file.read()
        foldersalida = dialog.browseSingle(3, 'Selecciona la Carpeta de Salida', 'local', '', False, False, '')
        if (foldersalida != ''):
            file2 = open(foldersalida+"salida.json", "w")
            file2.write("[" + os.linesep)
            matches = re.findall('(#EXTINF.*?,.*\n.*)',data, re.IGNORECASE)
            i = 1
            for match in matches:
                titulo = re.findall('.*\,(.*)', match, re.IGNORECASE)[0]
                url = re.findall(',.*\n(.*)', match, re.IGNORECASE)[0]
                file2.write("{" + os.linesep)
                file2.write('"Folder":"False",' + os.linesep)
                file2.write('"Titulo":"'+titulo.strip()+'",' + os.linesep)
                file2.write('"Poster":"",' + os.linesep)
                file2.write('"Fondo":"",' + os.linesep)
                file2.write('"Sinopsis":"",' + os.linesep)
                file2.write('"Enlace":"'+url+'"' + os.linesep)
                if i < len(matches):
                    file2.write('},' + os.linesep)
                else:
                    file2.write('}' + os.linesep)
                i = i+1
            file2.write("]" + os.linesep)
            file.close()
            file2.close()
            mensaje("La Convesion Termino Satisfactoriamente")
        else:
            dialog = xbmcgui.Dialog()
            dialog.notification("Fusion", 'La conversion se cancelo',
                                xbmcgui.NOTIFICATION_INFO, 3500 , False)
    else:
        dialog = xbmcgui.Dialog()
        dialog.notification("Fusion", 'La conversion se cancelo',
                            xbmcgui.NOTIFICATION_INFO, 3500 , False)

def menuppal(categorias, infos, fanarts, modes, posters):
    xbmcplugin.setContent(addon_handle, 'albums')
    xbmcplugin.setPluginCategory(addon_handle, 'Menu')
    for categoria, info, fanart, mode, poster in zip(categorias, infos, fanarts, modes, posters):
        url = build_url({'mode':mode})
        li = xbmcgui.ListItem('[COLOR white][B]'+categoria+'[/B][/COLOR]')
        li.setInfo("video", {"Plot": info})
        li.setArt({'fanart': fanart, 'poster': poster})
        addMenuitem(url, li, True)
    endMenu()

def menucategoriasmovies(categorias, infos, fanarts, modes, posters, archivos):
    xbmcplugin.setContent(addon_handle, 'albums')
    xbmcplugin.setPluginCategory(addon_handle, 'Categorias')
    serial = 'aHR0cDovL2Z1c2lvbm9yZy5uZXQvY2F0ZWdvcmllcy9tb3ZpZXMv'
    serial = base64.b64decode(serial)
    for categoria, info, fanart, mode, poster, archivo in zip(categorias, infos, fanarts, modes, posters, archivos):
        url = build_url({'mode':mode, 'direccion': serial+archivo+'.php', 'categoria': categoria})
        li = xbmcgui.ListItem('[COLOR white][B]'+categoria+'[/B][/COLOR]')
        li.setInfo("video", {"Plot": info})
        li.setArt({'fanart': fanart, 'poster': poster})
        addMenuitem(url, li, True)
    endMenu()
    
def menucategoriastvshows(categorias, infos, fanarts, modes, posters, tags):
    xbmcplugin.setContent(addon_handle, 'albums')
    xbmcplugin.setPluginCategory(addon_handle, 'Categorias')
    serial = 'aHR0cDovL2Z1c2lvbm9yZy5uZXQvdHZzaG93cy9sYXRpbm8vaW5kZXgucGhwP3RhZz0='
    serial = base64.b64decode(serial)
    for categoria, info, fanart, mode, poster, tags in zip(categorias, infos, fanarts, modes, posters, tags):
        url = build_url({'mode':mode, 'direccion': serial+tags, 'categoria': categoria})
        li = xbmcgui.ListItem('[COLOR white][B]'+categoria+'[/B][/COLOR]')
        li.setInfo("video", {"Plot": info})
        li.setArt({'fanart': fanart, 'poster': poster})
        addMenuitem(url, li, True)
    endMenu()

def movieslist(web, mode, categoria):
    xbmcplugin.setContent(addon_handle, 'albums')
    xbmcplugin.setPluginCategory(addon_handle, categoria.title())
    data = read(web)
    matches = re.findall('<ppal(.*?)<\/ppal',data,re.MULTILINE)
    for match in matches:
        try:
            title = re.findall('titulo.*?lue=(.*?)\/>', match, re.MULTILINE)[0]
            title = base64.b64decode(title)
        except:
            try:
                title = re.findall('title.*?lue=(.*?)\/>', match, re.MULTILINE)[0]
                title = base64.b64decode(title)
            except:
                title = 'Sin Titulo (reportar video)'
        
        poster = re.findall('thumb.*?lue=(.*?)\/>', match, re.MULTILINE)[0]
        poster = base64.b64decode(poster)
        fanart = re.findall('fanart.*?lue=(.*?)\/>', match, re.MULTILINE)[0]
        fanart = base64.b64decode(fanart)
        sinopsis = re.findall('info.*?lue=(.*?)\/>', match, re.MULTILINE)[0]
        link = re.findall('link.*?lue=(.*?)\/>', match, re.MULTILINE)[0]
        link = base64.b64decode(link)
        year = re.findall('id=.year.*?lue=(.*?)\/>', match, re.MULTILINE)[0]
        yeari = int(base64.b64decode(year))
        years = base64.b64decode(year)

        url = build_url({'mode': mode, 'foldername': title, 'direccion': link, 'thumbnail': poster, 'fanart': fanart, 'info': sinopsis, 'year': years})
        li = xbmcgui.ListItem(iconImage=poster, thumbnailImage=poster)
        if yeari == 0:
            li.setInfo("video", {"Title": title, "Plot": sinopsis, "MediaType": "Movie", "OriginalTitle": title, "SortTitle": title})
        else:
            li.setInfo("video", {"Title": title, "Plot": sinopsis, "Year": yeari, "MediaType": "Movie", "OriginalTitle": title, "SortTitle": title})
        li.setArt({'fanart': fanart, 'poster': poster})
        li.setProperty('fanart_image', fanart)
        if years == '0' or years == '0000':
            title = '[COLOR white][B]'+title+'[/B][/COLOR]'
        else:
            title = '[COLOR white][B]'+title+'[/B][/COLOR]  [COLOR blue][B]('+years+')[/B][/COLOR]'
        li.setLabel(title)
        li.setLabel2(title)
        addMenuitem(url, li, True)
    endMenu()
    
def movieslistyear(web, mode, categoria):
    xbmcplugin.setContent(addon_handle, 'albums')
    xbmcplugin.setPluginCategory(addon_handle, categoria.title())
    dir_pos_pel = os.path.join(get_dir_addon(), 'resources', 'media', 'peliculas', 'poster')
    poster = os.path.join(dir_pos_pel, 'year.png')
    dir_fan_pel = os.path.join(get_dir_addon(), 'resources', 'media', 'peliculas', 'fanart')
    fanart = os.path.join(dir_fan_pel, 'fanart.png')
    data = read(web)
    matches = re.findall('<ppal(.*?)<\/ppal',data,re.MULTILINE)
    for match in matches:
        try:
            title = re.findall('titulo.*?lue=(.*?)\/>', match, re.MULTILINE)[0]
            title = base64.b64decode(title)
        except:
            try:
                title = re.findall('title.*?lue=(.*?)\/>', match, re.MULTILINE)[0]
                title = base64.b64decode(title)
            except:
                title = 'Sin Titulo (reportar video)'
        
        sinopsis = re.findall('info.*?lue=(.*?)\/>', match, re.MULTILINE)[0]
        link = re.findall('link.*?lue=(.*?)\/>', match, re.MULTILINE)[0]
        link = base64.b64decode(link)
        year = re.findall('id=.year.*?lue=(.*?)\/>', match, re.MULTILINE)[0]
        yeari = int(base64.b64decode(year))
        years = base64.b64decode(year)
        
        url = build_url({'mode': mode, 'foldername': title, 'direccion': link, 'thumbnail': poster, 'fanart': fanart, 'info': sinopsis, 'year': years, 'categoria': years})
        li = xbmcgui.ListItem(iconImage=poster, thumbnailImage=poster)
        if yeari == 0:
            li.setInfo("video", {"Title": title, "Plot": sinopsis, "MediaType": "Movie", "OriginalTitle": title, "SortTitle": title})
        else:
            li.setInfo("video", {"Title": title, "Plot": sinopsis, "Year": yeari, "MediaType": "Movie", "OriginalTitle": title, "SortTitle": title})
        li.setArt({'fanart': fanart, 'poster': poster})
        li.setProperty('fanart_image', fanart)
        if years == '0' or years == '0000':
            title = '[COLOR white][B]'+title+'[/B][/COLOR]'
        else:
            title = '[COLOR white][B]'+title+'[/B][/COLOR]  [COLOR blue][B]('+years+')[/B][/COLOR]'
        li.setLabel(title)
        li.setLabel2(title)
        addMenuitem(url, li, True)
    endMenu()

def tvshowslist(web,mode, categoria):
    xbmcplugin.setContent(addon_handle, 'tvshows')
    xbmcplugin.setPluginCategory(addon_handle, categoria.title())
    data = read(web)
    matches = re.findall('<ppal>(.*?)<\/ppal', data, re.MULTILINE)
    for match in matches:
        title = re.findall('titulo.*?value=(.*?)\/>', match, re.MULTILINE)[0]
        sinopsis = re.findall('info.*?value=(.*?)\/>', match, re.MULTILINE)[0]
        link = re.findall('link.*?value=(.*?)\/>', match, re.MULTILINE)[0]
        thumbnail = re.findall('thumbnail.*?value=(.*?)\/>', match, re.MULTILINE)[0]
        fanart = re.findall('fanart.*?value=(.*?)\/>', match, re.MULTILINE)[0]
        tmdbid = re.findall('tmdbid.*?value=(.*?)\/>', match, re.MULTILINE)[0]

        url = build_url({'mode': mode, 'direccion': link, 'fanart': fanart, 'info': sinopsis, 'tmdbid': tmdbid, 'serie': title})
        li = xbmcgui.ListItem(title, iconImage=thumbnail, thumbnailImage=thumbnail)
        li.setInfo("video", {"Title": title, "FileName": title, "Plot": sinopsis})
        li.setArt({'fanart': fanart, 'poster': thumbnail})
        li.setProperty('fanart_image', fanart)
        li.setLabel('[COLOR white][B]'+title+'[/B][/COLOR]')
        addMenuitem(url, li, True)
    endMenu()

def seasonlist(web,fanart,sinopsis,mode,tmdbid, serie):
    xbmcplugin.setContent(addon_handle, 'albums')
    xbmcplugin.setPluginCategory(addon_handle, serie.title())
    data = read(web)
    matches = re.findall('<season>(.*?)<\/season', data, re.MULTILINE)
    for match in matches:
        title = re.findall('temporada.*?value=(.*?)\/>', match, re.MULTILINE)[0]
        title = title.replace('Temporada','Temporada ')
        sinopsis = sinopsis
        link = re.findall('link.*?value=(.*?)\/>', match, re.MULTILINE)[0]
        thumbnail = re.findall('poster.*?value=(.*?)\/>', match, re.MULTILINE)[0]
        fanart = fanart

        url = build_url({'mode': mode, 'direccion': link, 'tmdbid': tmdbid, 'serie': serie})
        li = xbmcgui.ListItem(title, iconImage=thumbnail, thumbnailImage=thumbnail)
        li.setInfo("video", {"Title": title, "FileName": title, "Plot": sinopsis})
        li.setArt({'fanart': fanart, 'poster': thumbnail})
        li.setProperty('fanart_image', fanart)
        li.setLabel('[COLOR white][B]'+title+'[/B][/COLOR]')
        addMenuitem(url, li, True)
    endMenu()


def episodeslist(web, mode, tmdbid, serie):
    xbmcplugin.setContent(addon_handle, 'episodes')
    xbmcplugin.setPluginCategory(addon_handle, serie.title())
    data = read(web)
    matches = re.findall('<episodio>(.*?)<\/episodio', data, re.IGNORECASE)
    for match in matches:
        title = re.findall('title.*?value=(.*?)\/>', match, re.MULTILINE)[0]
        sinopsis = re.findall('sinopsis.*?value=(.*?)\/>', match, re.MULTILINE)[0]
        link = re.findall('link.*?value=(.*?)\/>', match, re.MULTILINE)[0]
        thumbnail = re.findall('thumbnail.*?value=(.*?)\/>', match, re.MULTILINE)[0]
        fanart = re.findall('fanart.*?value=(.*?)\/>', match, re.MULTILINE)[0]
        season = int(re.findall('S(.*?)E.*?', title)[0])
        episode = int(re.findall('.*?E(.*?)-', title)[0])
        url = build_url({'mode': mode, 'direccion': link, 'tmdbid': tmdbid, "episode": episode, "season": season, "serie": serie})
        li = xbmcgui.ListItem(iconImage=thumbnail, thumbnailImage=thumbnail)
        li.setInfo("video", {"Title": title, "FileName": title, "Plot": sinopsis})
        li.setProperty('fanart_image', fanart)
        li.setArt({'fanart': fanart, 'poster': thumbnail})
        li.setLabel('[COLOR white][B]'+title+'[/B][/COLOR]')
        addMenuitem(url, li, True)
    endMenu()

def servidores(titulo, thumbnail, fanart, sinopsis, url):
    xbmcplugin.setContent(addon_handle, 'movies')
    xbmcplugin.setPluginCategory(addon_handle, titulo.title())
    titulo = titulo.decode('utf-8')
    html = read(url)
    items = re.findall("<ppal>(.*?)<\/ppal>", html, re.MULTILINE)
    trailer = re.findall("trailer.*?value=(.*?)\/\>\<\/trailer", html, re.MULTILINE)[0]
    trailer = base64.b64decode(trailer)
    if trailer != 'novideo':
        titletrailer = '[COLOR orange][B]Trailer:[/B][/COLOR] [COLOR white][B]'+titulo+'[/B][/COLOR]'
        url = build_url({'mode': 'play', 'playlink': trailer, 'tmdbid': '0'})
        li = xbmcgui.ListItem(titletrailer, iconImage=thumbnail, thumbnailImage=thumbnail)
        li.setInfo("video", {"Title": titletrailer, "Plot": sinopsis})
        li.setArt({'fanart': fanart, 'poster': thumbnail})
        li.setProperty('IsPlayable', 'true')
        li.setProperty('fanart_image', fanart)
        addMenuitem(url, li, False)
    tmdbid = re.findall("tmdbid.*?value=(.*?)\/\>\<\/tmdbid", html, re.MULTILINE)[0]
    tmdbid = base64.b64decode(tmdbid)
    year = re.findall("year.*?value=(.*?)\/\>\<\/year", html, re.MULTILINE)[0]
    year = base64.b64decode(year)
    for item in items:
        url = re.findall('link.*?value=(.*?)\/\>\<\/br\>', item, re.IGNORECASE)[0]
        url = base64.b64decode(url)
        if url != '':
            servidores3(url,titulo,thumbnail,fanart,sinopsis,tmdbid,year,season='',episode='')
    endMenu()

def servidores2(web,tmdbid,season,episode, serie):
    xbmcplugin.setContent(addon_handle, 'episodes')
    xbmcplugin.setPluginCategory(addon_handle, serie.title())
    data = read(web)
    matches = re.findall('<episodio>(.*?)<\/episodio', data, re.MULTILINE)
    for match in matches:
        name = re.findall('title.*?value=(.*?)\/>', match, re.MULTILINE)[0]
        sinopsis = re.findall('sinopsis.*?value=(.*?)\/>', match, re.MULTILINE)[0]
        url = re.findall('link.*?value=(.*?)\/>', match, re.MULTILINE)[0]
        thumbnail = re.findall('thumbnail.*?value=(.*?)\/>', match, re.MULTILINE)[0]
        fanart = re.findall('fanart.*?value=(.*?)\/>', match, re.MULTILINE)[0]
        if url != '':
            name = name.decode('utf-8')
            servidores3(url,name,thumbnail,fanart,sinopsis,tmdbid,'',season,episode)
    endMenu()

def servidores3(url,titulo,thumbnail,fanart,sinopsis,tmdbid,year='',season='',episode=''):
    video_info = {}
    video_info['Title'] = titulo
    video_info['FileName'] = titulo
    video_info['Plot'] = sinopsis
    if year != '':
            video_info['Year'] = year
    if season != '':
            video_info['Season'] = season
    if episode != '':
            video_info['Episode'] = episode       
    if 'rapidvideo.com' in url:
        if '/d/' in url:
            url = url.replace('/d/', '/v/')
        if '/embed/' in url:
            url = url.replace('/embed/', '/v/')
        if '/e/' in url:
            url = url.replace('/e/', '/v/')
        if '?v=' in url:
            url = url.replace('?v=', '/v/')
        try:
            data = read2(url)
            try:
                calidades = re.findall('<a href="(.*rapidvideo.*q\=.*p)"',data, re.IGNORECASE)
            except HTTPError as e:
                mensaje = 'No Funciona'
            except URLError as e:
                mensaje = 'No Funciona'
 
            video_info['Title'] = '[COLOR orange][B][Rapidvideo=Directo][/B][/COLOR] [COLOR white][B]'+titulo+'[/B][/COLOR]'
            if year != '':
                video_info['Title'] = video_info['Title'] + ' [COLOR blue][B]('+year+')[/B][/COLOR]'
            urld = build_url({'mode': 'play', 'playlink': url, 'tmdbid': tmdbid})
            li = xbmcgui.ListItem(video_info['FileName'], iconImage=thumbnail, thumbnailImage=thumbnail)
            li.setInfo("video", video_info)
            li.setProperty('IsPlayable', 'true')
            li.setProperty('fanart_image', fanart)
            li.setArt({'fanart': fanart, 'poster': thumbnail})
            addMenuitem(urld, li, False)
            
        except HTTPError as e:
            mensaje = 'No Funciona'
        except URLError as e:
            mensaje = 'No Funciona'
        else:

            for calidad in calidades:
                if '360' in calidad:
                    video_info['Title'] = '[COLOR orange][B][Rapidvideo=360p][/B][/COLOR] [COLOR white][B]'+titulo+'[/B][/COLOR]'
                    if year != '':
                        video_info['Title'] = video_info['Title'] + ' [COLOR blue][B]('+year+')[/B][/COLOR]'
                    url = build_url({'mode': 'play', 'playlink': calidad, 'tmdbid': tmdbid})
                    li = xbmcgui.ListItem(video_info['Title'], iconImage=thumbnail, thumbnailImage=thumbnail)
                    li.setInfo("video", video_info)
                    li.setProperty('IsPlayable', 'true')
                    li.setProperty('fanart_image', fanart)
                    li.setArt({'fanart': fanart, 'poster': thumbnail})
                    addMenuitem(url, li, False)

                elif '480' in calidad:
                    video_info['Title'] = '[COLOR orange][B][Rapidvideo=480p][/B][/COLOR] [COLOR white][B]'+titulo+'[/B][/COLOR]'
                    if year != '':
                        video_info['Title'] = video_info['Title'] + ' [COLOR blue][B]('+year+')[/B][/COLOR]'
                    url = build_url({'mode': 'play', 'playlink': calidad, 'tmdbid': tmdbid})
                    li = xbmcgui.ListItem(video_info['Title'], iconImage=thumbnail, thumbnailImage=thumbnail)
                    li.setInfo("video", video_info)
                    li.setProperty('IsPlayable', 'true')
                    li.setProperty('fanart_image', fanart)
                    li.setArt({'fanart': fanart, 'poster': thumbnail})
                    addMenuitem(url, li, False)

                elif '720' in calidad:
                    video_info['Title'] = '[COLOR orange][B][Rapidvideo=720p][/B][/COLOR] [COLOR white][B]'+titulo+'[/B][/COLOR]'
                    if year != '':
                        video_info['Title'] = video_info['Title'] + ' [COLOR blue][B]('+year+')[/B][/COLOR]'
                    url = build_url({'mode': 'play', 'playlink': calidad, 'tmdbid': tmdbid})
                    li = xbmcgui.ListItem(video_info['Title'], iconImage=thumbnail, thumbnailImage=thumbnail)
                    li.setInfo("video", video_info)
                    li.setProperty('IsPlayable', 'true')
                    li.setProperty('fanart_image', fanart)
                    li.setArt({'fanart': fanart, 'poster': thumbnail})
                    addMenuitem(url, li, False)

                elif '1080' in calidad:
                    video_info['Title'] = '[COLOR orange][B][Rapidvideo=1080p][/B][/COLOR] [COLOR white][B]'+titulo+'[/B][/COLOR]'
                    if year != '':
                        video_info['Title'] = video_info['Title'] + ' [COLOR blue][B]('+year+')[/B][/COLOR]'
                    url = build_url({'mode': 'play', 'playlink': calidad, 'tmdbid': tmdbid})
                    li = xbmcgui.ListItem(video_info['Title'], iconImage=thumbnail, thumbnailImage=thumbnail)
                    li.setInfo("video", video_info)
                    li.setProperty('IsPlayable', 'true')
                    li.setProperty('fanart_image', fanart)
                    li.setArt({'fanart': fanart, 'poster': thumbnail})
                    addMenuitem(url, li, False)

    elif 'drive.google.com' in url:
        from base.servers import gvideo
        try:
            calidades = gvideo.google_calidades(url)
            for calidad in calidades:
                video_info['Title'] = '[COLOR orange][B][Gvideo='+calidad+'][/B][/COLOR] [COLOR white][B]'+titulo+'[/B][/COLOR]'
                if year != '':
                    video_info['Title'] = video_info['Title'] + ' [COLOR blue][B]('+year+')[/B][/COLOR]'
                url2 = build_url({'mode': 'play', 'playlink': url + '&q=' + calidad, 'tmdbid': tmdbid})
                li = xbmcgui.ListItem(video_info['Title'], iconImage=thumbnail, thumbnailImage=thumbnail)
                li.setInfo("video", video_info)
                li.setProperty('IsPlayable', 'true')
                li.setProperty('fanart_image', fanart)
                li.setArt({'fanart': fanart, 'poster': thumbnail})
                addMenuitem(url2, li, False)
        except:
            pass

    elif 'clipwatching.com' in url:
        calidades = calidadesclipwatching(url)
        if calidades != 'dead':
            for calidad in calidades:
                video_info['Title'] = '[COLOR orange][B][Clipwatching='+calidad+'][/B][/COLOR] [COLOR white][B]'+titulo+'[/B][/COLOR]'
                if year != '':
                    video_info['Title'] = video_info['Title'] + ' [COLOR blue][B]('+year+')[/B][/COLOR]'
                url2 = build_url({'mode': 'play', 'playlink': url + '&q=' + calidad, 'tmdbid': tmdbid})
                li = xbmcgui.ListItem(video_info['Title'], iconImage=thumbnail, thumbnailImage=thumbnail)
                li.setInfo("video", video_info)
                li.setProperty('IsPlayable', 'true')
                li.setProperty('fanart_image', fanart)
                li.setArt({'fanart': fanart, 'poster': thumbnail})
                addMenuitem(url2, li, False)

    elif 'gamovideo.com' in url:
        video_info['Title'] = '[COLOR orange][B][Gamovideo][/B][/COLOR] [COLOR white][B]'+titulo+'[/B][/COLOR]'
        if year != '':
            video_info['Title'] = video_info['Title'] + ' [COLOR blue][B]('+year+')[/B][/COLOR]'
        url = build_url({'mode': 'play', 'playlink': url, 'tmdbid': tmdbid})
        li = xbmcgui.ListItem(video_info['Title'], iconImage=thumbnail, thumbnailImage=thumbnail)
        li.setInfo("video", video_info)
        li.setProperty('IsPlayable', 'true')
        li.setProperty('fanart_image', fanart)
        li.setArt({'fanart': fanart, 'poster': thumbnail})
        addMenuitem(url, li, False)
        
    elif 'streamango.com' in url:
        video_info['Title'] = '[COLOR orange][B][Streamango][/B][/COLOR] [COLOR white][B]'+titulo+'[/B][/COLOR]'
        if year != '':
            video_info['Title'] = video_info['Title'] + ' [COLOR blue][B]('+year+')[/B][/COLOR]'
        url = build_url({'mode': 'play', 'playlink': url, 'tmdbid': tmdbid})
        li = xbmcgui.ListItem(video_info['Title'], iconImage=thumbnail, thumbnailImage=thumbnail)
        li.setInfo("video", video_info)
        li.setProperty('IsPlayable', 'true')
        li.setProperty('fanart_image', fanart)
        li.setArt({'fanart': fanart, 'poster': thumbnail})
        addMenuitem(url, li, False)
        
    elif 'openload.' in url:
        video_info['Title'] = '[COLOR orange][B][Openload][/B][/COLOR] [COLOR white][B]'+titulo+'[/B][/COLOR]'
        if year != '':
            video_info['Title'] = video_info['Title'] + ' [COLOR blue][B]('+year+')[/B][/COLOR]'
        url = build_url({'mode': 'play', 'playlink': url, 'tmdbid': tmdbid})
        li = xbmcgui.ListItem(video_info['Title'], iconImage=thumbnail, thumbnailImage=thumbnail)
        li.setInfo("video", video_info)
        li.setProperty('IsPlayable', 'true')
        li.setProperty('fanart_image', fanart)
        li.setArt({'fanart': fanart, 'poster': thumbnail})
        addMenuitem(url, li, False)
        
    elif 'uptobox.com' in url:
        servers = uptoboxtest(url,tmdbid)
        if len(servers)>0:
            for server in servers:
                if server == 'uptostream':
                    for calidad in servers['uptostream']:
                        video_info['Title'] = '[COLOR orange][B]' + servers['uptostream'][calidad][0] + '[/B][/COLOR] [COLOR white][B]'+titulo+'[/B][/COLOR]'
                        if year != '':
                            video_info['Title'] = video_info['Title'] + ' [COLOR blue][B]('+year+')[/B][/COLOR]'
                        url = build_url({'mode': 'play', 'playlink': servers['uptostream'][calidad][1], 'tmdbid': tmdbid})
                        li = xbmcgui.ListItem(video_info['Title'], iconImage=thumbnail, thumbnailImage=thumbnail)
                        li.setInfo("video", video_info)
                        li.setProperty('IsPlayable', 'true')
                        li.setProperty('fanart_image', fanart)
                        li.setArt({'fanart': fanart, 'poster': thumbnail})
                        addMenuitem(url, li, False)
                
                if server == 'uptobox':
                    for calidad in servers['uptobox']:
                        video_info['Title'] = '[COLOR orange][B]' + servers['uptobox'][calidad][0] + '[/B][/COLOR] [COLOR white][B]'+titulo+'[/B][/COLOR]'
                        if year != '':
                            video_info['Title'] = video_info['Title'] + ' [COLOR blue][B]('+year+')[/B][/COLOR]'
                        url = build_url({'mode': 'play', 'playlink': servers['uptobox'][calidad][1], 'tmdbid': tmdbid})
                        li = xbmcgui.ListItem(video_info['Title'], iconImage=thumbnail, thumbnailImage=thumbnail)
                        li.setInfo("video", video_info)
                        li.setProperty('IsPlayable', 'true')
                        li.setProperty('fanart_image', fanart)
                        li.setArt({'fanart': fanart, 'poster': thumbnail})
                        addMenuitem(url, li, False)
               
    elif 'uptostream.com' in url:
        servers = uptostreamtest(url,tmdbid)
        if len(servers)>0:
            for server in servers:
                if server == 'uptostream':
                    for calidad in servers['uptostream']:
                        video_info['Title'] = '[COLOR orange][B]' + servers['uptostream'][calidad][0] + '[/B][/COLOR] [COLOR white][B]'+titulo+'[/B][/COLOR]'
                        if year != '':
                            video_info['Title'] = video_info['Title'] + ' [COLOR blue][B]('+year+')[/B][/COLOR]'
                        url = build_url({'mode': 'play', 'playlink': servers['uptostream'][calidad][1], 'tmdbid': tmdbid})
                        li = xbmcgui.ListItem(video_info['Title'], iconImage=thumbnail, thumbnailImage=thumbnail)
                        li.setInfo("video", video_info)
                        li.setProperty('IsPlayable', 'true')
                        li.setProperty('fanart_image', fanart)
                        li.setArt({'fanart': fanart, 'poster': thumbnail})
                        addMenuitem(url, li, False)
                
                if server == 'uptobox':
                    for calidad in servers['uptobox']:
                        video_info['Title'] = '[COLOR orange][B]' + servers['uptobox'][calidad][0] + '[/B][/COLOR] [COLOR white][B]'+titulo+'[/B][/COLOR]'
                        if year != '':
                            video_info['Title'] = video_info['Title'] + ' [COLOR blue][B]('+year+')[/B][/COLOR]'
                        url = build_url({'mode': 'play', 'playlink': servers['uptobox'][calidad][1], 'tmdbid': tmdbid})
                        li = xbmcgui.ListItem(video_info['Title'], iconImage=thumbnail, thumbnailImage=thumbnail)
                        li.setInfo("video", video_info)
                        li.setProperty('IsPlayable', 'true')
                        li.setProperty('fanart_image', fanart)
                    	li.setArt({'fanart': fanart, 'poster': thumbnail})
                        addMenuitem(url, li, False)

def search():
    xbmcplugin.setContent(addon_handle, 'albums')
    website= 'http://fusionorg.net/searching.php?'
    kb = xbmc.Keyboard('default', 'heading')
    kb.setDefault('')
    kb.setHeading('Buscar en la Coleccion Fusion')
    kb.setHiddenInput(False)
    kb.doModal()
    if (kb.isConfirmed()):
        if kb.getText() == '':
            duration = 3500
            dialog = xbmcgui.Dialog()
            dialog.notification("Fusion", 'No se detecto nada escrito en el buscador Vuelve a Intentar',
                                xbmcgui.NOTIFICATION_INFO, duration, False)
        else:
            search_term = kb.getText()
            xbmcplugin.setPluginCategory(addon_handle, 'Buscar: '+search_term.title())
            search_term = urllib.urlencode({'search': search_term})
            dir = website + search_term
            html = read(dir)
            pattern = "<ppal>(.*?)<\/ppal>"

            matches = re.findall('<ppalseries>(.*?)<\/ppalseries', html, re.MULTILINE)
            for match in matches:
                title = re.findall('titulo.*?value=(.*?)\/>', match, re.MULTILINE)[0]
                sinopsis = re.findall('info.*?value=(.*?)\/>', match, re.MULTILINE)[0]
                link = re.findall('link.*?value=(.*?)\/>', match, re.MULTILINE)[0]
                thumbnail = re.findall('thumbnail.*?value=(.*?)\/>', match, re.MULTILINE)[0]
                fanart = re.findall('fanart.*?value=(.*?)\/>', match, re.MULTILINE)[0]
                tmdbid = re.findall('tmdbid.*?value=(.*?)\/>', match, re.MULTILINE)[0]
                url = build_url({'mode': 'seasons', 'direccion': link, 'fanart': fanart, 'info': sinopsis, 'tmdbid': tmdbid, 'serie': title})
                title = '[COLOR white][B]'+title+'[/B][/COLOR]  [COLOR orange][B][TV Show][/B][/COLOR]'
                li = xbmcgui.ListItem(title, iconImage=thumbnail, thumbnailImage=thumbnail)
                li.setInfo("video", {"Title": title, "FileName": title, "Plot": sinopsis})
                li.setProperty('fanart_image', fanart)
                li.setArt({'fanart': fanart, 'poster': thumbnail})
                addMenuitem(url, li, True)

            items = re.findall(pattern, html, re.MULTILINE)
            for item in items:
                # Not the better way to parse XML, but clean and easy
                try:
        		    title = re.findall('.*titulo.*?=(.*?)\/>', item, re.MULTILINE)[0]
        		    title = base64.b64decode(title)
                except:
        		    try:
        		        title = re.findall('.*title.*?=(.*?)\/>', item, re.MULTILINE)[0]
        		        title = base64.b64decode(title)
        		    except:
        		        title = 'Sin Titulo (reportar video)'
        
                pattern = '.*info.*?=(.*?)\/>'
                plot = re.findall(pattern, item, re.IGNORECASE)[0]

                pattern = '.*thum.*?=(.*?)\/>'
                thumbnail = re.findall(pattern, item, re.IGNORECASE)[0]
                thumbnail = base64.b64decode(thumbnail)

                pattern = '.*fanart.*?=(.*?)\/>'
                fanart = re.findall(pattern, item, re.IGNORECASE)[0]
                fanart = base64.b64decode(fanart)

                pattern = '.*lin.*?=(.*?)\/>'
                url = re.findall(pattern, item, re.IGNORECASE)[0]
                url = base64.b64decode(url)
                
                year = re.findall('id=.year.*?lue=(.*?)\/>', item, re.IGNORECASE)[0]
                yeari = int(base64.b64decode(year))
                years = base64.b64decode(year)
                
                url = build_url({'mode': 'servidores', 'foldername': title, 'direccion': url, 'thumbnail': thumbnail, 'fanart': fanart, 'info': plot, 'year': years})
                li = xbmcgui.ListItem(iconImage=thumbnail, thumbnailImage=thumbnail)
                li.setInfo("video", {"Title": title, "Plot": plot, "Year": yeari, "MediaType": "Movie", "OriginalTitle": title, "SortTitle": title})
                li.setProperty('fanart_image', fanart)
                li.setArt({'fanart': fanart, 'poster': thumbnail})
                li.setLabel('[COLOR white][B]'+title+'[/B][/COLOR] [COLOR blue][B]('+years+')[/B][/COLOR] [COLOR orange][B][Pelicula][/B][/COLOR]')
                li.setLabel2('[COLOR white][B]'+title+'[/B][/COLOR] [COLOR blue][B]('+years+')[/B][/COLOR] [COLOR orange][B][Pelicula][/B][/COLOR]')
                addMenuitem(url, li, True)
                
            matches = re.findall('<ppalcollections(.*?)<\/ppalcollections',html,re.MULTILINE)
            for match in matches:
                id = re.findall('id.*?lue=(.*?)\/>', match, re.MULTILINE)[0]
                id = base64.b64decode(id)
                sinopsis = re.findall('info.*?lue=(.*?)\/>', match, re.MULTILINE)[0]
                sinopsis = base64.b64decode(sinopsis)
                titulo = re.findall('titulo.*?lue=(.*?)\/>', match, re.MULTILINE)[0]
                titulo = base64.b64decode(titulo)
                link = re.findall('link.*?lue=(.*?)\/>', match, re.MULTILINE)[0]
                link = base64.b64decode(link)
                poster = re.findall('thumb.*?lue=(.*?)\/>', match, re.MULTILINE)[0]
                poster = base64.b64decode(poster)
                fanart = re.findall('fanart.*?lue=(.*?)\/>', match, re.MULTILINE)[0]
                fanart = base64.b64decode(fanart)
                url = build_url({'mode': 'movies', 'foldername': titulo, 'direccion': link, 'thumbnail': poster, 'fanart': fanart, 'info': sinopsis, 'categoria': titulo})
                titulo = '[COLOR white][B]'+titulo+'[/B][/COLOR]  [COLOR orange][B][Coleccion][/B][/COLOR]'
                li = xbmcgui.ListItem(titulo, iconImage=poster, thumbnailImage=poster)
                li.setInfo("video", {"Title": titulo, "FileName": titulo, "Plot": sinopsis})
                li.setArt({'fanart': fanart, 'poster': poster})
                li.setProperty('fanart_image', fanart)
                addMenuitem(url, li, True)
            endMenu()
    else:
        dialog = xbmcgui.Dialog()
        dialog.notification("Fusion", 'La Busqueda se cancelo',
                            xbmcgui.NOTIFICATION_INFO, 3500 , False)
def reproductor(url,tmdbid=''):
    if tmdbid != '':
        ids = json.dumps({'tmdb': tmdbid})
        xbmcgui.Window(10000).setProperty('script.trakt.ids', ids)
    if 'drive.google.com' in url:
        from base.servers import gvideo
        final_link = gvideo.google_final_link(url)
        play_video(final_link)
    elif 'rapidvideo' in url:
        data2 = read2(url)
        try:
            final_link = re.findall('source src=\"(.*?)\"',data2,re.MULTILINE)[0]
        except:
            try:
                final_link = re.findall('src: \"(.*?)\"',data2,re.MULTILINE)[0]
            except:
                return
        header_test = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
        header_test = '|' + urllib.urlencode(header_test)
        play_video(final_link + header_test)
    elif 'gamovideo' in url:
        final_link = urlgamovideo(url)
        if 'File was locked by administrator' in final_link:
            duration = 5500  # in milliseconds
            message = 'Contenido Bloqueado'
            dialog = xbmcgui.Dialog()
            dialog.notification("Fusion", message,
                                xbmcgui.NOTIFICATION_INFO, duration , False)
            return
        play_video(final_link)
    elif 'clipwatching.com' in url:
        final_link = urlclipwatching(url)
        play_video(final_link)
    elif 'streamango' in url:
        final_link = get_video_streamango(url)
        play_video(final_link)
    elif 'openload' in url:
        final_link = get_video_openload(url)
        play_video(final_link)
    elif 'uptobox' in url:
        echo, final_link = uptobox(url,tmdbid)
        if echo:
            play_video(final_link)
        else:
            duration = 5500  # in milliseconds
            if final_link == '':
                message = 'UPTOBOX Fallo al obtener Link'
            else:
                message = final_link
            dialog = xbmcgui.Dialog()
            dialog.notification("Fusion", message,
                                xbmcgui.NOTIFICATION_INFO, duration , False)
            xbmc.executebuiltin("XBMC.Container.Refresh")
                
    elif 'uptostream' in url:
        echo, final_link, subtitles = uptostream(url)
        if echo:
            play_video(final_link, subtitles)
        else:
            if final_link == '':
                message = 'UPTOSTREAM Fallo al obtener Link'
            else:
                message = final_link
            duration = 5500  # in milliseconds
            dialog = xbmcgui.Dialog()
            dialog.notification("Fusion", message,
                                xbmcgui.NOTIFICATION_INFO, duration , False)
            xbmc.executebuiltin("XBMC.Container.Refresh")
    elif 'youtube' in url:
        play_video(url)
    else:
        play_video(url)

def play_video(path, subtitles = []):
    play_item = xbmcgui.ListItem(path=path)
    if len(subtitles) > 0:
        play_item.setSubtitles(subtitles)
    vid_url = play_item.getfilename()
    if 'uptostream' in path or 'uptobox' in path or 'oload' in path or 'clipwatching' in path or 'streamango' in path:
        duration = 5500  # in milliseconds
        message = 'En Breve empezara la Reproduccion'
        dialog = xbmcgui.Dialog()
        dialog.notification("Fusion", message,
                            xbmcgui.NOTIFICATION_INFO, duration , False)
        xbmcplugin.setResolvedUrl(addon_handle, True, listitem=play_item)
    else:
        try:
            stream_url = resolve_url(vid_url)
            if stream_url:
                play_item.setPath(stream_url)
        # Pass the item to the Kodi player.
        except:
            pass
        xbmcplugin.setResolvedUrl(addon_handle, True, listitem=play_item)

def resolve_url(url):
    duration = 5500  # in milliseconds
    message = "En Breve empezara la Reproduccion"
    stream_url = urlresolver.HostedMediaFile(url=url).resolve()
    # If urlresolver returns false then the video url was not resolved.
    if not stream_url:
        dialog = xbmcgui.Dialog()
        dialog.notification("Fusion", message,
                            xbmcgui.NOTIFICATION_INFO, duration, False)
        return False
    else:
        return stream_url

def get_dir_addon():
    return xbmc.translatePath(addon.getAddonInfo('Path'))

def collections_list(categorias, urls, posters, fanarts, infos, modes):
    xbmcplugin.setContent(addon_handle, 'albums')
    xbmcplugin.setPluginCategory(addon_handle, 'Colleciones')
    for categoria, info, fanart, mode, poster, url in zip(categorias, infos, fanarts, modes, posters, urls):
        url = build_url({'mode':mode, 'direccion': url, 'categoria': categoria})
        li = xbmcgui.ListItem('[COLOR white][B]'+categoria+'[/B][/COLOR]')
        li.setInfo("video", {"Plot": info})
        li.setArt({'fanart': fanart, 'poster': poster})
        addMenuitem(url, li, True)
    endMenu()

def collection_list(web,categoria, mode = 'movies'):
    xbmcplugin.setContent(addon_handle, 'albums')
    xbmcplugin.setPluginCategory(addon_handle, categoria.title())
    data = read(web)
    matches = re.findall('<ppal(.*?)<\/ppal',data,re.MULTILINE)
    for match in matches:
        id = re.findall('id.*?lue=(.*?)\/>', match, re.MULTILINE)[0]
        id = base64.b64decode(id)
        sinopsis = re.findall('info.*?lue=(.*?)\/>', match, re.MULTILINE)[0]
        sinopsis = base64.b64decode(sinopsis)
        titulo = re.findall('titulo.*?lue=(.*?)\/>', match, re.MULTILINE)[0]
        titulo = base64.b64decode(titulo)
        link = re.findall('link.*?lue=(.*?)\/>', match, re.MULTILINE)[0]
        link = base64.b64decode(link)
        poster = re.findall('thumb.*?lue=(.*?)\/>', match, re.MULTILINE)[0]
        poster = base64.b64decode(poster)
        fanart = re.findall('fanart.*?lue=(.*?)\/>', match, re.MULTILINE)[0]
        fanart = base64.b64decode(fanart)
        url = build_url({'mode': mode, 'foldername': titulo, 'direccion': link, 'thumbnail': poster, 'fanart': fanart, 'info': sinopsis, 'categoria': titulo})
        titulo = '[COLOR white][B]'+titulo+'[/B][/COLOR]'
        li = xbmcgui.ListItem(titulo, iconImage=poster, thumbnailImage=poster)
        li.setInfo("video", {"Title": titulo, "FileName": titulo, "Plot": sinopsis})
        li.setArt({'fanart': fanart, 'poster': poster})
        li.setProperty('fanart_image', fanart)
        addMenuitem(url, li, True)
    endMenu()


