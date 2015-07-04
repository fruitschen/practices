from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'

class Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    
    def __unicode__(self):
        return self.name

class TaskPoint(models.Model):
    task = models.ForeignKey(Task)
    category = models.ForeignKey(Category)
    point = models.IntegerField(default=1)

    def __unicode__(self):
        return '%s %s +%s' % (self.task, self.category, self.point)