from django.conf import settings
from django.db import models
from django.utils import timezone


class UserMixin(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        null=Fasle,
        blank=False,
        verbose_name='User',
        help_text='',

    )

    class Meta:
        abstract = True


class Category(models.Model, UserMixin):

    name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        verbose_name="Name",
        help_text='',
    )

    slug = models.SlugField()

    description = models.CharField(
        max_length=150,
        blank=True,
        verbose_name="Description",
        help_text='',
        default='',

    )

    image_url = models.URLField(
        verbose_name="Image URL",
        help_text='',
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        null=Fasle,
        blank=False,
        verbose_name='User',
        help_text='',

    )


class Plant(models.Model, UserMixin):

    name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        verbose_name="Name",
        help_text='',
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        null=Fasle,
        blank=False,
        verbose_name='Category',
        help_text='',

    )

    watering_interval = models.PositiveIntegerField(
        null=False,
        blank=False,
        verbose_name='Watering interval',
        help_text="In seconds",
    )

    fertilizing_interval = models.PositiveIntegerField(
        null=False,
        blank=False,
        verbose_name='Fertilising interval',
        help_text="In seconds",
    )

    EXPOSURE_CHOICES = [
        ('dark', 'Dark'),
        ('shade', 'Shade'),
        ('partsun', 'Part Sun'),
        ('fullsun', 'Full Sun'),
    ]

    required_exposure = models.CharField(
        max_length=10, choices=EXPOSURE_CHOICES,
        null=False, blank=False,
        verbose_name='Amount of sun',
        help_text='Amount of sun'
    )

    HUMIDITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    required_humidity = models.CharField(
        max_length=10, choices=HUMIDITY_CHOICES,
        null=False, blank=False,
        verbose_name='Humidity',
        help_text=''
    )

    TEMPERATURE_CHOICES = [
        ('cold', 'Cold'),
        ('medium', 'Medium'),
        ('warm', 'Warm'),
    ]

    required_temperature = models.CharField(
        max_length=10, choices=TEMPERATURE_CHOICES,
        null=False, blank=False,
        verbose_name='Temperature',
        help_text=''
    )

    blooming = models.BooleanField(
        default=False,
        null=False,
        blank=True,
        help_text=''
    )

    DIFFICULTY_CHOICES = [
        (1, 'Low'),
        (2, 'Medium-Low'),
        (3, 'Medium'),
        (4, 'Medium-Hight'),
        (5, 'Hight'),

    ]

    difficulty = models.PositiveIntegerField(
        choices=DIFFICULTY_CHOICES,
        null=False,
        blank=False,
        default=1,
        verbose_name='Cultivation difficulty level',
        help_text='',

    )


class Room(models.Model, UserMixin):
    name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        verbose_name="Name",
        help_text='',
    )

    EXPOSURE_CHOICES = [
        ('dark', 'Dark'),
        ('shade', 'Shade'),
        ('partsun', 'Part Sun'),
        ('fullsun', 'Full Sun'),
    ]

    room_exposure = models.CharField(
        max_length=10, choices=EXPOSURE_CHOICES,
        null=False, blank=False,
        verbose_name='Amount of sun in the room',
        help_text=''
    )

    HUMIDITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    room_humidity = models.CharField(
        max_length=10, choices=HUMIDITY_CHOICES,
        null=False, blank=False,
        verbose_name='Humidity in the room',
        help_text=''
    )

    TEMPERATURE_CHOICES = [
        ('cold', 'Cold'),
        ('medium', 'Medium'),
        ('warm', 'Warm'),
    ]

    room_temperature = models.CharField(
        max_length=10, choices=TEMPERATURE_CHOICES,
        null=False, blank=False,
        verbose_name='Temperature in the room',
        help_text=''
    )

    drafty = models.BooleanField(
        default=False,
        null=False,
        blank=False,
        help_text=''
    )


class UserPlant(models.Model, UserMixin):

    name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        verbose_name="Name",
        help_text='',
    )

    description = models.CharField(
        max_length=150,
        blank=True,
        verbose_name="Description",
        help_text='',
        default='',
    )

    room = models.ForeignKey(
        Room,
        on_delete=models.PROTECT,
    )

    plant = models.ForeignKey(
        Plant,
        on_delete=models.PROTECT,
    )

    last_watering = models.DateTimeField()

    last_fertilizing = models.DateTimeField()
