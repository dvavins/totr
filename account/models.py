from django.db import models

from django.contrib.auth.models import AbstractUser, BaseUserManager
from account.utils import ref_code_generator


class AccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, username, password=None):
        if not first_name:
            raise ValueError('User must enter first name')
        if not last_name:
            raise ValueError('User must enter last name')
        if not username:
            raise ValueError('User must enter username')
        if not email:
            raise ValueError('User must enter email')

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.is_active = True
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, username, password):
        if not first_name:
            raise ValueError('User must enter first name')
        if not last_name:
            raise ValueError('User must enter last name')
        if not username:
            raise ValueError('User must enter username')
        if not email:
            raise ValueError('User must enter email')

        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractUser):
    first_name = models.CharField(max_length=15, blank=False, null=True)
    last_name = models.CharField(max_length=15, blank=False, null=True)

    username = models.CharField(max_length=15, unique=True, blank=False, null=True)
    email = models.CharField(max_length=15, unique=True, blank=False, null=True)
    phone = models.CharField(max_length=15, unique=True, blank=False, null=True)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = AccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ('first_name', 'last_name', 'email')

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    class Meta:
        verbose_name = 'Account'


class Profile(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    pimg = models.ImageField()
    confirmation_needed = models.BooleanField(default=False)
    hide_email = models.BooleanField(default=False)
    show_details = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    def full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'


class Referral(models.Model):
    """This referral code is one-time-use only will change automatically if it is used."""

    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    ref_code = models.CharField(max_length=20, unique=True, null=True, blank=True)
    used_by = models.OneToOneField(Account, on_delete=models.DO_NOTHING, related_name='used_by',
                                   blank=True, null=True)
    used_on = models.DateTimeField(auto_now_add=True)
    is_used = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        if self.ref_code is None or self.ref_code is '':
            code = ref_code_generator()
            self.ref_code = code
        super(Referral, self).save(*args, **kwargs)


class Contact(models.Model):
    contact = models.ForeignKey(Account, on_delete=models.DO_NOTHING, related_name='contact')
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='user')
    STATUS_CHOICE = (('requested', 'Requested'),
                     ('confirmed', 'Confirmed'),
                     ('rejected', 'Rejected'))
    status = models.CharField(max_length=9, choices=STATUS_CHOICE, default='requested')

    def __str__(self):
        return self.contact.username

    def save(self, *args, **kwargs):
        if self.user == self.contact:
            raise ValueError('')
