from bs4 import BeautifulSoup
import requests
try:
    from report.scrapper.utils import get_html, strip_url, get_name
except:
    from utils import get_html, strip_url, get_name

URL = "http://{}.cutestat.com"

def scrape_report(url):
    html = get_html(URL.format(strip_url(url)))
    soup = BeautifulSoup(html, "lxml")
    stat_overview = soup.select_one(".stat_half_right .stat_overview").text
    age = stat_overview.split("is")[1].split(".")[0].strip()
    seo_info = soup.select(".stat_details .row-fluid.marginBottom_10 .span9 table")
    seo_info = "{} <br> {}".format(str(seo_info[2]), str(seo_info[3]))
    data = {
        "age":age,
        "seo_info":seo_info
    }
    return data

# print(scrape_report("http://siitgo.com"))