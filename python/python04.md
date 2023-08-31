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

`expression` : 참/거짓에 대한 조건식
조건이 참인 경우 `:` 이후의 문장 수행
조건이 거짓인 경우 `else:` 이후의 문장을 수행
여러 개의 `elif` 가 있을 수 있고 else는 선택적으로 사용

## 1.2 elif 복수 조건

2개 이상의 조건을 활용할 경우 elif <조건>: 을 활용

## 1.3 중첩 조건문(Nested Conditional Statement)

조건문은 다른 조건문에 중첩 가능

## 1.4 조건 표현식(Conditional Expression)

삼항 연산자(Ternary Operator)라고 부르기도 함

활용법
`true value if <조건식> else false_value`

# 02. 반복문(Loop Statement)

## While 반복문

while문은 조건식이 참(True)인 경우 반복적으로 코드를 실행

```while <조건식>:
    <코드 블럭>
```

반드시 종료조건을 설정해야 한다.
