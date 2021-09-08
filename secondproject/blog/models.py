from django.db import models

# Create your models here.

class Blog(models.Model):
    '''
    모델의 속성: title, pub_date, body
    '''
    title = models.CharField(max_length=200) # 문자열 속성
    pub_date = models.DateTimeField('date published') # 날짜, 시간 속성
    body = models.TextField() # 긴 문자열 속성

    def __str__(self):
        return self.title