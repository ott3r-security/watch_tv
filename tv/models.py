from django.db import models
from django.utils.timezone import now

class tvTime(models.Model):
    length = models.IntegerField(help_text='How Long is the Show')
    show_name = models.CharField(max_length=20, help_text="Enter Show Name")
    days = (
        ('sun', 'Sunday'),
        ('mon', 'Monday'),
        ('tue', 'Tuesday'),
        ('wed', 'Wednesday'),
        ('thur', 'Thursday'),
        ('fri', 'Friday'),
        ('sat', 'Saturday')
        )
    days_on = models.CharField(choices=days, max_length=10)
    active_choice = (
        ('y','Yes'),
        ('n','No'),
    )
    active = models.CharField(default='y', choices=active_choice, max_length=5)
    names = (
        ('jennifer', 'Jennifer'),
        ('erik', 'Erik'),
    )
    watcher = models.CharField(choices=names, max_length=10)
    start_date = models.DateField(default=now)
    providers = (
        ('paramount', 'Paramount+'),
        ('hbo', 'HBO Max'),
        ('hulu', 'Hulu'),
        ('netflix', 'Netflix'),
        ('prime', 'Prime'),
    )
    provider = models.CharField(choices=providers, max_length=15)

    class Meta:
        verbose_name = 'Let\'s Watch TV'
        verbose_name_plural = 'Let\'s Watch TV'


    def __str__(self):
        return self.days_on

#2003Yamaha!