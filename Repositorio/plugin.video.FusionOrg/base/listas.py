import urllib
import urllib2
import re
import os
import xbmc
import xbmcplugin
import xbmcgui
import xbmcaddon
import xbmcvfs
import traceback
import cookielib,base64
import sys
import tools
import json
import hashlib
import requests

addon = xbmcaddon.Addon()
addon_dir = xbmc.translatePath(xbmc.translatePath(addon.getAddonInfo('Path')).decode('utf-8'))
addon_data_dir = xbmc.translatePath(xbmc.translatePath(addon.getAddonInfo('profile')).decode('utf-8'))
default_poster = os.path.join(addon_dir, 'resources','media','default_poster_list.jpg')
default_fanart = os.path.join(addon_dir, 'resources','media','default_fan_list.jpg')
icon = os.path.join(addon_dir, 'icon.png')
my_lists_file_path = addon_data_dir + '/my_lists.json'
my_shared_lists_file_path = addon_data_dir + '/my_shared_lists.json'
base_url = sys.argv[0] 
addon_handle = int(sys.argv[1])
username = addon.getSetting('username')
password = addon.getSetting('password')
addonname   = addon.getAddonInfo('name')
server = 'http://fusionorg.net/'

def get_poster (poster = None):
    if poster == "default" or poster == '' or poster == None:
        poster = default_poster
    return poster

def get_fanart (fanart = None):
    if fanart == "default" or fanart == '' or fanart == None:
        fanart = default_fanart
    return fanart

def get_synopsis(title, synopsis = None):
    if synopsis == "default" or synopsis == '' or synopsis == None:
        synopsis = 'Lista ' + title
    return synopsis

def makeRequest(url, headers=None):
    try:
        if headers is None:
            headers = {'User-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0'}
        if '|' in url:
            url,header_in_page=url.split('|')
            header_in_page=header_in_page.split('&')
            
            for h in header_in_page:
                if len(h.split('='))==2:
                    n,v=h.split('=')
                else:
                    vals=h.split('=')
                    n=vals[0]
                    v='='.join(vals[1:])
                    #n,v=h.split('=')
                headers[n]=v
                
        req = urllib2.Request(url,None,headers)
        response = urllib2.urlopen(req)
        data = response.read()
        response.close()
        return data
    except urllib2.URLError, e:
        if hasattr(e, 'code'):
            xbmc.executebuiltin("XBMC.Notification(FusionOrg, Fallo al obtener la lista, codigo - "+str(e.code)+",10000,"+icon+")")
        elif hasattr(e, 'reason'):
            xbmc.executebuiltin("XBMC.Notification(FusionOrg, No puede conectar al servidor. - "+str(e.reason)+",10000,"+icon+")")

def add_Menu_item(mode, link, title = '', rating = None, score = None, votes = None, synopsis = None, 
                  fanart = None, poster = None, contextMenu = None, folder = False):
    li = xbmcgui.ListItem(title)
    label = title
    if not (rating == '' or rating == None):
        label = label + ' [COLOR yellow]R=' + rating + '[/COLOR]'
        li.setInfo("video", {"rating": rating})
        li.setInfo("video", {"userrating": rating})
        
    if not (score == '' or score == None):
        label = label + ' [COLOR blue]P=' + score + '[/COLOR]'
        
    if not(votes == '' or votes == None):
        li.setRating("FusionOrg", float(rating), int(votes))
        li.setInfo("video", {"votes": votes})
    
    if not contextMenu == [] or not contextMenu == '' or not contextMenu == None:
        li.addContextMenuItems(contextMenu)
        
    poster = get_poster(poster)
    fanart = get_fanart(fanart)
    synopsis = get_synopsis(title, synopsis)
    
    url = build_url({'mode':mode, 'link': link})
    li.setInfo("video", {"plot": synopsis})
    li.setArt({'fanart': fanart, 'poster': poster})
    li.setLabel(label)
    li.setPath(path=url)
    return xbmcplugin.addDirectoryItem(handle=addon_handle, url = url, listitem = li, isFolder = folder)

def end_menu():
    xbmcplugin.endOfDirectory(addon_handle)

def build_url(query):
    return base_url + '?' + urllib.urlencode(query)

def message(message):
    xbmcgui.Dialog().ok(addonname, message)

def upload_list(file_path, name, type, sha, synopsis, poster, fanart):
    s = requests.Session()
    data = {'email':username,'password':password}
    url = server + "checklogin.php"
    r = s.post(url, data=data)
    texto = str(s.cookies)
    cookie = re.findall('.*?(PHPSESSID=.*?) .*',texto,re.MULTILINE)[0]
    headers = {'User-Agent':'FusionOrgByTeamFusion/1.0', 'Connection':'keep-alive', 'Cookie': cookie,
               'Host':'fusionorg.net','Referer':'http://fusionorg.net/index.php'}
    url2 = server + "uploadv2.php"

    if type == 'online':
        url_list = file_path
        file = ''
        file_data = ''
    elif type == 'file':
        file = open(file_path)
        file_data = file.read()
        url_list = ''
    d = requests.post(url2, headers = headers, files = {'name': (None, name), 'type_list': (None, type), 'sha': (None, sha), 'synopsis': (None, synopsis),
                                                        'poster': (None, poster), 'fanart': (None, fanart), 'link': (None, url_list), 
                                                        'file': (file, file_data,'application/octet-stream')})
    
    return d.text

def add_my_list(url=None):
    not_str = ''
    source_url = ''
    if url is None:
        if not addon.getSetting("new_file_list") == "":
           source_url = addon.getSetting('new_file_list').decode('utf-8')
        elif not addon.getSetting("new_url_list") == "":
           source_url = addon.getSetting('new_url_list').decode('utf-8')
    if source_url == '' or source_url is None:
        not_str = ' informacion de la lista.'
        xbmc.executebuiltin("XBMC.Notification(FusionOrg,Falta"+not_str+" ,10000,"+icon+")")
        addon.openSettings()
        return
    if addon.getSetting("new_name_list") == "":
        not_str = ' nombre de la lista.'
        xbmc.executebuiltin("XBMC.Notification(FusionOrg,Falta"+not_str+" ,10000,"+icon+")")
        addon.openSettings()
        return
    
    new_list = {}
    new_list['name'] = addon.getSetting("new_name_list").decode('utf-8')
    new_list['link'] = source_url
    new_list['poster'] = get_poster(addon.getSetting("new_poster_list").decode('utf-8'))
    new_list['fanart'] = get_fanart(addon.getSetting("new_fanart_list").decode('utf-8'))
    new_list['synopsis'] = get_synopsis(addon.getSetting("new_synopsis_list").decode('utf-8'), new_list['name'])
    
    if os.path.exists(my_lists_file_path)==False:
        my_lists = []
    else:
        my_lists = json.loads(open(my_lists_file_path,"r").read())
    
    my_lists.append(new_list)
    b = open(my_lists_file_path,"w")
    b.write(json.dumps(my_lists))
    b.close()
   
    addon.setSetting('new_file_list', "")
    addon.setSetting('new_url_list', "")
    addon.setSetting('new_name_list', "")
    addon.setSetting('new_poster_list', "")
    addon.setSetting('new_fanart_list', "")
    addon.setSetting('new_synopsis_list', "")
   
    xbmc.executebuiltin("XBMC.Notification(FusionOrg,Lista Agregada,5000,"+icon+")")
    addon.openSettings()

def add_shared_list(url=None):
    not_str = ''
    source_url = ''
    type_list = ''
    
    if username == '' or username == None or password == '' or password == None:
         xbmc.executebuiltin("XBMC.Notification(FusionOrg,Requiere registrarse en www.fusionorg.net y" +
                             " configurar su usuario en el addon ,10000,"+icon+")")
         addon.openSettings()
         return
     
    sha_list = hashlib.sha1()
    
    if url is None:
        if not addon.getSetting("new_file_share_list") == "":
            source_url = addon.getSetting('new_file_share_list').decode('utf-8')
            type_list = 'file'
            try:
                if os.path.exists(file)==True:
                    data = open(file,'r')
                    data = data.read()
                    sha_list.update(data)
                else:
                    xbmc.executebuiltin("XBMC.Notification(FusionOrg, No existe la lista!!!,5000,"+icon+")")
            except:
                pass 
        elif not addon.getSetting("new_url_share_list") == "":
           source_url = addon.getSetting('new_url_share_list').decode('utf-8')
           type_list = 'online'
           sha_list.update(source_url)
    if source_url == '' or source_url is None:
        not_str = ' informacion de la lista a compartir.'
        xbmc.executebuiltin("XBMC.Notification(FusionOrg,Falta"+not_str+" ,10000,"+icon+")")
        addon.openSettings()
        return
    if addon.getSetting("new_name_share_list") == "":
        not_str = ' nombre de la lista a compartir.'
        xbmc.executebuiltin("XBMC.Notification(FusionOrg,Falta"+not_str+" ,10000,"+icon+")")
        addon.openSettings()
        return
    
    new_list = {}
    new_list['name'] = addon.getSetting("new_name_share_list").decode('utf-8')
    new_list['link'] = source_url
    if  'http' in addon.getSetting("new_poster_share_list").decode('utf-8'):
        new_list['poster'] = addon.getSetting("new_poster_share_list").decode('utf-8')
    else:
        new_list['poster'] = 'default'
    if  'http' in addon.getSetting("new_fanart_share_list").decode('utf-8'):
        new_list['fanart'] = addon.getSetting("new_fanart_share_list").decode('utf-8')
    else:
        new_list['fanart'] = 'default'
    new_list['synopsis'] = get_synopsis(new_list['name'], addon.getSetting("new_synopsis_share_list").decode('utf-8'))
    new_list['type'] = type_list
    new_list['sha'] = sha_list.hexdigest()        
    new_list['iddb'] = 'pendiente'
    
    resultado = upload_list(new_list['link'], new_list['name'], new_list['type'], 
                            new_list['sha'], new_list['synopsis'], new_list['poster'], 
                            new_list['fanart'])
    
    if 'Error' in resultado:
        message(resultado)
        xbmc.executebuiltin("XBMC.Notification(FusionOrg,Error Al Compartir ,10000,"+icon+")")
        addon.openSettings()
        return
        
    new_list['iddb'] = re.findall('correctamente ID: (.*)',resultado)[0]
    
    if os.path.exists(my_shared_lists_file_path)==False:
        my_shared_lists_file_data = []
    else:
        my_shared_lists_file_data = json.loads(open(my_shared_lists_file_path,"r").read())

    for index in range(len(my_shared_lists_file_data)):
        if my_shared_lists_file_data[index]['name'] == new_list['name'] and my_shared_lists_file_data[index]['iddb'] == new_list['iddb']:
            del my_shared_lists_file_data[index]
            break
    my_shared_lists_file_data.append(new_list)
    b = open(my_shared_lists_file_path,"w")
    b.write(json.dumps(my_shared_lists_file_data))
    b.close()
        
    addon.setSetting('new_file_share_list', "")
    addon.setSetting('new_url_share_list', "")
    addon.setSetting('new_name_share_list', "")
    addon.setSetting('new_poster_share_list', "")
    addon.setSetting('new_fanart_share_list', "")
    addon.setSetting('new_synopsis_share_list', "")
    
    xbmc.executebuiltin("XBMC.Notification(FusionOrg,Lista Compartida ID:"+new_list['iddb']+",5000,"+icon+")")
    message(resultado)
    addon.openSettings()

def read_list(data, file):
    if "#EXTM3U" in data or '.m3u' in file:
        from base import parse_m3u
        parse_m3u.read_m3u_file(data)
    elif '"Titulo":"' in data or '.json' in file:
        from base import parse_json
        parse_json.read_json_file(data)
    elif "<title>" in data or '.xml' in file:
        from base import parse_xml
        parse_xml.read_xml_file(data)

def read_local_list(file):
    try:
        if os.path.exists(file)==True:
            data = open(file,'r')
            data = data.read()
            read_list(data, file)
        else:
            xbmc.executebuiltin("XBMC.Notification(FusionOrg,No existe la lista!!!,5000,"+icon+")")
    except:
        pass
        
def read_url_list(url):
    data = makeRequest(url)
    try: 
        read_list(data, url)
    except:
        pass
    
def remove_my_list(url,name):
    my_lists_file_data = json.loads(open(my_lists_file_path,'r').read())
    for index in range(len(my_lists_file_data)):
        if my_lists_file_data[index]['name'] == name and my_lists_file_data[index]['link'] == url:
            del my_lists_file_data[index]
            b = open(my_lists_file_path,"w")
            b.write(json.dumps(my_lists_file_data))
            b.close()
            break
    xbmc.executebuiltin("XBMC.Notification(FusionOrg,Se ha eliminado la lista '" + name + "',5000,"+icon+")")
    xbmc.executebuiltin("XBMC.Container.Refresh")

def read_my_lists():
    if os.path.exists(my_lists_file_path)==True:
        my_lists_file_data = json.loads(open(my_lists_file_path,'r').read())
        count_lists = 0
        for index in range(len(my_lists_file_data)):
            title = my_lists_file_data[index]['name']
            link = my_lists_file_data[index]['link']
            poster = my_lists_file_data[index]['poster']
            fanart = my_lists_file_data[index]['fanart']
            synopsis  = my_lists_file_data[index]['synopsis']
            contextMenu = []
            contextMenu.append(('quitar de mis listas',
                                'XBMC.RunPlugin({})'.format(build_url({'mode': 'remove_my_list',
                                                                       'name':title, 'link':link}))))
            if 'http' in link:
                mode = 'read_url_list'
            else:
                mode = 'read_local_list'
            add_Menu_item(mode, link, title, None, None, None, synopsis, fanart, poster, contextMenu, folder = True)
            count_lists = count_lists + 1
        if count_lists < 1:
            xbmc.executebuiltin("XBMC.Notification(FusionOrg,No tiene listas agregadas,5000,"+icon+")")
            return
        end_menu()
    else:
        xbmc.executebuiltin("XBMC.Notification(FusionOrg,Aun no tiene listas agregadas,5000,"+icon+")")
        
def get_shared_lists():
    page = 'listv2.php'
    data = makeRequest(server+page,{'User-Agent' : 'FusionOrgByTeamFusion/1.0'})
    data = data.replace('\n','').replace('\t','').replace('  ','')
    matches = re.findall('(<a.*?\/a>)',data,re.IGNORECASE)
    for match in matches:
        link = re.findall('href=\'(.*?)\'',match,re.MULTILINE)[0]
        if 'getfilev2.php' in link:
            link = server+link
        rating = re.findall('.*?rating=\'(.*?)\'',match,re.MULTILINE)[0]
        votes = re.findall('.*?votes=\'(.*?)\'',match,re.MULTILINE)[0]
        score = re.findall('.*?score=\'(.*?)\'',match,re.MULTILINE)[0]
        synopsis = re.findall('.*?synopsis=\'(.*?)\'',match,re.MULTILINE)[0]
        fanart = re.findall('.*?fanart=\'(.*?)\'',match,re.MULTILINE)[0]
        poster = re.findall('.*?poster=\'(.*?)\'',match,re.MULTILINE)[0]
        title = re.findall('.*?>(.*?)<\/a>',match,re.MULTILINE)[0]
        iddb = re.findall('.*?id=\'(.*?)\'',match,re.MULTILINE)[0]
        poster = get_poster(poster)
        fanart = get_fanart(fanart)
        synopsis = get_synopsis(title, synopsis)
        contextMenu = []
        contextMenu.append(('Valorar', 'XBMC.RunPlugin({})'.format(build_url({'mode': 'vote_list', 'iddb':iddb,'namedb':title}))))
        mode = 'read_url_list'
        add_Menu_item(mode, link, title, rating, score, votes, synopsis, fanart, poster, contextMenu, folder = True)
    end_menu()
    
def get_my_shared_lists():
    s = requests.Session()
    data = {'email':username,'password':password}
    if username == '' or username == None or password == '' or password == None:
        message('Requieres configurar tu usuario de FusionOrg-Addon.')
        addon.openSettings()
        return
    
    url = server + "checklogin.php"
    r = s.post(url, data=data)
    texto = str(s.cookies)
    cookie = re.findall('.*?(PHPSESSID=.*?) .*',texto,re.MULTILINE)[0]
    headers = {'User-Agent':'FusionOrgByTeamFusion/1.0', 'Connection':'keep-alive', 'Cookie': cookie,
               'Host':'fusionorg.net','Referer':'http://fusionorg.net/index.php'}
    
    page = 'mysharedlistv2.php'
    data = requests.post(server+page, headers = headers, files = {'email': (None, username)}).text
    data = data.replace('\n','').replace('\t','').replace('  ','')
    matches = re.findall('(<a.*?\/a>)',data,re.IGNORECASE)
    for match in matches:
        link = re.findall('href=\'(.*?)\'',match,re.MULTILINE)[0]
        if 'getfilev2.php' in link:
            link = server+link
        rating = re.findall('.*?rating=\'(.*?)\'',match,re.MULTILINE)[0]
        votes = re.findall('.*?votes=\'(.*?)\'',match,re.MULTILINE)[0]
        score = re.findall('.*?score=\'(.*?)\'',match,re.MULTILINE)[0]
        synopsis = re.findall('.*?synopsis=\'(.*?)\'',match,re.MULTILINE)[0]
        fanart = re.findall('.*?fanart=\'(.*?)\'',match,re.MULTILINE)[0]
        poster = re.findall('.*?poster=\'(.*?)\'',match,re.MULTILINE)[0]
        title = re.findall('.*?>(.*?)<\/a>',match,re.MULTILINE)[0]
        iddb = re.findall('.*?id=\'(.*?)\'',match,re.MULTILINE)[0]
        contextMenu = []
        contextMenu.append(('Valorar', 'XBMC.RunPlugin({})'.format(build_url({'mode':'vote_list', 'iddb':iddb, 'namedb':title}))))
        contextMenu.append(('Dejar de compartir esta lista',
                            'XBMC.RunPlugin({})'.format(build_url({'mode':'remove_shared_list', 'iddb':iddb, 'namedb':title})))) 
        poster = get_poster(poster)
        fanart = get_fanart(fanart)
        synopsis = get_synopsis(title, synopsis)
        mode = 'read_url_list'
        add_Menu_item(mode, link, title, rating, score, votes, synopsis, fanart, poster, contextMenu, folder = True)
    end_menu()
    
def remove_shared_list(iddb,namedb):
    s = requests.Session()
    data = {'email':username,'password':password}
    if username == '' or username == None or password == '' or password == None:
        message('Requieres configurar tu usuario de FusionOrg-Addon.')
        addon.openSettings()
        return
    
    url = "http://fusionorg.net/checklogin.php"
    r = s.post(url, data=data)
    texto = str(s.cookies)
    cookie = re.findall('.*?(PHPSESSID=.*?) .*',texto,re.MULTILINE)[0]
    headers = {'User-Agent':'FusionOrgByTeamFusion/1.0', 'Connection':'keep-alive', 'Cookie': cookie,
               'Host':'fusionorg.net','Referer':'http://fusionorg.net/index.php'}
    
    page = 'removesharedlistv2.php'
    d = requests.post(server+page, headers = headers, files = {'name': (None, namedb), 'id': (None, iddb)});
    if 'correctamente' in d.text:
        message(d.text)
    elif 'Error' in d.text:
        message(d.text)
        return
    else:
        message(d.text)
        return
        
    if os.path.exists(my_shared_lists_file_path)==False:
        my_shared_lists_file_data = []
    else:
        my_shared_lists_file_data = json.loads(open(my_shared_lists_file_path,"r").read())

    for index in range(len(my_shared_lists_file_data)):
        if my_shared_lists_file_data[index]['name'] == namedb and my_shared_lists_file_data[index]['iddb'] == iddb:
            del my_shared_lists_file_data[index]
            break
    b = open(my_shared_lists_file_path,"w")
    b.write(json.dumps(my_shared_lists_file_data))
    b.close()
    xbmc.executebuiltin("XBMC.Container.Refresh")
    
def vote_list(iddb, namedb):
    dialog = xbmcgui.Dialog()
    ret = dialog.select('Califica esta Lista', ['10 Puntos', '9 Puntos', '8 Puntos', '7 Puntos', '6 Puntos','5 Puntos', '4 Puntos', '3 Puntos', '2 Puntos', '1 Punto'])
    
    if ret == 0:
        valoracion = 10 - ret
    elif ret == 1:
        valoracion = 10 - ret
    elif ret == 2:
        valoracion = 10 - ret
    elif ret == 3:
        valoracion = 10 - ret 
    elif ret == 4:
        valoracion = 10 - ret
    elif ret == 5:
        valoracion = 10 - ret
    elif ret == 6:
        valoracion = 10 - ret
    elif ret == 7:
        valoracion = 10 - ret 
    elif ret == 8:
        valoracion = 10 - ret
    elif ret == 9:
        valoracion = 10 - ret
    else:
        return    
    s = requests.Session()
    data = {'email':username,'password':password}
    url = "http://fusionorg.net/checklogin.php"
    r = s.post(url, data=data)
    texto = str(s.cookies)
    cookie = re.findall('.*?(PHPSESSID=.*?) .*',texto,re.MULTILINE)[0]
    headers = {'User-Agent':'FusionOrgByTeamFusion/1.0', 'Connection':'keep-alive', 'Cookie': cookie,'Host':'fusionorg.net','Referer':'http://fusionorg.net/index.php'}
    url2 = "http://fusionorg.net/valorar.php"
    data2 = {'id':iddb,'lista':namedb,'valoracion':valoracion}
    d= requests.post(url2, headers= headers, data = data2)
    
    return message(d.text)
