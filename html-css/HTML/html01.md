# 00. Intro

    <!-- html 형식 -->
    <!DOCTYPE HTML>
    <html lang='en'>

        <!-- Metadata: 데이터의 데이터 -->
        <head>

            <!-- 글자 인코딩 -->
            <meta charset="utf-8" />

            <!-- 문서 제목 -->
            <title></title>
        </head>

        <!-- 실제 문서에 표시되는 데이터 -->
        <body>
        </body>
    </html>

# 01. Heading

    <!DOCTYPE HTML>
    <html>
        <head>
        </head>

        <body>
            <h1>가장 큰 제목</h1>
            <h2>하위 제목1</h2>
            <h3>1111</h3>
            <h4>2222</h4>
            <h5>3333</h5>
            <h6>4444</h6>
        </body>

    </html>

# 02. Content

    <!DOCTYPE HTML>
    <html>
        <head>
            <title>Document</title>
        </head>

        <body>
            <!-- 문단 paragraph-->
            <p>
                content
            </p>

            <p>
                <!-- Semantic(의미론적) -->
                <strong>강조</strong>
                <em>강조2</em>

                <br/>

                <!-- Non-Semantic -->
                <b>굵게</b>
                <i>이탤릭</i>
            </p>

            <p>def hello(x, y): return 'Hello'</p>
            <pre>
                def hello(x, y):
                    return 'Hello'
            </pre>
        </body>

    </html>

# 03. Link

    <!DOCTYPE HTML>
    <html>
        <head>
        </head>

        <body>
            <!-- Hyper link : a 태그(anchor) : inline -->

            <!-- 기본 링크 -->
            <p>구글로 가려면 <a href="https://google.com">Google</a>을 클릭하세요</p>

            <!-- 새탭에서 열기 -->
            <p>
            <a href="https://naver.com" target="_blank">Naver</a>는 새탭에서 열립니다.

            <!-- 비워있는 링크 -->
            </p>
            <p><a href="#">아직 목적지를 정하지는 못했지만</a> 우선 링크로 만들게요!</p>
        </body>

    </html>

# 04. List

    <body>
        <h2>Ordered List (순서 있는 리스트)</h2>
        <ol>
            <li>HTML 배우기</li>
            <li>복습하기</li>
            <li>마크다운 정리하기</li>
            <li>
                내일 내용 예습하기
                <ol>
                <li>CSS</li>
                <li>Bootstrap5</li>
                </ol>
            </li>
        </ol>

        <h2>Unordered List (순서 없는 리스트)</h2>
        <ul>
            <li>Python</li>
            <li><strong>Web</strong></li>
            <li>Django</li>
            <li>DB</li>
            <li>Algorithms</li>
        </ul>
    </body>

# 05. Table

    <body>
        <h1>Table</h1>

        <table>
            <thead>
                <tr>
                <th>이름</th>
                <th>나이</th>
                <th>전공</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>김김김</td>
                    <td>25</td>
                    <td>경영</td>
                </tr>
                <tr>
                    <td>이이이</td>
                    <td>28</td>
                    <td>컴공</td>
                </tr>
                <tr>
                    <td>박박박</td>
                    <td>22</td>
                    <td>수학</td>
                </tr>
            </tbody>
        </table>
    </body>

# 06. Media

    <body>
        <h1>Media Content</h1>

        <h2>Image</h2>
        <p>
            <!-- 직접 가지고 있는 (local) 파일 위치 -->
            <img src="./html5.png" alt="html5 logo image" width="300" />
            <br />

            <!-- 외부 이미지 주소 -->
            <img
                src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/HTML5_logo_and_wordmark.svg/240px-HTML5_logo_and_wordmark.svg.png"
                alt="html5 logo image"
                width="300"
            />
        </p>

        <h2>IFrame</h2>
        <iframe
            width="560"
            height="315"
            src="https://www.youtube.com/embed/ZXjUBkEmuqA?si=u1hAGLD-PmwQOUMc"
            title="YouTube video player"
            frameborder="0"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
            allowfullscreen
        >
        </iframe>
    </body>
