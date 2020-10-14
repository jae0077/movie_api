from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie # 모델설정
        fields = ("id", "title", "genre", "year", "registration_date") # 필드 설정
