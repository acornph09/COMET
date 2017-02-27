from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    portfolio_title = models.CharField(max_length=255, default='no portfolio name')
    number_of_projects = models.IntegerField()
    portfolio_type = models.CharField(max_length=127, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    status = models.BooleanField(default=True)


class Project(models.Model):
    project_name = models.CharField(max_length=255, default='no project name')
    project_description = models.CharField(max_length=500, null=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

class ProjectFile(models.Model):
    project_file = models.FileField(upload_to='accounts/projects/', blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)


class Tag(models.Model):
    tag_name = models.CharField(max_length=100, default='no tags')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)

class ProjectPortfolio(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

class UserProject(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class UserProfile(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school = models.CharField(_('school'), max_length=127, null=True)
    degree = models.CharField(_('degree'), max_length=127, null=True)
    address = models.CharField(_('address'), max_length=255, null=True)
    mobile_number = models.CharField(_('mobile number'), max_length=12, null=True)
    telephone_number = models.CharField(_('telephone number'), max_length=12, null=True)
    birth_date = models.DateTimeField(_('birthday'), null=True)
    gender = models.CharField(_('gender'), max_length=1, choices=GENDER_CHOICES, null=True)
    bio = models.CharField(_('biography'), max_length=500, null=True)
    profile_picture = models.ImageField(_('profile_picture'), blank=True, upload_to='accounts/avatar/')


    @receiver(post_save, sender=User)
    def create_profile(sender, **kwargs):
        user = kwargs["instance"]
        if kwargs["created"]:
            userprofile = UserProfile(user=user)
            userprofile.save()
    post_save.connect(create_profile, sender=User)

    '''
    def create_or_update_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)
            instance.userprofile.save()
    '''