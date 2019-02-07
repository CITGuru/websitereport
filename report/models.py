from django.db import models
from datetime import datetime
import uuid
# Create your models here.
class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(default=datetime.utcnow, editable=False)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        abstract = True

class Website(BaseModel):
    url = models.URLField()
    age = models.CharField(max_length=250, blank=True, null=True)
    name = models.CharField(max_length=250)
    worth = models.CharField(max_length=250)
    daily_unique_users = models.CharField(max_length=250)
    daily_page_views = models.CharField(max_length=250)
    daily_revenue = models.CharField(max_length=250)
    alexa_rank = models.CharField(max_length=250)
    website_info = models.TextField()
    basic_info = models.TextField()
    dns_info = models.TextField()
    ip_info = models.TextField()
    whois_info  = models.TextField()
    seo_info = models.TextField(blank=True, null=True)
    similar_websites = models.TextField(blank=True, null=True)

    def __str__(self):
        return "{} - {}".format(self.name, self.url)