from django.db import models
import re

class UserManager(models.Manager):
    
    def reg_validation(self , formData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        
        if len(formData['phonenumber']) == 0:
            errors["phonenumberError"] = "PhoneNumber should be greater than 0"
        if len(formData['username'] ) == 0:
            errors["usernameError"] = "Username should be greater than 0"
        if len(formData['email'] ) == 0:
            errors["emailError"] = "Emails should be greater than 0"
        if len(formData['password'] ) == 0:
            errors["passwordError"] = "Password should be greater than 0"
        if not EMAIL_REGEX.match(formData['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"
        return errors

# Create your models here.


class User(models.Model):
    #id
    username  = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    phonenumber = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #addresses 
    #courses
    objects = UserManager()
    
class Address(models.Model):
    #id
    country = models.CharField(max_length= 50)
    city = models.CharField( max_length= 40)
    street = models.CharField (max_length= 50)
    user = models.ForeignKey(  User   , related_name="addresses" , on_delete= models.CASCADE    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #objects


class Course ( models.Model):
    #id
    courseName = models.CharField(max_length= 50)
    courseDesc = models.CharField(max_length= 300)
    users  = models.ManyToManyField( User , related_name="courses"  )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #objects


def get_users():
    users = User.objects.all()
    return users


def create_new_user( data , hashed):
    username = data['username']
    password = hashed
    email = data['email']
    phonenumber = data['phonenumber']
    
    User.objects.create( username = username , password = hashed , email =email , phonenumber = phonenumber)