from django.db import models

class DogWalker(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    company_name = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=64)
    email = models.EmailField(max_length=254)

    def __unicode__(self):
        return '%s' '%s' '%s' '%s' '%s'  % (self.first_name, self.last_name,
        self.company_name, self.phone_number, self.email)

class DogOwner(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=64)
    email = models.EmailField(max_length=254)
    emergency_contact = models.CharField(max_length=64)
    contact_phone = models.CharField(max_length=64)
    vet_name = models.CharField(max_length=64)
    vet_phone = models.CharField(max_length=64)
    dogwalker = models.ForeignKey('DogWalker')

    def __unicode__(self):
        return '%s' '%s' '%s' '%s' '%s' '%s' '%s' '%s' '%s' % (self.first_name,
        self.last_name, self.phone_number, self.email, self.emergency_contact,
        self.contact_phone, self.vet_name, self.vet_phone, self.dogwalker)

class Dog(models.Model):
    FEMALE = 'F'
    MALE = 'M'
    OTHER = 'O'
    SEX_CHOICES = {
        (FEMALE, 'F'),
        (MALE, 'M'),
        (OTHER, 'O'),
    }
    sex = models.CharField(max_length=1,
                           choices=SEX_CHOICES,
                           default=OTHER)
    owner = models.ForeignKey('DogOwner')
    dog_name = models.CharField(max_length=64)
    breed = models.CharField(max_length=64)
    needs = models.TextField()

class Walk(models.Model):
    ONE = '1'
    TWO = '2'
    THREE = '3'
    FOUR = '4'
    FIVE = '5'
    STAR_CHOICES = {
        (ONE, '1'),
        (TWO, '2'),
        (THREE, '3'),
        (FOUR, '4'),
        (FIVE, '5'),
    }
    obedience_rating = models.CharField(max_length=1,
                                        choices=STAR_CHOICES,
                                        default=THREE)
    ONE = '1'
    TWO = '2'
    THREE = '3'
    FOUR = '4'
    FIVE = '5'
    MOOD_CHOICES = {
        (ONE, '1'),
        (TWO, '2'),
        (THREE, '3'),
        (FOUR, '4'),
        (FIVE, '5'),
    }
    dog_mood = models.CharField(max_length=1,
                                        choices=MOOD_CHOICES,
                                        default=THREE)
    dogwalker = models.ForeignKey('DogWalker')
    dog = models.ForeignKey('Dog')
    start_time = models.DateTImeField()
    end_time = models.DateTimeField()
    walk_location = models.TextField()
    elapsed_distance = models.FloatField()
    elapsed_time = models.FloatField()


class Event(models.Model):

