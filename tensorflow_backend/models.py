# only contains common model which used between apps
from django.db import models


class Session(models.Model):
    name = models.CharField(max_length=1024)
    start_date = models.DateTimeField()


class Person(models.Model):
    name = models.CharField(max_length=255, unique=True)
    full_name = models.CharField(max_length=2014, default="")
    image_url = models.CharField(max_length=1024)


class Image(models.Model):
    PENDING = "PENDING"
    SUCCESS = "SUCCESS"
    STATUS_CHOICE = ((PENDING, PENDING), (SUCCESS, SUCCESS))

    name = models.CharField(max_length=100, default="", null=True, unique=True)
    session = models.ForeignKey(Session)
    person = models.ForeignKey(Person, null=True)
    prob = models.FloatField(default=0)
    status = models.CharField(max_length=16, choices=STATUS_CHOICE, default=PENDING)
    created_date = models.DateTimeField(auto_now_add=True)
    response_date = models.DateTimeField(null=True)


class Food(models.Model):
    name = models.CharField(max_length=1024)
    image_url = models.CharField(max_length=1024)
    food_number = models.CharField(max_length=16)


class FoodPerson(models.Model):
    NOT_CHECKED = "NOT_CHECKED"
    CHECKED = "CHECKED"
    STATUS_CHOICES = ((NOT_CHECKED, NOT_CHECKED), (CHECKED, CHECKED))

    person = models.ForeignKey(Person)
    food = models.ForeignKey(Food)
    date = models.DateTimeField()
    status = models.CharField(max_length=16, choices=STATUS_CHOICES, default=NOT_CHECKED)


class SessionPerson(models.Model):
    person = models.ForeignKey(Person)
    session = models.ForeignKey(Session)
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (('person', 'session'),)