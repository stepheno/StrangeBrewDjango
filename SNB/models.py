from django.db import models
from django.contrib.auth.models import User
from django.contrib.localflavor.us.models import PhoneNumberField,USStateField
from django.contrib.localflavor.us.us_states import STATE_CHOICES

# Brewing Method Choices
TYPE_CHOICES = (
    ('All Grain','All Grain'),
    ('Partial Mash','Partial Mash'),
    ('Extract','Extract'),
)

class UserProfile(models.Model):
    home_address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = USStateField(choices=STATE_CHOICES)
    zip = models.CharField(max_length=10)
    phone_number = PhoneNumberField('Phone Number',blank=True)
    is_bjcp = models.BooleanField()
    club = models.CharField(max_length=100,null=True,blank=True)
    user = models.ForeignKey(User, unique=True)

    def __unicode__(self):
        return self.club

class Category(models.Model):
    category = models.CharField(max_length=25)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000,null=True,blank=True)

    def __unicode__(self):
        return "%s - %s" % (self.category,self.name)
    class Meta:
        verbose_name_plural = "Categories"

class Competition(models.Model):
    competition = models.CharField(max_length=200)
    date = models.DateField()
    registration_deadline = models.DateField()
    entry_deadline = models.DateField()
    location = models.CharField(max_length=500)
    fee = models.DecimalField(decimal_places=2,max_digits=4)

    def __unicode__(self):
        return "%s - %s" % (self.competition,self.date)

class Judging(models.Model):
    user = models.ForeignKey(User,null=True,blank=True)
    competition = models.ForeignKey(Competition)
    preferred_styles = models.ManyToManyField(Category)

    def __unicode__(self):
    	return "%s - %s" % (self.competition,self.user.first_name)

class Entry(models.Model):
    category = models.ForeignKey(Category)
    description = models.CharField(max_length=500)
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User,null=True,blank=True)
    type = models.CharField(max_length=20,choices=TYPE_CHOICES)
    competition = models.ForeignKey(Competition)

    def __unicode__(self):
        return "%s - %s" % (self.category.category,self.name)

    class Meta:
        verbose_name_plural = "Entries"
