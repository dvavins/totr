from django.db import models
from django.template.defaultfilters import slugify

from account.models import Account, Contact
from teams.utils import random_string_generator


class Teams(models.Model):

    team = models.CharField(max_length=40)
    team_admin = models.ManyToManyField(Account, related_name='team_admin')
    slug = models.SlugField(max_length=40, blank=True, unique=True)

    type = (('private', 'Private'),
            ('public', 'Public'),
            ('others', 'Others'))
    team_type = models.CharField(max_length=7, choices=type, default='private')
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.team

    def save(self, *args, **kwargs):
        self.slug = slugify(self.team)
        if Teams.objects.filter(slug=self.slug).exists():
            self.slug = '{slug}-{randstr}'.format(slug=self.slug, randstr=random_string_generator(size=4))
        return super(Teams, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'


class Members(models.Model):
    team = models.ForeignKey(Teams, on_delete=models.CASCADE)
    members = models.ManyToManyField(Contact)
    joined_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.team.team

    class Meta:
        verbose_name = 'Member'
        verbose_name_plural = 'Members'


class TodosGroup(models.Model):
    team = models.OneToOneField(Teams, on_delete=models.CASCADE)
    member = models.ManyToManyField(Members, blank=True)

    def __str__(self):
        return f'{self.team}-Todos'


class TranxGroup(models.Model):
    team = models.OneToOneField(Teams, on_delete=models.CASCADE)
    member = models.ManyToManyField(Members, blank=True)

    def __str__(self):
        return f'{self.team}-Tranx'

