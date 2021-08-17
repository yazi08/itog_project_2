from django.db import models

class Blog(models.Model):
    name_blog = models.TextField('Название')
    athor_blog = models.CharField('Автор',max_length=50,null=True)
    # slug = models.SlugField('URL', max_length=225, unique=True, db_index=True)
    data_blog = models.DateTimeField('Дата публикации',auto_now_add =True, null=True)
    data_blog_update = models.DateTimeField ('Дата изменения', auto_now =True, null=True )
    description_blog = models.TextField('Описание', null=True)




