# Crawling

## Http Request Method(Verb)

1. GET 95%
2. POST 4%

## Code

```python
# kospi.py
import requests
from bs4 import BeautifulSoup

# 요청 => 응답 객체
res = requests.get('https://finance.naver.com/sise/')

# HTML 문서 파싱 완료 결과
soup = BeautifulSoup(res.text, 'html.parser')
tag = soup.select_one('#KOSPI_now')

print(tag.text)
```

```python
# lotto_api.py
import requests

res = requests.get('https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1086')
data = res.json() # dict 형식
#data['drwtNo2']와 같이 접근 가능

# 로또번호 6개
numbers = [data[f'drwtNo{i}'] for i in range(1, 7)]


# 보너스 번호
bonus_no = data['bnusNo']

print(numbers, bonus_no)

# JSON => 개발자 쓰라고 => Web API
# Appliccation Programming Interface

```

```python
# lotto_crawling.py
import requests
from bs4 import BeautifulSoup

res = requests.get('https://dhlottery.co.kr/common.do?method=main')
soup = BeautifulSoup(res.text, 'html.parser')

numbers = []

for i in range(1, 7):
    num = int(soup.select_one(f'#drwtNo{i}').text)
    numbers.append(num)

bonus_no = soup.select_one('#bnusNo').text

print(numbers, bonus_no)
```
