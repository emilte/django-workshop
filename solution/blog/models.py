from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ...


class FieldDisplay(models.Model):

    class Type(models.TextChoices):
        NURSE = 'nurse'
        DOCTOR = 'doctor'

    charfield = models.CharField(max_length=140)
    charfield_unique = models.CharField(max_length=140, unique=True)
    unique_together_one = models.CharField(max_length=140, unique=True)
    unique_together_two = models.CharField(max_length=140, unique=True)
    charfield_unique = models.CharField(max_length=140, unique=True)

    textfield = models.TextField()
    boolean = models.BooleanField()
    time = models.TimeField()
    date = models.DateField()
    boolean = models.DateTimeField()
    choices = models.CharField(choices=Type.choices, max_length=20)
    many_to_many = models.ManyToManyField(to='FieldDisplay', related_name='many')
    foreignkey = models.ForeignKey(to='FieldDisplay', on_delete=models.PROTECT, related_name='foreign')
    duration = models.DurationField()
    file_field = models.FileField()
    email = models.EmailField()
    float_field = models.FloatField()
    integer = models.SmallIntegerField()
    email = models.IntegerField()
    image = models.ImageField()
    json = models.JSONField()
    url = models.URLField()
    uuid = models.UUIDField()

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        All models can have a Meta class to further configure behaviour.
        This is documented by Django.
        https://docs.djangoproject.com/en/4.1/ref/models/options/
        """
        ordering = ['updated']
        unique_together = ['unique_together_one', 'unique_together_two']
        permissions = [
            ('can_change_created_date', 'Can change created date'),
        ]
        get_latest_by = ['-created']
