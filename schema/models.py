from django.db import models
from datetime import datetime
from slugify import Slugify, UniqueSlugify
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from django.core.exceptions import ValidationError
from django_countries.fields import CountryField
from djchoices import DjangoChoices, ChoiceItem

class Manufacturer(models.Model):
    name = models.CharField(
        help_text='Name of the manufacturer', max_length=45, blank=True, unique=True)
    city = models.CharField(
        help_text='City in which the manufacturer is based', max_length=45, blank=True, null=True)
    country = CountryField(
        help_text='Country in which the manufacturer is based', blank=True, null=True)
    link = models.URLField(
        help_text='Link to the manufacturers main website', max_length=45, blank=True, null=True)
    founded = models.PositiveIntegerField(
        help_text='Year in which the manufacturer was founded', blank=True, null=True)
    dissolved = models.PositiveIntegerField(
        help_text='Year in which the manufacturer was dissolved', blank=True, null=True)
    slug = models.SlugField(editable=False, null=True, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = "manufacturers"
        indexes = [
            models.Index(fields=['slug',]),
            models.Index(fields=['country', 'country']),
        ]

    def save(self, *args, **kwargs):
        custom_slugify_unique = Slugify(to_lower=True)
        self.slug = custom_slugify_unique(self.name)
        return super().save(*args, **kwargs)

    def clean(self):
        # City/country
        if self.country is None and self.city is not None:
            raise ValidationError({
                'country': ValidationError(('Must specify country if city is given')),
            })
        # Founded/dissolved
        if self.founded is not None and self.dissolved is not None and self.founded > self.dissolved:
            raise ValidationError({
                'founded': ValidationError(('Founded date must be earlier than dissolved date')),
                'dissolved': ValidationError(('Dissolved date must be later than founded date')),
            })
        if self.founded is not None and self.founded > datetime.now().year:
            raise ValidationError({
                'founded': ValidationError(('Founded date must be in the past')),
            })
        if self.dissolved is not None and self.dissolved > datetime.now().year:
            raise ValidationError({
                'dissolved': ValidationError(('Dissolved date must be in the past')),
            })


class PaperStock(models.Model):
    # Choices for mount purposes
    class Finish(DjangoChoices):
        Matt = ChoiceItem()
        Gloss = ChoiceItem()
        Satin = ChoiceItem()
        Semi_gloss = ChoiceItem()
        Pearl = ChoiceItem()
        Lustre = ChoiceItem()

    name = models.CharField(
        help_text='Name of this paper stock', max_length=45)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE,
                                     blank=True, null=True, help_text='Manufacturer of this paper stock')
    resin_coated = models.BooleanField(
        help_text='Whether the paper is resin-coated', blank=True, null=True)
    colour = models.BooleanField(
        help_text='Whether this is a colour paper', blank=True, null=True)
    finish = models.CharField(help_text='The finish of the paper surface',
                              choices=Finish.choices, max_length=25, blank=True, null=True)

    def __str__(self):
        mystr = self.name
        if self.manufacturer is not None:
            mystr = str(self.manufacturer) + ' ' + mystr
        if self.finish is not None:
            mystr = mystr + ' [' + self.finish + ']'
        return mystr

    class Meta:
        ordering = ['manufacturer', 'name']
        verbose_name_plural = "paper stocks"
