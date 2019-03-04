# -*- coding: utf-8 -*-
import urllib
import re
import urllib2
from base import jsunpack
import json
import urlparse

def read2(url):
    opener = urllib2.build_opener()
    opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.71 Safari/537.36')]
    try:
        response = opener.open(url)
	data = response.read()
    except:
        data = 'fail 404'
    return data

def calidadesclipwatching(url):
    sources = read2(url)
    if 'File was deleted' in sources or 'fail 404' in sources:
        return 'dead'
    
    sources = sources.replace('\r\n','').replace('\r','').replace('\n','').replace('\t','')
    jspack = re.findall("<script type='text/javascript'>(eval.function.p,a,c,k,e,d..*?)</script>", sources, re.IGNORECASE)[0]

    if jspack != "":
        sources = jsunpack.unpack(jspack)
        sources = re.findall('.*?sources:(\[.*?\]).*?', sources, re.IGNORECASE)[0]
        sources = sources.replace('file','"file"').replace('label','"label"')
        sources = json.loads(sources)
    else:
        return 'dead'
    
    calidades = {}
    for source in sources:
        calidades[source['label']]=source['label']

    return calidades
    
def urlclipwatching(url):
    calidad = urlparse.parse_qs(url)['q'][0]
    url = url.split('&q')[0]
    sources = read2(url)
    if 'File was deleted' in sources or 'fail 404' in sources:
        return 'dead'
    
    sources = sources.replace('\r\n','').replace('\r','').replace('\n','').replace('\t','')
    jspack = re.findall("<script type='text/javascript'>(eval.function.p,a,c,k,e,d..*?)</script>", sources, re.IGNORECASE)[0]

    if jspack != "":
        sources = jsunpack.unpack(jspack)
        sources = re.findall('.*?sources:(\[.*?\]).*?', sources, re.IGNORECASE)[0]
        sources = sources.replace('file','"file"').replace('label','"label"')
        sources = json.loads(sources)
    else:
        return 'dead'
    
    for source in sources:
        if calidad == source['label']:
            finalurlclipwatching = source['file'] 
    
    header_test = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    header_test = '|' + urllib.urlencode(header_test)
    return finalurlclipwatching.replace('https','http') + header_test
