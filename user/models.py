from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class MyUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Geçerli Bir Emailiniz olmalı')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='Email adres',
        max_length=255,
        unique=True,
    )
    LOW = "1"
    LIGHT = "2"
    MODERATE = "3"
    HIGHT = "4"
    VHIGHT = "5"
    AKTIF = [
        (LOW, "HAREKETSİZ"),
        (LIGHT, "HAFTADA 1 - 3 GÜN EKSERSİZ"),
        (MODERATE, "HAFTADA 3 - 5 GÜN EKSERSİZ"),
        (HIGHT, "HAFTADA 6 - 7 GÜN EKSERSİZ"),
        (VHIGHT, "HAFTADA 1 - 3 GÜN EKSERSİZ"),
    ]
    activite = models.CharField(max_length=2, choices=AKTIF, default=LOW)
    kilo = models.DecimalField(max_digits=5, decimal_places=2,  blank=True, null=True)
    boy = models.DecimalField(max_digits=5, decimal_places=2,  blank=True, null=True)


    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin