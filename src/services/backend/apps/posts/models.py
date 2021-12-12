import os
from PIL import Image
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class Post(models.Model):
    class IntervalChoices(models.TextChoices):
        HOUR = 'hr', _('hr')
        DAY = 'day', _('day')
        WEEK = 'week', _('week')
        MONTH = 'month', _('month')
        YEAR = 'year', _('year')

    class ExpertiseChoices(models.TextChoices):
        STD = 'Student', _('Student')
        JNR = 'Junior', _('Junior')
        MDL = 'Mid-Level', _('Mid-Level')
        SNR = 'Senior', _('Senior')
        EPT = 'Expert', _('Expert')
        
    class EnvironmentChoices(models.TextChoices):
        NON = 'Not Specified', _('Not Specified')
        RMT = 'Remote', _('Remote')
        OFC = 'Office', _('Office')
        
    class CompensationChoices(models.TextChoices):
        USD = 'USD', _('USD')
        RND = 'ZAR', _('ZAR')
        BTC = 'BTC', _('BTC')
        ETH = 'ETH', _('ETH')
        
    class JobChoices(models.TextChoices):
        CON = 'Contract', _('Contract')
        FLT = 'Permanent', _('Permanent')
        ITN = 'Internship', _('Internship')
        
    class IndustryChoices(models.TextChoices):
        ACC = 'Accounting', _('Accounting')
        ADV = 'Advertising', _('Advertising')
        AGR = 'Agriculture', _('Agriculture')
        BFI = 'Banking & Finance', _('Banking & Finance')
        CST = 'Construction', _('Construction')
        NON = 'None', _('None')
        PCP = 'Computer Programming', _('Computer Programming')

    title = models.CharField(max_length=55)
    description = models.TextField(max_length=2000, null=True, blank=True)
    location = models.CharField(max_length=255, blank=True)
    compensation = models.DecimalField(max_digits=10, decimal_places=4)
    currency = models.CharField(
        max_length=255,
        blank=True,
        choices=CompensationChoices.choices,
        default=CompensationChoices.USD,
    )
    interval = models.CharField(
        max_length=255,
        blank=True,
        choices=IntervalChoices.choices,
        default=IntervalChoices.DAY,
    )
    industry = models.CharField(
        max_length=255,
        blank=True,
        choices=IndustryChoices.choices,
        default=IndustryChoices.NON,
    )
    experience = models.CharField(
        max_length=255,
        blank=True,
        choices=ExpertiseChoices.choices,
        default=ExpertiseChoices.JNR,
    )
    tech = models.TextField(max_length=995, blank=True)
    environment = models.CharField(
        max_length=255,
        blank=True,
        choices=EnvironmentChoices.choices,
        default=EnvironmentChoices.NON,
    )
    mode = models.CharField(
        max_length=255,
        blank=True,
        choices=JobChoices.choices,
        default=JobChoices.CON,
    )
    benefits = models.TextField(max_length=995, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    
    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        ordering = ['-created']

    def __str__(self):
        return self.title

