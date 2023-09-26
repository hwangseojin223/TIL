# Django

## 01. django

| 사용         | 명령어                                  |
| ------------ | --------------------------------------- |
| django 설치  | pip install django                      |
| project 시작 | django-admin startproject (projectname) |
| 실행         | python manage.py runserver              |
| app 시작     | python manage.py startapp (appname)     |

## 기본 실행 순서 정리

(django 실습 파일 순서대로 작성한 것임)

"""  
django-admin startproject intro  
python manage.py startapp first_app  
실행 시  
"""

### 1. intro/intro/settings.py

1.  `INSTALLED_APPS = []` 에 `path('first_app/', include('first_app.urls'))`, 와 같은 형식으로 등록을 한다.

### 2. intro/intro/urls.py

1.  `path('first_app/', include('first_app.urls')),` 추가
2.  `from django.urls import path, include` 추가

### 3. first_app

1.  `urls.py` 를 만들고
2.  `from django.urls import path` 와 `from . import views` 추가
3.  `urlpatterns = { path ('hello/', views.hello),}` 와 같은 형식으로 urlpatterns에 path들을 추가한다.

### 4. first_app/views.py

1.  `from django.shortcuts import render`, `from django.http import HttpResponse` 추가하고
2.  ```python
     def hello(request):
         return render(request, 'hello.html')
    ```
    과 같은 형식으로 함수를 추가한다.

### 5. first_app

1.  `/templates/hello.html` 를 만들고 화면에 나올 말들을 작성한다.

### 6. 만약, views.py에 def를 작성하고 `리턴한 값을 html에 나타내기` 하기 위해서는

1.  `views.py`에서는

```python
def lunch(request):
 menus = ['카레','돈까스','초밥', '샤브샤브']
 menu = random.choice(menus)

 return render(request, 'lunch.html', {
     'menu': menu
 })
```

와 같은 dict 형식으로 return

2.  `lunch.html` 에서는

    ```html
    <body>
      <h1>Lunch</h1>
      <p>{{menu}}</p>
    </body>
    ```

    와 같은 {{}} 형식으로 받아올 수 있다.

### 7. a.html 에서 for문 사용은

```html
<ul>
  {% for num in lucky_numbers %}
  <li>{{ num}}</li>
  {% endfor %}
</ul>
```

와 같은 형식으로 사용할 수 있다.
