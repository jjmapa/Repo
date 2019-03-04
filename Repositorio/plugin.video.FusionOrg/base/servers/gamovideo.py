# -*- coding: utf-8 -*-
import re
import urllib2
import urllib
from base import jsunpack

def read2(url):
    opener = urllib2.build_opener()
    opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.71 Safari/537.36')]
    response = opener.open(url)
    data = response.read()
    return data

def urlgamovideo(url):
    source = read2(url)
    if 'File was deleted' in source or 'Not Found' in source or 'File was locked by administrator' in source:
        return 'El archivo no existe o ha sido borrado'
    if 'Video is processing now' in source:
        return 'El video está procesándose en estos momentos. Inténtelo mas tarde.'
    if 'File is awaiting for moderation' in source:
        return 'El video está esperando por moderación.'
    
    source = source.replace('\r\n','').replace('\r','').replace('\n','').replace('\t','')
    jspack = re.findall("<script type='text/javascript'>(eval.function.p,a,c,k,e,d..*?)</script>", source, re.IGNORECASE)[0]

    if jspack != "":
        source = jsunpack.unpack(jspack)
        
    finalurlgamo = re.findall('file:"(http.*?mp4)"', source, re.IGNORECASE)[0]
    header_test = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36'}
    header_test = '|' + urllib.urlencode(header_test)
    return finalurlgamo + header_test
