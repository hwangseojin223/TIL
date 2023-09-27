# Django

## MODEL

"""  
django-admin startproject MODEL  
python manage.py startapp students  
실행 후  
"""

### 1. model/model/students/models.py

    ```python
    class Student(models.Model):
        name = models.CharField(max_length=10)
        address = models.TextField()
        major = models.CharField(max_length=100)
        age = models.IntegerField()
        cgpa = models.FloatField()
    ```
        와 같이 테이블을 추가할 수 있다.

<br>

### 2. 명령어 실행

1.  `python manage.py makemigrations students`
2.  `python manage.py migrate students`
    <br>
    <br>

### 3. modl/model/students/migrations/ 에

1.  `0001_initial.py`

```python
class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=10)),
                ("address", models.TextField()),
                ("major", models.CharField(max_length=100)),
                ("age", models.IntegerField()),
                ("cgpa", models.FloatField()),
            ],
        ),
    ]
```

와 같은 파일이 추가된 것을 확인할 수 있다.
<br>

### 4. model/db.sqlite3 에서 id가 추가된 테이블을 확인할 수 있다.
