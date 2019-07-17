from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class AuthUserManager(BaseUserManager):
    def create_user(self, email, password=None, is_staff=False, is_admin=False, is_active=True):
        if not email:
            raise ValueError('User must have an email address')
        if not password:
            raise ValueError('User password missing')
        user_obj = self.model(
            email = self.normalize_email(email)
        )
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.save(using=self._db)

        return user_obj

    def create_staffuser(self, email, password=None):
        user_obj = self.create_user(
            email,
            password=password,
            is_staff=True
        )

        return user_obj

    def create_superuser(self, email, password=None):
        user_obj = self.create_user(
            email,
            password=password,
            is_staff=True,
            is_admin=True
        )

        return user_obj

class AuthUser(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = AuthUserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active

class Profile(models.Model):
    user = models.OneToOneField(AuthUser, on_delete=models.CASCADE)
    skype = models.CharField(max_length=30, blank=True)
    whatsapp = models.CharField(max_length=30, blank=True)
    twitter = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    max_spread = models.FloatField(default=0)
    size = models.FloatField(default=0)
    profit_limit = models.FloatField(default=0)
    stop_limit = models.FloatField(default=0)
    # currency_1 = models.CharField(max_length=6, null=True, blank=True)
    # currency_2 = models.CharField(max_length=6, null=True, blank=True, choices=[('eur_usd', 'EUR'), ('gbp_usd', 'GBP'), ('usd', 'USD'), ('btc', 'BTC'), ('ltc', 'LTC'), ('eth', 'ETH')])
    # currency_3 = models.CharField(max_length=6, null=True, blank=True, choices=[('eur_usd', 'EUR'), ('gbp_usd', 'GBP'), ('usd', 'USD'), ('btc', 'BTC'), ('ltc', 'LTC'), ('eth', 'ETH')])
    # currency_4 = models.CharField(max_length=6, null=True, blank=True, choices=[('eur_usd', 'EUR'), ('gbp_usd', 'GBP'), ('usd', 'USD'), ('btc', 'BTC'), ('ltc', 'LTC'), ('eth', 'ETH')])
    # currency_5 = models.CharField(max_length=6, null=True, blank=True, choices=[('eur_usd', 'EUR'), ('gbp_usd', 'GBP'), ('usd', 'USD'), ('btc', 'BTC'), ('ltc', 'LTC'), ('eth', 'ETH')])
    # currency_6 = models.CharField(max_length=6, null=True, blank=True, choices=[('eur_usd', 'EUR'), ('gbp_usd', 'GBP'), ('usd', 'USD'), ('btc', 'BTC'), ('ltc', 'LTC'), ('eth', 'ETH')])
    product = models.CharField(max_length=1, choices=[('1', 'Invest IQ Premium Signals'), ('2', 'Invest IQ Automated Trading'), ('3', 'Invest IQ Managed Service')])
    perdiction_accuracy = models.FloatField(default=0)
    price_charge_hight = models.FloatField(default=0)
    price_charge_low = models.FloatField(default=0)
    use_client_sentiment = models.CharField(max_length=3, choices=[('yes', 'Yes'), ('no', 'No')])
    client_sentiment_contrarian = models.CharField(max_length=3, choices=[('yes', 'Yes'), ('no', 'No')])
    client_sentiment_value = models.CharField(max_length=255, null=True, blank=True)
    watermark = models.CharField(max_length=255, null=True, blank=True)

@receiver(post_save, sender=AuthUser)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()