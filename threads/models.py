from django.db import models


def get_default(model):
    return model.objects.last()

class Status(models.Model):
    status = models.CharField(max_length=30)
    def __str__(self):
        return self.status


class Threads(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    image = models.ImageField(upload_to='photos',blank=True,null=True)
    user = models.CharField(max_length=30)
    def __str__(self):
        return self.text
    class Meta:
        verbose_name = 'Тред'
        verbose_name_plural = 'Треды'
    status = models.ForeignKey('Status',on_delete=models.CASCADE,default=get_default(Status))


class Comments(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    image = models.ImageField(upload_to='photos/%Y/%m',blank=True,null=True)
    user = models.CharField(max_length=30)
    thread = models.ForeignKey('Threads',on_delete=models.CASCADE,)
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'



