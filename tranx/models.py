from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.template.defaultfilters import slugify
from datetime import date

from accounts.models import Account


class Transactions(models.Model):

    objects = None
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=30, blank=True)
    amount = models.CharField(max_length=10, verbose_name='Amount(in ₹)')
    desc = models.TextField()
    paid_on = models.DateField(default=date.today)
    date_created = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = _("Transactions")
        verbose_name_plural = _("Transactions")

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('detailtranx', args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Transactions, self).save(*args, **kwargs)
