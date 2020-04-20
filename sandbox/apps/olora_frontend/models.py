from django.db import models


class Contact(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()

    class Meta:
        verbose_name_plural = "Contact us"

    def __str__(self):
        return self.date.__str__() + "\t" + self.name + " - " + self.email
