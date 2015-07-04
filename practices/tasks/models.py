from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'

PRIORITIES = (
    (1, 'Critical'),
    (2, 'High'),
    (3, 'Normal'),
    (4, 'Low'),
    (5, 'Backlog'),
) 

class Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    priority = models.IntegerField(default=3, choices=PRIORITIES)
    finished = models.BooleanField(default=False, blank=True)
    finished_timestamp = models.DateTimeField(default=None, null=True, blank=True)
    
    
    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['priority']

class TaskPoint(models.Model):
    task = models.ForeignKey(Task)
    category = models.ForeignKey(Category)
    point = models.IntegerField(default=1)

    def __unicode__(self):
        return u'%s %s +%s' % (self.task, self.category, self.point)