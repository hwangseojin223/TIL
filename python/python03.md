# # Python

<br/>

# 01. 연산자

## 1.1 산술 연산자

| 연산자 | 내용     |
| ------ | -------- |
| +      | 덧셈     |
| \*     | 곱셈     |
| /      | 나눗셈   |
| //     | 몫       |
| %      | 나머지   |
| \*\*   | 거듭제곱 |

- 나눗셈의 결과는 항상 float

## 1.2 비교 연산자

| 연산자 | 내용                   |
| ------ | ---------------------- |
| <      | 미만                   |
| <=     | 이하                   |
| >      | 초과                   |
| =>     | 이상                   |
| ==     | 같음                   |
| !=     | 같지않음               |
| is     | 객체 아이엔티티        |
| is not | 부정된 객체 아이엔티티 |

## 1.3 논리 연산자

| 연산자  | 내용                         | -                      |
| ------- | ---------------------------- | ---------------------- |
| a and b | a와 b 모두 True면 True       | 하나라도 False면 False |
| a or b  | a와 b 모두 False면 False     | 하나라도 True면 True   |
| not a   | True => False, False => True | -                      |

- `and`는 a가 거짓이면 a를 리턴, 참이면 b를 리턴
- `or`는 a가 참이면 a를 리턴, 거짓이면 b를 리턴

### 1.3.1 단축평가 (Short circuit Evaluation)

- 첫 번째 값이 학실할 때, 두 번째 값은 확인하지 않음
- 조건문에서 뒷 부분을 판단하지 않아도 되기 때문에 속도 향상

- `and`는 둘 다 True일 경우만 True 이므로 첫 번째 값이 True라도 두 번째 값을 확인해야 하기 때문에 b가 반환됨
- `or`는 하나만 True여도 True이므로 True를 만나면 해당 값을 바로 반황

```python
True and True and True and False and False and True # False
```

```python
1 and 3.14 and 'asdf' and [] ad {} and () and True # []
```

```python
0 or '' or [] or None or 'a' or 1234 or {1, 2} # 'a'
```

## 1.4 복합 연산자

복합 연산자는 연산과 대입이 함께 이루어짐
|연산자|내용|
|----|---|
|a += b|a = a + b|
|a -= b|a = a - b|
|a \*= b|a = a \* b|
|a /= b|a = a / b|
|a //= b|a = a // b|
|a %= b|a = a % b|
|a \*\*= b|a = a \*\* b|

### 1.4.1 Containment Test

`in` 연산자를 통해 요소가 속해있는지 여부 확인 가능

```python
'a' in 'apple' # True

2 in [1, 2, 3, 4] # True

3 in range(5) # True
3.5 in range(5) # False


#dict에서는 in 연산을 key만 확인.
1 in {'a': 1}
```

### 1.4.2 Identity

`is` 연산자를 통해 동일한 object인지 확인 가능

```pyton
l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(id(l1), id(l2))

l1 == l2, l1 is l2 # (True, False)
```

파이썬에서 -5부터 256까지의 id는 동일함

### 1.4.3 연산자 우선순위

0. `()`을 통한 grouping
1. Slicing
2. Indexing
3. 제곱연산자
   `**`
4. 단항연산자
   `+`, `-` (음수/양수 부호)
5. 산술연산자
   `*`, `/`, `%`
6. 산술연산자
   `+`, `-`
7. 비교연산자, `in`, `is`
8. `not`
9. `and`
10. `or`
