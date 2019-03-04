# -*- coding: utf-8 -*-
import urllib
import urllib2
import re
import time

def read2(url):
    opener = urllib2.build_opener()
    opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.71 Safari/537.36')]
    response = opener.open(url)
    data = response.read()
    return data


def get_video_streamango(page_url):
    if '/f/' in page_url:
        page_url='https://streamango.com/embed/' + page_url.split('/f/')[1].split('/')[0]
    data = read2(page_url)

    video_urls = []
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.71 Safari/537.36'}
    matches = re.search('''srces\.push\(.*?{type:"video/mp4",src:\w+\('([^']+)',(\d+)''', data)
    if matches:

        source = decode(matches.group(1), int(matches.group(2)))
        if source:
            source = "http:%s" % source if source.startswith("//") else source
            source = source.split("/")
            if not source[-1].isdigit():
              source[-1] = re.sub('[^\d]', '', source[-1])
            source = "/".join(source)
            headers.update({'Referer': page_url})
            time.sleep(1)
            return source + '|'+ urllib.urlencode(headers)


def decode(encoded, code):

    _0x59b81a = ""
    k = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/='
    k = k[::-1]

    count = 0

    for index in range(0, len(encoded) - 1):
        while count <= len(encoded) - 1:
            _0x4a2f3a = k.index(encoded[count])
            count += 1
            _0x29d5bf = k.index(encoded[count])
            count += 1
            _0x3b6833 = k.index(encoded[count])
            count += 1
            _0x426d70 = k.index(encoded[count])
            count += 1

            _0x2e4782 = ((_0x4a2f3a << 2) | (_0x29d5bf >> 4))
            _0x2c0540 = (((_0x29d5bf & 15) << 4) | (_0x3b6833 >> 2))
            _0x5a46ef = ((_0x3b6833 & 3) << 6) | _0x426d70
            _0x2e4782 = _0x2e4782 ^ code

            _0x59b81a = str(_0x59b81a) + chr(_0x2e4782)

            if _0x3b6833 != 64:
                _0x59b81a = str(_0x59b81a) + chr(_0x2c0540)
            if _0x3b6833 != 64:
                _0x59b81a = str(_0x59b81a) + chr(_0x5a46ef)

    return _0x59b81a
