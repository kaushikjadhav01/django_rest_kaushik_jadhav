from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.validators import RegexValidator
from multiselectfield import MultiSelectField
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.dispatch import receiver
import re

# Manager for handling custom User Model
class UserManager(BaseUserManager):
    
    def create_user(self, email, name, phone,pincode,password,address=None,city=None,state=None,country=None):        
        # Password Validation has to be done again for users created through seeding to override default password validation
        if not re.match('^(?=.*[a-z])(?=.*[A-Z])[a-zA-Z\d]{8,}$', password):
        	raise ValueError('Password must contain at least one uppercase and lowercase character and at least 8 characters.')
        user = self.model(email=email, name=name, phone=phone,pincode=pincode,address=address,city=city,state=state,country=country)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, phone,pincode, password,address=None,city=None,state=None,country=None):
        user = self.create_user(email, name, phone,pincode, password, address,city,state,country)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

# Custom User Model
class UserModel(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    
    # Field Validation for Users who register using API
    password = models.CharField(max_length=50, validators=[RegexValidator(regex='^(?=.*[a-z])(?=.*[A-Z])[a-zA-Z\d]{8,}$', message='Password must contain at least one uppercase and lowercase character and at least 8 characters.', code = 'invalid_pass')])
    phone = models.IntegerField(validators=[RegexValidator(regex='^.{10}$', message='Phone no. has to be exactly 10 characters', code= 'invalid_phone')])
    pincode = models.IntegerField(validators=[RegexValidator(regex='^.{6}$', message='Pincode has to be exactly 6 characters', code = 'invalid_pincode')])

    # Specify fields as optional. Blank applies to inputs and Null applies to databases, indicating them that the value is optional
    address = models.CharField(max_length=255,blank=True,null=True)
    city = models.CharField(max_length=255,blank=True,null=True)
    state = models.CharField(max_length=255,blank=True,null=True)
    country = models.CharField(max_length=255,blank=True,null=True)

    # Other relevant fields and UserManager
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','phone','pincode']
    # Django uses this when it needs to convert object to text. Acts as label for an object model.
    def __str__(self):
        return self.email

# Content Model
class ContentModel(models.Model):
	# ForeignKey to map author to user.id in User model
    author = models.ForeignKey('UserModel', on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    body = models.CharField(max_length=300)
    summary = models.CharField(max_length=60)
    pdf = models.BooleanField()
    choices = (('Sports', 'Sports'), ('Entertainment', 'Entertainment'), ('Education', 'Education'),('Arts', 'Arts'))
    categories = MultiSelectField(choices=choices, blank=True, null=True)
    
    def __str__(self):
        return self.title

# Each time a user registers, generate a token
@receiver(post_save, sender='cms_api.UserModel')
def create_auth_token(sender, instance=None, created=False, **kwargs):
	if created:
		Token.objects.create(user=instance)