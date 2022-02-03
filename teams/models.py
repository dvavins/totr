from os import name
from django.db import models
from django.template.defaultfilters import slugify

from accounts.models import Account
# from todos.models import Todos
from tranx.models import Transactions


class Teams(models.Model):
    name = models.CharField(max_length=40,)
    slug = models.SlugField(max_length=40, blank=True)

    type = (('private', 'Private'),
            ('open', 'Public'),
            ('others', 'Others'))
    team_type = models.CharField(max_length=7, choices=type, default='private')
    date_created = models.DateField(auto_now_add=True)

    # Add some logic to prevent admin field empty if used deletes him/herself
    admin = models.ForeignKey(Account, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name
        
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Teams, self).save(*args, **kwargs)


class Members(models.Model): 

    team = models.ForeignKey(Teams, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    status_choices = (('requested', 'Requested'),
                      ('accepted', 'Accepted'),
                      ('rejected', 'Rejected'))
    status = models.CharField(max_length=9, choices=status_choices, default='requested')
    requested_on = models.DateTimeField(auto_now_add=True)
    date_joined = models.DateField()

    def __str__(self):
        return self.user.username
    

class TeamTodos(models.Model):

    name = models.ForeignKey(Teams, on_delete=models.CASCADE)
    member = models.ManyToManyField(Members)

    @property
    def team_name(self):
        return f'{self.name}-Todos'

    def __str__(self):
        return self.team_name

    # def save(self, *args, **kwargs):
    #     if self.member in self.name.user:
    #         return super(TeamTodos, self).save(*args, **kwargs)
    
