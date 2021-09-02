from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    name_blog = models.TextField('Название')
    athor_blog = models.CharField('Автор',max_length=50,null=True)
    # slug = models.SlugField('URL', max_length=225, unique=True, db_index=True)
    data_blog = models.DateTimeField('Дата публикации',auto_now_add =True, null=True)
    data_blog_update = models.DateTimeField ('Дата изменения', auto_now =True, null=True )
    description_blog = models.TextField('Описание', null=True)

class SummClientItog(models.Model):
    sum_client = models.FloatField('Сумма клиента')
    who_client = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    date_client = models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return f"{self.sum_client}"

    #
    # class Meta:
    #     ordering = ['sum_client']

class HistoryClient(models.Model):
    summ_history_client = models.FloatField('Сумма клиента',null=True)
    who = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    date = models.DateTimeField(auto_now_add=True,null=True)
    data_end =models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return f"{self.summ_history_client}"



class IdPid(models.Model):
    id_pid = models.IntegerField('id процесса',null=True)

    def __str__(self):
        return f"{self.id_pid}"


