from django.db import models
import datetime as date
from django.contrib.auth.models import AbstractUser


# user table
class User(AbstractUser):
    # add additional fields here
    pass


# class User(models.Model):
#     username = models.CharField(max_length=100)
#     email = models.EmailField(max_length=255)
#     password = models.TextField()
#     isActivated = models.BooleanField(default=True)

#     last_login = models.DateTimeField(auto_now_add=True)


# class Person(models.Model):
#     # SEX_CHOICE = [('M','Male'),('F','Female')]
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     first_name = models.CharField(max_length=70)
#     last_name = models.CharField(max_length=70)
#     # birthdate = models.DateField()
#     # sex = models.CharField(max_length=1, choices=SEX_CHOICE,blank=True)
#     # street_address = models.CharField(max_length=100)
#     # apartment_no = models.IntegerField(null=True)
#     # city = models.CharField(max_length=70)
#     # postal_code = models.IntegerField()


class Alerts(models.Model):
    NOTIF_ACTION = [
        ("Applicant", "New Applicant Applied to your post"),
        ("MatchSkill", "Job matches your skill"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class ActivityLog(models.Model):
    ACTION_CHOICES = [
        ("signin", "Sign in"),
        ("logout", "Sign out"),
        ("applied", "Applied"),
        ("postJob", "Posted Job"),
        ("updatePost", "Update Post"),
        ("updateProfile", "Update Profile"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=14, choices=ACTION_CHOICES)
    timestamp = models.DateTimeField(default=date.datetime)  # automatic date today


class Education(models.Model):
    DEGREE_LEVEL_CHOICES = [
        ("PE", "Primary Education"),
        ("LSE", "Junior High School"),
        ("USE", "Senior High School"),
        ("UG", "College"),
        ("PG", "Master"),
        ("DC", "PhD"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    education_level = models.CharField(max_length=4, choices=DEGREE_LEVEL_CHOICES)
    school_name = models.CharField(max_length=120)


class SocialMedia(models.Model):
    SOCMED_CHOICES = [
        ("FB", "Facebook"),
        ("IG", "Instagram"),
        ("GM", "Gmail"),
        ("LI", "LinkedIn"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    social_media = models.CharField(max_length=3, choices=SOCMED_CHOICES)