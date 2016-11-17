from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Courses(models.Model):
	course_name = models.CharField(max_length = 45)
	description = models.TextField(null=True)
	create_at = models.DateTimeField(auto_now_add=True, auto_now=False)


