# 영화정보API
영화 정보를 CRUD 해주는 api 입니다.


## 개발 및 실행 환경

본 API는 아래의 환경에서 개발되었습니다.
- Ubuntu 18.04.4 LTS
- Python 3.6.9
- Django 3.1.2
- Django Rest Framework 3.12.1

1. Python (버전 확인 방법 : ``$ python --version``)
2. pip (설치 유무 확인 방법: ``$ git --version``)
3. Django (설치 유무 확인 방법: ``$python -m django --version``)
4. Django Rest Framework (설치 유무 확인 방법: ``pip list``

### Python 설치
Mac, Linux: 기본적으로 Python이 제공 됩니다.
다만 버전이 낮다면 업그레이드를 권장 합니다.

### pip 설치
``$ apt-get install python-pip``

### virtualenv 설치 (권장)
- ``virtualenv`` 설치 : ``$ pip install virtualenv``
- ``virtualenv``를 통한 가상환경 폴더 생성 : ``$ virtualenv venv``
- 가상환경 활성화 ``$ source venv/bin/activate``

### Django 설치
``$ pip install django``

### DRF 설치
``$ pip install djangorestframework``

## 실행 방법

- 소스코드 저장

	``$ git clone https://github.com/jae0077/movieapi.git``
- 변경내용 저장 및 테이블 적용

  ``$ python manage.py makemigrations``
  
	``$ python manage.py migrate``
- 서버 실행

	``$ python manage.py runserver 포트번호``
	
## 사용 방법
- GET /movie
	영화 리스트를 조회
	
- POST /movie
	영화 객체 추가
	
- GET /movie/{id}
	영화 객체 조회

- PUT /movie/{id}
	영화 객체 수정
	
- DELETE /movie/{id}
	영화 객체 삭제

아래의 형식으로 객체 추가, 수정 가능

Content:
```
{
  "title" : "제목",
  "genre" : "장르",
  "year" :  제작년도(int)
}
```