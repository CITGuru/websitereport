from bs4 import BeautifulSoup
import requests
try:
    from report.scrapper.utils import get_html, strip_url, get_name
except:
    from utils import get_html, strip_url, get_name

URL = "http://alexa.com/siteinfo/{}"

def scrape_report(url):
    print()
    html = get_html(URL.format(strip_url(url)))
    soup = BeautifulSoup(html, "lxml")
    similar_website = soup.select_one("#audience_overlap_table")
    similar_website = str(similar_website).replace("/siteinfo/", "/lookup?site=").replace("&amp;nbsp", "")
    print(similar_website)
    data = {
      "similar_websites":similar_website
    }
    return data

# print(scrape_report("http://siitgo.com"))