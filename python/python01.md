# # Python

<br/>

# 01. 기초 문법(Syntax)

## 1. 들여쓰기(Indentation)

들여쓰기 : space키 4번 혹인 1탭

## 2. 변수(Variable)

### 2.1 변수

컴퓨터 메모리 어딘가에 저장되어 있는 객체를 참조하기 위해 사용되는 이름

- 객체(object): 값을 가지고 있는 모든 것
  - 파이썬 : 객체지향 언어, 모든 것이 객체로 구현
- 동일 변수에 다른 객체를 언제든 할당 가능
  - 즉, 참조하는 객체가 바뀔 수 있기 때문에 '변수'

### 2.2 할당 연산자(Assignment Operator) : `=`

- 변수는 `= `을 통해 할당됨
- `type()`: 해당 데이터 타입 확인
- `id()` : 해당 값의 메모리 주소 확인

```python
x = '황서진'
type(x)
id(x)
```

### 2.3 변수 연산

```python
i = 5
j = 3
s = 'python'

print(i + j)
print('hello' + s)
```

### 2. 4 변수 할당

- 같은 값을 동시에 할당 가능

  ```python
  x = y = 100
  ```

- 다른 값을 동시에 할당 가능

  ```python
  x, y = 1, 2
  ```

### 2.5 식별자(Identifiers)

변수, 함수, 모듈, 클래스 등을 식별하는데 사용되는 이름(name)

- 식별자의 이름은 영문 알파벳, 언더스코어, 숫자로 구성
- 첫 글자에 숫자 X
- 길이에 제한 X
- 대/소문자(case) 구별
- 사용 금지 키워드: <br/>
  ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
- 내장함수나 모듈등의 이름 사용 X
- 기존의 이름에 다른 값을 할당하게 되므로 더이상 동작 X

  ```python
  print = 'hi'
  print(100) #error

  del print
  print('good')
  ```

## 3. 사용자 입력(input)

### 3.1 input([prompt])

- 사용자로부터 값을 즉시 입력 받을 수 있는 파이썬 내장함수
- 대괄호 안에 문자열 입력하면 해당 문자열을 출력 가증
  - 단. 대괄호는 생략
    ```python
    data = input('입력: ' )
    print(data)
    ```
- 반환값은 항상 문자열의 형태

## 4. 주석(Comment)

- #: 한 줄 주석
- 여러 줄 주석
  - 한 줄 씩 # 사용
  - """ 또는 '''

<br/>

# 02. 자료형(Data Type)

## 2.1 자료형 분류

- 불린형(Boolean Type)
- 수치형(Numeric Type)
  - int(정수, integer)
  - float(부동소수점, 실수, floating point number)
  - complex(복소수, complex number)
- 문자열(String Type)
- None
  - 값이 없음을 표현하기 위한 타입

## 2.2 불린형(Boolean Type)

`bool` : `True` or `False`  
`bool()` : 특정 데이터가 True인지 False인지 검증

- `bool(0)` # False
- `bool('')` # False
- `bool([])` # False
- `bool(None)` # False
- `bool(1)` # True

## 2.3 수치형(Numeric Type)

### 2.3.1 int(정수, Integer)

모든 정수는 int로 표현
|n진수|표기법|
|---|---|
|8진수|0o|
|2진수|0b|
|16진수|0x|

```python
binary_num = 0b10 # 2진수
octal_num = 0o10 # 8진수
decimal_num = 10 # 10진수
hexadecimal_num = ox10 # 16진수
```

파이썬에서 표현할 수 있는 가장 큰 수

- sys 모듈 사용
- 임의 정밀도 산술(arbitrary-precision arithmetic) 사용으로 오버플로우 없음
- 오버플로우
  - 데이터 타입별로 사용할 수 있는 메모리의 크기가 제한됨
  - 표현할 수 있는 수의 범위를 넘어가는 연산을 하게 되면 기대했던 값이 출력되지 않는 현상
  - 메모리를 넘어선 상황
- 임의 정밀도 산술

  - 사용할 수 있는 메모리양이 정해져 있는 기존의 방식과 달리, 현재 남아있는 만큼의 가용 메모리를 모두 수 표현에 끌어다 쓸 수 있는 형태를 의미
  - 특정 값을 나타내는데 4바이트가 부족하다면 5바이트, 6바이트까지 사용할 수 있게 유동적으로 운용

    ```python
    import sys
    max_int = sys.maxsize
    print(max_int)

    super_max = sys.maxsize 8 sys.maxsize
    print(super_max)
    ```

### 2.3.2 flot(부동소수점, 실수, floating point number)

실수를 컴퓨터가 표현하는 과정에서 부동소수점 사용하므로 항상 같은 값으로 일지되지 않는다.(floating point rounding error)  
=> 컴퓨터가 2진수(비트)를 통해 숫자를 표현하는 과정에서 생기는 오류, 값이 같은지 비교하는 과정에서 문제 발생

컴퓨터식 지수 표현 방식

- e를 사용(e와 E 모두 사용 가능)
- `5e3` == 5000.0

실수의 연산

```python
x = 3.5 - 3.12 # x = 3.7999999
```

    해결방법

1.  ```python
    a = 3.5 - 3.12
    b = 0.38

    abs(a-b) < 1e-10
    ```

2.  ```python
    import sys
    abs(a-b) <= sys.float_info.epsilon
    ```

3.  ```python
    import math
    math.isclose(a, b)
    ```

- `round()` : 반올림
- `ceil` : 올림
- `floor` : 내림

### 2.3.3 complex(복소수, complex number)

각각 실수로 표현되는 실수부와 허수부를 가징
복소수는 허수부를 j로 표시

```python
a = 3 + 4j
```

## 2.4 문자열 (String Type)

### 2.4.1 문자열

모든 문자는 `str`로 표현

### 2.4.2 기본 활용법

문자열은 `'` 나 `"`을 활용하여 표현 가능
단, 문자열을 묶을 때 동일한 문장부호 활용, 하나의 문장부호를 선택해서 유지

```python
print('철수 \'안녕\'')
print('철수 "안녕"')
```

### 2.4.3 중첩 따옴표(Nested Quotes)

따옴표 안에 따옴표를 표현

1. `'작은 "큰"'`
2. `"작은 '큰'"`

### 2.4.4 삼중 따옴표(Triple Quotes)

작은 따옴표나 큰 따옴표를 삼중으로 사용

- 문자열 안에 따옴표 넣을 때
- 여러줄에 걸쳐있는 문장

```python
    print("""
    문자열 안에 '작은 따옴표'나
    "큰 따옴표"를 사용할 수 있고
    여러 줄을 사용할 때도 편리하다.
    """)
```

### 2.4.5 이스케이프 시퀀스(Escape sequence)

| 예약문자 |    내용(의미)     |
| :------: | :---------------: |
|    \n    |      줄 바꿈      |
|    \t    |        탭         |
|    \r    |    캐리지리턴     |
|    \0    |     널(Null)      |
|   \\\\   |        `\`        |
|   \\'    | 단일인용부호(`'`) |
|   \\"    | 이중인용부호(`"`) |

### 2.4.6 String interpolation

- %-formatting
  - %d : 정수
  - %f : 실수
  - %s : 문자열
- str.format()

  ```python
    name = '황서진'
    score = 3.5

    print('내 이름은 %s, 성적은 %f' %(name, score))
    print('내 이름은 {}, 성적은 {}'.format(name,score))
    print(f'내 이름은 {name}, 성적은 {score}')
    print(f'''안녕하세요
    제 이름은
    {name}입니다.''')
  ```

- f-strings

  ```python
  # 1
  import datetime
  today = datetime.datetime.now()
  print(today)

  #2
  print(f'오늘은 {today:%Y}년 {today:%m}월 {today:%d}일 {today:%A}')

  #3
  pi = 3.141592
  print(f'원주율은 {pi:.3}. 반지름이 2일 때 원의 넓이는 {pi * 2 * 2}이라고 출력해봅시다.')
  ```

### 2.4.7 None Type

값이 없음을 표현

```python
a = None
print(a) # None
```
