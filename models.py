from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE
from django.utils import timezone

# Create your models here.


'''
'''

COMPONENTTYPES = (
    (1, "herb"),
    (2, "gem"),
    (3, "leftover"),
    (4, "other"),
)

EQTYPES = (
    (10, "sword"),
    (20, "polearm"),
    (30, "axe"),
    (40, "club"),
    (50, "knife"),
    (60, "shield"),
    (70, "chest"),
    (80, "helm"),
    (90, "bracers"),
    (100, "legs"),
    (110, "feet"),
    (120, "ring"),
    (130, "neck"),
    (140, "hands"),
    (150, "cloak"),
    (160, "pack"),
    (170, "pouch"),
    (180, "other"),
)


class Domain(models.Model):
    name = models.CharField(max_length=16, unique=True)


    def populate(self):
        domain_names = ("Sparkle", "Earthsea", "Calia", "Terel", "Cirath", "Kalad",
                        "Ansalon", "Krynn", "Raumdor", "Faerun", "Shire", "Gondor",
                        "Avenir", "Emerald", "Kalakhor")
        for dname in domain_names:
            if dname not in self.objects.all():
                self.objects.create(name=dname)
                self.save()


    def __str__(self):
        return self.name


class Quest(models.Model):
    name = models.CharField(max_length=32)
    hint = models.TextField(null=True)
    solution = models.TextField()
    domain = models.ForeignKey(Domain)
    date_added = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User)

    def __str__(self):
        return self.name

'''
class Npc(models.Model):
    name = models.CharField(max_length=32)
    short_desc = models.CharField(max_length=32)
    comment = models.TextField()
    domain = models.OneToOneField(Domain)
    date_added = models.DateField()
    creator = models.ForeignKey(User)

    def __str__(self):
        return self.name


class Equipment(models.Model):
    name = models.CharField(max_length=32)
    owner = models.ForeignKey(Npc)
    desc = models.TextField()
    type = models.IntegerField(choices=EQTYPES)
    date_added = models.DateField()
    creator = models.ForeignKey(User)

    def __str__(self):
        return self.name


class Component(models.Model):
    name = models.CharField(max_length=32)
    type = models.SmallIntegerField(choices=COMPONENTTYPES)
    comment = models.TextField()
    date_added = models.DateField()
    creator = models.ForeignKey(User)

    def __str__(self):
        return self.name


class Scrapbook(models.Model):
    note = models.TextField()
    date_added = models.DateField()
    creator = models.ForeignKey(User, on_delete=CASCADE)

    def __str__(self):
        return self.creator.name
'''