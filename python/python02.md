# # Python

# 01 컨테이너(Container)

여러 개의 값을 저장할 수 있는 거(객체)
서로 다른 자료형을 저장 가능

## 1.1 컨테이너 분류

- 시퀀스(Sequence)형: 순서가 있는(ordered) 데이터
- 비 시퀀스(Non-sequence)형: 순서가 없는(unordered) 데이터

## 1.2 시퀀스(Sequence)형 컨테이너

시퀀스: 데이터가 순서대로 나열된(ordered) 형식

- 순서대로 나열된 것이 정렬되었다(sorted)는 아님

### 1.2.1 특징

1. 순서가 있다
2. 특정 위치의 데이터를 가리킬 수 있다

### 1.2.2 종류

- list
- tuple
- range
- string
- binary

### 1.2.3 List

[value1, value2, value3]  
대괄호 [] 및 list()를 통해 만듦

```python
my_list = []
another_lilst = list()
```

```python
locations = ['a', 'b', 'c', 'd', [0, 1]]
locations[0] # 'a'
```

원하는 위치의 인덱스를 통해 할당(`=`) 연산자로 요소의 수정 가능

```python
numbers = [1, 2, 3, 4, 5]

# 접근
numbers[2]

#수정
numbers[2] = 30
print(numbers)

#추가
numbers.append(6)
print(numbers)

#삭제
numbers.pop()
print(numbers)
```

### 1.2.4 Tuple

()로 묶어서 표현
수정 불가능(불변, immutable)

```python
my_tuple = (2, 4)
another_tuple = 2, 4
single_tuple = (1, )
```

튜플 대입

- 우변의 값을 좌변의 변수에 한 번에 할당하는 과정
  ```python
  x, y = 1, 2
  (x, y) = (1, 2)
  ```

**수정 불가능** : 튜플은 데이터 추가/수정/삭제 모두 불가능

```python
numbers = (1, 2, 3)

# 접근 O
numbers[1]

#수정 X
numbers[1] = 20

numbers.append(1) # X
```

### 1.2.5 range()

정수의 시퀀스를 나타내기 위해 사용
range(n) (0 ~ n-1)

```python
range(1, 10, 2)
```

### 1.2.6 패킹/언패킹 연산자 (Packing / Unpacking Operator)

모든 시퀀스형은 패킹/언패킹 연산자 \*을 사용하여 객체의 패킹/언패킹이 가능

`x, *y = i, j, k, ...`

**패킹**

- 대입문의 좌변 변수에 위치
- 우변의 객체 수가 좌변의 변수 보다 만흥ㄹ 경우 개체를 순서대로 대입
- 나머지 항목들은 모두 별 기호 표시된 변수에 리스트로 대입

```python
x, *y = 1, 2, 3, 4, 5
# x = 1, y =[2, 3, 4, 5]
```

**수정 불가능**

```python
r = range(10)

#접근 가능
print(r[4])

# 수정 불가능
r[4] = 1
```

**언패킹**

- argument 이름이 \*로 시작하는 경우, argument unpacking
- 패킹의 경우, 리스트로 대입

```python
def multiply(x, y, z):
  return x * y * z

numbers = [1, 2, 3]
multiply(*numbers)
```

**패킹/언패킹 연산자 주의 사항**

- 연산자가 곱셈을 의미하는지 패킹/언패킹 연산자인지 구분

## 1.3 비 시퀀스형(Non-sequence) 컨테이너

### 1.3.1 Set

- 순서가 없고 중복된 값이 없는 자료구조
- {}
- 담고 있는 객체를 삽입 변경, 삭제 가능(mutable)
- 빈 세트를 만들려면 set()
- -, |, & 가능
  ```python
  s1 = {1, 2, 3}
  ```

**수정 가능**

- 할당 방식이 아닌 메서드로 변경

```python
s = {1, 2, 3, 2, 1}

# idx 없음 => 단일 요소 접근 불가

# 추가
s.add(4)
print(s)

#삭제
s.remove(2)
print(s)
```

### 1.3.2 Dictionary

- key와 value가 쌍으로 이뤄져있음
- {}, dict()
- 순서 보장 X
- key는 변경 불가능 immutable 한 데이터만 가능
- value는 list, dictionary 를 포함한 몯느 것이 가능

```python
d1 = {}
d2 = dict()

phone_book = {'서울' : '02', '경기' : '031', '인천' : '032', '대전': '042', '광주' : '062'}
phone_book.keys()
phone_book.values()
phone_book.items()
```

**수정 가능**

- 할당식을 통해 Key-Value 추가 기능
- 할당식을 통해 Value 수정 가능

```python
# dict key 중복 안됨. (Value는 무관)
phone_book = {
    '서울' : '02',
    '경기' : '031',
    '인천' : '032',
    '대전': '042',
    '광주' : '062', # 컨테이너 자료형을 여러 줄에 쓸 경우, 반드시 Trailing Comma 적을 것!!!
}


# 접근 (Key 없으면 Error)
print(phone_book['서울'])
#print(phone_book['평양'])

#변경
#Key가 이미 존재한다면 => Value 수정
phone_book['서울'] = '022'
print(phone_book)

#Key가 존재하지 않는다면 => Key-Value 추가
phone_book['평양'] = '냉면'
print(phone_book)

```

**dict key는 immutable 자료형, value는 상관 없음**

- number
- bool
- str
- tuple
- range

```python
# str도 immutable 하다
# 접근 가능
'asdf'[0]
# 수정 불가능
# 'asdf'[0] = 'A' # X

d = {
    1: 1,
    3.2 : [1, 2, 3],
    'asdf': 'ASDF',
    (1, 2): {1, 2, 3},
    range(10): [1, 2, 3,],
    # list는 mutable
    # [1, 2, 3] : 100
}
```

<br/>

표 나타내기

```python
table = [
    {'이름':'김김김' ,'나이':25 ,'MBTI': 'entj'},
    {'이름':'이이이' ,'나이':26 ,'MBTI': 'intp'},
    {'이름':'박박박' ,'나이':22 ,'MBTI': 'esfj'},
]
```

# 02 형변환(Type conversion, Typecasting)

## 2.1 컨테이너형 형변환

```python
# 1. list
l = [1, 2, 3]
# tuple(l) # O
# range(l) # X
# set(l) # O 중복 요소 제거됨
# dict(l) # X

# 2. tuple
t = (1, 2, 3, 1, 2)
# list(t) # O
# range(t) # X
# set(t) # O 중복 요소 제거됨
# dict(t) # X

# 3. range
r = range(10)
# list(r) # O
# tuple(r) # O
# set(r) # O
# dict(r) # X

# 4. set
s = {1, 2, 3}
# list(s) # O
# tuple(s) # O
# range(s) # X
# dict(s) # X

# 5. dictionary
d = {'a'; 1, 'b': 2}
# list(d) # O key로만 구성
# tuple(d) # O key로만 구성
# range(d) # X
# set(d) # O key로만 구성

# 6 string
# 슷자로 이루어진 문자열만 O
# int('100')
# int('asdf') # X
# bool(''), bool('asdf') # F, T
# list('asdf') # O 문자열의 한글자 한글자를 요소로 갖는 리스트
# tuple('asdf') # O
# range('asdf') # X
# set('asdf') # O 중복 제거된 글자로 이루어진 set
# dict('asdf') # X
```

## 2.2 시퀀스형 연산자(Sqeuence Type Operator)

### 2.2.1 산술 연산자(+)

시퀀스를 연결(concatenation) 가능

```python
[1, 2] + ['a'] # [1, 2, 'a']

(1, 2) + ('a',) # (1, 2, 'a)

range(1) + range(2, 5) # error

'12' + 'a' # '12a'
```

### 2.2.2 반복 연산자 (\*)

시퀀스 반복 가능

```python
[0] * 8 # [0, 0, 0, 0, 0, 0, 0, 0]

(1, 2) * 3 # (1, 2, 1, 2, 1, 2)

range(1) * 3 # error

'hi' * 3 # 'hihihi'
```

## 2.3 인덱싱/슬라이싱(Indexing/Slicing)

[]를 통한 값을 접근, [:]을 통해 슬라이싱

### 2.3.1 인덱싱

시퀀스의 특정 인덱스 값에 접근
해당 인덱스가 없는 경우 IndexError

```python
[1, 2, 3][2] # 3

(1, 2, 3)[0] # 1

range(1, 10, 2)[2] # 5

'abc'[0] # 'a'

'apple'[100] # error
```

### 2.3.2 슬라이싱

Sequence[start:end[:step]]

```python
s = 'abcdefghi'

print(s[:3])
print(s[5:])
print(s[::])
print(s[::-1])
```

## 2.4 함수(Function)

특정 명령을 수행하는 함수 묶음

```python
def multiply(x, y, z):
    return x * y * z


multiply(5, 6, 3)
```

## 2.5 모듈(Module)

함수/클래스의 모음 또는 하나의 프로그램을 구성하는 단위

## 2.6 패키지(Package)

프로그램과 무듈의 묶음

- 프로그램: 실행하기 위한 것
- 모듈: 다른 프로그램에서 불러와 사용하기 위한 것

## 2.6 라이브러리(Library)

- 패키지의 모음
