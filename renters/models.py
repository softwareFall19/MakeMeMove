from django.db import models
from django.contrib.auth.models import User
from agents.models import Agent
from datetime import datetime

class Rental(models.Model):
    """Creating the components of Listing; to be coupled with the movingdb database."""
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, related_name=None)
    agent = models.ForeignKey(Agent, on_delete=models.DO_NOTHING, blank=True, null=True)
    property_title = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=200)
    State_Choices = (
        ("AL", "AL"), ("AK", "AK"), ("AZ", "AZ"), ("AR", "AR"), ("CA", "CA"),
        ("CO", "CO"), ("CT", "CT"), ("DE", "DE"), ("FL", "FL"), ("GA", "GA"),
        ("HI", "HI"), ("ID", "ID"), ("IL", "IL"), ("IN", "IN"), ("IA", "IA"), ("KS", "KS"),
        ("KY", "KY"), ("LA", "LA"), ("ME", "ME"), ("MD", "MD"), ("MA", "MA"),
        ("MI", "MI"), ("MN", "MN"), ("MS", "MS"), ("MO", "MO"), ("MT", "MT"),
        ("NE", "NE"), ("NV", "NV"), ("NH", "NH"), ("NJ", "NJ"), ("NM", "NM"),
        ("NY", "NY"), ("NC", "NC"), ("ND", "ND"), ("OH", "OH"), ("OK", "OK"),
        ("OR", "OR"), ("PA", "PA"), ("RI", "RI"), ("SC", "SC"),
        ("SD", "SD"), ("TN", "TN"), ("TX", "TX"), ("UT", "UT"), ("VT", "VT"), ("VA", "VA"),
        ("WA", "WA"), ("WV", "WV"), ("WI", "WI"), ("WY", "WY"),

    )
    state = models.CharField(max_length=100, choices= State_Choices)
    zipcode = models.CharField(max_length=100)
    information = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    garage = models.IntegerField(default=0, blank=True)
    homesize = models.IntegerField()
    top_photo = models.ImageField(upload_to='pictures/%Y/%m/%d/')
    picture1 = models.ImageField(upload_to='pictures/%Y/%m/%d/', blank=True)
    picture2 = models.ImageField(upload_to='pictures/%Y/%m/%d/', blank=True)
    picture3 = models.ImageField(upload_to='pictures/%Y/%m/%d/', blank=True)
    picture4 = models.ImageField(upload_to='pictures/%Y/%m/%d/', blank=True)
    picture5 = models.ImageField(upload_to='pictures/%Y/%m/%d/', blank=True)
    picture6 = models.FileField(upload_to='pictures/%Y/%m/%d/', blank=True)
    is_posted = models.BooleanField(default=True)
    date_posted = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.property_title
