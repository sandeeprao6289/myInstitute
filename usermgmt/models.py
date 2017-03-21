import os
import uuid

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone

class UserManager(BaseUserManager):

	def create_user(self, email, first_name, password=None):

		if not email:
			raise ValueError('Users must have an email address')

		now = timezone.now()
		user = self.model(email=UserManager.normalize_email(email))
		user.first_name = first_name
		user.email = email
		user.set_password(password)
		user.last_login = user.date_joined = user.last_attempt = now
		user.save(using=self._db)
		return user

	def create_superuser(self, email, first_name, password):
		user = self.create_user(email=email,
            first_name=first_name, password=password)
		user.email = email
		user.first_name = first_name
		user.is_superuser = True
		user.is_staff = True
		user.save(using=self._db)
		return user

class User(AbstractBaseUser,PermissionsMixin):
	first_name = models.CharField(max_length=150)
	last_name = models.CharField(max_length=150,null=True)
	email = models.EmailField(unique=True)

	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)

	created_on = models.DateTimeField(auto_now_add = True)
	modified_on = models.DateTimeField(auto_now = True)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['first_name']
	objects = UserManager()

	def __unicode__(self):
		return self.first_name

	def get_short_name(self):
		return self.first_name
		
	def get_full_name(self):
		if self.last_name:
			full_name = self.first_name +" "+ self.last_name
		else:
			full_name = self.first_name
		return full_name


