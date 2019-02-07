from django.shortcuts import render
from report.scrapper import siteworthtraffic,alexa, websiteoutlook, cutestat
from report.models import Website
from report.scrapper.utils import strip_url
# Create your views here.
def home(request):
    return render(request, "index.html")

def create_website(data):
    website = Website.objects.create(
        name=data.get("name"),
        url=data.get("url"),
        age=data.get("age"),
        worth=data["worth"],
        daily_unique_users=data["daily_unique_users"],
        daily_page_views=data["daily_page_views"],
        daily_revenue=data["daily_revenue"],
        alexa_rank=data["alexa_rank"],
        website_info=data["website_info"],
        basic_info=data["basic_info"],
        dns_info=data["dns_info"],
        whois_info=data["whois_info"],
        ip_info=data["ip_info"],
        seo_info=data["seo_info"],
        similar_websites=data["similar_websites"]
    )
    return website

def scrape_site_report(url):
    data = siteworthtraffic.scrape_report(url)
    data.update(websiteoutlook.scrape_report(url))
    data.update(cutestat.scrape_report(url))
    data.update(alexa.scrape_report(url))
    return data

def lookup(request):
    context = {}
    url = request.GET.get("site")
    website = Website.objects.filter(url=strip_url(url))
    if not website.exists():
        data = scrape_site_report(url)
        context["data"]=data
        create_website(data)
    else:
        data = website.first()
        context["data"]=data

    return render(request, "lookup.html", context)