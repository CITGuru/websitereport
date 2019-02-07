import requests

cookies = {
    '_omappvp': 'oRlqyTdkxzYopr6UWBDOKHJYmtKEsZnX0GvinZub0m16Dw9pMPCXSA6pWixKShASeHHwGxa13pRHz2MWkpVmAgLPllIynoBt',
    'cookiebanner-accepted': '1',
    '_ga': 'GA1.2.1541156287.1548626961',
    '__utmc': '183319076',
    '__utmz': '183319076.1548813690.2.2.utmcsr=l.facebook.com|utmccn=(referral)|utmcmd=referral|utmcct=/',
    '__utma': '183319076.1541156287.1548626961.1548923427.1548926978.6',
    '__unam': 'b14a8e2-168915c1f53-ea03126-90',
    '__utmb': '183319076.3.10.1548926979',
}

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,ha;q=0.8',
}


def get_html(url):
    print(url)
    request = requests.get(url, headers=headers, cookies=cookies)
    print(request)
    if request.status_code == 200:
        return request.content
    else:
        raise Exception("Error occured")


def strip_url(url):
    _url = url.replace("http://", "").replace("https://", "").replace("www.", "")
    return _url

def get_name(url):
    _url = strip_url(url)
    _url = _url.split(".")
    name = _url[-2]
    return name
    
# print(get_html("http://www.siteworthtraffic.com/report/siitgo.com"))