from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    message = models.TextField()
    likes = models.PositiveIntegerField(default=0)
    created_by = models.ForeignKey(User, related_name="created_message")
    created_datetime = models.DateTimeField()

    def __unicode__(self):
        return u'%s' % self.message

    class Meta:
        ordering = ['-id']

