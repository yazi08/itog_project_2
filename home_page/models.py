from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    name_blog = models.TextField(verbose_name ='Название')
    athor_blog = models.CharField(verbose_name ='Автор',max_length=50,null=True)
    # slug = models.SlugField('URL', max_length=225, unique=True, db_index=True)
    data_blog = models.DateTimeField(verbose_name ='Дата публикации',auto_now_add =True, null=True)
    data_blog_update = models.DateTimeField (verbose_name ='Дата изменения', auto_now =True, null=True )
    description_blog = models.TextField(verbose_name ='Описание', null=True)


    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блог'
        ordering = ['data_blog']
class SummClientItog(models.Model):
    sum_client = models.FloatField(verbose_name='Сумма клиента')
    who_client = models.ForeignKey(User,verbose_name='Клиент',on_delete=models.CASCADE,null=True)
    date_client = models.DateTimeField(verbose_name='Дата',auto_now_add=True,null=True)
    def __str__(self):
        return f"{self.sum_client}"

    class Meta:
        verbose_name = 'Буфер истории'
        verbose_name_plural = 'Буфер истории'

class HistoryClient(models.Model):
    summ_history_client = models.FloatField(verbose_name='Сумма клиента',null=True)
    who = models.ForeignKey(User,verbose_name = 'Клиент', on_delete=models.CASCADE,null=True)
    date = models.DateTimeField(verbose_name = 'Дата',auto_now_add=True,null=True)
    data_end =models.DateTimeField(verbose_name = 'Дата завершения',auto_now_add=True,null=True)
    def __str__(self):
        return f"{self.summ_history_client}"

    class Meta:
        verbose_name = 'История'
        verbose_name_plural = 'История'
        ordering = ['date']



class IdPid(models.Model):
    id_pid = models.IntegerField('id процесса',null=True)

    def __str__(self):
        return f"{self.id_pid}"


