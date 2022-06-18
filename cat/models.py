from django.db import models

# Create your models here.


class Topic(models.Model):

    """A topic that user is learning about"""

    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        """A string representation of the model"""

        return self.text


class Entry(models.Model):

    """Something specific about the topic"""

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):

        """A string representation of the model"""

        len_text = len(self.text[:])
        if len_text <= 50:
            return f'{self.text[:]}'
        else:
            return f'{self.text[:50]}...'

