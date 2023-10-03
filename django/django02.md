# Django

"""  
django-admin startproject form  
python manage.py startapp review  
실행 후  
"""

## 1. form/templates/base.html 을 추가하여 중복 코드 없애기

base.html 에

```html
<body>
  <p>base</p>
  {% block content %}{% endblock content %}
</body>
```

`<body></body>`안에 위와 같은 형식을 추가해주면

review/templates/review/index.html 에서

```html
{% extends "base.html" %} {% block content %}
<h1>index</h1>
<p>good</p>
{% endblock content %}
```

위와 같이 block 안의 코드만 다르게 작성헤서 app의 html마다 모든 코드를 작성하는 중복을 줄일 수 있다.

다만, 이를 하기 위해서는  
form/settings.py에서 TEMPLATES의 DIRS에 BASE_DIR/'templates'를 추가해줘야 한다.
(BASE_DIR은 form을 뜻한다.)

또한, base.html의 `block (name)` 과 index.html의 `block (name`)이 같아야함

---

<br>
<br>
<br>

"""
python manage.py startapp user_input
user_input/templates/user_input 에 hello.html 만들기
실행 후
"""

## 2. user_input 받기

1. form/user_input/urls.py 의 patterns 에  
   path('hello/<str:name>/, views.hello)를 추가
2. form/user_input/views.py 에
   ```python
   def hello(request, name):
    message = f'반갑습니다 {name} !'
    return render(request, 'user_input/hello.html',{
        'message': message,
    })
   ```
3. form/user_input/templates/user_input/hello.html 에

```html
{% extends "base.html" %} {% block content %}
<h1>{{message}}</h1>
{% endblock content %}
```

## 를 추가하면 http://127.0.0.1:8000/user_input/hello/(직접이름을적음)/ url을 통해 html를 확인할 수 있다.

<br>
<br>
<br>
"""

user_input/templates/user_input 에 ping.py , pong.py 를 만든 후  
"""

## 3. user_input 받고 출력하기

1. form/user_input/urls.py 의 urlpatterns에  
   path('ping/', views.ping),
   path('pong/', views.pong), 추가 후

2. form/user_input/views.py 에

```python

def ping(request):
    return render(request, 'user_input/ping.html')

def pong(request):
    username = request.GET['username']
    password = request.GET['password']
    return render(request, 'user_input/pong.html',{
        'username': username,
        'password': password,
    })
```

3. 각 html에

   ```html
   <!-- ping.html -->
   {% extends "base.html" %} {% block content %}
   <form action="/user_input/pong/">
     {% comment %}목적지를 적는 것임 {% endcomment %}
     <p>
       <label for="username">Username: </label>
       <input type="text" id="username" name="username" /> {% comment %}name은
       값을 입력하고 얍을 눌렀을 때 dict 형식으로 넘어가는거임{% endcomment %}
     </p>
     <p>
       {% comment %} for 랑 id는 같아야함 {% endcomment %}
       <label for="password">Password: </label>
       <input type="password" id="password" name="password" />
     </p>
     <p>
       <input type="submit" value="얍!" />
       <button>야얍</button>
     </p>
   </form>
   {% endblock content %}
   ```

   ```html
   <!-- pong.html -->
   {% extends "base.html" %} {% block content %}
   <h1>Data from PING</h1>
   <p>{{username}}</p>
   <p>{{password}}</p>
   {% endblock content %}
   ```

을 작성해서 ping.py로 user_input을 받고 pong.py에 출력시킬 수 있다.

## 4. 다른 port로 server 돌리는 명령어

`python manage.py runserver 8001`
