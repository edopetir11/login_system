from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class Jabatan(models.Model):
    jabatan_name = models.CharField(max_length=100)

    def __str__(self):
        return self.jabatan_name

class Divisi(models.Model):
    divisi_name = models.CharField(max_length=100)

    def __str__(self):
        return self.divisi_name

class UserAccountManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('User must have an email address!')
        
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)

        user.save()

        return user
    
    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True

        user.save()

        return user

class UserAccount(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200, unique=True)
    address = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=100, null=True)
    education = models.CharField(max_length=255, null=True)
    divisi = models.ForeignKey(Divisi, null=True, on_delete=models.SET_NULL)
    jabatan = models.ForeignKey(Jabatan, null=True, on_delete=models.SET_NULL)
    photo = models.ImageField(upload_to="photos/", null=True)
    join_date = models.DateTimeField(null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.email
