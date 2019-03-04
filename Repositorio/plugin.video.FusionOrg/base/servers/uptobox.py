# -*- coding: utf-8 -*-
import requests
import pickle
import os
import xbmcaddon
import xbmc
import urllib
import re
import xbmcgui
import json
import time
import datetime
import base64
import urlparse
import urllib2
import cookielib
import gzip
from StringIO import StringIO
from requests.api import request
from datetime import date

addon = xbmcaddon.Addon()
addonname = addon.getAddonInfo('name')
addon_dir = xbmc.translatePath(xbmc.translatePath(addon.getAddonInfo('Path')).decode('utf-8'))

data_path = xbmc.translatePath(addon.getAddonInfo('Profile'))
if not os.path.exists(data_path):
    os.makedirs(data_path)

icon = os.path.join(addon_dir, 'icon.png')

headers_f = dict()
headers_f['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
headers_f['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q='
headers_f['Accept-Language'] = 'es-419,es;q=0.9,en;q=0.8'
headers_f['Accept-Encoding'] = 'gzip, deflate, br'
headers_f['Referer'] = ''

default_headers = dict()
default_headers['User-Agent'] = 'Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3163.100 Safari/537.36'
default_headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
default_headers['Accept-Language'] = 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3'
default_headers['Accept-Charset'] = 'UTF-8'
default_headers['Accept-Encoding'] = 'gzip'

def post_utb(url, post, referer = 'https://uptobox.com/'):
    
    retry = 1
    while retry < 3:
        headers_f['Referer'] = referer
        response = requests.post(url, headers = headers_f, data = post, timeout=20)
        if response.status_code == 200:
            data = response.content
            retry = 3
        else:
            retry = retry + 1
            data = 'Imposible conectar con el server'
    return data

def read_utb(url, referer = 'https://uptobox.com/'):
    
    retry = 1
    while retry < 3:
        headers_f['Referer'] = referer 
        response = requests.get(url, headers = headers_f, timeout=20)
        if response.status_code == 200:
            data = response.content
            retry = 3
        else:
            retry = retry + 1
            data = 'Imposible conectar con el server'
    return data

def get_token_uptobox():
    
    user = addon.getSetting("username_utb")
    passw = addon.getSetting("password_utb")
    if user == '' or passw == '':
        xbmc.executebuiltin("XBMC.Notification(FusionOrg,Introducir usuario y contraseña de uptobox ,10000,"+icon+")")
        addon.openSettings()
        return
    data = read_utb('https://uptobox.com/?op=login&referer=homepage', 'homepage')
    post = {'login': user, 'password': passw}
    data = post_utb('https://uptobox.com/?op=login&referer=my_account', post, 'homepage')
    if 'Imposible conectar con el server' in data:
        xbmc.executebuiltin("XBMC.Notification(FusionOrg,Fallo al conectar con el servidor,10000,"+icon+")")
        addon.openSettings()
        return
    if 'Incorrect Login or Password' in data:
        xbmc.executebuiltin("XBMC.Notification(FusionOrg,Usuario o contraseña incorrecto!!!,10000,"+icon+")")
        addon.openSettings()
        return
    if 'Token:' in data:
        token_path = os.path.join(data_path,'token.dat')
        patron = '<span class=\'to-clipboard\'><span class=\'none\'>(.*?)<\/span><\/span>'
        token = re.findall(patron, data,re.MULTILINE)[1]
        handler = open(token_path,"w")
        handler.write(token)
        handler.close()
        xbmc.executebuiltin("XBMC.Notification(FusionOrg,Token de Uptobox obtenido!!!,10000,"+icon+")")
        return
    if 'Invalid captcha' in data:
        xbmcgui.Dialog().ok(addonname,'Se detecto un Captcha','Inice sesion usando esta misma conexion y resuelve el captcha')
        addon.openSettings()
        return
    
    xbmc.executebuiltin("XBMC.Notification(FusionOrg,Fallo al obtener el token (intenta de nuevo),10000,"+icon+")")
    addon.openSettings()
    return

def uptoboxtest(url,tmdbid):
    utb_id_file = get_id(url)
    
    if utb_id_file == 'fallo al obtener el id':
        return dict()
    
    utb_user_types = get_utb_user_type()
    
    utb_data, cookie = get_utb_data(utb_id_file)
    if ("Unfortunately, the file you want is not available." in utb_data
        or "Unfortunately, the video you want to see is not available" in utb_data 
        or "This stream doesn" in utb_data 
        or "Site is Under Maintenance" in utb_data 
        or "This file is temporarily unavailable, please retry later" in utb_data
        or "Our website is currently undergoing maintenance and will be back online shortly !" in utb_data):
        return dict()
    if utb_user_types['premium'] != 'yes':
        utb_waits = get_utb_wait_time(utb_user_types, utb_data, utb_id_file)
    else:
        utb_waits = dict()
        utb_waits['mode'] = 'premium'
        utb_waits['wait_time'] = 0
        utb_waits['seekable'] = 1
    uptobox_path = os.path.join(data_path,'uptobox.json')
    try:
        data_test = open(uptobox_path,"r").read()
    except:
        data_test = ''
    media = ''
    patron  = "<h1 class='file-title'>(.*?)</h1>"
    media1 = re.findall(patron, utb_data)[0]
    if ('360p' in media1 or '360P' in media1):
        media = '360p'
    elif ('480p' in media1 or '480P' in media1):
        media = '480p'
    elif ('720p' in media1 or '720P' in media1):
        media = '720p'
    elif ('1080p' in media1 or '1080P' in media1):
        media = '1080p'
    elif ('2k' in media1 or '2K' in media1):
        media = '2K'
    elif ('4k' in media1 or '4K' in media1):
        media = '4K'
    patron  = "<h1 class='file-title'>.*\((.*)\)</h1>"
    media2 = re.findall(patron, utb_data)[0]
    if 'MB' in media2 or utb_waits['mode'] == 'premium':
        utb_waits['seekable'] = 1    
    else:
        utb_waits['seekable'] = 0
    media = media + ' ' + media2
    if tmdbid in data_test:
        data_test = json.loads(data_test)
        if data_test['tmdbid'] == tmdbid:
            data_test[tmdbid][utb_id_file]=dict()
            data_test[tmdbid][utb_id_file]=utb_waits
        else:
            data_test=dict()
            data_test['tmdbid']=tmdbid
            data_test[tmdbid]=dict()
            data_test[tmdbid][utb_id_file]=dict()
            data_test[tmdbid][utb_id_file]=utb_waits
    else:
        data_test=dict()
        data_test['tmdbid']=tmdbid
        data_test[tmdbid]=dict()
        data_test[tmdbid][utb_id_file]=dict()
        data_test[tmdbid][utb_id_file]=utb_waits
    handler = open(uptobox_path,"w")
    handler.write(json.dumps(data_test))
    handler.close()
    
    servers = dict()
    if utb_data == 'Imposible conectar con el server':
        return servers
    if 'https://uptostream.com/' in utb_data:
        url_uts = 'https://uptostream.com/' + re.findall('uptostream.com/([^"]*)', utb_data)[0]
        calidades = get_calidades_uts('',url_uts)
        if len(calidades) > 0:
            if len(calidades['uptostream']) > 0:
                servers['uptostream'] = calidades['uptostream'] 
    if not ("Unfortunately, the file you want is not available." in utb_data
            or "Unfortunately, the video you want to see is not available" in utb_data 
            or "This stream doesn" in utb_data 
            or "Site is Under Maintenance" in utb_data 
            or "This file is temporarily unavailable, please retry later" in utb_data
            or "Our website is currently undergoing maintenance and will be back online shortly !" in utb_data):
        if media != '':
            if utb_waits['mode'] == 'premium':
                wait_str = '[premium]'
            elif utb_waits['wait_time'] > 0:
                if 'You must be premium to download this file' in utb_data: 
                    return servers
                wait_str = '[Espera: ' + str(datetime.timedelta(seconds=utb_waits['wait_time'])) + ' HH:MM:SS]'
            elif utb_waits['wait_time'] == 0 and utb_waits['dl_link'] != '':
                if utb_waits['mode'] == 'registred':
                    wait_str = '[Registrado]'
                if utb_waits['mode'] == 'free':
                    wait_str = '[Free]'
            servers['uptobox']={}
            servers['uptobox'][media] = ['[Uptobox=' + media + ']' + wait_str, 'https://uptobox.com/' + utb_id_file]

    return servers

def get_id(url):
    
    xs = url.replace('https://','').replace('http://','').replace('www.','').replace('uptobox.com/','').replace('/embed/','').replace('/iframe/','')
    xs = xs.split('/')
    for x in xs:
        if len(x) == 12:
            return x
    return 'fallo al obtener el id'

def get_utb_user_type():
    
    user_type = dict()
    user_type['registred'] = 'no'
    user_type['user_token']= ''
    user_type['premium'] = 'no'
    token_path = os.path.join(data_path,'token.dat')
    user_me_path = os.path.join(data_path,'me.json')
    
    if os.path.isfile(token_path):
        data = open(token_path,'r')
        data = data.read()
        if data != '':
            user_type['registred'] = 'yes'
            user_type['user_token'] = data
                
    if user_type['registred'] == 'yes':
        data = ''
        if os.path.isfile(user_me_path):
            data = open(user_me_path,'r')
            data = data.read()
            if data != '':
                data = json.loads(data)
            else:
                data = dict()
        if data != '':
            try:
                if data['time_valid'] < time.time():
                    retry = 1
                    while retry < 3:
                        response = requests.get('https://uptobox.com/api/user/me?token=' + user_type['user_token'], timeout=20)
                        if response.status_code == 200:
                            data = response.content
                            retry = 3
                        else:
                            retry = retry + 1
                            data = 'Imposible conectar con el server'
                    if data != 'Imposible conectar con el server':
                        data = json.loads(data)
                        data['time_valid'] = time.time() + 3600
                else:
                    if data['statusCode'] == 0:
                        if data['data']['premium'] == 0:
                            user_type['premium'] = 'no'
                        if data['data']['premium'] == 1:
                            user_type['premium'] = 'yes'
                    else:
                        user_type['registred'] = 'no'
                        user_type['user_token']= '' 
            except:
                retry = 1
                while retry < 3:
                    response = requests.get('https://uptobox.com/api/user/me?token=' + user_type['user_token'], timeout=20)
                    if response.status_code == 200:
                        data = response.content
                        retry = 3
                    else:
                        retry = retry + 1
                        data = 'Imposible conectar con el server'
                if data != 'Imposible conectar con el server':
                    data = json.loads(data)
                    data['time_valid'] = time.time() + 3600
            else:
                if data['statusCode'] == 0:
                    if data['data']['premium'] == 0:
                        user_type['premium'] = 'no'
                    if data['data']['premium'] == 1:
                        user_type['premium'] = 'yes'
                else:
                    user_type['registred'] = 'no'
                    user_type['user_token']= '' 
        else:
            retry = 1
            while retry < 3:
                response = requests.get('https://uptobox.com/api/user/me?token=' + user_type['user_token'], timeout=20)
                if response.status_code == 200:
                    data = response.content
                    retry = 3
                else:
                    retry = retry + 1
                    data = 'Imposible conectar con el server'
            if data != 'Imposible conectar con el server':
                data = json.loads(data)
                data['time_valid'] = time.time() + 3600
                if data['statusCode'] == 0:
                    if data['data']['premium'] == 0:
                        user_type['premium'] = 'no'
                    if data['data']['premium'] == 1:
                        user_type['premium'] = 'yes'
                else:
                    user_type['registred'] = 'no'
                    user_type['user_token']= ''
        
        handler = open(user_me_path,"w")
        handler.write(json.dumps(data))
        handler.close()     
    else:
            user_type['registred'] = 'no'
            user_type['user_token']= ''
    
    return user_type
        
def get_utb_data(id):
    
    url = 'https://uptobox.com/' + id
    retry = 1
    while retry < 3:
        response = requests.get(url, timeout=20)
        if response.status_code == 200:
            data = response.content
            cookie = response.cookies
            retry = 3
        else:
            retry = retry + 1
            data = 'Imposible conectar con el server'
            cookie = dict() 
    return data, cookie

def get_utb_wait_time(user_types, data, id):
    
    time_registred = 99999
    dl_link_registred = ''
    w_token_registred = ''
    time_now_registred = ''
    time_free = ''
    dl_link_free = ''
    w_token_free = ''
    time_now_free = ''
    if user_types['registred'] == 'yes' and user_types['premium'] == 'no' and user_types['user_token'] != '':
        url = 'https://uptobox.com/api/link?token=' + user_types['user_token'] + '&file_code=' + id
        retry = 1
        while retry < 3:
            response = requests.get(url, timeout=20)
            if response.status_code == 200:
                data_registred = response.content
                retry = 3
            else:
                retry = retry + 1
                data_registred = 'Imposible conectar con el server'
        
        if data_registred != 'Imposible conectar con el server':
            data_registred = json.loads(data_registred)
            if data_registred['statusCode'] == 0 or data_registred['statusCode'] == 16:
                if data_registred['statusCode'] == 0:
                    time_registred = 0
                    dl_link_registred = data_registred['data']['dlLink']
                    w_token_registred = ''
                    time_now_registred = time.time()
                if data_registred['statusCode'] == 16:
                    time_registred = data_registred['data']['waiting']
                    dl_link_registred = ''
                    w_token_registred = data_registred['data']['waitingToken']
                    time_now_registred = time.time()
            
    if 'you can wait' in data and 'to launch a new download' in data:
        wait = re.findall('you can wait (.*?) to launch a new download', data)
        if 'hour' in wait[0]:
            hours = re.findall('([0-9]+) hour', wait[0])[0]
        else: 
            hours = 0
        if 'minute' in wait[0]:
            minutes = re.findall('([0-9]+) minute', wait[0])[0]
        else: 
            minutes = 0
        if 'second' in wait[0]:
            seconds = re.findall('([0-9]+) second', wait[0])[0]
        else: 
            seconds = 0
        time_free = (int(hours)*60*60) + (int(minutes) * 60) + int(seconds)
        dl_link_free = ''
        w_token_free = ''
        time_now_free = time.time()
    elif '<input name=' in data  and 'value=' in data:
        matches = re.findall("<input name='(.*?)' value='(.*?)' type='hidden'", data)
        for inputname, inputvalue in matches:
            w_token_free = inputvalue
        time_free = 30
        dl_link_free = ''
        time_now_free = time.time()
    elif 'uptobox.com/dl' in data:
        dl_link_free = re.findall('<a href="(.*?)" class=.big-button-green-flat mt-4 mb-4.', data)[0].replace('"', '')
        time_free = 0
        w_token_free = ''
        time_now_free = time.time()

    resp = dict()
    if dl_link_free != '' or dl_link_registred != '':
        resp['wait_token'] = ''
        resp['wait_time'] = 0
        resp['time'] = time.time()
        if dl_link_free != '':
            resp['file_id'] = id
            resp['dl_link'] = dl_link_free 
            resp['mode'] = 'free'
        if dl_link_registred != '':
            resp['file_id'] = id
            resp['dl_link'] = dl_link_registred
            resp['mode'] = 'registred'
    elif w_token_free != '' or w_token_registred != '':
        if w_token_free != '' and w_token_registred == '':
            resp['file_id'] = id
            resp['time'] = time_now_free
            resp['dl_link'] = '' 
            resp['mode'] = 'free'
            resp['wait_time'] = time_free
            resp['wait_token'] = w_token_free
        if w_token_free == '' and w_token_registred != '':
            resp['file_id'] = id
            resp['time'] = time_now_registred
            resp['dl_link'] = '' 
            resp['mode'] = 'registred'
            resp['wait_time'] = time_registred
            resp['wait_token'] = w_token_registred
        if w_token_free != '' and w_token_registred != '':
            if time_free < time_registred:
                resp['file_id'] = id
                resp['time'] = time_now_free
                resp['dl_link'] = '' 
                resp['mode'] = 'free'
                resp['wait_time'] = time_free
                resp['wait_token'] = w_token_free
            if time_free >= time_registred:
                resp['file_id'] = id
                resp['time'] = time_now_registred
                resp['dl_link'] = '' 
                resp['mode'] = 'registred'
                resp['wait_time'] = time_registred
                resp['wait_token'] = w_token_registred

    elif (time_free > 30) or (time_registred > 30):
        if ((time_free < time_registred) or (time_registred == 99999)):
            resp['file_id'] = id
            resp['time'] = time_now_free
            resp['dl_link'] = '' 
            resp['mode'] = 'free'
            resp['wait_time'] = time_free
            resp['wait_token'] = ''
        if ((time_free > time_registred) and (time_registred != 99999)):
            resp['file_id'] = id
            resp['time'] = time.time()
            resp['dl_link'] = '' 
            resp['mode'] = 'registred'
            resp['wait_time'] = time_registred
            resp['wait_token'] = ''

    return resp
    
def uptostream(url):
    
    media_subtitles = []
    calidad = urlparse.parse_qs(url)['calidad'][0]
    lang = urlparse.parse_qs(url)['lang'][0]
    url = url.split('&')[0]
    data = read_uts(url)
    if data == 'Imposible conectar con el server':
        return False, ''
    patron  = "JSON.parse\('(\[{.*?}\])'\);"
    media = re.findall(patron, data)
    if len(media)>0:
        for media_select in media:
            if not 'srcLang' in media_select:
                media_video = json.loads(media_select)
            else:
                media_subs = json.loads(media_select)
                for subtitles in media_subs:
                    media_subtitles.append(subtitles['src'])
        for item in media_video:
            if lang == item['lang'] and calidad == item['label']:
                return True, item['src'].replace('https','http'), media_subtitles
    return False, ''

def get_calidades_utb(data, id):
    
    if data == '':
        data = get_utb_data('https://uptobox.com/' + id)
    video_calidades = dict()
    if data == 'Imposible conectar con el server':
        return video_calidades
    media = ''
    patron  = "<h1 class='file-title'>(.*?)</h1>"
    media1 = re.findall(patron, utb_data)[0]
    if ('360p' in media1 or '360P' in media1):
        media = '360p'
    elif ('480p' in media1 or '480P' in media1):
        media = '480p'
    elif ('720p' in media1 or '720P' in media1):
        media = '720p'
    elif ('1080p' in media1 or '1080P' in media1):
        media = '1080p'
    elif ('2k' in media1 or '2K' in media1):
        media = '2K'
    elif ('4k' in media1 or '4K' in media1):
        media = '4K'
    patron  = "<h1 class='file-title'>.*\((.*)\)</h1>"
    media2 = re.findall(patron, utb_data)[0]
    media = media + ' ' + media2
    if media != '':
        video_calidades['uptobox']={}
        video_calidades['uptobox'][media] = ['[Uptobox=' + media + ']', url]
    return video_calidades

def uptobox(url,tmdbid):
    
    utb_id_file = get_id(url)
    utb_user_types = get_utb_user_type()
    
    uptobox_path = os.path.join(data_path,'uptobox.json')
    data_test1 = json.loads(open(uptobox_path,"r").read())
    data_test = data_test1[tmdbid][utb_id_file]
    
    if data_test['mode'] == 'premium':
        if utb_user_types['premium'] == 'yes' and utb_user_types['user_token'] != '':
            url = 'https://uptobox.com/api/link?token=' + utb_user_types['user_token'] + '&file_code=' + utb_id_file
            retry = 1
            while retry < 3:
                response = requests.get(url, timeout=20)
                if response.status_code == 200:
                    data = response.content
                    retry = 3
                else:
                    retry = retry + 1
                    data = 'Imposible conectar con el server'
            
            if data != 'Imposible conectar con el server':
                data = json.loads(data)
                if data['statusCode'] == 0:
                    dl_link_registred = data['data']['dlLink']
                    header_test = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
                    header_test = '|' + urllib.urlencode(header_test)
                    return True, dl_link_registred + header_test            

    if data_test['mode'] == 'registred' and data_test['file_id'] == utb_id_file:
        if int(data_test['time'])+(30*60) > int(time.time()):
            if data_test['dl_link'] != '':
                if data_test['seekable'] == 0:
                    header_test = {'seekable': 0,
                                   'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
                if data_test['seekable'] == 1:
                    data_test['seekable'] = 0
                    data_test1[tmdbid][utb_id_file] = data_test 
                    uptobox_path = os.path.join(data_path,'uptobox.json')
                    handler = open(uptobox_path,"w")
                    handler.write(json.dumps(data_test1))
                    handler.close()
                    header_test = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
                header_test = '|' + urllib.urlencode(header_test)
                return True, data_test['dl_link'] + header_test
            
            if data_test['wait_token'] != '' and utb_user_types['user_token'] != '' and utb_id_file == data_test['file_id'] and data_test['wait_time'] < 31:
                if (int(data_test['time']) + int(data_test['wait_time']) > int(time.time())):
                    time_res = int(time.time())-(int(data_test['time']) + int(data_test['wait_time']))
                    pDialog = xbmcgui.DialogProgress()
                    pDialog.create(addonname,'Espera: ' + str(time_res) + ' segs')
                    cancelado = False
                    percent = 0
                    time_fin = int(data_test['time']) + int(data_test['wait_time']) + 1
                    while time_fin > int(time.time()) and not cancelado and percent < 100:
                        time.sleep(0.5)
                        time_res = time_fin - int(time.time())
                        percent = (100 * (30-time_res))/30 
                        pDialog.update(percent,'Espera: ' + str(time_res) + ' segs')
                        cancelado = pDialog.iscanceled()
                        if cancelado:
                            percent = 101
                            time_fin = 0
                    if cancelado:
                        xbmc.executebuiltin("XBMC.Notification(FusionOrg,Se cancelo uptobox,10000,"+icon+")")
                        return False,'Cancelado'
                    pDialog.close()
                url = 'https://uptobox.com/api/link?token=' + utb_user_types['user_token'] + '&file_code=' + utb_id_file + '&waitingToken=' + data_test['wait_token']
                retry = 1
                while retry < 3:
                    response = requests.get(url, timeout=20)
                    if response.status_code == 200:
                        data = response.content
                        retry = 3
                    else:
                        retry = retry + 1
                        data = 'Imposible conectar con el server'
                if data != 'Imposible conectar con el server':
                    data = json.loads(data)
                    if data['statusCode'] == 0:
                        dl_link = data['data']['dlLink']
                        if data_test['seekable'] == 0:
                            header_test = {'seekable': 0,
                                           'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
                        if data_test['seekable'] == 1:
                            data_test['seekable'] = 0
                            data_test1[tmdbid][utb_id_file] = data_test 
                            uptobox_path = os.path.join(data_path,'uptobox.json')
                            handler = open(uptobox_path,"w")
                            handler.write(json.dumps(data_test1))
                            handler.close()
                            header_test = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
                        header_test = '|' + urllib.urlencode(header_test)
                        return True, dl_link + header_test

    if data_test['mode'] == 'free' and data_test['file_id'] == utb_id_file:
        if int(data_test['time'])+(30*60) > int(time.time()):
            if data_test['dl_link'] != '':
                if data_test['seekable'] == 0:
                    header_test = {'seekable': 0,
                                   'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
                if data_test['seekable'] == 1:
                    data_test['seekable'] = 0
                    data_test1[tmdbid][utb_id_file] = data_test 
                    uptobox_path = os.path.join(data_path,'uptobox.json')
                    handler = open(uptobox_path,"w")
                    handler.write(json.dumps(data_test1))
                    handler.close()
                    header_test = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
                header_test = '|' + urllib.urlencode(header_test)
                return True, data_test['dl_link'] + header_test
            
            if data_test['wait_token'] != '' and utb_id_file == data_test['file_id'] and data_test['wait_time'] == 30:
                if (int(data_test['time']) + int(data_test['wait_time']) > int(time.time())):
                    time_res = int(time.time())-(int(data_test['time']) + int(data_test['wait_time']))
                    pDialog = xbmcgui.DialogProgress()
                    pDialog.create(addonname,'Espera: ' + str(time_res) + ' segs')
                    cancelado = False
                    percent = 0
                    time_fin = int(data_test['time']) + int(data_test['wait_time']) + 1
                    while time_fin > int(time.time()) and not cancelado and percent < 100:
                        time.sleep(0.5)
                        time_res = time_fin - int(time.time())
                        percent = (100 * (30-time_res))/30 
                        pDialog.update(percent,'Espera: ' + str(time_res) + ' segs')
                        cancelado = pDialog.iscanceled()
                        if cancelado:
                            percent = 101
                            time_fin = 0
                    if cancelado:
                        xbmc.executebuiltin("XBMC.Notification(FusionOrg,Se cancelo uptobox,10000,"+icon+")")
                        xbmc.executebuiltin("XBMC.Container.Refresh")
                        return False,'Cancelado'
                    pDialog.close()
                url = 'https://uptobox.com/' +  utb_id_file
                data = uptobox_free(url, data_test['wait_token'])
                if data != 'Imposible conectar con el server':
                    if 'Invalid captcha' in data:
                        xbmcgui.Dialog().ok(addonname,'Se detecto un Captcha','Inice sesion usando esta misma conexion y resuelve el captcha')
                        False, 'Fallo por Captcha'
                    if 'uptobox.com/dl' in data:
                        media = re.findall('<a href="(.*?)" class=.big-button-green-flat mt-4 mb-4.', data)[0].replace('"', '')
                        media2 = re.findall("<h1 class='file-title'>.*\((.*)\)</h1>", data)[0]
                        if 'MB' in media2:
                            header_test = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
                        else:
                            header_test = {'seekable': 0,
                                           'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
                        header_test = '|' + urllib.urlencode(header_test)
                        return True, media + header_test
                
    if data_test['wait_token'] == '' or utb_id_file != data_test['file_id'] or data_test['wait_time'] > 30:
        message = 'Requiere esperar (' + str(datetime.timedelta(seconds=data_test['wait_time'])) + '), vuelva a intentarlo mas tarde.'
        message2 = 'Solo se puede solicitar video cuando falte 30 segs.'
        xbmcgui.Dialog().ok(addonname, message, message2)
        return False, message

def get_calidades_uts(data, url):
    
    if data == '':
        data = read_uts (url)
    video_calidades = dict()
    if data == 'Imposible conectar con el server':
        return video_calidades
    patron  = "JSON.parse\('(\[{.*?}\])'\);"
    media = re.findall(patron, data)
    if len(media)>0:
        for media_select in media:
            if not 'srcLang' in media_select:
                media_select = json.loads(media_select)
                video_calidades['uptostream']={}
                for item in media_select:
                     video_calidades['uptostream'][item['label']+' '+item['lang']] = ['[Uptostream=' + item['label'] + ' ' + item['lang'] + ']',
                                                                                      url + '&calidad=' + item['label'] + '&lang=' + item['lang']]
    return video_calidades

def read_uts(url):
    
    retry = 1
    while retry < 3:
        response = requests.get(url, timeout=20)
        if response.status_code == 200:
            data = response.content
            retry = 3
        else:
            retry = retry + 1
            data = 'Imposible conectar con el server'
    return data

def uptobox_free(url, inputvalue, inputname='waitingToken'):
    
    post = ''
    post += inputname + '=' + inputvalue + '&'
    cj = cookielib.MozillaCookieJar()
    request_headers = default_headers.copy()
    url = urllib.quote(url, safe="%/:=&?~#+!$,;'@()*[]")
    handlers = [urllib2.HTTPHandler(debuglevel=False)]
    handlers.append(urllib2.HTTPCookieProcessor(cj))
    opener = urllib2.build_opener(*handlers)
    req = urllib2.Request(url, post, request_headers)
    handle = opener.open(req, timeout=None)
    if handle.code == 200:
        data = handle.read()
        data = gzip.GzipFile(fileobj=StringIO(data)).read()
        return data
    return 'Imposible conectar con el server'

def uptostreamtest(url,tmdbid):
    if 'embed' in url:
        url = url.replace('/embed/', '/')
    if 'iframe' in url:
        url = url.replace('/iframe/', '/')
    data = read_uts(url)
    servers = dict()
    if data == 'Imposible conectar con el server':
        return servers
    if 'Requested link:' in data:
        utb_id_file = get_id(url)
    
        if utb_id_file == 'fallo al obtener el id':
            return dict()
 
        servers = dict()
        utb_user_types = get_utb_user_type()
        utb_data, cookie = get_utb_data(utb_id_file)
        if utb_data == 'Imposible conectar con el server':
            return servers
        if not ("Unfortunately, the file you want is not available." in utb_data
                or "Unfortunately, the video you want to see is not available" in utb_data 
                or "This stream doesn" in utb_data
                or "Site is Under Maintenance" in utb_data 
                or "This file is temporarily unavailable, please retry later" in utb_data
                or "Our website is currently undergoing maintenance and will be back online shortly !" in utb_data):

            if utb_user_types['premium'] != 'yes':
                utb_waits = get_utb_wait_time(utb_user_types, utb_data, utb_id_file)
            else:
                utb_waits = dict()
                utb_waits['mode'] = 'premium'
                utb_waits['wait_time'] = 0
                utb_waits['seekable'] = 1
            media = ''
            patron  = "<h1 class='file-title'>(.*?)</h1>"
            media1 = re.findall(patron, utb_data)[0]
            if ('360p' in media1 or '360P' in media1):
                media = '360p'
            elif ('480p' in media1 or '480P' in media1):
                media = '480p'
            elif ('720p' in media1 or '720P' in media1):
                media = '720p'
            elif ('1080p' in media1 or '1080P' in media1):
                media = '1080p'
            elif ('2k' in media1 or '2K' in media1):
                media = '2K'
            elif ('4k' in media1 or '4K' in media1):
                media = '4K'
            patron  = "<h1 class='file-title'>.*\((.*)\)</h1>"
            media2 = re.findall(patron, utb_data)[0]
            if 'MB' in media2:
                utb_waits['seekable'] = 1    
            else:
                utb_waits['seekable'] = 0
                
            uptobox_path = os.path.join(data_path,'uptobox.json')
            try:
                data_test = open(uptobox_path,"r").read()
            except:
                data_test = ''
            if tmdbid in data_test:
                data_test = json.loads(data_test)
                if data_test['tmdbid'] == tmdbid:
                    data_test[tmdbid][utb_id_file]=dict()
                    data_test[tmdbid][utb_id_file]=utb_waits
                else:
                    data_test=dict()
                    data_test['tmdbid']=tmdbid
                    data_test[tmdbid]=dict()
                    data_test[tmdbid][utb_id_file]=dict()
                    data_test[tmdbid][utb_id_file]=utb_waits
            else:
                data_test=dict()
                data_test['tmdbid']=tmdbid
                data_test[tmdbid]=dict()
                data_test[tmdbid][utb_id_file]=dict()
                data_test[tmdbid][utb_id_file]=utb_waits
            handler = open(uptobox_path,"w")
            handler.write(json.dumps(data_test))
            handler.close()
            media = media + ' ' + media2
            if media != '':
                if utb_waits['mode'] == 'premium':
                    wait_str = '[premium]'
                elif utb_waits['wait_time'] > 0:
                    wait_str = '[Espera: ' + str(datetime.timedelta(seconds=utb_waits['wait_time'])) + ' HH:MM:SS]'
                elif utb_waits['wait_time'] == 0 and utb_waits['dl_link'] != '':
                    if utb_waits['mode'] == 'registred':
                        wait_str = '[Registrado]'
                    if utb_waits['mode'] == 'free':
                        wait_str = '[Free]'
                if not 'You must be premium to download this file' in utb_data and utb_waits['mode'] != 'premium': 
                    servers['uptobox']={}
                    servers['uptobox'][media] = ['[Uptobox=' + media + ']' + wait_str, 'https://uptobox.com/' + utb_id_file]
   
    if not ("Unfortunately, the file you want is not available." in data
            or "Unfortunately, the video you want to see is not available" in data
            or "This stream doesn" in data
            or "Site is Under Maintenance" in data
            or "This file is temporarily unavailable, please retry later" in data
            or "Our website is currently undergoing maintenance and will be back online shortly !" in data):
        calidades = get_calidades_uts(data, url)
        if len(calidades) > 0:
            if len(calidades['uptostream']) > 0:
                servers['uptostream'] = calidades['uptostream']
    return servers
