1. README.md
2. .gitignore
   1. git이 관리할 때 아예 무시할 파일들
   2. 캐시파일/중요한파일/등등등
   3. https://www.toptal.com/developers/gitignore/ 참고
3. db
   <app_name> 지정안하면 다 migrate 됨.
   1. python manage.py makemigrations
   2. python manage.pyt migrate
4. db.sqlite3 => is_superuser 을 정하는 방법
   1. (base) hwangseojin@hwangseojin-ui-MacBookAir 03_REL % python manage.py createsuperuser
      (base) hwangseojin@hwangseojin-ui-MacBookAir 03_REL % python manage.py createsuperuser
      Username (leave blank to use 'hwangseojin'): admin
      Email address:
      Password: #admin
      Password (again): #admin
      The password is too similar to the username.
      This password is too short. It must contain at least 8 characters.
      This password is too common.
      Bypass password validation and create user anyway? [y/N]: y
      Superuser created successfully.
   2. http://127.0.0.1:8000/admin/ 접속
   3. board/admin.py 에 코드 추가
5. accounts
   1. python manage.py startapp accounts
   2. cd accounts
   3. touch urls.py forms.py
   4. mkdir -p templates/accounts
   5. cd templates/accounts
   6. touch login.html signup.html
   7. accounts/urls.py 코드 추가
   8. accounts/views.py 코드 추가
   9. signup.html
6. 그외에도 코드 추가
