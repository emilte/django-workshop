from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ...


class FieldDisplay(models.Model):

    class Type(models.TextChoices):
        NURSE = 'nurse'
        DOCTOR = 'doctor'

    charfield = models.CharField(max_length=140, blank=True, null=True)
    charfield_unique = models.CharField(max_length=140, unique=True, blank=True, null=True)
    unique_together_one = models.CharField(max_length=140, unique=True, blank=True, null=True)
    unique_together_two = models.CharField(max_length=140, unique=True, blank=True, null=True)
    charfield_unique = models.CharField(max_length=140, unique=True, blank=True, null=True)
    textfield = models.TextField(blank=True, null=True)
    boolean = models.BooleanField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    boolean = models.DateTimeField(blank=True, null=True)
    choices = models.CharField(choices=Type.choices, max_length=20, blank=True, null=True)
    many_to_many = models.ManyToManyField(to='FieldDisplay', related_name='many', blank=True)
    foreignkey = models.ForeignKey(to='FieldDisplay', on_delete=models.PROTECT, related_name='foreign', blank=True, null=True)
    duration = models.DurationField(blank=True, null=True)
    file_field = models.FileField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    float_field = models.FloatField(blank=True, null=True)
    integer = models.SmallIntegerField(blank=True, null=True)
    email = models.IntegerField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    json = models.JSONField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    uuid = models.UUIDField(blank=True, null=True)

    updated = models.DateTimeField(auto_now=True, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        """
        All models can have a Meta class to further configure behaviour.
        This is documented by Django.
        https://docs.djangoproject.com/en/4.1/ref/models/options/
        """
        ordering = ['updated']
        unique_together = [
            ('unique_together_one', 'unique_together_two'),
        ]
        permissions = [
            ('can_change_created_date', 'Can change created date'),
        ]
        get_latest_by = ['-created']
