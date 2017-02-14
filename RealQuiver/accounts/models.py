from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin, AbstractBaseUser
from django.utils import timezone
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail


class User(AbstractBaseUser):
    pass


class CustomManager(BaseUserManager):
    def create_user(self, email, username, first_name, middle_name, last_name, password=None,
                    ):
        '''
        Create a CustomUser with email, name, password and other extra fields
        '''
        now = timezone.now()
        if not email:
            raise ValueError('The email is required to create this user')
        email = CustomManager.normalize_email(email)
        user = self.model(email=email, username=username, first_name=first_name, middle_name=middle_name,
                           last_name=last_name, is_staff=False,
                           is_active=True, is_superuser=False,
                           date_joined=now, last_login=now, )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, first_name, middle_name, last_name, password=None,
                         ):
        s_user = self.create_user(email, username, first_name, middle_name, last_name, password,
                             )
        s_user.is_staff = True
        s_user.is_active = True
        s_user.is_superuser = True
        s_user.is_admin = True
        s_user.save(using=self._db)
        return s_user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email'), max_length=254, unique=True)
    username = models.CharField(_('user name'), max_length=100, blank=True)
    first_name = models.CharField(_('first name'), max_length=100)
    middle_name = models.CharField(_('middle name'), max_length=100)
    last_name = models.CharField(_('last name'), max_length=100)
    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_('Determines if user can access the admin site'))
    is_active = models.BooleanField(_('active'), default=True)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    is_admin = models.BooleanField(_('administrator'), default=False)
    is_superuser = models.BooleanField(_('super'), default=False)
    last_login = models.DateTimeField(_('last accounts'), default=timezone.now)
    objects = CustomManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'middle_name', 'last_name']


    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_absolute_url(self):
        return "/users/%s/" % urlquote(self.email)

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None):
        send_mail(subject,message, from_email, [self.email])

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True







