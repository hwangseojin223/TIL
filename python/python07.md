# # Python

<br/>

# 01. OOP

- object
- object oriented programming
- class & object

# 02. 객체(Object)

python에서 모든 것은 객체이다.

## 2.1 객체의 특징

- 타입(type) : 어떤 연산자(operator)와 조작(method)이 가능한가?
- 속성(attribute) : 어떤 상태(데이터)를 가지는가?
- 조작법(method) : 어떤 행위(함수)를 할 수 있는가?

# 03. 객체 지향 프로그래밍(Object-Oriented Programming)

object가 중심(oriented)이 되는 프로그래밍

## 3.1 객체 중심의 장점

- 코드의 직관성
- 활용의 용이성
- 변경의 유연성

## 3.2 OOP 기초

### 3.2.1 기본 문법

```python
# 클래스 정의
class MyClass:
    pass

# 인스턴스(instance) 생성
my_instance = MyClass()

# 속성 접근
my_instance.my_attribute

# 매서드 호출
my_instance.my_method()

```

### 3.2.2 class

공통된 속성(attribute)과 조작법(method)을 가진 객체들의 분류

### 3.2.3 인스턴스(Instance)

- 특정 클래스의 실제 데이터 예시(instance)
- 파이썬에서 모든 것은 객체이고, 모든 객체는 특정 클래스의 인스턴스이다.
  ```python
  # Person 클래스
  class Person:
      pass
  # yu는 Person 클래스의 인스턴스
  yu = Person()
  ```
- `isinstance(p, Person)`: p변수에 담긴 인스턴스가 Person 클래스의 인스턴스인지 확인

## 3.3 속성(attribute)과 메서드(method)

| type      | attributes       | methods                                |
| --------- | ---------------- | -------------------------------------- |
| `complex` | `.real`, `.imag` | \_                                     |
| `str`     | \_               | `.capitalize()`, `.join()`, `.split()` |
| `list`    | \_               | `.append()`, `.reverse()`, `.sort()`   |
| `dict`    | \_               | `.keys()`, `.values()`, `.items()`     |

### 3.3.1 속성(attribute)

attribute은 object의 상태/데이터를 뜻한다.
활용법: `<객체>.<속성>`

### 3.3.2 메서드(method)

특정 객체가 할 수 있는 행위(behavior)를 뜻한다.
활용법: `<객체>.<메서드>()`

# 04. 인스턴스(instance)

## 4.1 인스턴스(instance) 생성

- instance : 정의된 class에 속하는 객체
  활용법

```python
# 인스턴스 = 클래스()
person1 = Person()
```

## 4.2 인스턴스 변수

- 인스턴스의 속성(attribute)
- 각 인스턴스들의 고유한 데이터
- 생성자 메서드에서 `self.변수명` 로 정의
- 인스턴스가 생성된 이후 `인스턴스.변수명` 로 접근 및 할당
  활용법

```python
class Person:
    pass

p1 = Person()
p1.name = 'jack'
p1.age = 25
```

## 4.3 인스턴스 메서드

메서드 : 특정 데이터 타입(또는 클래스)의 객체에 공통적으로 적용 가능한 행위(behavior)들을 의미

- 인스턴스 메서드는 인스턴스가 사용할 메서드에 해당
- 클래스 내부에 정의되는 메서드는 기본적으로 인스턴스 메서드로 생성
- 메서드 호출시, 첫번째 인자로 인스턴스 self가 전달됨

활용법

```python
class MyClass:
  def instance_method(self, arg1, ...):

my_instance = MyClass()
my_instance.instance_method(..,..)
```

- 메서드도 함수이기 때문에 추가적인 인자를 받을 수 있음

```python
class MyClass:
  def method1(self):
    print('hi')
  def method2(self, arg):
    print(arg)
```

## 4.4 `self`

인스턴스 자신(self)

### 4.4.1 생성자(constructor) 메서드

- 인스턴스 객체가 생성될 때 자동으로 호출되는 함수
- **init** 으로 정의

활용법

```python
class MyClass:
  def __init__(self):
    print('-')
```

### 4.4.2 소멸자(destructor) 메서드

- 인스턴스 객체가 소멸(파괴)되기 직전에 자동으로 호출되는 함수
- **del** 으로 정의

활용법

```python
def __del__(self):
  print('-')

del 인스턴스
```

## 4.5 속성(Attribute) 정의

- 특정 데이터 타입(또는 클래스)의 객체들이 가지게 디ㅗㄹ 상태/데이터를 의미
- `self.<속성명> = <값>` or `<인스턴스>.<속성명> = <값>` 으로 설정

활용법

```python
class Person:
  def __init__(self, name):
    self.name = name
  def talk(self):
    print(f'{self.name}')
```

## 4. 6 매직(스페셜) 메서드

특별한 일을 하기 위해 만들어진 메서드

```python
 '__str__(self)',
 '__len__(self)',
 '__repr__(self)',
 '__lt__(self, other)',
 '__le__(self, other)',
 '__eq__(self, other)',
 '__ne__(self, other)',
 '__gt__(self, other)',
 '__ge__(self, other)',
```

## 4.6.1 `__str__(self)`

```python
class Person:
  def __str__(self):
    return 'content'
```

특정 객체를 출력할 때 보여줄 내용을 정의할 수 있음

# 05. 클래스(class)

객체들의 분류를 정의할 때 쓰이는 키워드

## 5.1 클래스(Class) 생성

- 클래스 생성은 `class` 키워드와 정의하고자 하는 <클래스의 이름>으로 가능
- <클래스의 이름> 은 PascalCase로 정의
- 클래스 내부에는 데이터와 함수를 정의할 수 있고, 이때 데이터는 속성(attribute) 정의된 함수는 \*\*메서드(method)로 부른다.

활용법

```python
class <클래스이름>:
  <statement>
class ClassName:
  statement
```

클래스 정의하기

```python
class Person:
  """사람 클래스입니다."""

help(Person)
Person.__doc__
```

## 5.2 클래스 변수

- 클래스의 속성(attribute)
- 모든 인스턴스가 공유
- 클래스 선언 내부에서 정의
- 클래스.변수명 으로 접근 및 할당

## 5.3 클래스 메서드(class method)

- 클래스가 사용할 메서드에 해당
- @classmethod 로 정의
- 메서드 호출 시, 첫 번째 인자로 클래스 cls가 전달됨

활용법

```python
class Myclass:
  @classmethod
  def class_method(cls, arg1, arg2, ...):

MyClass.class_method(..,..)

```

## 5.4 스태틱 메서드(static method)

- 클래스가 사용할 메서드에 해당함
- 인스턴스와 클래스의 속성과 무관한 메서드
- @staticmethod 로 정의
- 호출시, 어떠한 인자도 자동으로 (self, cls) 전달되지 않음
- 속성을 다루지 않고 단지 기능(행동)만을 하는 메서드를 정의할 떄 사용함
  활용법

```python
class MyClass:
  @staticmethod
  def static_method(arg1, arg2, ...)

  MyClass.static_method(.., ..)
```

## 5.5 인스턴스와 클래스 간의 이름 공간(namespace)

- 클래스를 정의하면 클래스와 해당하는 이름 공간이 생성됨
- 인스턴스를 만들면 인스턴스 객체가 생성되고 이름 공간이 생성됨
- 인스턴스에서 특정 속성에 접근하면, 인스턴스-클래스 순으로 탐색함

```python
class Person:
    # class var
    spices = 'human'

    # instance method
    def __init__(self, name):
        # instance var
        self.name = name

```

#변수는 LEGB 순으로 찾고

#객체의 속성값(attr)과 메서드(method)는 instance => class => 상위 class

## 5.6 비교 정리

### 5.6.1 인스턴스와 메서드

인스턴스는 3가지 메서드(인스턴스, 클래스, 정적 메서드) 모두에 접근할 수 있음

- 인스턴스에서 클래스 메서드와 스태틱 메서드는 호출하지 않음
  인스턴스가 할 행동은 모두 인스턴스 메서드로 한정 지어서 설계

```python
class MyClass:

    def instance_method(self):
        return 'instance method: ', self

    @classmethod
    def class_method(cls):
        return 'class method: ', cls

    @staticmethod
    def static_method():
        return 'static method'
```

### 5.6.2 클래스와 메서드

클래스는 3가지 메서드(인스턴스, 클래스, 정적 메서드) 모두에 접근할 수 있음

- 클래스에서 인스턴스 메서드는 호출하지 않음
  클래스가 할 행동은 다음 원칙에 따라 설계한다
- 클래스 자체(cls)와 그 속성에 접근할 필요가 있다면 클래서 메서드로 정의함
- 클래스와 클래스 속성에 접근할 필요가 없다면 정적 메서드로 정의함
  - 정적 메서드는 cls, self와 같이 묵시적인 첫번째 인자를 받지 않기 때문

# 06. OOP의 핵심 개념

추상화/상속/다형성/캡슐

## 6.1 추상화(Abstraction)

- 세부적인 내용은 감추고 필수적인 부분만 표현하는 것
- 현실 세계를 프로그램 설계에 반영하기 위해 사용됨
- 여러 클래스가 공통적으로 사용할 속성 및 메서드를 추출하여 기본 클래스로 작성하여 활용

## 6.2 상속(Inheritance)

클래스에서 가장 큰 특징은 상속이 가능하다는 것
부모 클래스의 모든 속성이 자식 클래스에게 상속되므로 코드 재사용성이 높아짐

```python
class ChildClass(ParentClass):
  <code block>
```

`issubclass(class, classinfo)`: class가 classinfo의 subclass인 경우 True 반환

`isinstance(object, classinfo)`: object가 classinfo의 인스턴스거나 subclass인 경우 True 반환

`super()`

- 자식 클래스에 메서드를 추가로 구현 가능
- 부모 클래스의 내용을 사용하고자 할 떄, super()를 사용할 수 있음

```python
class ChildClass(ParentClass):
    def method(self, arg):
        super().method(arg)
```

```python
class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email

    def greeting(self):
        print(f'안녕, {self.name}')


class Student(Person):
    def __init__(self, name, age, number, email, student_id):
        # 부모 클래스의 __init__ 함수를 이자리에서 실행
        super().__init__(name, age, number, email)
        self.student_id = student_id
```

## 6.3 다형성(Polymorphism)

- 동일한 메서드가 클래스에 따라 다르게 행동할 수 있음

### 6.3.1 메서드 오버라이딩

자식 클래스에서 부모 클래스의 메서드를 재정의하는 것

- 상속 받은 메서드 재정의 가능
- 상속 받은 클래스에서 같은 이름의 메서드로 덮어씀
  - `_init__`, `__str__`의 메서드를 정의하는 것 역시, 메서드 오버라이딩

## 6.4 캡슐화(Encapsulation)

객체의 일부 구현 내용에 대해 외부로부터의 직접적인 엑세스를 차단하는 것

### 6.4.1 Public Member

- 언더바가 없이 시작하는 메서드나 속성들이 이에 해당
- 어디서나 호출 가능
- 하위 클래스에서 메서드 오버라이딩을 허용함
- 일반적으로 작성되는 메서드와 속성의 대다수를 차지

### 6.4.2 Protected Member

- 언더바 1개로 시작하는 메서드나 속성들이 이에 해당
- 암묵적 규칙에 의해 부모 클래스 내부와 자식 클래스에서만 호출 가능
- 하위 클래스에서 메서드 오버라이딩을 허용함

### 6.4.3 Private Member

- 언더바 2개로 시작하는 메서드나 속성들이 이에 해당
- 본 클래스 내부에서만 사용 가능
- 하위 클래스 상속 및 호출이 불가능
- 외부 호출 불가능

### 6.4.4 다중 상속

두 개 이상의 클래스를 상속받은 경우

- 상속 받은 모든 클래스의 요소를 활용 가능
- 중복된 속성이나 메서드가 있는 경우 상속 순서에 의해 결정

### 6.4.5 상속관계에서의 이름 공간과 MRO(Method Resolution Order)

- 기존의 인스턴스 -> 클래스 순으로 이름 공간을 탐색해나가는 과정에서 상속관계에 있으면 아래와 같이 확장됨
  - 인스턴스 -> 자식 클래스 -> 부모 클래스
- MRO는 해당 인스턴스의 클래스가 어떤 부모 클래스를 가지는지 확인하는 속성 또는 메서드

```python
ClassName.__mro__
ClassName.mro()
```
