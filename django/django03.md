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

<br>
<br>

## RDBMS vs NoSQL

참고. https://www.whatap.io/ko/blog/173/

### 데이터베이스(DB) : 데이터의 집합

- 계층형(Hierarchical) DB
- 망형(Network) DB
- 관계형(Relational) DB = RDB

### RDB

고정된 행과 열로 구성된 테이블에 데이터를 저장  
최소단위 : 테이블  
테이블: 하나 이상의 열과 행으로 이루어짐  
열: 하나의 속성에 대한 정보가 저장됨  
행: 각 열의 데이터 형식에 맞는 데이터가 저장됨

특징:

1. 데이터가 정해진 데이터 스키마에 따라 테이블에 저장된다
2. 데이터가 관계를 통해 여러 테이블에 분산된다

\* 스키마: 데이터베이스 전체 또는 일부의 논리적인 구조를 표현하는 것으로 데이터베이스 내에서 데이터가 어떤 구조로 저장되는지를 나타낸다.

장점:

1. 스키마가 명확하게 정의되어 있다.
2. 데이터 무결성을 보장한다.
3. 각 데이터를 중복 없이 한 번만 저장한다.

단점:

1. 추후 수정이 어렵다.
2. 관계를 맺고 있어 조인문이 많은 복잡한 쿼리가 만들어질 수 있다.

### NoSQL: 비관계형 데이터베이스

데이터 유형에 따라 다양한 유형을 갖추고 있으며, 문서, 키 값, 와이드 컬럼, 그래프 등이 있다.

장점:

1. 스키마가 없어 유연하고 언제든지 저장된 데이터를 조정 및 새로운 필드를 추가할 수 있다.
2. 데이터는 애플리케이션이 필요로 하는 형식으로 저장되기 때문에 데이터를 읽어오는 속도가 빨라진다.
3. 수직 및 수평 확장이 가능해서 애플리케이션이 발생시키는 모든 읽기와 쓰기 요청 처리가 가능하다.

단점:

1. 데이터 중복을 계속 업데이트해야한다.

### RDBMS vs NoSQL

| 특징                 | RDBMS                                                                                                 | NoSQL                                                                                                  |
| -------------------- | ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| 데이터 저장(storage) | 데이터를 SQL언어를 통해 테이블에 저장, 미리 작성된 스키마를 기반으로 정해징 형식에 맞게 데이터를 저장 | key-value, document, wide-column, graph 등의 방식으로 데이터를 저장                                    |
| Schema               | 고정된 schema                                                                                         | 유연한 schema                                                                                          |
| Query                | 테이블 형식과 테이블 간의 관계에 맞춰 데이터를 요청(SQL)                                              | 데이터 그룹 자체를 조회하는 것에 초점을 두고 있어 구조화되지 않은 쿼리 언어로도 데이터 요청 가능(UnQL) |

\* Qeury: 데이터베이스에 대해서 정보를 요청하는 행위

### DMBS

Database Management System: 데이터베이스를 관리하고 운영하는 소프트웨어  
역할: 데이터베이스에 여러 사용자 혹은 응용 프로그램이 데이터를 공유 및 접근할 수 있도록 함

- MySQL
- Oracle
- MariaDB
- PostgreSQL
