from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Recommended by Django.
    Inherit all the same functionality.

    Makes the User object part of our object instead of hidden behind the Django framework.
    Enables custom configuration if needed later.
    """
    ...


class FieldDisplay(models.Model):
    """
    This model was created to display an overview of which Fields that exist in Django.

    You should inspect it in the admin panel.
    """

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


class Author(models.Model):
    first_name = models.CharField(max_length=42, blank=True, null=True)
    last_name = models.CharField(max_length=42, blank=True, null=True)
    born = models.DateTimeField(blank=True, null=True)

    def __str__(self) -> str:
        """
        Returns the string representation of an instance.
        We want to see the full name (strip whitespace if partially missing name)
        """
        return f'{self.last_name} {self.last_name}'.strip()


class BlogPost(models.Model):
    title = models.CharField(max_length=100, blank=False, null=True)
    text = models.TextField(blank=False, null=True)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, blank=True, null=True)
    published = models.DateTimeField()
    hidden = models.BooleanField(default=False)

    last_updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        """
        Returns the string representation of an instance.
        We want to see the title.
        """
        return f'{self.title}'
