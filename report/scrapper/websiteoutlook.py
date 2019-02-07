import os

from bs4 import BeautifulSoup
import requests
try:
    from report.scrapper.utils import get_html, strip_url, get_name
except:
    from utils import get_html, strip_url, get_name
    
URL = "http://{}.websiteoutlook.com"

def open_html():
    html_file = open("/home/oyetoke/websiterport/report/scrapper/websiteoutlook.html").read()
    return html_file

def scrape_report(url=None):
    # html = open_html()
    
    if url:
        html = get_html(URL.format(strip_url(url)))

    soup = BeautifulSoup(html, "lxml")
    basic = soup.select_one("#basic table")
    website = soup.select_one("#website .dl-horizontal")
    dns = soup.select_one("#dns table")
    ip_info = soup.select_one("#geo .dl-horizontal")
    whois = soup.select_one("#whois pre")
    data = {
        "website_info":str(website),
        "basic_info":str(basic),
        "dns_info": str(dns),
        "ip_info": str(ip_info),
        "whois_info": str(whois)
    }
    return data

# print(scrape_report("facebook.com"))