from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=50, help_text="영화 제목을 입력해 주세요")
    genre = models.CharField(max_length=20, help_text="영화 장르를 입력해 주세요")
    year = models.IntegerField(help_text="제작 년도를 입력해 주세요")
    registration_date = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.title
