# # Python

<br/>

# 01. 조건문(Conditional Statement)

`if`문은 반드시 참/거짓을 판단할 수 있는 조건과 함께 사용

## 1.1 if 조건문의 구성

### 1.1.1 활용법

```python
if <expression>:
    <코드 블럭>
else:
    <코드 블럭>
```

- `expression` : 참/거짓에 대한 조건식
- 조건이 참인 경우 `:` 이후의 문장 수행
- 조건이 거짓인 경우 `else:` 이후의 문장을 수행
- 여러 개의 `elif` 가 있을 수 있고 else는 선택적으로 사용

## 1.2 elif 복수 조건

2개 이상의 조건을 활용할 경우 elif <조건>: 을 활용

## 1.3 중첩 조건문(Nested Conditional Statement)

조건문은 다른 조건문에 중첩 가능

## 1.4 조건 표현식(Conditional Expression)

삼항 연산자(Ternary Operator)라고 부르기도 함

활용법

- `true value if <조건식> else false_value`

# 02. 반복문(Loop Statement)

## 2.1 while 반복문

while문은 조건식이 참(True)인 경우 반복적으로 코드를 실행

```python
while <조건식>:
    <코드 블럭>
```

반드시 종료조건을 설정해야 한다.

## 2.2 for 문

시퀀스(string, tuple, list, range)를 포함한 순회가능한 객체(iterable)의 요소들을 순회

```python
for <임시변수> in <순회가능한데이터(iterable)>:
    <코드블럭>
```

### 2.2.1 문자열(String) 순회

`range(문자열의 길이)`

### 2.2.2 딕셔너리 순회 (반목문 활용)

```python
grades = {'john': 80, 'eric': 90}

for key in grades:
    print(key) # john eric
    print(grades[key]) # 80 90
```

`dictionary`에서 `for`를 활용하는 4가지 방법

```python
#1 dictionary 순회 (key 활용)
for key in dict:
    print(key)
    print(dict[key])

#2 '.keys()' 활용
for key in dict.keys():
    print(key)
    print(dict[key])

#3 '.values()' 활용
# 이 경우 key는 출력할 수 없음
for val in dict.values():
    print(val)

#4'.items()' 활용
for key, val in dict.items():
    print(key, val)
```

### 2.2.3 enumerate()

인덱스(index)와 값(value)을 함께 활용 가능

```python
members = ['a', 'b', 'c']

for idx, member in enumerate(members):
    print(idx, member)
# 출력
# 0 a
# 1 b
# 2 c

list(enumerate(members))
# 출력
# [(0, '민수'), (1, '영희'), (2, '철수')]
```

### 2.2.4 List Comprehension

[expression for 변수 in iterable]

```python
#1~3까지의 숫자로 만든 세제곱 리스트

numbers = [1, 2, 3]
cubic_list = [num **  for num in numbers]

#10*10 체스판

matrix = []
for _ in range(n):
    matrix.append([0]*10)
```

### 2.2.5 Dictionary Comprehension

{키: 값 for 요소 in iterable}

```python
#1~3의 세제곱 딕셔너리

cubic_dict = {i: i**3 for i in range(1, 4)}
```

## 2.3 반복제어(break, continue, for-else)

`break` : 반복문을 종료

`continue` : continue 이후의 코드를 수행하지 않고 다음 요소부터 계속하여 반복을 수행

`pass`: 아무것도 하지 않음, 자리를 채우는 용도

`else`: 끝까지 반복문을 실행한 이유에 실행

- 반복문이 `break` 문으로 종료될 때는 실행되지 않음(즉, `break`를 통해 중간에 종료되지 않은 경우만 실행)
- 즉, `break`가 없는 `for`문에서는 사용할 이유 X
  ```python
  for char in 'apple':
     if char == 'b':
         print('b!!!')
         break
  else:
     print('b가 없습니다.')
  ```
