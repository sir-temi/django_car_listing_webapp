from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse
from django_resized import ResizedImageField

class Car(models.Model):
    AUTO = 'Automatic'
    MANUAL = 'Manual'
    PETROL = 'Petrol'
    DIESEL = 'Diesel'
    LEATHER = 'Leather'
    FABRIC = 'Fabric'
    NAIJA = 'Naija Used'
    FOREIGN = 'Foreign Used'
    TRANSMISSION = [
        (None, 'Choose'),
        (AUTO, 'Automatic'),
        (MANUAL, 'Manual'),
    ]
    FUEL = [
        (None, 'Choose'),
        (PETROL, 'Petrol'),
        (DIESEL, 'Diesel'),
    ]
    INTERIOR = [
        (None, 'Choose'),
        (LEATHER, 'Leather'),
        (FABRIC, 'Fabric'),
    ]
    USED = [
        (None, 'Choose'),
        (FOREIGN, 'Foreign Used'),
        (NAIJA, 'Naija Used'),
    ]
    by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='by')
    title = models.CharField(max_length=100)
    maker = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
    mileage = models.PositiveIntegerField()
    foreign_or_naija_used = models.CharField(
        max_length=12,
        choices=USED
        )
    slugy = models.SlugField(unique=True, allow_unicode=True)
    uploaded = models.DateTimeField(default=timezone.now)
    colour = models.CharField(max_length=10)
    year = models.PositiveSmallIntegerField()
    doors = models.PositiveSmallIntegerField()
    transmission = models.CharField(
        max_length=10,
        choices=TRANSMISSION
        )
    fuel = models.CharField(
        max_length=10,
        choices=FUEL
        )
    interior = models.CharField(
        max_length=10,
        choices=INTERIOR
    )
    extra_features = models.TextField(max_length=500)
    description = models.TextField()
    # mainpic = models.ImageField(upload_to='images')
    mainpic = ResizedImageField(size=[600, 400], crop=['middle', 'center'], upload_to='images')
    pic1 = ResizedImageField(size=[600, 400], crop=['middle', 'center'], upload_to='images')
    pic2 = ResizedImageField(size=[600, 400], crop=['middle', 'center'], upload_to='images')
    pic3 = ResizedImageField(size=[600, 400], crop=['middle', 'center'], upload_to='images')
    pic4 = ResizedImageField(size=[600, 400], crop=['middle', 'center'], upload_to='images')
    pic5 = ResizedImageField(size=[600, 400], crop=['middle', 'center'], upload_to='images')

    def __str__(self):
        return f"{self.title} by {self.by.username}"

    def save(self, *args, **kwargs):
        self.slugy = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('cardetail', kwargs={'slug': self.slugy})

class Photos(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='car')
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.car.title
