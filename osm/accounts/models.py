from __future__ import unicode_literals

from django.db import models

import hashlib

# Create your models here.
#
class UserGroup(models.Model):
	groupname = models.CharField(max_length=50,unique=True)

	def __unicode__(self):
		return self.groupname


class User(models.Model):
	groupname = models.ForeignKey(UserGroup)
	username = models.CharField(max_length=50,unique=True)
	password = models.CharField(max_length=50)

	def __unicode__(self):
		return self.username

	# def hashed_password(self,password=None):
	# 	if not password:
	# 		return self.password
	# 	else:
	# 		return hashlib.md5(password).hexdigest()
			
	# def check_password(self,password):
	# 	if self.hashed_password(password) == self.password:
	# 		return True
	# 	else:
	# 		return False
