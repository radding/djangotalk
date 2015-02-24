from django.db import models

# Create your models here.

class Question(models.Model):
	text = models.CharField(max_length=200)
	date_published = models.DateTimeField('date_published')

class Answer(models.Model):
	question = models.ForeignKey(Question)
	text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	
