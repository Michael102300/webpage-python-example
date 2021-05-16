from django.db import models

# Create your models here.
class User(models.Model):
    name = models.TextField(verbose_name="names")
    lastname = models.TextField(verbose_name="lastnames")
    email = models.EmailField(verbose_name="emails")
    phone = models.IntegerField(max_length=10, verbose_name="phone")
    plaque = models.TextField(verbose_name="plaque")
    vehicule = models.TextField(verbose_name="vehicule")

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        db_table= "User"
        ordering=['id']

    def __str__(self):
        return self.name

