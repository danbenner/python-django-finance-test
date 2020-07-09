from django.db import models

class Transaction(models.Model):
  name = models.CharField(max_length=200)
  date = models.DateField()
  description = models.TextField(blank=True)
  category = models.TextField(blank=True)
  amount = models.DecimalField(max_digits=7,decimal_places=2)

class Budget(models.Model):
  name = models.CharField(max_length=200)
  description = models.TextField(blank=True)
  category = models.TextField(blank=True)
  amount = models.DecimalField(max_digits=7,decimal_places=2)

class Earned(models.Model):
  total = models.DecimalField(max_digits=7,decimal_places=2)
  today = models.DecimalField(max_digits=7,decimal_places=2)

class Spent(models.Model):
  total = models.DecimalField(max_digits=7,decimal_places=2)
  today = models.DecimalField(max_digits=7,decimal_places=2)