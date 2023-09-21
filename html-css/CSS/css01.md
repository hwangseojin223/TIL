# CSS

## 기본 형식

```html
<!DOCTYPE html>
  <head>
    <!-- 3 -->
    <link rel="stylesheet" href="./style.css" />
    <!-- 2 -->
    <style>
      .green-md {
        color: green;
        font-size: 24px;
        text-decoration: underline;
      }
    </style>
  </head>
  <body>
    <!-- 1. inline CSS(마크업에 직접) => X  -->
    <p style="font-size: 30px; color: red">Inline CSS</p>

    <!-- 2.<head> 안에 <style> 을 정의 하기 -->
    <p class="green-md">Head Style Tag</p>
    <a href="#" class="green-md">This is LINK</a>

    <!-- 3. 별도의 CSS 파일로 분리하기 -->
    <p class="blue-sm">Seperated .css file</p>
  </body>
</html>

```

## <style></style>

| 형식                        | 역할                            | 특징                                                 |
| --------------------------- | ------------------------------- | ---------------------------------------------------- |
| .(ClassName){}              | class style 지정                | -                                                    |
| color: green;               | 글자색                          | rgb, rgba(rgb + 투명도)로 지정 가능                  |
| font-style                  | 글꼴스타일                      | normal, italic                                       |
| font-size: 20px;            | 글자크기(16px 기본)             | px, em 단위                                          |
| font-weight                 | 글자두께                        | lighter, bold, bolder                                |
| line-height: 2rem;          | 텍스트 줄 사이의 거리 설정      | -                                                    |
| text-align                  | 텍스트 정렬 방향                | left, right, center, justify                         |
| background-color            | 배경 색 지정                    | -                                                    |
| border-width                | 테두리 두께                     | px                                                   |
| border-style                | 테두리 스타일                   | solid,dotted,dashed,double,groove,ridge,inset,outset |
| border-color                | 테두리 색상                     | -                                                    |
| text-decoration: underline; | 글자 밑줄                       | -                                                    |
| width                       | 가로길이 (px, %)                | inline 요소 적용 X                                   |
| height                      | 세로길이 (px, %)                | inline 요소 적용 X                                   |
| em                          | 0.5em = 16px(기본) \* 0.5 = 8px | -                                                    |

## `<p></p>`

하나의 문단

## `<div></div>`

레이아웃을 나누는데 주로 쓰임

## `content < padding < border < margin`

- margin: 10px 10px 10px 10px; => 상우하좌 순(시계방향)

## `<span></span>`

- div와의 차이점: display 속성이 block이 아닌 inline
- div는 줄 바꿈이 되지만 span은 줄 바꿈이 되지 않음

## `<img src="" alt"">`

## `<input type="text">`

## `<button></button>`

## `<textarea cols="10" rows="5"></textarea>`
