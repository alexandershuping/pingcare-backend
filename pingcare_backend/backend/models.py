from django.db import models

# Create your models here.
class Ping(models.Model):
	app_label = 'backend'
	latitude = models.DecimalField(decimal_places=15, max_digits=20)
	longitude = models.DecimalField(decimal_places=15, max_digits=20)

	text_loc = models.CharField(max_length=255)
	issue = models.CharField(max_length=5000)

	ping_count = models.PositiveIntegerField()
