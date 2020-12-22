from django.db import models

# Create your models here.

class Bottle(models.Model):
	domain = models.CharField(max_length=255)
	batch = models.CharField(max_length=255)
	year = models.IntegerField(null=True)
	area = models.CharField(max_length=255, null=True)
	appellation = models.CharField(max_length=255, null=True)

	def __str__(self):
		return f"{self.domain} {self.batch} {self.year}"
