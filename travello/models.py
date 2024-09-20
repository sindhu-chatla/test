from django.db import models
#from .models import Person
# Create your models here.
class Destination(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='hai/')
    desc = models.TextField()
    price = models.IntegerField()
    def __str__(self):
        return self.name
class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.TextField()
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='people', null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    def __str__(self):
        return self.name
class Profile(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='profiles/')

    def __str__(self):
        return f'{self.person.name} Profile'
'''queryset = Person.objects.all()
queryset'''