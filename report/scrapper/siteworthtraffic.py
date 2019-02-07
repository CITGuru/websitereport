from bs4 import BeautifulSoup
import requests
try:
    from report.scrapper.utils import get_html, strip_url, get_name
except:
    from utils import get_html, strip_url, get_name
    
URL = "http://siteworthtraffic.com/report/{}"

def extract_number(string):
    string = string.split()
    _str = string[0]
    return _str

def scrape_report(url):
    html = get_html(URL.format(strip_url(url)))
    soup = BeautifulSoup(html, "lxml")
    wrapper = soup.select_one("#content > div > div.wrapper")
    title = wrapper.select_one(".left h1#page-title")
    if title.text == "An Error Occurred":
        return {"success":False, "code":404, "site":url}
    first_paragraph = wrapper.select_one(".left p")
    dib = first_paragraph.select("b")
    # print(first_paragraph, title)
    data = {
        "website":dib[0].text,
        "url":dib[0].text,
        "worth":dib[1].text,
        "daily_unique_users":extract_number(dib[2].text),
        "daily_page_views":extract_number(dib[3].text),
        "daily_revenue":dib[4].text,
        "alexa_rank": dib[5].text,
        "success": True,
        "code": 200,
        "name": get_name(url)
    }
    return data
