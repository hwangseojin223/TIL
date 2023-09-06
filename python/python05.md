# # Python

<br/>

# 01. 함수(function) I

## 1.1 함수 function

```python
def <함수이름>(parameter1, parameter2):
    <코드 블럭>
    return value
```

## 1.2 함수의 Output

**함수의 return**
함수는 반환되는 값이 있으며, 이는 어떠한 종류 값도 상관 없음  
단, 오직 한 개의 객체만 반환됨  
함수가 return 되거나 종료되면, 함수를 호출한 곳으로 돌아감

## 1.3 함수의 입력(Input)

### 1.3.1 매개변수 & 전달인자

**매개변수(parameter)**

```python
def func(x):
    return x + 2
```

- `x`는 매개변수
- 입력을 받아 함수 내부에서 활용할 변수
- 함수를 정의하는 부분에서 확인 가능

**전달인자(argument)**

`func(2)`

- `2`는 전달인자
- 실제로 전달되는 값
- 함수를 호출하는 부분에서 볼 수 있음

### 1.3.2 함수의 인자

함수는 input으로 argument를 넘겨줄 수 있음

**위치 인자(Postion Arguments)**  
기본적으로 인자는 위치에 따라 함수 내에 전달

**기본 인자 값(Default Argument values)**

```python
def 함수이름(이름='입력이 없으면 사용할 값'):
    return
```

단, 기본 인자값을 가지는 인자 다음에 기본 값이 없는 인자를 사용할 수 없음

**키워드 인자(Keyword Arguments)**  
함수를 호출할 때 키워드 인자를 활용하여 직접 변수의 이름으로 특정 인자를 전달 가능

```python
def greeting(age, name, address, major):
    return f'{name}은 {age}살입니다. 전공은 {major}, 주소는 {address}입니다.'

greeting(name='h', major='c', age=20, address='s')
greeting(20, 'h', major='c', address='s')
# greeting(major='경영', age=24, '서울', '철수') #error
```

### 1.3.3 정해지지 않은 여러 개의 인자 처리

**가변(임의) 인자 리스트(Arbitrary Argument Lists)**  
개수가 정해지지 않은 임의읭 인자를 받기 위해 가변인자 리스트 _args 활용  
가변 인자 리스트는 `tuple` 형태로 처리, 매개변수에 `_`로 표현

```python
def func(a, b, *args):
    pass
```

**가변(임의) 키워드 인자(Arbitrary Keyword Arguments)**  
정해지지 않은 키워드 인자들은 함수를 정의할 때 가변 키워드 인자 `**kwargs` 활용  
가변 키워드 인자는 `dict` 형태로 처리, 매개변수에 `**`로 표현

```python
def func(**kwargs):
    pass
```

```python
def my_func(a, b=1, *args, **kwargs):
    print(a, b, args, kwargs)

my_func(1, 2, True, False, 'a', x=1, y=2, z=3)

# 출력
# 1 2 (True, False, 'a') {'x': 1, 'y': 2, 'z': 3}
```

# 02. 함수 Function II

## 2.1 함수와 스코프(scope)

함수는 코드 내부에 스코프를 생성

- `전역 스코프(global scope)` : 코드 어디에서든 참조할 수 있는 공간
- `지역 스코프(local scope)`: 함수가 만든 스코프로 함수 내부에서만 참조할 수 있는 공간
- `전역 변수(global variable)`: 전역 스코프에 정의된 변수
- `지역 변수(local variable)`: 로컬 스코프에 정의된 변수

1. 함수 밖의 변수(global var), 함수 안의 변수(local var)
   - 인자는 함수 안의 변수 취급
2. 함수 안(local scope)에서는 함수 밖(global scope) 에 접근 가능
   - 함수 안에 `a`가 없으면, 함수 밖에서 `a`를 찾음
   - 만약, 함수 안에 `a`가 있다면, 함수 밖 `a`는 접근 불가능
3. 함수 밖에서는 함수 안에 접근 불가능

## 2.2 이름 검색(resolution) 규칙

파이썬에서 사용되는 이름(식별자)들은 이름공간(namespace)에 저장
LEGB Rule

- Local scope: 함수
- Enclosed scope: 특정 함수의 상위 함수
- Global scope: 함수 밖의 변수 혹은 import된 모듈
- Built-in scope: 파이썬안에 내장되어 있는 함수 또는 속성

# 03. 재귀 함수(recursive function)

함수 내부에서 자기 자신을 호출하는 함수
반드시, base case가 존재
**팩토리얼**

```python
def factorial(n):
    # Base Case
    if n == 1:
        return 1
    return n * factorial(n-1)
```

**피보나치**

```python
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
```

## 3.1 함수 응용

**`map(function, iterable)`**

- 순회 가능한 데이터 구조(iterable)의 모든 요소에 function을 적용한 후 그 결과를 돌려줌
- `return`은 `map_object` 형태

```python
list(map(int, ['1', '2', '3'])) #[1, 2, 3]
```

**lambda 함수**

- 표현식을 계산한 결과 값을 반환하는 함수
- 이름 없는 함수(익명함수)
- return 문을 가질 수 없고, 간단한 조건문 외의 구성이 어려움

```python
f1 = lambda x, y : x + y

print(f1(3, 4)) # 7
(lambda x, y : x + y)(1, 3)# 4
```
