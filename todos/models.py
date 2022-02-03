from datetime import date
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.template.defaultfilters import slugify


from accounts.models import Account


class Todos(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=50, blank=True)
    desc = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    todo_date = models.DateField(default=date.today)
    is_completed = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("Todo")
        verbose_name_plural = _("Todos")
        ordering = ['-date_created']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Todos, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('tododetail', args=[self.slug])
