from django.db import models

# Create your models here.

class Todo(models.Model):
    todo_id = models.CharField(unique=True, max_length=5)
    title = models.CharField(max_length=50)
    keyword = models.CharField(max_length=50)
    main_text = models.CharField(max_length=2000)
    split_text1 = models.CharField(max_length=300,blank=True)
    split_text2 = models.CharField(max_length=300,blank=True)
    split_text3 = models.CharField(max_length=300 ,blank=True)
    split_text4 = models.CharField(max_length=300 ,blank=True)
    split_text5 = models.CharField(max_length=300 ,blank=True)
    split_text6 = models.CharField(max_length=300 ,blank=True)
    split_text7 = models.CharField(max_length=300 ,blank=True)
    split_text8 = models.CharField(max_length=300 ,blank=True)
    split_text9 = models.CharField(max_length=300 ,blank=True)
    split_text10 = models.CharField(max_length=300 ,blank=True)
    split_text11 = models.CharField(max_length=300 ,blank=True)

    update_date = models.DateTimeField('date published')
