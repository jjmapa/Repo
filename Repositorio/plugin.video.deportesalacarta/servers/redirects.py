# -*- coding: utf-8 -*-
# ------------------------------------------------------------
# deportesalacarta - XBMC Plugin
# Conector para animeid, animeflv, jkanime
# ------------------------------------------------------------

import re
import urllib2

from core import logger
from core import scrapertools


def get_video_url(page_url, premium=False, user="", password="", video_password=""):
    video_urls = []
    if 'jkanime' in page_url:
        request_headers = {
            "Accept-Language": "en-US,en;q=0.5",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Connection": "keep-alive"
        }
        jk_url = page_url.replace("/jk.php?u=stream/", "/stream/")
        request = urllib2.Request(jk_url, headers=request_headers)
        response = urllib2.urlopen(request)
        video_urls.append([".mp4 [redirects]", response.geturl()])
    else:
        headers = []
        headers.append(["User-Agent",
                        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.94 Safari/537.36"])
        headers.append(["Accept-Encoding", "gzip,deflate,sdch"])
        page_url = page_url.replace("https://animeflv.net/embed_izanagi.php?key=",
                                    "https://s2.animeflv.net/izanagi.php?id=")
        page_url = page_url.replace("http://animeflv.net/embed_yotta.php?key=", "https://s1.animeflv.com/gdrive.php?id=")
        data = scrapertools.cache_page(page_url, headers=headers)
        data = data.replace("\\\\", "")
        data = data.replace("\\/", "/")
        patronvideos = '"file":"(.+?)"'
        matches = re.compile(patronvideos, re.DOTALL).findall(data)
        for match in matches:
            video_urls.append([".mp4 [redirects]", match])

        patronvideos = '(http://www.animeid.+?)"'
        matches = re.compile(patronvideos, re.DOTALL).findall(data)
        for match in matches:
            response = urllib2.urlopen(match)
            video_urls.append([".mp4 [redirects]", response.geturl()])

    return video_urls


# Encuentra vídeos del servidor en el texto pasado
def find_videos(data):
    encontrados = set()
    devuelve = []
    patronvideos = '(https://animeflv.net/embed_izanagi.php\?key=.+?),'
    logger.info("#" + patronvideos + "#")
    matches = re.compile(patronvideos, re.DOTALL).findall(data)

    titulo = "[izanagi]"
    for match in matches:
        url = match
        if url not in encontrados:
            logger.info("  url=" + url)
            devuelve.append([titulo, url, 'redirects'])
            encontrados.add(url)
        else:
            logger.info("  url duplicada=" + url)

    patronvideos = "(https://s1.animeflv.com/gdrive.php?id=.+?)\\\\"
    logger.info("#" + patronvideos + "#")
    matches = re.compile(patronvideos, re.DOTALL).findall(data)

    for match in matches:
        titulo = "[yotta]"
        url = match

        if url not in encontrados:
            logger.info("  url=" + url)
            devuelve.append([titulo, url, 'redirects'])
            encontrados.add(url)
        else:
            logger.info("  url duplicada=" + url)

    patronvideos = "(http://www.animeid..{2,3}/embed/.+?/)"
    logger.info("#" + patronvideos + "#")
    matches = re.compile(patronvideos, re.DOTALL).findall(data)

    titulo = "[animeimoe]"
    for match in matches:
        url = match

        if url not in encontrados:
            logger.info("  url=" + url)
            devuelve.append([titulo, url, 'redirects'])
            encontrados.add(url)
        else:
            logger.info("  url duplicada=" + url)

    patronvideos = "(https://jkanime.net/jk.php\?u=stream/jkmedia.+?)\s"
    logger.info("#" + patronvideos + "#")
    matches = re.compile(patronvideos, re.DOTALL).findall(data)

    titulo = "[jkanime]"
    for match in matches:
        url = match.replace('"', '')

        if url not in encontrados:
            logger.info("  url=" + url)
            devuelve.append([titulo, url, 'redirects'])
            encontrados.add(url)
        else:
            logger.info("  url duplicada=" + url)

    return devuelve
