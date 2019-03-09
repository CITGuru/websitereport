from django.shortcuts import render, redirect
from report.scrapper import siteworthtraffic, alexa, websiteoutlook, cutestat
from report.models import Website
from report.scrapper.utils import strip_url
# Create your views here.


def recent_analysed(limit=10):
    if limit:
        if limit == "all":
            website = Website.objects.all().order_by("-created")
        else:
            website = Website.objects.all().order_by("-created")[:limit]
    return website


def home(request):
    recent_site = recent_analysed()

    return render(request, "index.html", {"recent_site": recent_site})

def add(request):
    recent_site = recent_analysed()

    return render(request, "add.html", {"recent_site": recent_site})


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

def update(request, url):
    data = scrape_site_report(url)
    print(url)
    website = Website.objects.get(url=url)
    website.age=data.get("age")
    website.worth=data["worth"]
    website.daily_unique_users=data["daily_unique_users"]
    website.daily_page_views=data["daily_page_views"]
    website.daily_revenue=data["daily_revenue"]
    website.alexa_rank=data["alexa_rank"]
    website.website_info=data["website_info"]
    website.basic_info=data["basic_info"]
    website.dns_info=data["dns_info"]
    website.whois_info=data["whois_info"]
    website.ip_info=data["ip_info"]
    website.seo_info=data["seo_info"]
    website.similar_websites=data["similar_websites"]
    website.save()
    return redirect(f"/lookup/{url}")

def loookup(request):
    return redirect("/lookup/{}".format(strip_url(request.GET.get("site"))))

def lookup(request, url):

    context = {}
    recent_site = recent_analysed()
    context["recent_site"] = recent_site
    website = Website.objects.filter(url=strip_url(url))
    if not website.exists():
        data = scrape_site_report(url)
        context["data"] = data
        create_website(data)
    else:
        data = website.first()
        context["data"] = data

    return render(request, "lookup.html", context)

def recent(request):
    context = {}
    recent_site = recent_analysed("all")
    context["recent_site"] = recent_site
    return render(request, "recent.html", context)


