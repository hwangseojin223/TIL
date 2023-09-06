# # Python

<br/>

# 01. 데이터 구조(Data Structure)

데이터 구조(자료구조) :

- 데이터에 효율적인 접근 및 수정을 가능케 하는 데이터의 구성, 관리 및 저장형식
- 데이터 값들, 해당 값들의 관계, 그리고 해당 데이터들에게 적용할 수 있는 함수와 명령어들의 모음을 총칭하는 단어

# 02. 순서가 있는 데이터 구조

## 2.1 문자열(String)

immutable, ordered, iterable

### 2.1.1 조회/탐색

**`.find(x)`**
x의 첫 번째 위치 반환, 없으면 -1 반환

**`.index(x)`**
x의 첫 번째 위치를 반환, 없으면 오류

**`.startswith(x)`**
문자열이 x로 시작하면 True 반환, 아니면 False 반환

**`.endswith(x)`**
문자열이 x로 끝나면 True 반환, 아니면 False 반환

### 2.1.2 기타 문자열 관련 검증 메서드

`.isalpha()`: 문자열이 (숫자가 아닌)글자로 이루어져 있는가  
`.isspace()`: 문자열이 공백으로 이루어져 있는가  
`.isupper()`: 문자열이 대문자로 이루어져 있는가  
`.istitle()`: 문자열이 타이틀 형식으로 이루어져 있는가  
`.islower()`: 문자열이 소문자로 이루어져 있는가

`isdecimal()`: 문자열이 0~9까지의 수로 이루어져 있는가  
`isdigit()`: 문자열이 숫자로 이루어져 있는가  
`isnumeric()`: 문자열을 수로 볼 수 있는가

## 2.2 문자열 변경

**`.replace(old, new[, count])`**  
바꿀 대상 글자를 새로운 글자로 바꿔서 반환
count를 지정하면 해당 갯수만큼만 시행

**`.strip([chars])`**  
특정한 문자들을 지정하면

- 양쪽을 제거(strip)
- 왼쪽을 제거(lstrip)
- 오른쪽을 제거(rstrip)
  chars 파라미터를 지정하지 않으면 공백을 제거

**`.split([chars])`**  
문자열을 특정한 단위로 나누어 리스트로 반환

**`'separator'.join(iterable)`**  
iterable의 문자열들을 separator(구분자)로 이어 붙인 (join()) 문자열을 반환
다른 메서드들과 달리, 구분자가 join 메서드를 제공하는 문자열

**`.capitalize()`**  
앞글자를 대문자로 만들어 반환

**`.title()`**  
' 나 공백 이후를 대문자로 만들어 반환

**`.upper()`**  
모두 대문자로 만들어 반환

**`.lower()`**  
모두 소문자로 만들어 반환

**`.swapcase()`**  
대 <-> 소문자로 변경하여 반환

###### 문자열 메서드 모두 확인하기 => dir('')

## 2.3 리스트(List)

mutable, ordered, iterable

## 2.3.1 값 추가 및 삭제 => 원본 변경

**`.append(x)`**  
리스트에 값 추가 가능
`a[len(a):] = [x]` 와 동일

**`.extend(iterable)`**  
리스트에 iterable(list, range, tuple, string) 값을 붙일 수 있음  
`a[len(a): ] = iterable` 와 동일

**`.insert(i, x)`**  
정해진 위치 i에 값을 추가

**`.remove(x)`**  
리스트 값이 x인 첫번째 항목을 삭제, 없으면 ValueError

**`.pop([i])` => 삭제되는 값을 `return`**  
정해진 위치 i에 있는 값을 삭제, 그 항목을 반환
i가 지정되지 않으면 마지막 항목을 삭제하고 반환

**`.clear()`**  
리스트의 모든 항목을 삭제

## 2.3.2 탐색 및 정렬

**`.index(x)`**  
x 값을 찾아 해당 index 값을 반환

**`.count(x)`**  
원하는 값의 개수를 반환

**`.sort()`**  
리스트를 정렬
내장함수 `sorted()` 와는 다르게 워본 list를 변형시키고 `None`을 리턴
올림차순: a.sort(reverse = True)

**`.reverse()`**  
리스트의 element들을 반대로 뒤집음
내장함수 reversed()완느 다르게 원본 list를 변형, None 리턴

###### 리스트 메서드 모두 확인하기 => dir([]), help(list), help([])

## 2.4 튜플(tuple)

immutable

### 2.4.1 탐색

**`.index(x[, start[, end]])`**  
튜플에 있는 항목 중 값이 x와 같은 첫 번째 인덱스를 반환, 없으면 ValueError

**`.count()`**  
튜플에서 x가 등장하는 횟수 반환

# 03. 순서가 없는 데이터 구조

## 3.1 셋(Set)

mutable, unordered, iterable

## 3.1.1 추가 및 삭제

**`.add(elem)`**  
elem을 set에 추가

**`.update(*others)`**  
여러 값을 추가
반드시 iterable 데이터 구조를 전달해야 한다

**`.remove(elem)`**  
elem을 set에서 삭제, 존재하지 않으면 KeyError

**`.discard(elem)`**  
elem을 set에서 삭제, 존재하지 않아도 에러 발생 안 함

###### set 메서드 모두 확인하기 => dir(set)

## 3.2 딕셔너리(Dictionary)

mutable, unordered, iterable
`key:value` => pair의 자료구조

### 3.2.1 조회

**`.get(key[, default])`**  
key를 통해 value 가져오고 존재하지 않으면 None 반환

**`.setdefault(key[, default])`**  
key가 dictionary에 있으면 value 반환
없을 경우, default값을 갖는 key를 삽입한 후 default 반환
만약, default 없을 경우 None 반환

### 3.2.2 추가 및 삭제

**`.pop(key[, default])`**  
key가 딕셔너리에 있으면 제거하고 그 값을 돌려주고 그렇지 않으면 default 반환
default가 없는 상태에서 해당 key가 딕셔너리에 없는 경우, KeyError 발생

**`.update([other])`**  
other가 제공하는 key, value쌍으로 dictionary 덮어씀
other는 다른 dictionary나 key/value 쌍으로 되어 있는 모든 iterable을 사용 가능

###### dictionary 메서드 모두 확인하기 => dir(dict)

# 04. 얕은 복사와 깊은 복사

## 4.1 데이터 분류

### 4.1.1 immutable data

- literal
  - number
  - string
  - bool
- range()
- tuple()
- frozenset()

### 4.1.2 mutable data

- list
- dict
- set

## 4.2 데이터 복사하는 방법

1. 할당
2. 얕은 복사
3. 깊은 복사

## 4.3 할당

```python
original = [1, 2, 3]
copy = original

copy[0] = 5
print(copy, original) # [5, 2, 3] [5, 2, 3]
```

id(copy) == id(original)

## 4.4 얕은 복사 Shallow copy

### 4.4.1 slice 연산자 활용 [:]

```python
a = [1, 2]

b = a[:]
# id(a) != id(b)

a[0] = 5
print(a, b) #[5, 2] [1, 2]
```

### 4.4.2 list() 활용

```python
a = [1, 2]

b = list(a)
a[0] = 5
print(a, b) #[5, 2] [1, 2]
```

### 4.4.3 '.copy()' 활용

```python
a = [1, 2]

b = a.copy()
a[0] = 5
print(a, b) #[5, 2] [1, 2]
```

#### 그 외 얕은 복사

```python
a = [1, 2, [1, 2]]

b = a[:]
b[2][0] = 5
print(a, b) #[1, 2, [5, 2]] [1, 2, [5, 2]]

id(a), id(b) # 다름
id(a[2]), id(b[2]) # 같음
```

## 4.5 깊은 복사 (Deep copy)

중첩된 상호아 => 깊은 복사
깊은 복사는 새로운 객체를 만들고 원본 객체 내에 있는 객체에 대한 복사를 재귀적으로 삽입  
즉, 내부에 있는 모든 객체까지 새롭게 값이 변경됨

```python
import copy

a = [1, 2, [1, 2]]
b = copy.deepcopy(a)
a,b #([1, 2, [1, 2]], [1, 2, [1, 2]])

# id(a) != id(b)
# id(a[2]) != id(b[2])
```
