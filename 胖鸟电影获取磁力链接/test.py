import requests
import re

url = "http://www.pniao.com/Mov/one/b2NwRkh1NCtnc1JmZUtPYnpxcE1UblpvemUxdk03T3dsZ09pY1VoRGowMD0=.html"
# http://www.pniao.com/Mdown/ajax_downUrls/b2NwRkh1NCtnc1JmZUtPYnpxcE1UblpvemUxdk03T3dsZ09pY1VoRGowMD0=
# str = http://www.pniao.com/Mdown/ajax_downUrls/ +  id + =
url ="http://www.pniao.com/Mdown/ajax_downUrls/b2NwRkh1NCtnc1JmZUtPYnpxcE1UblpvemUxdk03T3dsZ09pY1VoRGowMD0="

headers = {

"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
"Accept-Encoding": "gzip, deflate",
"Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
"Cache-Control": "max-age=0",
"Connection": "keep-alive",
"Host": "www.pniao.com",
"Referer": "http://www.pniao.com/Mov/latest/movie",
"Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"


}


r = requests.get(url,headers = headers)

# print(r.text)

str = r.text
pattern = re.compile(r"\"magnet.*?\"")
ok = pattern.findall(str)


print(ok)


