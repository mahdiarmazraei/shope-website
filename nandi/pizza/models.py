from django.db import models

class size(models.Model):

    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    


class pizza(models.Model):
    topping1 = models.CharField(max_length=100)
    topping2 = models.CharField(max_length=100)
    size = models.ForeignKey(size,on_delete=models.CASCADE)